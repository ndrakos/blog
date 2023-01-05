---
layout: post
title:  "MIRISim Updates Part IV"
date:   2023-01-04
categories: cosmos_web
---

In this post, I am going to do a quick check on the MIRI data, and add stars to the images.


## Quick WCS Check

My first check is that the raw images span the correct WCS. For this post, I will focus on Observation 43.

This should be located at an RA and Dec of 149.9296 deg and 2.4317 deg. Each visit has 4 dithers, each with 8 exposures.

The dither pattern I have calculated is (in pixels; note 200 pixels ~ 0.005 degrees):
```
-224.2712,-9.6723
-221.4668,+44.1934
+224.2700,+10.3781
+221.1110,-43.5871
```

For now I will assume this is the correct dither pattern. It is very similar to Daizhong's calculation (about 0.1 pixel off).

When I check the location of (149.93, 2.43) in each 4 dithers, I find the following:

<img src="{{ site.baseurl }}/assets/plots/20230104_miri_test.png">


The centres of these do not look quite right! The angle looks roughly right, but I don't know how to check what it should be. Fixing this will be the subject of my next post. Right now it is unclear whether the image is correct, but the WCS is wrong, or vice versa!


## Add Stars

Max gave me a star catalog for the MIRI filter.

I added it into the target list in the MiriC-Config script. Here is my script for defining the stars

```
##################################
# Get star catalog
##################################
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
```


This added a bunch of entries to the scene.ini file, as follows:

```
[point_9515]
  Type       = Point                    # Type of target.
  Cen        = -262.406 1097.42         # Where to place the target (arcsec offsets from centreFOV).

  [[sed]]
    Type       = PL                     # Type of spectral energy distribution (e.g. Power law spectrum).
    alpha      = 0                      # Exponent.  Zero: flat spectrum.
    b          = 0                      # {optional} additional constant [muJy].
    wref       = 7.7                    # {optional} reference wavelength (in micron).
    flux       = 85.1017                # {optional} Reference flux (in microJy) for scaling the power law function.
  ```

This seemed to run correctly in the "run" step. 


## To-do/check

So the main thing I need to do next is figure out why the observation is not centred correctly. Some ideas I have for what to check next:

1. Download a real observation, check to see what the FITS header looks like

2. Run observation through the basic pipeline, check if objects have the right positions


Other things to check (from previous posts):

1. Are the units correct in BUNIT?

2. Is the pixel resolution of the FITS image fine, or should i make it more precise?

3. Right now I am just repeating the same image to make a data cube. How does MIRISIM interpolate between images in the cube?

4. I am cutting out 0.01x0.01 degrees of the scene around the centre of the visit. Is this enough? -> Can double check this when I run the basic pipeline on the MIRI images
