---
layout: post
title:  "JWST Pipeline 1 over f noise"
date:   2022-09-01
categories: cosmos_web
---

In the <a href="https://ndrakos.github.io/blog/cosmos_web/JWST_Pipeline_Stage_3/">previous post</a> I generated a mosaic of the DREaM simulated catalog. One thing I wanted to fix were the black lines in the mosaic. Anton pointed out that that was from the 1/f noise.

## Fixing the 1/f noise

This is something that will be implemented in future versions of the pipeline. For now, the easiest fix is to use Micaela's script and apply it to the rate files at the end of Step 1 of the pipeline (to the rate.fits files).

## Results

This seemed to fix things! Here are the four filters:

<img src="{{ site.baseurl }}/assets/plots/20220901_Mosaics.png">
