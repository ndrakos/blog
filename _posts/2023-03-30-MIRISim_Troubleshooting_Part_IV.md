---
layout: post
title:  "MIRISim Troubleshooting Part IV"
date:   2023-03-30
categories: cosmos_web
---

In this post I'm going to troubleshoot why my MIRI simulations don't have any visible sources.

This is a continuation of:

<a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_I/">Part I</a>

<a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_II/">Part II</a>.

<a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_III/">Part III</a>.



## Test 4

For Test 4, I will read in a FITS file with just 1 test galaxy, where I make the fits file using the MIRISim capabilities.



### The Source

Here is my code for making a FITS file. The example galaxy is the same, bright, large, galaxy used in Troubleshooting I.


```

from mirisim.config_parser import SceneConfig, SimConfig
from mirisim.skysim import Background, Point, Galaxy, Skycube
from mirisim.skysim import sed


galaxy = Galaxy(Cen = (0,0),n=1.,re=5.,q=0.4,pa=0)
PL = sed.PLSed(alpha = 0, flux = 1e7, wref = 10.) #reference flux [microJy] at wavelength [microns]
galaxy.set_SED(PL)
scene = galaxy

FOV = np.array([[-57.,57.],[-57.,57.]]) # field of view [xmin,xmax],[ymin,ymax] (in arcsec)
SpatialSampling = 0.1 # spatial sampling (in arcsec)
WavelengthRange = [5,15] # wavelength range to process (in microns)
WavelengthSampling = 0.5 # channel width (in microns)
scene.writecube(cubefits = 'scene.fits',
FOV = FOV, time = 0.0,
spatsampling = SpatialSampling,
wrange = WavelengthRange,
wsampling = WavelengthSampling,
overwrite = True)
```

Here is what the source looks like:

<img src="{{ site.baseurl }}/assets/plots/20230330_Source.png">

Notes:
- the image is centred in the middle of the image, as expected
- for some reason the image is tilted. I'm not sure why it isn't a square in -57 to 57? This doesn't seem to effect how it is read into MiriSim though, so I'm not too worried

Here is the header:

<img src="{{ site.baseurl }}/assets/plots/20230330_SourceHeader.png">




### MIRISim Results  


Here is the first dither/observation:

<img src="{{ site.baseurl }}/assets/plots/20230330_Test4.png">


Notes:
- This is located in the same place as in <a href-"https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_II/">Test 2</a>, as expected. However, the galaxy is rotated. I'm not worried about this for now, since the orientation in the source FITS file and the simulated data match
- Overall, this looks about what I would expect, and gives a good baseline to compare what I've been working on!


### Comparison of test galaxy to my DREaM files

Here is the header for the DREaM file:

<img src="{{ site.baseurl }}/assets/plots/20230330_DREaMHeader.png">

One obvious thing to do is check that I am specifying the UNITS for the DREaM header. Other than that, nothing obvious pops out at me.


## Next Steps

There are two different things to pursue to fix this...

1. Fix the DREaM fits files
- Specify units properly
- Check visually a cutout from the fits file versus some of the cutouts from the Mirage simulations

2. Use the test galaxy to really understand the pointings/whether I'm setting the WCS right
- Run this example through the full MIRISim code, check the WCS of the final images. 
