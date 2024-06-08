from argparse import ArgumentParser


def main():
    
    parser = ArgumentParser("vreplacer", description="A program to edit svg files")
    parser.add_argument("svg_file", help="The input svg file")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ####    Replace sub command
    
    replace = subparsers.add_parser("replace", help="Replace a color of a svg file with another")    
    replace.add_argument("old_color", help="The color you want to replace from the svg file")
    replace.add_argument("new_color", help="The color to replace with")
    replace.add_argument("dist_file", help="The file you want to save the result in")
    replace.set_defaults(func=replaceFunc)
    
    
    ####    convert sub command
    
    convert = subparsers.add_parser("convert", help="Convert the svg file to whatever format wanted")
    convert.set_defaults(func=convertFunc)
    
    args = parser.parse_args()
    args.func(args)
    

def replaceFunc(args):
    with open(args.svg_file, 'r', 'utf-8') as old:
        content = old.read()
        
        with open(args.dist_file, 'w', 'utf-8') as new:
            new.write(content.replace(args.old_colour, args.new_colour))


def convertFunc(args):
    ...
    
    

if __name__=="__main__":
    main()