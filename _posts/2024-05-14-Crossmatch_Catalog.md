---
layout: post
title:  "Crossmatch Catalog"
date:   2024-05-14
categories: cosmos_web
---

Max created Cosmos Web images for the DREaM catalogs, and Marko has recovered catalogs from the images.
In order to compare input to output, we need to cross match the two catalogs. 

## Intrinsic Catalog

Max created the images using MIRAGE from the input catalogs <code>gal_DREaM_JAN_2024.cat</code>. 
These catalogs contain the intrinsic parameters, galaxy IDs, and the corresponding DREaM IDs. 

## Recovered Catalog 

Marko has the recovered catalogs from SE++ in <code>COSMOSWeb_DREaM_JAN24_merged_v1.0.fits</code>. 
There are 89 fields. For now, I only care about the RA ('world_centroid_alpha') and Dec ('world_centroid_alpha') values.


## Method

The most important quantity to match is location. I used RA and Dec, weighted by the range of RA and Dec values. 

I then used a k-d tree from sklearn to find the nearest neighbours in the input catalog. 

This did a good job at matching location! My only concern is that there are multiple galaxies on top of each other, and I am not necessarily matching the correct one.

When I tried to use more information, I found that I had much worse fits. 
Part of the problem is that I'm not sure that some of the quantities (e.g. radius, flux) are 
exactly the same quantity in the two catalogs. For now I'll leave it matched on location, and see if I need to go back and revisit this.