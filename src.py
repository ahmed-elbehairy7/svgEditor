from argparse import ArgumentParser

class Parser(ArgumentParser):
    def __init__(self) -> None:
        super().__init__(add_help=False)
        self.add_argument("src", metavar="src", help="The input svg file")