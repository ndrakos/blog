---
layout: post
title:  "JWST Pipeline - Stage 3"
date:   2022-08-30
categories: cosmos_web
---

In the <a href="https://ndrakos.github.io/blog/cosmos_web/Add_Catalog_to_Mirage/">previous post</a> I generated a mosaic of the DREaM simulated catalog. There are a few things to fix in Stage 3 of the pipeline (this stage combines the calibrated images into a mosiaic), which I will document here.  


## Separating the Association Files

It looks like the pipeline mosaics all the images you give it, regardless if they are in separate filters. I updated my code to make association files so that it only takes files of a specific filter.

Here is an example of what the 150W image looks like now:

<img src="{{ site.baseurl }}/assets/plots/20220830_cw-F150W_1.png">


## Steps in Stage 3

### 1. Refine relative WCS ("tweakreg")

This step uses point sources that are common to two or more images, and uses these locations to correct the WCS of the input images.

Micaela suggested we turn this off, as it "can make the sources all look slightly smeared out even if the images are aligned, and that's a result of TweakReg trying to apply corrections to individual exposures that already have correct WCS".

I think I can just turn this off by setting "image3.tweakreg.skip=True" if I call the whole pipeline.

### 2. Moving target WCS ("assign_mtwcs")

This is only for moving target data, it is not relevant to me. (if I call the whole pipeline, I will just set "image3.assign_mtwcs.skip=True")


### 3. Background matching ("skymatch")

"This step corrects the overall background level of each image so that the overlapping regions of the images have the same background"

This is the step that probably needs to be refined, so I will dig into this a little (see additional documentation on this step <a href="https://jwst-pipeline.readthedocs.io/en/stable/jwst/skymatch/
">here</a>).

Micaela said "The SkyMatch Step in Stage 3 also calculates the sky background, but it tries to match the sky across detectors and it's not flexible enough (hence why you'll do your own subtraction first). But it does add important keywords to the headers." and they run it with 1. SkyMatch step with subtraction set to false 2. Their own background subtraction (calculated from the median after sigma clipping) and 3. Running resample to fix the headers (updating the headers with the new background value and telling it that the background has been subtracted)

Here are the possible parametrs in skymatch:

General sky matching parameters:
- skymethod = option('local', 'global', 'match', 'global+match', default='match') # sky computation method
- match_down = boolean(default=True) # adjust sky to lowest measured value?
-  subtract = boolean(default=False) # subtract computed sky from image data? #
Image's bounding polygon parameters:     
- stepsize = integer(default=None) # Max vertex separation        
Sky statistics parameters:
- skystat = option('median', 'midpt', 'mean', 'mode', default='mode') # sky statistics      
- dqbits = string(default='~DO_NOT_USE+NON_SCIENCE') # "good" DQ bits      
- lower = float(default=None) # Lower limit of "good" pixel values       
- upper = float(default=None) # Upper limit of "good" pixel values        
- nclip = integer(min=0, default=5) # number of sky clipping iterations        
- lsigma = float(min=0.0, default=4.0) # Lower clipping limit, in sigma        
- usigma = float(min=0.0, default=4.0) # Upper clipping limit, in sigma       
- binwidth = float(min=0.0, default=0.1) # Bin width for 'mode' and 'midpt' skystat, in sigma


It looks like if you set the skymethod to local, it will essentially do sigma clipping on each image. So I will do this. The default sky statistic parameters all look reasonable.

I will just stick with this, since I don't have any methods more sophisticated than sigma-clipping for background estimation!


### 4. Outlier detection

"A 2nd pass at outlier detection is done using the overlapping regions observed in different exposures. The majority of the outliers will be due to cosmic rays undetected during the 1st pass at outlier detection done" in Stage 1


### 5. Imaging combination

Combines images into a mosaic using AstroDrizzle

### 6. Source catalog

Source catalogs created using Astropy Photoutils package. "The goal of this step is to produce a good quality catalog that can be used as a basic 1st-pass source list."

### 7. Update exposure level

"The exposure level products are re-created at this stage to provide the highest quality products that include the results of the ensemble processing (updated WCS, matching backgrounds, a 2nd pass outlier detection)."


## Summary

I tried altering some of the defaults for the "SkyMatch" step, but nothing really made much of a difference. Here is what the output for F115W, F150W, F277W and F444W look like:

<img src="{{ site.baseurl }}/assets/plots/20220830_cw-F115W.png">

<img src="{{ site.baseurl }}/assets/plots/20220830_cw-F150W.png">

<img src="{{ site.baseurl }}/assets/plots/20220830_cw-F277W.png">

<img src="{{ site.baseurl }}/assets/plots/20220830_cw-F444W.png">

I'm not sure if the background subtraction is good enough. I'm also not sure about the black lines in the image, and if I should be able to get rid of those (this seems to be because of black borders around each pointing... does this happen in the pipeline somewhere?).

## Other Things to Look Out For

This post focused on Stage 3, but it was also suggested I provide my own gain maps for Stage 1 (MIRAGE uses a single mean value for each detector while the gain reference files vary across the detector).
