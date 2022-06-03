---
layout: post
title:  "Measurement Uncertainties in the DREaM Catalogs"
date:   2022-06-03
categories: reion
---

A main goal of the reionization project is quantify the uncertainties on reionization measurements with future surveys. I would like to know how well JWST can constrain reionization, and how a future Roman UDF could best complement JWST.

In this post I am gathering my thoughts on how to estimate uncertainties on the **photometric** galaxy catalogs (I'll think about spectroscopy after). For now I am going to focus on properties that will be used to constrain the ionizing photon production of galaxies (e.g. I'm not currently worried about morphology or clustering).

The most "correct" way to do some of these steps would probably be to start from the simulated image, and run imaging pipelines on them. This is getting pretty outside my area of expertise, and is probably overkill/not feasible. I also don't want to deal with things like modelling the PSF. So I will try and simplify this where possible.


## Population Level Uncertainties

1. Cosmic Variance

Cosmic variance is expected to dominate over poisson noise in future surveys with Roman, so it is something I really need to calculate. To quantify cosmic variance, I will begin with looking at the work by <a href="https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.2401T/abstract">Trapp and Furlanetto 2020</a>. I think I looked at their calculator before, and it maybe didn't extend entirely into the regime I wanted? I will look into this again.

2. Completeness

I already did a rough estimate of how many galaxies would be "detectable" in the DREaM paper, based on their magnitude in their "drop-out" band. I could potentially use this same calculation, or update it to something more sophisticated.

Another thing to consider is that many of the high redshift galaxies will be obscured by foreground galaxies. I will come up for some criteria for when this is true.  As a first step, I'll try and come up with a rule of thumb that decides whether a galaxy will be detected or not, depending on how much it is covered by a foreground galaxy. I might need to look a bit into deblending as well.


3. Poisson Noise

This is very straightforward, and something I had already implemented in the DREaM paper


## Uncertainties in Galaxy Properties

Given the detected galaxies in a specific survey, I plan to assign "measured" galaxy properties that will not necessarily agree with the "truth". These measured values will be different for each survey.

1. Photometry

I could try and measure the photometry directly from a noisy image, and compare it to the "true" value. This will be too hard to do for every galaxy though, and would require generating images for every survey. The error in the photometry should mainly depend on the SNR, so I will probably just add noise to the photometry directly given the depth of the survey. I can then use the image as a sanity check.


2. Redshifts

I need to assign each galaxy a drop-out redshift. I'll start by looking at <a href="https://ui.adsabs.harvard.edu/abs/2020ApJ...892..125H/abstract">Hainline et al. 2020</a>.  


3. Reionization Properties

I need to go through the literature on how the three reionization parameters are typically measured. Some of these might involve SED fitting. I don't really want to dive into all the literature on how to run SED fits on every galaxy, so I might try and estimate the uncertainties on these parameters as a function of galaxy luminosity/redshift, and then add the uncertainties directly.
