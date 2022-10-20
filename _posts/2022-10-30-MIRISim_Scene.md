---
layout: post
title:  "MIRISim Scene"
date:   2022-10-18
categories: cosmos_web
---


In this post I'm going to go through creating a MIRISim Scene from components. An alternative is to give MIRISim a FITS image. This is what Jed is using to simulate the COSMOS2020 catalog. If I decide to go this route, Vasily will send his code to create an image using astropy.

## Components

### Background

The background created in MIRISim includes thermal emission of JWST, Zodiacal light, ect.

Here is how to create the background in Python:

```
from mirisim.skysim import Background
bg = Background(level = 'low', gradient = 5., pa = 45., centreFOV=(0,0))
```

This is a "low" level of background that has a 5 percent gradient over 1 arcmin. The position angle of the gradient is 45, and the centre of the image is (0,0). These are the example values, and I'm not sure what they should be set to.

I'm not sure how sophisticated this background model is, and whether I have the option to specify a background in a different way.


### Extended Sources

You can specify the location, sersic index, radius, shape and position angle of the galaxy as:

```
galaxy = Galaxy(Cen = (0.,0.),n=1.,re=1.,q=0.4,pa=0)
```

I am pretty sure Cen is the offset from the center of the scene (which might be specified by the background?)

You also need to specify an SED. I will assume it is flat in fnu, and use the powerlaw model:

```
PL = sed.PLSed(alpha = 0, flux = 1e3, wref = 10.) #reference flux [microJy] at wavelength [microns]
galaxy.set_SED(PL)
```



### Point Sources

For now, I will not include stars.

The star list I have doesn't have magnitudes for this filter. I will likely just assume a blackbody spectrum and use one of the magnitudes in the star catalog as the reference magnitude. This requires a temperature for the star

## Simulation Config File

Here is what I have for the configuration currently:

```
sim_config = SimConfig.makeSim(
    name = "mirisim",    	# name given to simulation
    scene = scene_file, 				# name of scene file to input
    rel_obsdate = 0.0,          				# relative observation date (0 = launch, 1 = end of 5 yrs)
    POP = 'IMA',                				# Component on which to center (Imager or MRS)
    ConfigPath = 'IMA_FULL', 					# Configure the Optical path (MRS sub-band)
    Dither = True,             				    # Dither
    StartInd = 1,               				# start index for dither pattern
    DitherPat = 'ima_recommended_dither.dat', 	# dither pattern to use
    filter = 'F770W',          					# Imager Filter to use
    ima_mode = 'FAST',         					# Imager read mode (default is FAST ~ 2.3 s)
    ima_frames = 45,            				# number of groups (for MIRI, # Groups = # Frames)
    ima_integrations = 2,      					# number of integrations
    NDither = 4,                				# number of dither positions
    ima_exposures = 8,         					# number of exposures
    readDetect = 'FULL',         				# Portion of detector to read out
    disperser = 'SHORT',        # [NOT USED HERE]
    detector = 'SW',            # [NOT USED HERE]
    mrs_mode = 'SLOW',          # [NOT USED HERE]
    mrs_exposures = 2,          # [NOT USED HERE]
    mrs_integrations = 3,       # [NOT USED HERE]
    mrs_frames = 5,             # [NOT USED HERE]
)
```

Caitlin sent some information on the actual dither pattern, so I will look into updating this later.

## Testing

I created a scene using a my "test" catalog (the brightest sources in DREaM) and ran it.

### Error 1

<code>ValueError: Unknown format code 'g' for object of type 'str'</code>

I tracked it down to the fact that the path of my scene file (specified in the simulation config file) had a space in it. I put it in a different path and it was fine.

### Error 2


<code>There appear to be 2 leaked semaphore objects to clean up at shutdown</code>

This looks like a memory error to me. I tried decreasing the area of the scene (only including galaxies in that small patch of sky), and only do one pointing at a time. Neither of these fixed the error. I think I'm going to use Vasily's code to make the scene instead.


## Next Steps

1. Make scene as FITS file (using Vasily's code)
2. Update dither patterns
3. How should I set the background? I think I can either add it to the scene, or include it as shown earlier in the post
4. Add stars 
