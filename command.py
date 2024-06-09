from argparse import _SubParsersAction, ArgumentParser

class Command():
    def __init__(self, subparsers : _SubParsersAction, data) -> None:
        
        self.parser : ArgumentParser = subparsers.add_parser(**data)
    
    
    def setDefaultFunc(self):
        self.parser.set_defaults(func=self.parserFunc)