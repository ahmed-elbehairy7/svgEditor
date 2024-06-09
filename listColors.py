from argparse import ArgumentParser, _SubParsersAction
from re import findall
from command import Command

class Parser(Command):
    
    parserData = {
        "name" : "listColors",
        "help":"List available colors in the svg file", 
        "aliases":["l"]
    }
    
    def __init__(self, subparsers : _SubParsersAction, files) -> None:
        Parser.parserData.update({"parents" : [files]})
        super().__init__(subparsers, Parser.parserData) 
        self.setDefaultFunc()
        
    

    #############################
    ####    Main Function    ####
    #############################
     
    def parserFunc(self, args):
        with open(args.src, encoding='utf-8') as file:
            content = file.read()
        
        types = ["fill", "stroke"]
        
        for colorType in types:
            print(f"{colorType}s in file:\n")
            for color in findall(colorType +": (#([\\da-f]{3}){1,2}|none);", content):
                print(color[0])
            
            print()