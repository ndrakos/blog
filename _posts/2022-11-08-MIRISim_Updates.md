---
layout: post
title:  "MIRISim Updates"
date:   2022-11-08
categories: cosmos_web
---

I am going to use MIRISim to make mock MIRI images, as I outlined <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim/">here</a>.


## Scene

Previously, I created a scene (i.e. a FITS image with galaxies) as described in <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Scene_Part_II/">this post</a>. This was a "test catalog" with only the brightest sources.

In the previous post, I showed how the scene visually looked a little strange, but noted it might be because of the way the image was displaying. I have checked the galaxy properties, and everything looks okay so far.

I'm going to try running this test scene through MIRISim and see if it looks better once the noise is added on.

You can test that it will load by using:

```
from mirisim.skysim import Skycube
s = Skycube(myfile)
```

### Issue 1: Data Cube

At first it crashed with an error: <code>assert(source_hdr["NAXIS"] == 3)</code>. This is because the scene file actually needs to be a data cube to be read by MIRISim.

Therefore, the fits file need to be changed as follows:

```
cube = np.array([mydata,mydata,mydata])
hdu_new = fits.PrimaryHDU(cube)
hdu_new.header = sources_hdul[0].header
hdu_new.header['CRVAL3']=7.7
hdu_new.header['UNIT3']='um'
hdu_new.header['CTYPE3']='WAVE'
hdu_new.writeto('cube.fits',overwrite=True)
```

### Issue 2: BUNIT

There is a warning "Keywords UNITS or BUNIT not found. Assuming microjansky/arcsec^2". I THINK those are the correct units, but I should double check this and set BUINT properly. I'll leave this for now because it still runs.


### Issue 3: Memory

My computer ran out of memory, and it crashed with the "Skycube" command. So it looks like I will need to specify smaller scenes. This is definitely fine, but I will need to be careful that I am creating a large enough area for each dither pattern. I will need to re-create a scene for each pointing OR create a large FITS image with all the sources, and take slices for each pointing. I think, in the interests of compute time, it makes more sense to do the latter.



## Test Running MiriSim

Now that I have a scene file, I am running MiriSim with the background specified as follows in the <code>scene.init</code> file:


```
[sky]
  name       = sky0                     # Name of sky scene.
  loglevel   = 0                        # 0: no log, 1: single summary, 2: full report.

[Background]
  gradient   = 5                        # % over 1 arcmin (JWST component only).
  pa         = 45                       # position angle of gradient (background increasing towards PA).
  centreFOV  = 540429 7941              # centre of FOV.
  level      = low                      # Background with the G-component of the model included 'high' or missing 'low'.
  fast       = 0                        # Use or not the 2.5D speed up when flux(RA, DEC, WAV) = flux1(RA, DEC) * flux2(WAV).

[skycube_1]
  Type       = SkyCube                  #
  cubefits   = /Users/nicoledrakos/Documents/Research/Projects/CW_Image/Miri/testsources.fits             # filename of the cube .fits.
  fits_ext   = 0                        # the index of the fits file extension where the data cube is stored. 0 index by default if you omit the keyword.
  center     = yes                      # If yes, the input file is centered anyway, and astrometry ignored.
  method     = 1                        # Interpolation method selected (0, 1 or 2, default is 1).
  conserve   = wave                     # how the flux is conserved (full or wave, default is wave).

```

I am running this with dithering set to False, and only for one pointing.

This ran fine, but would struggle a lot unless the scene was a very small area (see memory issue above). Therefore, I will need to make sure to appropriately cut the fits image for every pointing.


## Adding All Sources to Scene

There are $$10^7$$ sources in the full DREaM catalog, and ~40000 in "test" catalog.

I timed the code, and it takes about 1 minute for every 1000 sources. Therefore it would take a week to run the whole catalog in serial (it takes ~40 minutes for the test catalog). Therefore, I want to parallelize this code. This should be straightforward

### Parallelizing Attempt 1 -- Lux

I'm having trouble with mpi4py on lux. When I put <code>from mpi4py import MPI</code>:

```
The application appears to have been direct launched using "srun",
but OMPI was not built with SLURM's PMI support and therefore cannot
execute. There are several options for building PMI support under
SLURM, depending upon the SLURM version you are using:

version 16.05 or later: you can use SLURM's PMIx support. This
requires that you configure and build SLURM --with-pmix.

Versions earlier than 16.05: you must use either SLURM's PMI-1 or
PMI-2 support. SLURM builds PMI-1 by default, or you can manually
install PMI-2. You must then build Open MPI using --with-pmi pointing
to the SLURM PMI library location.
```

I tried reinstalling mpi4py (making sure I was careful about what modules were imported), and also installing it in a conda environment. None of this seemed to really work. For now, I'll run on Candide instead.

### Parallelizing Attempt 2 -- Candide

Initially, the conda install of mpi4py failed (error message was something about MPI linking), but I managed to get it working with

<code> conda install -n jwst -c conda-forge mpi4py mpich  </code>

I then parallelized the scene code. Ran into a couple small issues, and really would rather use lux for a few reasons.

### Parallelizing Attempt 3 -- Lux again

I realized that if I went into a compute node and typed

```
import mpi4py
mpi4py?
```
The path to mpi4py was not what it should be in the conda environment. So I pip uninstalled mpi4py, and then everything worked!

Therefore, I am ready to run this code on lux :)


## Next Steps

1. Pass a test image onto Santosh and/or Daizhong. Make sure we are in place to analyze these. I can then iterate with them if there are any obvious issues with my images.

2. Run the full scene on lux (decide the exact bounds for this image).

3. Decide how I am specifying the pointings/dithering patterns. I then need to calculate how much of scene I need to read in for each of these pointings. Then, for each pointing, I will (1) read in full scene (2) take slice that I need (3) save it as a 3D datacube, as outlined above.

4. Generate test images for the full catalog, for one December pointing.

5. Include Stars (decide how to do this... maybe Jed is already putting in a star catalog, and I can use his.)


## Things to check

1. Are the units correct in BUNIT?

2. Is the pixel resolution of the FITS image fine, or should i make it more precise?

3. Right now I am just repeating the same image to make a data cube. How does MIRISIM interpolate between images in the cube?
