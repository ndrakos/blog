---
layout: post
title:  "DREaM Extra Photometry"
date:   2024-03-31
categories: cosmos_web
---

In order to get the final galaxy catalogs for the simulated COSMOS-Web catalogs, we need to simulate the extra ground-based photometry.

## Summary of Filters

The filters I plan to generate for DREaM are:

1. Main (needed for catalog pipeline):
Miri-F770W, 'HST-F814W', 'CFHT-u', 'HSC-g', 'HSC-r', 'HSC-i', 'HSC-z', 'HSC-y', 'HSC-NB0816', 'HSC-NB0921', 'HSC-NB1010', 'UVISTA-Y', 'UVISTA-J', 'UVISTA-H', 'UVISTA-Ks', 'UVISTA-NB118', 'SC-IA484', 'SC-IA527', 'SC-IA624', 'SC-IA679', 'SC-IA738', 'SC-IA767', 'SC-IB427', 'SC-IB505', 'SC-IB574', 'SC-IB709', 'SC-IB827', 'SC-NB711', 'SC-NB816'

2. Primer Filters: F090W, F115W, F150W, F200W, F277W, F356W, F410M and F444W

3. Other Requests:
24um MIPS, IRAC CH1-4, Herschel bands (100, 160, 250, 350, 500), Scuba2- 450 and 850, radio 1.4GHz and 3GHz, 50GHz (CHAMPS?), Euclid, Roman, PRIMA, JWST NIRCam medium bands

For now I'm going to focus on the "main" photometry, since this is needed to generate the catalog.

## FSPS install Notes

Recall that to add new filters to FSPS you need to:
1. add name to data/FILTER_LIST
2. add the filter data to data/allfilters.dat
3. change nbands in src/sps_vars.f90 (line 285)
4. recompile fsps (run make)

Before, we could just reinstall python-fsps, and it was ready to go. Now, however, you need to make sure you are installing from source: download python-fsps from git, change the number of filters in the code (src/fsps/libfsps/src/sps_vars.f90), and then reinstall.

## Check Photometry

It looks like  is working reasonably. Here is an example specrum:

<img src="{{ site.baseurl }}/assets/plots/20240331_Example_Spectrum.png">



## Add Uncertainties

I will use Max's method:

1. Get the depth of the survey for the band --- convert this to a flux ($$F_{\rm limit}$$)
2. To get the standard deviation of the flux, divide this flux by three ($$\sigma = F_{\rm limit}$$/3); this assumes all the surveys are reporting the depth to $$3\sigma$$
3. Randomly draw a Gaussian error with this $$\sigma$$
4. Add this error to the flux of the galaxy


I mainly got the depths from Weber+2022. Here is a table of all the filters and depths:

<img src="{{ site.baseurl }}/assets/plots/20240331_externalphot_table.png">


For all of them I used the 2'' aperture, and the three sigma error. For MIRI, I only have the 3'', 5 sigma depth right now --- I need to update this. I am also missing a couple of depths, and need to figure out what to use for these. 
