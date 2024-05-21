from argparse import ArgumentParser,_SubParsersAction,Namespace

from ..base_subcommand import SubCommand
from .create_template import create_template
from .modify_template import modify_template


class TemplateSubCommand(SubCommand):
    def __init__(self) -> None:
        super().__init__()
        self.template_path = '/etc/pyeasymailer/template/'

    def add_subparser(self,subparser:_SubParsersAction):
        parser:ArgumentParser = subparser.add_parser('template',help='Run to edit, create or modify templates')
        parser.add_argument('-b','--body',action='store',help='Run to add/modify the body text of a template',dest='template_body',metavar="")
        parser.add_argument('-c','--create',action='store_true',help='Runs to create a template file',dest='template_create')
        parser.add_argument('-l','--list',action='store_true',help='Run to list all created templates',dest='template_list')
        parser.add_argument('-m','--modify',action='store_true',help='Run to choose what template to modify',dest='template_modify')
        parser.add_argument('-n','--name',action='store',help='Run to select or set the name of a template',dest='template_name',metavar="")
        parser.add_argument('-s','--subject',action='store',help='Used to set or modify the subject of a template',dest='template_subject',metavar="")

    def handle_command(self,namespace: Namespace):
        if namespace.template_name == None:
            raise ValueError("No template name was provided. Please use -n [name] to provide a name argument.")
        if namespace.template_create:
            self.handle_create(namespace.template_name,namespace.template_subject,namespace.template_body)
        elif namespace.template_modify:
            self.handle_modify(namespace.template_name,namespace.template_subject,namespace.template_body)

    def handle_create(self,name,subject,body):
        create_template(name,subject,body,self.template_path)

    def handle_modify(self,name,subject,body):
        if subject:
            modify_template(name,'subject',subject,self.template_path)
        if body:
            modify_template(name,'body',body,self.template_path)