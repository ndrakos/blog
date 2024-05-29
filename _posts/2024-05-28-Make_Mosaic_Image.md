---
layout: post
title:  "Make Mosaic Image"
date:   2024-05-28
categories: cosmos_web
---

I want to make a pretty image of the DREaM mosaic for the paper. I'm going to use the code <a href="https://github.com/dancoe/trilogy">Trilogy</a>

## Mosaic files

There are 20 tiles, each with four different filters (80 FITS files). 
There are also two different resolutions (60mas and 30 mas). I'll be working with the 60 mas files, since they are smaller.

I downloaded the A1 file, but strangely the file sizes are different --- they are 12 GB for the F115W and F150W files, 
but 5 GB for the F266 and F444 files. I'm not sure why this should be the case if they are the same resolution. 
It seems what is different in the FITS files is the parameter  "PXSCLRT", the "Pixel scale ratio relative to native detector". 
I'll need to check in about this. 


## Running Trilogy

- I downloaded the python code from https://github.com/oliveirara/trilogy
- I made an init file <code>input.txt</code> that had the following:

<pre><code>
B
mosaic_nircam_f115w_DREaM_COSMOS-Web_60mas_A1_i2d.fits[1]

G
mosaic_nircam_f150w_DREaM_COSMOS-Web_60mas_A1_i2d.fits[1]

R
mosaic_nircam_f277w_DREaM_COSMOS-Web_60mas_A1_i2d.fits[1]
mosaic_nircam_f444w_DREaM_COSMOS-Web_60mas_A1_i2d.fits[1]

indir  /Users/nicoledrakos/Work/Research/Projects/CW_Image/mosaics
outname  test
samplesize 1000
stampsize  1000
showstamps  0
satpercent  0.001
noiselum    0.15
colorsatfac  1
deletetests  0
sampledx  0
sampledy  0
</code></pre>

- I then ran the code as <code>python ~/Documents/Software/trilogy/trilogy/trilogy.py input.txt</code>
 


## Initial Results

Here are my initial results (low-resolution):

<img src="{{ site.baseurl }}/assets/plots/20240528_TestImage.png">

One thing that I noticed are some of the F444W galaxies seem to be oriented wrong compared to the other galaxies:


<img src="{{ site.baseurl }}/assets/plots/20240528_TestImageZoom.png">

I need to dig into this, but I suspect that some of the visits weren't updated with the correct orientations when the mosaic was made.



## Playing with Parameters

satpercent - "Percentage of pixels which will be saturated."
noiselum - "Noise luminosity for single channel (between 0 - 1)". Too small, you don't see the faint galaxies. Too big, you see a lot of the noise. 0.1 seems to work well. 
When you increase this the the galaxies "pop" more, but you lose some of the detailed structure. I changed this to 0.005
colorsatfac - "> 1 to boost color saturation.". When you decrease this the image looks more white, when you increase it it looks more red. I left it at 1. 

Here's how the tile changes with the new parameters (still very low resolution)

<img src="{{ site.baseurl }}/assets/plots/20240528_TestImage2.png">

It doesn't look that different from the initial parameters, but I'm pretty happy with that for now. 


## To Figure Out

- Why are files different sizes
- Why are some galaxies tilted differently in F444W
- What's the easiest way to plot the tiles together? 
Trilogy didn't seem to automatically combine them with the proper WCS, but maybe there is functionality to do this
- Can my computer handle all the 60 mas data for plotting, or do I have to get it running on a supercomputer?
- Zoom-ins: once I've sorted out how to plot the full mosaic, I'll make an image with the full field, a zoom in of tile A, and then a zoom in of a patch of tile A. 
I'll leave that for a future post though.