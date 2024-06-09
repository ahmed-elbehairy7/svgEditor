from re import match
from argparse import ArgumentTypeError

#############################
####     color Input     ####
#############################

def colorInput(text: str):
    stringColors = ["none", "transparent"]
    if not match("^#?([\\da-f]{3}){1,2}$", text) and not text in stringColors:
        raise ArgumentTypeError("color is not valid please enter a hex value or 'none'")
    
    if not text.startswith("#") and not text in stringColors:
        text = f"#{text}"
    
    if match("#(00|11|22|33|44|55|66|77|88|99|aa|bb|cc|dd|ee|ff){3}", text):
        text = f"#{text[0]}{text[2]}{text[4]}"
    
    return text


    #############################
    ####    Main Function    ####
    #############################
     
    def convertFunc(self, args):
        ...