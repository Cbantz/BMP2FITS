from PIL import Image
import numpy as np
from astropy.io import fits
from pathlib import Path



def convert_bmp_fits(filepath: str, save_dir: str, header = None):
    '''
    Converts a grayscale bitmap (.bmp) image to a FITS (.fits) file.

    Arguments:
     filepath: The path to the bitmap image you want to convert.
     save_dir: The path to the directory you want to save the created FITS image in.
     headers (optional): astropy.io.fits.header.header() object to use as the header of the new FITS file.
    '''
    with Image.open(filepath) as img:
    
        img_name = Path(filepath).stem
        img_array = np.array(img)
        img_mirror = np.flipud(img_array) #PIL loads upside down by default. Flipping gives original orientation.
        fits.writeto(f"{save_dir}/{img_name}.fits", img_mirror, header=header, overwrite=True)

    return f"{save_dir}/{img_name}.fits"