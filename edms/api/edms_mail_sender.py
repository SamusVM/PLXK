from plxk.api.mail_sender import send_email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Складаємо лист новому отримувачу документа EDMS
def send_email_new(doc_request, mail):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Новий електронний документ"
    message["From"] = 'it@lxk.com.ua'
    message["To"] = mail

    link = 'Щоб переглянути, перейдіть за посиланням: http://10.10.10.22/edms/my_docs/{}' \
        .format(doc_request['document'])
    text = 'Вашої реакції очікує новий документ ({}, автор: {}). {}' \
        .format(doc_request['doc_type_name'], doc_request['doc_author_name'], link)

    message.attach(MIMEText(text, "plain"))

    send_email(mail, message.as_string())


# Складаємо лист автору документа про нову позначку EDMS:
def send_email_mark(doc_request, mail):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Нова реакція на Ваш електронний документ"
    message["From"] = 'it@lxk.com.ua'
    message["To"] = mail

    link = 'Щоб переглянути, перейдіть за посиланням: http://10.10.10.22/edms/my_docs/{}' \
        .format(doc_request['document'])
    text = 'Ваш документ #{} ({}) отримав позначку "{}". Автор позначки: {}. {}' \
        .format(doc_request['document'], doc_request['doc_type_name'],
                doc_request['mark_name'], doc_request['mark_author_name'], link)

    message.attach(MIMEText(text, "plain"))

    send_email(mail, message.as_string())


# Лист автору оригінального коментарю про отримання відповіді:
def send_email_answer(doc_request, mail):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Ви отримали відповідь на коментар"
    message["From"] = 'it@lxk.com.ua'
    message["To"] = mail

    link = 'Щоб переглянути, перейдіть за посиланням: http://10.10.10.22/edms/my_docs/{}' \
        .format(doc_request['document'])
    text = 'Ви отримали відповідь на коментар до документу № {} ({}). {}' \
        .format(doc_request['document'], doc_request['doc_type_name'], link)

    message.attach(MIMEText(text, "plain"))

    send_email(mail, message.as_string())

