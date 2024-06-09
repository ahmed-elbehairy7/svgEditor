from argparse import ArgumentParser
from src import Parser as srcParser
from files import Parser as filesParser
from replace import Parser as replaceParser
from convert import Parser as convertParser
from listColors import Parser as listColorsParser
from warnings import filterwarnings
from os import path

filterwarnings("ignore", category=SyntaxWarning)

def main():
    
    parser = ArgumentParser("svge", description="A program to edit svg files")
    subparsers = parser.add_subparsers(dest="command", required=True, metavar="command")
    
    ####    src parser
    src = srcParser()
    
    ####    Files parser
    files = filesParser(src)

    ####    Replace sub command
    replaceParser(subparsers, files)
    
    ####    convert sub command
    convertParser(subparsers, files) 
    
    ####    list colors sub command
    listColorsParser(subparsers, src)   
    
    
    args = parser.parse_args()
    args.func(args)
    


if __name__=="__main__":
    main()