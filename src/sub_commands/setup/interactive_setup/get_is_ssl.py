from .get_user_input import get_user_input

def get_is_ssl():
    ssl_confirmed: bool = False
    while ssl_confirmed == False:
        is_ssl: str = get_user_input('Is this connection going to be via SSL? [y/n]').lower()

        if is_ssl == 'y' or is_ssl == 'n':
            ssl_confirmed = True
            if is_ssl == 'y':
                return True
            else:
                return False
        else:
            print("Please enter y/n")