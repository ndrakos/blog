---
layout: post
title:  "Redshift Errors"
date:   2022-06-29
categories: reion
---


One of the things I want to measure in the DREaM catalog is the redshift error.

Redshift can be measured from spectral lines, SED fitting, photo-z's, LBG dropout selection, and machine learning techniques. In general, the redshift measurements will depend on (1) whether there is spectra available (2) what photometric bands are used (3) the depth of the survey and (4) if there is complementary, e.g. HST data in the same field.

In this post I'm going to try and outline a plan for modelling redshift selection in the DREaM catalog.


# Lyman Break galaxies

A common way to select high-redshift dropout candidates is by requiring that it is detected at a certain significance in multiple wavelengths longer than the Lymann Break, with flux below a certain significance at wavelengths shorter than the break (another way is to use colour cuts).

## E.g. COSMOS-Web

COSMOS-Web (NIRCAM portion) will use three bands: F115W, F150W, F277W and F444W; the corresponding Lyman break redshifts are 8.46, 11.33, 21.78 and 35.51. It will also have MIRI coverage in some parts (which is much redder). There is also already HST F814W in the same area.

z~6-7 galaxies dropout in HST-F814W band, while z~9-10 galaxies dropout in F115W

Therefore, it really only makes sense to look into F115W and F150W dropouts with the JWST data. E.g. a F115W dropout galaxy would be detected in bands F277W and F444W (5sigma), but not in bands HST-F814W, F115W, and F150W (S/N<2 (this is commonly used in the literature, e.g., Bouwens2015))

Therefore you need to know/calculate the magnitude versus S/N, and potentially other data in the same field.

# Endsley et al. 2020

I also looked into the method used in Endsley et al. 2020. Endsley2020 looks at clustering measurements with JWST, specifically looking at JADES.

In their Section 2.2  "Modelling selection of high-redshift galaxies", they do a lot of what I am aiming to do

## Photometric selection

They

1. Add noise to the photometry (both JWST and HST), depending on the planned depth
2. Use colour cuts, detailed in their Appendix D1

## Spectroscopic

They say that "because NIRSpec microshutter assembly (MSA) targets must first be photometrically identified, the overall spectroscopic completeness... is determined by the spectroscopic redshift completeness, the photometric selection completeness, and the availability of MSA slits for targets"

Spectroscopic redshift completeness is calculated as the fraction of mock galaxies that have at least one emission line brighter than the 5σ flux limit (set by the NIRSpec depths.)


# Decision

I don't think it is worth it for me to try and reproduce what the data analysis will be on the catalogs.

However, I think that I will follow something similar to Endsley. This will require me knowing which HST data is available in the field. I will probably use the LGB dropout method (or some variation of whats detailed above), rather than colour cut selections, because that will be the easiest to extend to any generic collection of bands.

For COSMOS-Web, I don't have to think about spectroscopic redshifts, and this is something I'll try calculating soon. I will have to regenerate the spectra of the catalog to save HST photometry, but that is fine.

# Next Steps

1. Calculate HST photometry for entire DREaM Catalog
2. Calculate the COSMOS-Web drop-outs. See if the completeness looks reasonable.
3. In the future, I'll look into adding the spectroscopic predictions. 
