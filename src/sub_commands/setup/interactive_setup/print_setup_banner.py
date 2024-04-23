from os import get_terminal_size
from .print_input import print_input

console_width = get_terminal_size().columns

def print_startup_banner():
    '''I like cool banners. No other reason this is here.. well I guess it has notes. Thats cool.'''
    print('-' * console_width)
    print("PyEasyMailer Setup".center(console_width))
    print("NOTE: This is used as default settings if your email templates dont contain SMTP information".center(console_width))
    print("If you want new default settings. You can rerun 'pyeasymailer setup' at anytime.".center(console_width))
    print('-' * console_width)
    print("Press enter to continue")
    print_input()