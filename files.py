from argparse import ArgumentParser, ArgumentTypeError
from os import path

class Parser(ArgumentParser):
    def __init__(self, src : ArgumentParser) -> None:
        super().__init__(add_help=False, parents=[src])
        self.add_argument("-o", "--output", metavar="output_file", help="The output file for the result", required=True, type=self.outputName)
        self.add_argument("-d", "--dist", metavar="dist_dir", help="The dist dir to output the files in", default="")
        
    
    def outputName(self, text : str):
        root, file = path.split(text)
        if root or path.isdir(file):
            raise ArgumentTypeError("please enter only the file name, add the directory for the dist argument")
        
        return path.splitext(file)[0]