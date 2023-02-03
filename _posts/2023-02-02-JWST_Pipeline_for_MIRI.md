---
layout: post
title:  "JWST Pipeline for Miri"
date:   2023-02-02
categories: cosmos_web
---

The current status of the MIRISim simulations is that I have a running version that will read in a my scene file and star catalog, and APT files and create output, but (1) the WCS of the observations isn't right and (2) I haven't checked the sources look okay.

For troubleshooting MIRISim, it would be helpful to have some reduced images, so that I could see where the sources are! In this post I'll go through using the pipeline on the simulated MIRI images.

I am going to focus on Observation 43, seq 1, exposure 1.


## MIRI Pipeline

I went over the basic pipeline for NIRCam in <a href="https://ndrakos.github.io/blog/cosmos_web/JWST_Pipeline/">this post</a>. Some later posts also fixed the 1/f noise, and mosaic step. For now, I won't worry about this though!

Other than fixing some paths, I think the basic pipeline should run with basically the same code.

## Files

The "uncal" files are produced by MIRISim. The first step of the pipeline returns "rate" files, and the second step returns "cal" files.

Here are these three files:

<img src="{{ site.baseurl }}/assets/plots/20230202_pipeline.png">

and zoomed in:

<img src="{{ site.baseurl }}/assets/plots/20230202_pipeline_zoom.png">

It's not really clear whether I ran the pipeline ran right. Maybe the sources never actually got added? I should check this.

## Sources

MIRISim could not take in the FULL scene without crashing, so for each observation I cut out the relevant part of the scene. Here is the scene cut-out for Obs43:

<img src="{{ site.baseurl }}/assets/plots/20230202_cutout.png">


Note this looks a little funny, which I decided has to do with the fact I didn't use a background so it scales a little weird (see <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Scene_Part_II/">previous post</a>).

One thing I noticed is that the WCS doesn't display in DS9. It IS in the header though. So my thought is that this has something to do with the way the data cube is saved. I'm not sure If I'm doing something wrong, or if ds9 just has trouble reading data cubes.

When I save the cutout as a regular fits file (not a data cube) I can see the wcs, and compare to the MIRISim output

<img src="{{ site.baseurl }}/assets/plots/20230202_cutout_check.png">


Clearly the cutout is (1) not big enough and (2) the observation WCS is not centred where it should be (which we knew already)


I fixed the source cutout sizes; I was saving 0.01degx0.01deg, which is smaller than the Miri FOV! I changed it to 0.1deg x 0.1deg, which should be much larger than necessary. I will have to check with the dither pattern though, and possibly save an even bigger version!

## Rerun with larger cutout

Given the bigger scene, I reran MIRISim and the pipeline, and got the following:


<img src="{{ site.baseurl }}/assets/plots/20230202_pipeline2.png">

Either the objects are not placed in the image correctly, or I am running the pipeline wrong -> this will be the next thing I check.


## Next Step

Next I will run MIRISim with a couple of fixed objects (not trying to fix the pointings at all), and then run the images through the pipeline to check if its the pipeline step that is wrong.
