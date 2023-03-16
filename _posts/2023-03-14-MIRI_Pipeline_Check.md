---
layout: post
title:  "MIRISim Troubleshooting Part I"
date:   2023-03-14
categories: cosmos_web
---

In this post I'm going to troubleshoot why my MIRI simulations don't have any visible sources.


## Strategy

The overall structure of the code is
A) make a fits file of the scene, by drawing Sersic profiles from DREaM
B) read APT files to get information on the visits, pointings, dither patterns, ect
C) make a scene file (pointing to fits file + star catalog) and a config file (pointing to scene file and dither file)
D) run MIRISim, fixing all the WCS information
E) run JWST pipeline to check sources


It is most likely that this is going wrong at step D), since this is the step I understand the least!  I will try and isolate some of the steps though, and check how everything looks. I will start out with the simplest case, and build to more complicated tests.


## Test 1  

For Test 1, I will use the basic MIRISim functionality to generate one Sersic profile, and then check that I can recover it.


### Code:

```
####################################################
# Check I can recover input galaxy from JWST pipeline
# conda activate mirisim
####################################################

import sys,os
sys.path.insert(0,'../../../Analysis')
from MyInfo import *

##########################################
#STEP A - Make fits file (Skip)
##########################################
##########################################
#STEP B - Visit info (Skip)
##########################################
##########################################
#STEP C - Source and config files
##########################################

from mirisim.config_parser import SceneConfig, SimConfig
from mirisim.skysim import Background, Point, Galaxy, Skycube
from mirisim.skysim import sed

# Source File - just put on 1 sersic galaxy in centre
bg = Background(level = 'low', gradient = 5., pa = 45.,centreFOV=(0,0))
galaxy = Galaxy(Cen = (0,0),n=1.,re=5.,q=0.4,pa=0)
PL = sed.PLSed(alpha = 0, flux = 1e7, wref = 10.) #reference flux [microJy] at wavelength [microns]
galaxy.set_SED(PL)
targetlist = [galaxy]
scene_config = SceneConfig.makeScene(loglevel=0,background=bg,targets = targetlist)
scene_config.write('scene.ini',overwrite=True)


# Config File
sim_config = SimConfig.makeSim(
name = "mirisim",    	# name given to simulation
scene = "scene.ini", 				# name of scene file to input
rel_obsdate = 0.0,          				# relative observation date (0 = launch, 1 = end of 5 yrs)
POP = 'IMA',                				# Component on which to center (Imager or MRS)
ConfigPath = 'IMA_FULL', 					# Configure the Optical path (MRS sub-band)
Dither = False,             				    # Dither
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

sim_config.write('config.ini',overwrite=True)

##########################################
#STEP D - Run MIRISim
##########################################
from mirisim import MiriSimulation
mysim = MiriSimulation.from_configfiles('config.ini')
mysim.run()
```

### Plots:

Here is the raw MIRISim image (left), and after running the pipeline (right)

<img src="{{ site.baseurl }}/assets/plots/20230314_Test1.png">


### Notes:

- I had trouble setting the background FOV to anything other than (0,0), and still making sure the galaxy was in the field. This might be where my problem is when trying to create MIRI images before
- The Pipeline seems to be working fine, but the object I put in is unrealistically large/bright. I need to check for a fainter galaxy
- The object isn't located in the very centre, like I expected - note that I set Dither to False, so it shouldn't be using the specified dither pattern
- In the raw image, the WCS says the bottom corner is (0,0), while in the pipeline image, the WCS says the galaxy is at (0,0). The centre of the image is  (0.0055, -0.0004) degrees, or (19.8, -1.48) arcsec. Using the resolution 0.11 arcsec/pixel, this translates to approximately (180, 14) pixels


Looking at the documentation more:
<img src="{{ site.baseurl }}/assets/plots/20230314_reference_coord.png">

It seems like the centre FOV is not actually in the centre of the image, but offset by about ~175 pixels in one of the directions. This accounts for the offset in the image!


## Next Steps

In a future post, I'll continue testing, and figuring out how this code works. The next couple of tests I'll run are:

- Test 2: include reading in APT and dither files (i.e. include some of step B)
- Test 3: save scene as fits file (i.e. include some of step A). How do galaxy fluxes compare to DREaM?
