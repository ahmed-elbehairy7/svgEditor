from argparse import ArgumentParser, ArgumentTypeError, _SubParsersAction, Action
from wand.api import library
import wand.color
import wand.image
from common import colorInput
from decorators import commandWithOutputFile
from command import Command

class Parser(Command):
    
    parserData = {
        "name" : "convert",
        "help":"Convert the svg file to png or jpeg", 
        "aliases":["c"]
    }
    
    def __init__(self, subparsers : _SubParsersAction , files : ArgumentParser) -> None:
        
        Parser.parserData.update({"parents" : [files]})
        super().__init__(subparsers, Parser.parserData) 
        self.parser.add_argument("-f", "--file-format", metavar="jpg|png", choices=["png", "jpg"], required=True)
        self.parser.add_argument("-bc", "--background-color", metavar="hex", type=colorInput, default="transparent", help="The background color of the result image [default: transparent]")
        self.parser.add_argument("-dim", "--dimensions", metavar="wxh", help="The dimensions of the result image [default: 1024x1024]", default="1024x1024", action=dimAction)
        self.setDefaultFunc()
        

    #############################
    ####    Main Function    ####
    #############################
     
    @commandWithOutputFile
    def parserFunc(self, args):
        with open(args.src, 'rb') as file:
            blob = file.read()
            
        with wand.image.Image() as image:
            with wand.color.Color(args.background_color) as background_color:
                library.MagickSetBackgroundColor(image.wand, background_color.resource) 
            
            image.width = args.width
            image.height = args.height
            image.read(blob=blob, format="svg")
            png_image = image.make_blob(args.file_format)

        return [{
            "name" :f"{args.output}.{args.file_format}",
            "mode" :"wb",
            "data" : png_image
        }]


#############################
####  Dimensions action  ####
#############################

class dimAction(Action):
    
    def __call__(self, parser, namespace, values, option_string=None):
        
        try:
            width, height = values.split("x")
        except:
            raise ArgumentTypeError("Please enter the dimensions as 'widthxheight'")
        
        if not width.isdigit() or not height.isdigit():
            raise ArgumentTypeError("Please enter valid dimensions")
                
        setattr(namespace, "width", int(width))
        setattr(namespace, "height", int(height))