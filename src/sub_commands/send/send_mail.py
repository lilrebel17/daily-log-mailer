import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .get_smtp_credentials import get_smtp_credentials
from .get_template_data import get_template_data

def send_mail(template_name,to_address):
    smtp_credentials:dict = get_smtp_credentials()
    template_data:dict = get_template_data(template_name)

    message = MIMEMultipart()
    message['Subject'] = template_data.get('subject')
    message.attach(MIMEText(template_data.get('body')))

    try:
        smtp_server = smtplib.SMTP_SSL(smtp_credentials.get('hostname'),int(smtp_credentials.get('smtp_port')))
        smtp_server.login(smtp_credentials.get('email_address'),smtp_credentials.get('password'))
        message_string = message.as_string()
        smtp_server.sendmail(smtp_credentials.get('email_address'),to_address,message_string)
        smtp_server.quit()
    except Exception as e:
        print(e)
