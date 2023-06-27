from astropy.io import fits
from astropy.coordinates import SkyCoord
from reproject.mosaicking import find_optimal_celestial_wcs



def mosaic_output(filenames):
    fits_files = [fits.open(f)[0] for f in filenames]
    wcs_out, shape_out = find_optimal_celestial_wcs(fits_files)
    from reproject import reproject_interp
    from reproject.mosaicking import reproject_and_coadd
    array, footprint = reproject_and_coadd(fits_files,
                                        wcs_out, shape_out=shape_out,
                                        reproject_function=reproject_interp, match_background=True) 
    hdu = fits.PrimaryHDU(array)
    hdul = fits.HDUList([hdu])
    hdul.writeto('mosaic_output.fits')

    return array, footprint