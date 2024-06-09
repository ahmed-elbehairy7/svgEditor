# svge v1.0.0

## Edit svg files from your terminal

This application was developed to speed up the process of making logos for pamylka products, and the program has three commands: replace, convert, listColors

## setup

### First

make sure you have python installed by typing the following command and if not installed, install it

    python --version

pip install the modules used in the project by the following command

    pip install -r requirements.txt

### Second

go to this link to install ImageMagick, visit [this link](https://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-on-windows)

## All commands

### src

Every command in the application requires a src svg file as a positional argument

#### Ex

If you want to listColors in a file called pamylka.svg, the command should be something like this

    svge listColors pamylka.svg

## Most commands

### -o, --output

the output argument specifies the output file to store the results of the command you typed, if the command accepts it then it's a required argument.

Also, you can't have a directory in the path! for specifing directories, see the -d, --dist argument

#### Ex

    svge {command} src.svg -o out.svg

this will output the result of the command to out.svg file, if the command you entered outputs more than one file, the program will handle it by edit the output name to:

    {the_name_you_entered}_{some_variable}.svg

### -d, --dist

The distenation directory to put the results of the command

#### Ex

If you passed "pamylka.svg" for the output argument and "distdir" as dist directory like bellow:

    svge {command} src.svg -o pamylka.svg -d distdir

the final result's path will be:

    distdir/pamylka.svg

## listColors, l

the listColors command have an alias 'l' so you can do any of the following:

    svge listColors -h

or

    svge l -h

the listColors command accepts only the src argument and prints the colors that exist in the src svg file

## replace, r

The replace command have an alias 'r' so you can do any of the following:

    svge replace arguments...

or

    svge r arguments...

for help with the replace command you can type

    svge replace -h

The replace command accepts the src, output and dist arguments in addition to:

### -oc, --old-color

the old color argument is the color you want to replace in the svg file you specified as a src file, it should be in hex format

#### Ex

    svge replace src.svg -o output.svg -oc ff0000

the command above won't work but a command that starts like this will recolor any artworks that have the color f00 as a fill or stroke with the colors specified by the -nc, --new-color argument

### -nc, --new-color

The new color that will replace the -oc, --old-color in the output file, this don't have to be only one color, you can have as many colors as you want

#### Ex

    svge replace src.svg -o output.svg -oc f00 -nc #00f

also you can:

    svge r src.svg -o output.svg -oc #ff0000 -nc 00f 0f0 f00

the last command will output the following results:

    output_00f.svg,
    output_0f0.svg,
    output_f00.svg

### --no-fill and --no-strokes

Those are the only arguments for the replace command that are not required in addition to the dist argument

no fill will simply ignore any fills even if it have the save color as oc and strokes will do the same but for strokes

if the file have multiple fills or strokes with the same color and you want to execlude some, you will have to do it by hand and it's actually pretty easy! svg files are just some instructions in xml format with some style tags to style the paths, just search for them it should be similar to html

#### Ex

    svge r src.svg -o output.svg -oc 333 -nc fef --no-fill

will ignore all fills and replace only strokes that have the color 333

    svge r src.svg -o output.svg -oc 333 -nc fef --no-strokes

will ignore all strokes and replace only fill objects that have the color 333

    svge r src.svg -o output.svg -oc 333 -nc fef --no-strokes --no-fill

and this will simply do nothing to the file

## convert, c

the convert command have an alias 'c' so you can do any of the following:

    svge convert -h

or

    svge c -h

the convert command accepts the src, output and dist arguments in addition to:

### -f, --file-format

this one for choosing between jpg and png, the only accepted values are jpg and png

#### Ex

    svge c -f png

or

    svge convert -f jpg

for png and jpg photos respectivly

### -bc, --background-color

this one for specifing the background color of the result image, you can type transparent for png (this is the default value already), but transparent will also resault in a black background for jpg files! So, in order to overcome that you will have to specify the background color you want

#### Ex

    svge c {src_and_output} -f jpg -bc fff

this will output a jpg photo with a white background.

And this

    svge c {src_and_output} -f png

or

    svge c {src_and_output} -f png -bc transparent

will give the same png transparent background image as a result

### -dim, --dimensions

This is just the dimensions of the result photo as widthxheight, the default value for this is 1024x1024

#### Ex

    svge c {src_and_output} -f png -dim 100x200

will output a png photo with the dimensions 100px width x 200px height

## Thank you
