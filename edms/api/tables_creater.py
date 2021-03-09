from django.conf import settings
from plxk.api.try_except import try_except
from ..models import Document_Type_Module, Document, File, Document_Path
from plxk.api.datetime_normalizers import datetime_to_json, normalize_whole_date

testing = settings.STAS_DEBUG


@try_except
# Функція, яка повертає Boolean чи використовує документ фазу auto_approved
def create_table(doc_type):
    modules_list = get_modules_list(doc_type)

    column_widths = get_column_widths(modules_list)

    table_header = get_table_header(modules_list)

    table_rows = get_table_rows(doc_type, modules_list)

    table = {'column_widths': column_widths, 'header': table_header, 'rows': table_rows}

    return table


@try_except
def get_column_widths(modules):
    column_widths = [
        {'columnName': 'id', 'width': 40},
        {'columnName': 'author', 'width': 200},
        {'columnName': 'status', 'width': 30},
        {'columnName': 'stage', 'width': 100},
        {'columnName': 'importancy', 'width': 90},
        # {'columnName': 'files', 'width': 300},
        {'columnName': 'choose_company', 'width': 85}]

    if any(module['module_id'] == 27 for module in modules):  # packaging_type
        column_widths.append({'columnName': 'packaging_type', 'width': 35})

    for module in modules:
        if module['field'] == 'importancy':
            column_widths.append({'columnName': 'text-' + str(module['queue']), 'width': 105})
        elif module['field'] == 'accounting':
            column_widths.append({'columnName': 'text-' + str(module['queue']), 'width': 150})
        elif module['field'] == 'type':
            column_widths.append({'columnName': 'text-' + str(module['queue']), 'width': 150})
        elif module['module'] == 'stage':
            column_widths.append({'columnName': 'added_date', 'width': 100})
            column_widths.append({'columnName': 'done_date', 'width': 100})
        elif module['field'] == 'performer':
            column_widths.append({'columnName': 'text-' + str(module['queue']), 'width': 100})

    return column_widths


@try_except
def get_modules_list(meta_doc_type):
    modules = [{
        'id': module.id,
        'module': module.module.module,
        'field_name': module.field_name,
        'field': module.field,
        'queue': module.queue,
        'module_id': module.module_id
    } for module in Document_Type_Module.objects
        .filter(document_type__meta_doc_type_id=meta_doc_type)
        .filter(table_view=True)
        .filter(is_active=True)
        .order_by('queue')
    ]

    return modules


@try_except
def get_table_header(modules):
    header = [{'name': 'id', 'title': '№'}, {'name': 'author', 'title': 'Автор'}]

    for module in modules:
        if module['module_id'] == 29:  # auto_approved module
            header.append({'name': 'status', 'title': module['field_name']})
        # elif module['module_id'] == 16:  # text module
        elif module['module_id'] in [16, 32]:  # text, select
            header.append({'name': 'text-' + str(module['queue']), 'title': module['field_name']})
        elif module['module_id'] == 33:  # stage
            header.append({'name': 'added_date', 'title': 'Створено'})
            header.append({'name': 'done_date', 'title': 'Виконано'})
            header.append({'name': 'stage', 'title': 'Стадія'})
        elif module['module_id'] == 1:
            # Відсортовуємо модуль files
            a = 1
        else:
            header.append({'name': module['module'], 'title': module['field_name']})

    return header


@try_except
def get_table_rows(meta_doc_type, modules):

    documents = Document.objects.all().select_related()\
        .filter(document_type__meta_doc_type_id=meta_doc_type)\
        .filter(is_template=False)\
        .filter(is_draft=False)\
        .filter(closed=False).order_by('-id')

    if not testing:
        documents = documents.filter(testing=False)

    documents_arranged = [{
        'id': doc.id,
        'author': doc.employee_seat.employee.pip,
        # 'date': datetime_to_json(Document_Path.objects.values('timestamp').filter(document_id=doc.id).filter(mark_id=1)[0]),
        'status': 'ok' if doc.approved is True else 'in progress' if doc.approved is None else '',
        'stage': get_stage(doc.stage),
        'texts': get_texts(modules, doc),
        'mockup_type': get_mockup_type(modules, doc),
        'mockup_product_type': get_mockup_product_type(modules, doc),
        'client': get_client(modules, doc),
        'packaging_type': get_packaging_type(modules, doc),
        'doc_gate': doc.gate.all()[0].gate_id if doc.gate.all() else None,
        # 'files': get_files(modules, doc),
        'choose_company': doc.company + ' ПЛХК',
        'added_date': normalize_whole_date(
            Document_Path.objects.values('timestamp').filter(document_id=doc.id).filter(mark_id=1)[0]),
        'done_date': get_done_date(doc)
    } for doc in documents]

    for document in documents_arranged:
        if document['texts']:
            for text in document['texts']:
                document.update({text['name']: text['text']})

    return documents_arranged


@try_except
def get_stage(stage):
    if stage == 'done':
        return 'Виконано'
    elif stage == 'confirm':
        return 'Підтверджено'
    elif stage == 'in work':
        return 'В роботі'
    elif stage == 'denied':
        return 'Відмовлено'
    return 'Ініційовано'


@try_except
def get_mockup_type(modules, doc):
    if any(module['module_id'] == 24 for module in modules):
        return doc.mockup_type.all()[0].mockup_type.name if doc.mockup_type.all() else None
    return None


@try_except
def get_mockup_product_type(modules, doc):
    if any(module['module_id'] == 25 for module in modules):
        return doc.mockup_product_type.all()[0].mockup_product_type.name if doc.mockup_product_type.all() else None
    return None


@try_except
def get_client(modules, doc):
    if any(module['module_id'] == 26 for module in modules):
        return doc.client.all()[0].client.name if doc.client.all() else None
    return None


@try_except
def get_packaging_type(modules, doc):
    if any(module['module_id'] == 27 for module in modules):
        field_queue = next(module['queue'] for module in modules if module["module_id"] == 27)
        return doc.texts.filter(queue_in_doc=field_queue)[0].text if doc.texts.filter(queue_in_doc=field_queue) else None
    return None


@try_except
def get_texts(modules, doc):
    if any(module['module_id'] in [16, 32] for module in modules):
        texts = []
        for module in modules:
            if module['module_id'] in [16, 32]:
                queue = module['queue']
                texts.append(
                    {'name': 'text-' + str(queue),
                     'text': doc.texts.filter(queue_in_doc=queue)[0].text if doc.texts.filter(queue_in_doc=queue) else None}
                )
        return texts
    return None


@try_except
def get_files(modules, doc):
    if any(module['module_id'] == 1 for module in modules):
        files = [{
            'id': file.id,
            'file': file.file.name,
            'name': file.name,
            'version': file.version
        } for file in File.objects
            .filter(document_path__document=doc.id)
            .filter(first_path=True)
            .filter(is_active=True)]

        return files
    return None


@try_except
def get_done_date(doc):
    if doc.stage in ['done', 'confirm']:
        return normalize_whole_date(
            Document_Path.objects.values('timestamp').filter(document_id=doc.id).filter(mark_id=11).order_by('-id')[0]
        )
    return ''
