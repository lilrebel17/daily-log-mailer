from abc import ABC, abstractmethod
from argparse import _SubParsersAction,Namespace

class SubCommand(ABC):
    def __init__(self) -> None:
        super().__init__()
        '''
        Abstract Base class for a SubCommand.
        '''

    @abstractmethod
    def add_subparser(self,subparser: _SubParsersAction):
        '''
        To be ran in pyeasymailer.py\n
        Adds the parser & all arguments for it.\n
        Add as many arguments as needed.

        Standard Setup:
            parser:argparse.ArgumentParser = subparser.add_parser([Parser Name],help=[Help Message]')\n
            parser.add_arguments()
        '''
        pass