import os
import smtplib
import configparser

width = os.get_terminal_size().columns

def print_border():
    print('-' * width)

def print_input():
    return input('# ')

'''I like cool banners. No other reason this is here.. well I guess it has notes. Thats cool.'''
print_border()
print("PyEasyMailer Setup".center(width))
print("NOTE: This is used as default settings if your email templates dont contain SMTP information".center(width))
print("If you want new default settings. You can rerun 'pyeasymailer setup' at anytime.".center(width))
print_border()
print("Press enter to continue")
input("# ")

'''Setting up SMTP Hostname'''
print("Please input your SMTP server hostname")
SMTP_HOSTNAME:str = print_input()

'''Getting the SMTP port'''
isInt = False
while isInt == False:
    print("Please input your SMTP servers port")
    SMTP_PORT: str = print_input()

    try:
        int(SMTP_PORT)
        SMTP_PORT = int(SMTP_PORT)
        isInt = True
    except ValueError:
        print("[ERROR] - Please input a number")


'''Checking if were connecting via SSL'''
if SMTP_PORT != 465:
    isBool = False
    while isBool == False:
        print("Is your connection going to be via SSL? [Y/n]")
        SMTP_SSL: str = print_input()

        if SMTP_SSL == 'Y' or SMTP_SSL == 'y':
            SMTP_SSL = True
            isBool = True
        elif SMTP_SSL == 'N' or SMTP_SSL == 'n':
            SMTP_SSL = False
            isBool = True
        else:
            print("[ERROR] - Please input Y or N")
else:
    SMTP_SSL = True

'''Getting the Default sending address'''
print("Please input your default sending address")
FROM_ADDRESS: str = print_input()

'''Getting the default sending address password'''
print("Please input the password for your default sending address")
FROM_ADDRESS_PASSWORD: str = print_input()

print("\n")

print(f"SMTP Hostname: {SMTP_HOSTNAME}")
print(f"SMTP Port: {SMTP_PORT}")
print(f"Connect via SSL?: {SMTP_SSL}")
print(f"SENDING Address: {FROM_ADDRESS}")
print(f"SENDING Address Password: {FROM_ADDRESS_PASSWORD}")
CONFIRMATION = input('Are the setting above correct? [Y/n]: ')

print("Testing login..")
if SMTP_SSL == True:
    SMTP_SERVER = smtplib.SMTP_SSL(SMTP_HOSTNAME,SMTP_PORT)
else:
    SMTP_SERVER = smtplib.SMTP(SMTP_HOSTNAME,SMTP_PORT)

try:
    CONNECTION_TEST = SMTP_SERVER.login(FROM_ADDRESS,FROM_ADDRESS_PASSWORD)
    print(CONNECTION_TEST)
except smtplib.SMTPAuthenticationError as e:
    print(e)