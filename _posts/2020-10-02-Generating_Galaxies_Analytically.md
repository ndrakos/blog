---
layout: post
title:  "Generating Galaxies Analytically"
date:   2020-10-02
categories: mocks
---


There is a problem reproducing observed LFs, as discussed in <a href="https://ndrakos.github.io/blog/mocks/Luminosity_Function/">this post</a>. I concluded that this discrepancy is likely because we have a low resolution in $$512^3 simulations which is incomplete below galaxy masses of $$\approx 10^9 M_{\dot}$$.


Since analyzing the simulations will take a while, I am going to check this from a mock catalog where galaxy redshifts are determined analytically by sampling from the redshift distribution. Since these results aren't based on a simulation, we don't have halo information or exact positions (which is needed to measure the 2PCF), but we can still obtain redshifts, galaxy masses and SEDs.


## Methods


1. Redshifts - To generate redshifts, I selected $$1^6$$ galaxies from the redshift distribution, as outlined in <a href="https://ndrakos.github.io/blog/mocks/2PCF_Mock_Galaxies/">this post</a> when creating the random catalog for the 2PCF calculation.

2. Masses - The masses were drawn from the SMFs, as in abundance matching, but without the need to rank order. The minimum mass will be $$10^7$$.


3. SEDs - The SED assignment only depends on galaxy masses and redshifts, so this can be run the same as before.


## Results

To correct results, know that there should actually be $$\approx 3 \times 10^6$$ galaxies above $$10^7 M_{\odot}$$. Therefore, number counts should increase by a factor of 3, and the standard deviation in the galaxy counts should scale as $$1/\sqrt{3}$$.

### Detections

We can now have predictions for the completeness of the sample down to masses of $$10^7$$:

<img src="{{ site.baseurl }}/assets/plots/20201002_frac_detect.png">

This completeness measurement can be used to correct things like the LFs.


### UV properties


This is how including the low mass galaxies affects the UV properties:

<img src="{{ site.baseurl }}/assets/plots/20201002_MUV.png">

For comparision, see the same plot <a href="https://ndrakos.github.io/blog/mocks/Luminosity_Function/">here</a>.



There is an improvement on the faint end of the $$\beta$$--$$M_{\rm UV}$$ relation, but there are still descrepancies for bright objects. My best guess is it is because the age distribution I am sampling from is not realistic.


### Luminosity Functions

First, I realized Bouwens 2015 is only applicable for redshifts above 4, which is not approriate for all the comparisons. For now, I am using <a href="https://ui.adsabs.harvard.edu/abs/2005ApJ...619L..43A/abstract">Arnouts et al. 2005</a> for $$z<1$$, <a href="https://ui.adsabs.harvard.edu/abs/2010ApJ...725L.150O/abstract">Oesch et al. 2010</a> for $$1\leq z<3$$ and Bouwens et al. 2015 for $$z \ge 3$$

As before, I am sampling the UV magnitude from the W18 relations, rather than use those measured from our SEDs.

<img src="{{ site.baseurl }}/assets/plots/20201002_LF.png">

This looks a lot better than before, but there are still some descrepancies with observations. They look complete above a magnitude of $$\approx -18$$ at this mass resolution (is this enough for our purposes, or will we have to add in low mass halos to the simulations?).
