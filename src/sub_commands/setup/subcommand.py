import argparse
from .interactive_setup.interactive_setup_controller import run_interactive_setup
from sub_commands.base_subcommand import SubCommand

class SetupSubCommand(SubCommand):
    def __init__(self) -> None:
        super().__init__()

    def add_subparser(self,subparser:argparse._SubParsersAction):
        parser:argparse.ArgumentParser = subparser.add_parser('setup',help='Run by itself to run the interactive setup. This will set the default parameters.')

        parser.add_argument('-i', '--interactive', action='store_true',help='Runs the interactive setup', dest='interactive')

    def handle_command(self,namespace: argparse.Namespace):
        if namespace.interactive:
            if namespace.is_root:
                run_interactive_setup(namespace)
            else:
                raise PermissionError("Setup is to install system wide credentials. Please run as sudo")