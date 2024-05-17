from .get_user_input import get_user_input

def get_smtp_hostname():
    return get_user_input('Please enter the name of your remote SMTP server')