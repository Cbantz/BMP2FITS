# About

Bmp2fits is a tool to convert bitmap (.bmp) files to flexible image transport system (.fits) files.

# Highlights

- Usable as a CLI or python package.
- Free and open source using the MIT License.

# Getting Started

Bmp2fits can be installed from this repo using pip.

`pip install git+https://github.com/Cbantz/BMP2FITS.git`

After installation, you can use bmp2fits as a command line interface (CLI) or as a python package.

## Using CLI

Using the CLI takes a basic command structure:

`bmp2fits [input_path] [output_path] [args]`

- \[input_path\] is a path to either a .bmp file or a directory containing .bmp files that you wish to be converted.
- \[output_path\] is the location you wish the .fits file to be saved. It can be either a directory (recommended) or a file path.
- \[args\]
    - \--overwrite will overwrite any existing files with the same name in an output path when saving your converted files.
    - \--verbose will print confirmations of each image as it is converted and saved.

**NOTES:**

- Currently, if given a directory as an \[input_path\], the CLI will convert all .bmp files in said directory.
- If a directory is given for the \[output_path\], files will be saved as their original name but with .fits instead of .bmp
    - e.g. input_path/image.bmp -> output_path/image.fits
- You will get an error if you try to overwrite without using the overwrite flag.

## Using Python Package

Bmp2fits can be imported into your project using

`import bmp2fits`.

The only function you are likely to use is bmp2fits.convert().

This function, much like the CLI, takes arguments for bmp_path, output_path, overwrite, and verbose.

Unlike the CLI, the python package is not designed for converting an entire directory. Rather, it converts individual files, passed via the bmp_path argument, and saves them to the output_path, which has the same rules as the CLI. If you wish to convert full directories in python, this is easily accomplished using [glob](https://docs.python.org/3/library/glob.html).

Working in python gives you the option to add headers to your converted FITS file by passing an [astropy.io.fits.Header](https://docs.astropy.org/en/latest/io/fits/api/headers.html#astropy.io.fits.Header) object.

&nbsp;