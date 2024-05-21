from argparse import _SubParsersAction,ArgumentParser
from ..base_subcommand import SubCommand

class SendSubCommand(SubCommand):
    def __init__(self) -> None:
        super().__init__()

    def add_subparser(self, subparser: _SubParsersAction):
        parser:ArgumentParser = subparser.add_parser('send',help='Run to send one of your templates using your default SMTP credentials.')

        parser.add_argument()