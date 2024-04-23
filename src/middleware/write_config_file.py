import configparser

def write_config_file(config_object:configparser.ConfigParser,file_name:str,file_path:str):
        try:
            with open(f'{file_path}{file_name}','w') as file:
                config_object.write(file)
        except FileExistsError as error:
            pass