---
layout: post
title:  "World Coordinate System"
date:   2021-11-30
categories: mocks
---


These notes are on the (<a href="https://fits.gsfc.nasa.gov/">FITS</a>) World Coordinate Systems standard. An overview of representing celestial coordinate systems is given <a href="
https://www.atnf.csiro.au/people/mcalabre/WCS/Intro/"> here</a>.


## Our Catalog

Each galaxy has an RA and Dec centred on (0,0) spanning from -0.5 to 0.5 degrees. There are 0.11 arcsec per pixel.


## Implementation in Astropy

I followed <a href="https://docs.astropy.org/en/stable/wcs/example_create_imaging.html">this</a> example.

For our problem:

```
deg_per_pix = 0.11/3600
num_pixels = 1.0/deg_per_pix

w = wcs.WCS(naxis=2)
w.wcs.ctype = ["RA---TAN", "DEC--TAN"] # projection type
w.wcs.crpix = [0,0] # (X,Y) reference pixel
w.wcs.crval = [-0.5,-0.5] # Sky coord of reference pixel in degrees
w.wcs.cdelt = np.array([deg_per_pix, deg_per_pix]) # increment (X,Y) in degrees
```


## Testing

Start with some pixel coordinates: <code> pixcrd = np.array([[0, 0], [num_pixels,num_pixels], [num_pixels/2, num_pixels/2], [0,num_pixels]]) </code>.

To get the corresponding world coordinates: <code> world = w.all_pix2world(pixcrd, 0) </code>

```
array([[-4.99969443e-01, -4.99969444e-01],
       [-3.59500185e+02,  4.99852916e-01],
       [-1.17812552e-06,  1.78607360e-05],
       [-4.99969448e-01,  4.99929026e-01]])
```

This all looks fine. Note that -359.5 is the same as 0.5 degrees. Then, to convert back to pixels, we can use <code> pixcrd = w.all_world2pix(world, 0) </code>.

## Saving the WCS with the FITS Files

When writing the FITS file, we can include the WCS as follows:

```
header = w.to_header()
hdu = fits.PrimaryHDU(header=header)
```
