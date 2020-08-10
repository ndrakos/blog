---
layout: post
title:  "Assigning Galaxy Properties"
date:   2020-08-10
categories: mocks
---

So far I have positions, redshifts and masses for the galaxies in the mock survey. Here are my notes on how to assign galaxy properties, following the procedure from <a href="https://ui.adsabs.harvard.edu/abs/2018ApJS..236...33W/abstract"> Williams et al. 2018</a>.


## Galaxy Counts

My method for obtaining galaxy counts is roughly finished (with some things to sort out).

One thing I need to decide how to divide star forming and quiescent galaxies. It is straightforward to determine the number of galaxies that should be quiescent versus star forming as a function of redshift, but I might want to take into account environmental effects.

## Integrated Galaxy Properties

The next step in Williams is to use redshift and stellar mass to assign integrated galaxy properties for **star-forming galaxies**, including the UV absolute magnitude, $$M_{\rm UV}$$, and the continuum slope, $$\beta$$.

In <a href="https://ui.adsabs.harvard.edu/abs/2018ApJS..236...33W/abstract"> Williams et al. 2018</a>., they typically assigned values based on 3D-*HST* data when available, and otherwise sample from the relations outlined below. I will start by sampling the properties for all the galaxies, and then consider using the *HST* data after this is working.


### $$M_{\rm UV}$$

The $$M_{\rm UV}$$--$$M_*$$ relation is modelled as a linear relationship. The slope is fixed to $$-1.66$$, and the intercept of the $$M_{\rm UV}$$--$$M_*$$ relation is given in Equations 11-12. They found the scatter is constant in both stellar mass and redshift, and use a Gaussian scatter of $$\sigma_{UV}=0.7$$


### $$\beta$$

The rest frame UV continuum slope, $$\beta$$, is defined as $$f_{\lambda}\propto \lambda^{\beta}$$.

They model $$\beta$$---$$M_{\rm UV}$$ relation as a linear function. Equation 13 has equations for slope and interecept (the relation doesn't evolve after redshift 8). All mock galaxies are assigned $$\beta$$ based on this mean relationship, and the intrinsic  scatter $$\sigma_{\beta}=0.35$$. They also truncate the distribution at $$\beta=-2.6$$.


## Galaxy SEDs

Next, they assigned spectra that are consistent with the integrated properties.

### Parent SED Catalog


First, they created a parent mock catalog of SEDs to sample from; they used *HST* data where available, and otherwise created the parent sample from <a href="https://ui.adsabs.harvard.edu/abs/2018ApJS..236...33W/abstract">BEAGLE</href>. For now, I will just be using BEAGLE.

Details are in Section 3.4.3 for star-forming galaxies and 4.2 for quiescent galaxies.

### Matching Mock Galaxies to Parent Catalog

They find the closest match between the mock galaxy properties and those of the parent catalog galaxies.

Details are in Section 3.4.4 for star-forming galaxies and 4.2 for quiescent galaxies.

## Morphologies

They assigned sizes, shapes and sersic indicies by drawing from distributions, as described in Section 5.
