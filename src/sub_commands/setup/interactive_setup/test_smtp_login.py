import smtplib



def test_smtp_login(smtp_hostname:str,smtp_port:int,from_address:str,from_address_password:str,is_ssl:bool):
    if is_ssl == True:
        smtp_server = smtplib.SMTP_SSL(smtp_hostname,smtp_port)
    else:
        smtp_server = smtplib.SMTP(smtp_hostname,smtp_port)

    try:
        connection_test = smtp_server.login(from_address,from_address_password)
        print(connection_test)
        return True
    except smtplib.SMTPAuthenticationError as error:
        print(error)
        return False