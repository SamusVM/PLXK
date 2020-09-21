from django.db import models
from django.contrib.auth.models import User
from accounts.models import Department
from edms.models import Document as EdmsDocument, Employee_Seat


class Doc_group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Doc_type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=500)
    doc_type = models.ForeignKey(Doc_type, related_name='Documents', on_delete='CASCADE')
    doc_group = models.ForeignKey(Doc_group, related_name='Documents', on_delete='CASCADE')
    code = models.CharField(max_length=100, null=True, blank=True)
    doc_file = models.FileField(upload_to='docs/%Y/%m')
    act = models.CharField(max_length=50, null=True, blank=True)
    actuality = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, blank=True, related_name='+', on_delete=models.CASCADE)
    date_start = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    responsible = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Ct(models.Model):
    dt = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    u = models.ForeignKey(User, related_name='+', blank=True, on_delete=models.CASCADE)


class Order_doc_type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order_doc(models.Model):
    name = models.CharField(max_length=500)
    doc_type = models.ForeignKey(Order_doc_type, related_name='Documents', on_delete='CASCADE')
    code = models.CharField(max_length=100, null=True, blank=True)
    cancels_code = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='added_orders', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, blank=True, related_name='updated_orders', on_delete=models.CASCADE)
    date_start = models.DateField(null=True)
    date_canceled = models.DateField(null=True, blank=True)
    canceled_by = models.ForeignKey('self', related_name='cancels_order', null=True, blank=True)
    cancels = models.ForeignKey('self', related_name='cancelled_by_order', null=True, blank=True)
    author = models.ForeignKey(User, related_name='Created_documents')
    responsible = models.ForeignKey(User, related_name='responsible_for_documents', null=True, blank=True)
    supervisory = models.ForeignKey(User, related_name='supervisory_for_documents', null=True, blank=True)
    done = models.BooleanField(default=False)
    is_act = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class File(models.Model):
    file = models.FileField(upload_to='order_docs/%Y/%m')
    name = models.CharField(max_length=100, null=True, blank=True)
    order = models.ForeignKey(Order_doc, related_name='files', null=True)
    is_added_or_canceled = models.BooleanField(default=True)  # True - додані наказом документи, False - скасовані наказом документи
    is_active = models.BooleanField(default=True)


class Order_article(models.Model):
    order = models.ForeignKey(Order_doc, related_name='articles')
    text = models.CharField(max_length=5000)
    deadline = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


class Article_responsible(models.Model):
    article = models.ForeignKey(Order_article, related_name='responsibles')
    employee_seat = models.ForeignKey(Employee_Seat, related_name='orders_responsible')
    done = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


class Contract(models.Model):
    # Не можна перейменовувати ці поля, це вплине на автоматичний переніс Договорів з системи EDMS
    number = models.CharField(max_length=10)
    created_by = models.ForeignKey(User, related_name='added_contracts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, blank=True, related_name='updated_contracts', on_delete=models.CASCADE)
    subject = models.CharField(max_length=1000)
    counterparty = models.CharField(max_length=200)
    nomenclature_group = models.CharField(max_length=100, null=True, blank=True)
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    responsible = models.ForeignKey(User, null=True, blank=True, related_name='responsible_for_contracts')
    department = models.ForeignKey(Department, related_name='contracts', null=True, blank=True)
    lawyers_received = models.BooleanField(default=False)
    edms_doc = models.ForeignKey(EdmsDocument, related_name='contracts', null=True)  # посилання на документ в edms, яким було створено цей Договір (для отримання тим документом файлів для історії)

    basic_contract = models.ForeignKey('self', related_name='additional_contracts', null=True, blank=True)
    # Якщо це поле пусте, то документ є основним договором,
    # в іншому разі це додаткова угода і це поле вказує на основний договір

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject


class Contract_File(models.Model):
    file = models.FileField(upload_to='contract_docs/%Y/%m')
    name = models.CharField(max_length=100, null=True, blank=True)
    contract = models.ForeignKey(Contract, related_name='files', null=True)

    is_active = models.BooleanField(default=True)
