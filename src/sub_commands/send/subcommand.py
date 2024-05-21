from argparse import _SubParsersAction,ArgumentParser,Namespace
from ..base_subcommand import SubCommand

from .send_mail import send_mail

class SendSubCommand(SubCommand):
    def __init__(self) -> None:
        super().__init__()

    def add_subparser(self, subparser: _SubParsersAction):
        parser:ArgumentParser = subparser.add_parser('send',help='Run to send one of your templates using your default SMTP credentials.')

        parser.add_argument("-n","--name",action='store',help="Run with this to choose a template name",dest="template_name",metavar="",required=True)
        parser.add_argument("-t","-to",action='store',help='Adds the email address you want the template email to send to.', dest="to_address",metavar="",required=True)

    def handle_command(self,namespace:Namespace):
        send_mail(namespace.template_name,namespace.to_address)