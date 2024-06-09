from decorators import commandWithOutputFile
from argparse import ArgumentParser, _SubParsersAction
from re import sub
from common import colorInput
from os import path
from command import Command

class Parser(Command):
    
    parserData = {
            "name": "replace",
            "help": "Replace a color of a svg file with another",
            "aliases": ["r"]
        }


    def __init__(self, subparsers : _SubParsersAction, files : ArgumentParser):
        Parser.parserData.update({"parents" : [files]})
        super().__init__(subparsers, Parser.parserData)    
        self.parser.add_argument("-oc", "--old-color", metavar="hex", help="The color you want to replace from the svg file", type=colorInput, required=True)
        self.parser.add_argument("-nc", "--new-color", metavar="hex", help="The color to replace with", action="extend", nargs='+', type=colorInput, required=True)
        self.parser.add_argument("--no-fill", help="Don't replace fills only strokes [default: false]", action="store_true")
        self.parser.add_argument("--no-strokes", help="Don't replace strokes only fills [default: false]", action="store_true")
        self.setDefaultFunc()
    
        
    
    #############################
    ####    Main Function    ####
    #############################
    
    @commandWithOutputFile
    def parserFunc(self, args):
        
        original = None
                            
        with open(file=args.src, mode="r", encoding="utf-8") as old:
            
            original = old.read()
        
        files = []
        for color in args.new_color:
            
            content = original
            
            if not args.no_fill:
                content = sub(f"fill: {args.old_color}", f"fill: {color}", content)
            
            if not args.no_strokes:
                content = sub(f"stroke: {args.old_color}", f"stroke: {color}", content)
            
            if len(args.new_color) == 1:
                output =  f"{args.output}.svg"
            else:
                output = f"{args.output}_{color.replace("#", "")}.svg"
            
            
            files.append({
                "name" : path.join(args.dist, output),
                "data": content
                })
            
        return files