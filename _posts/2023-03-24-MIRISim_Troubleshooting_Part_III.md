---
layout: post
title:  "MIRISim Troubleshooting Part III"
date:   2023-03-24
categories: cosmos_web
---

In this post I'm going to troubleshoot why my MIRI simulations don't have any visible sources.

This is a continuation of <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_I/">Part I</a> and <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_II/">Part II</a>.


## Test 3

For Test 3, I will expand upon the working Test 2 case (see the previous post), and include the proper scene cutouts (from DREaM).



### Code:

Part B: I added this code

```
##################################
# c) Cut out Scene
##################################
from astropy.nddata import Cutout2D
from astropy import units as u
from astropy.coordinates import SkyCoord
scene_size = 0.1 #Size of cutout for each visit, in degrees

#Load full scene
hdu = fits.open(source_file)[0]
wcs = astropy.wcs.WCS(hdu.header)
image_data = hdu.data.copy()


for i in range(num_visits):
    #Get info
    obs = obs_num[i]
    df = data_frames[i]
    mypath = 'Obs' + str(obs) + '/'
    telescope_v1_ra = df['RA'].iloc[0] # all RA must be the same in a dither sequence
    telescope_v1_dec = df['Dec'].iloc[0] # all Dec must be the same in a dither sequence
    pos = SkyCoord(telescope_v1_ra ,telescope_v1_dec,unit='deg')

    #Cut out
    cut_im = Cutout2D(image_data,wcs=wcs,position=pos,size=(scene_size*u.deg),mode="trim",copy=False)

    hdu_cutout = fits.PrimaryHDU(np.array([cut_im.data,cut_im.data,cut_im.data]))
    hdu_cutout.header = hdu.header.copy()
    hdu_cutout.header.update(cut_im.wcs.to_header())
    hdu_cutout.header['CRVAL3']=7.7; hdu_cutout.header['UNIT3']='um'; hdu_cutout.header['CTYPE3']='WAVE'
    hdu_cutout.header['CDELT3']=0.1; hdu_cutout.header['CRPIX3']=1.0
    hdu_cutout.writeto(mypath + 'sources.fits', overwrite=True)
```

Part C is now:

```
##########################################
#STEP C - Source and config files
##########################################

from mirisim.config_parser import SceneConfig, SimConfig
from mirisim.skysim import Background, Point, Galaxy, Skycube
from mirisim.skysim import sed

myobsfile = pointing_file.split('/')[-1].split('.')[0]
myobsfile = myobsfile+ '.obs'
obs_num = np.loadtxt(myobsfile)


# Star Catalog
starlist = []
starcat = np.loadtxt(starcat)
refw = 7.7 #microns

for i,s in enumerate(starcat):
    pos = np.array([s[1]-ra_offset,s[2]-dec_offset]) #ra,dec
    pos = pos*3600 #offset in arcsec
    star = Point(Cen=pos)
    mag = s[-1]
    flux = 3631e6*10**(-mag/2.5) #microJy
    PL = sed.PLSed(alpha = 0.0, flux = flux, wref = refw)
    star.set_SED(PL)
    starlist.append(star)


for obs in obs_num:

    mypath = 'Obs' + str(int(obs)) + '/'

    # Source File - just put on 1 sersic galaxy in centre
    bg = Background(level = 'low', gradient = 5., pa = 45.,centreFOV=(0,0))
    s = Skycube(mypath+'sources.fits')
    s.fitsFilename = 'sources.fits'
    targetlist = np.append(s,starlist)
    scene_config = SceneConfig.makeScene(loglevel=0,background=bg,targets = targetlist)
    scene_config.write(mypath+'scene.ini',overwrite=True)


    # Config File
    sim_config = SimConfig.makeSim(
    name = "mirisim",    	# name given to simulation
    scene = "scene.ini", 				# name of scene file to input
    rel_obsdate = 0.0,          				# relative observation date (0 = launch, 1 = end of 5 yrs)
    POP = 'IMA',                				# Component on which to center (Imager or MRS)
    ConfigPath = 'IMA_FULL', 					# Configure the Optical path (MRS sub-band)
    Dither = True,             				    # Dither
    StartInd = 1,               				# start index for dither pattern
    DitherPat = 'dither.dat', 	# dither pattern to use
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
    sim_config.write(mypath+'config.ini',overwrite=True)
```

### Plots:

There are now sources in the image! Here is the uncal, and cal file (after running through the pipeline), matched in WCS:

<img src="{{ site.baseurl }}/assets/plots/20230324_Test3a.png">

Checking without stars, and only galaxies:

<img src="{{ site.baseurl }}/assets/plots/20230324_Test3b.png">


### Notes:

- Still doesn't seem like the galaxies are working. Maybe they are just too small/faint?
- Running the pipeline changes the WCS of the raw image. Why is this?


## Next Steps

Here is the current plan for the next tests:

- Test 4: Dig into the source creation a little more. Make a fits file with ONE objects, make sure it is in the right location. 
- Test 5: Look into the "Run" step, make sure I am setting the WCS information correctly. Does the WCS of the images match the dither pattern? Is the angle, ect, correct?
- Test 6: Are the sources and stars in the right places?
- Test 7: Do the sources and stars have the right fluxes?
