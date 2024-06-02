from argparse import ArgumentParser,_SubParsersAction,Namespace

from ..base_subcommand import SubCommand
from .create_template import create_template
from .modify_template import modify_template
from .list_templates import list_templates


class TemplateSubCommand(SubCommand):
    def __init__(self) -> None:
        super().__init__()
        self.template_path = '/etc/pyeasymailer/template/'

    def add_subparser(self,sub_parser:_SubParsersAction):
        parser:ArgumentParser = sub_parser.add_parser('template',help='Run to edit, create or modify templates')
        parser.add_argument('-b','--body',action='store',help='Used to set the body text of a template',dest='template_body',metavar="")
        parser.add_argument("-n","--name",action='store',help="Used to choose the template name to create or modify",dest="template_name",metavar="")
        parser.add_argument('-s','--subject',action='store',help='Used to set or modify the subject of a template',dest='template_subject',metavar="")
        parser.add_argument('-a','--attachment',action='store',help='Used to set a file path for an attachment within a template',dest='template_attachment',metavar="")

        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-m','--modify',action='store_true',help='Used to modify a templates configuration. Must be used with one of the setting arguments [-a,-b,-s] to choose what to edit',dest='template_modify')
        group.add_argument('-c','--create',action='store_true',help='Used to create a new template.',dest='template_create')
        group.add_argument('-l','--list',action='store_true',help='Used to list all current template names',dest='template_list')


    def handle_command(self,namespace: Namespace):
        if namespace.template_list:
            self.handle_list()
        elif namespace.template_name == None:
                raise ArgumentParser.error(ArgumentParser(prog='pyeasymailer'),"Please add -n {template name} argument to specify a template name")
        else:
            if namespace.template_create:
                self.handle_create(namespace.template_name,namespace.template_subject,namespace.template_body,namespace.template_attachment)
            elif namespace.template_modify:
                self.handle_modify(namespace.template_name,namespace.template_subject,namespace.template_body,namespace.template_attachment)

    def handle_create(self,name,subject,body,attachment):
        create_template(name,subject,body,attachment,self.template_path)

    def handle_modify(self,name,subject,body,attachment):
        if subject:
            modify_template(name,'subject',subject,self.template_path)
        if body:
            modify_template(name,'body',body,self.template_path)
        if attachment:
            modify_template(name,'attachment',attachment,self.template_path)


    def handle_list(self):
        list_templates()