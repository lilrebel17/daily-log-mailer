#!/usr/bin/env python

# Standard Library Imports
import argparse
from os import getuid

from sub_commands.setup import subcommand as setup



# Main argument parser
main_parser = argparse.ArgumentParser(prog='pyeasymailer',description='Quickly setup and send emails using a remote SMTP like gmail or ZoHo')
main_parser.add_argument("-v",'--verbose',help='Run to get more information while the program executes. Enables verbose logging for one run',action='store_true',dest='verbose')

# Sub Parser for any subcommands to work under
sub_parser = main_parser.add_subparsers(dest='subcommand')

# Init the setup subcommand.
setup_subcommand = setup.SetupSubCommand()
setup_subcommand.add_subparser(sub_parser)

# Init the config subcommand
config_subcommand = sub_parser.add_parser(name='config',help='Run to setup certain configurable options within pyeasymailer')
config_subcommand.add_argument('-lt','--list-templates',action='store_true',help='Lists all current template names',dest='list_templates')



if __name__ == '__main__':
    args = main_parser.parse_args()

    # Checks to see if its being ran as sudo.
    if getuid() == 0:
        args.is_root = True
    else:
        args.is_root = False

    match args.subcommand:
        case 'setup':
            setup_subcommand.handle_command(args)
        case 'config':
            print("WIP: Config Subcommand")

        
