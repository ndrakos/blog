---
layout: post
title:  "Initial Conditions"
date:   2020-03-23

categories: cosmo_sims
---

Here I am going to take a closer look at the initial conditions used to generate this
<a href="https://ndrakos.github.io/blog/cosmo_sims/Test_Simulation/">test simulation</a>. There are a few things I want to look into:

1) Why do the ICs look grid-like? Is this because of the ICs, or just how I am plotting them?

2) Does the transfer function make a difference to the predicted halo mass function?

3) Does the power spectrum of the ICs look right?   

4) Is the reason the HMF from the simulations is a little high because of the random realization?


## Grid-like ICs


My plot of the simulation at snapshot_000 (redshift 20) looks like this:

<img src="{{ site.baseurl }}/assets/plots/20200323_snapshot_000.png">

I want to see if this is because of the <a href=" https://github.com/astrofrog/mpl-scatter-density">plotting function</a> I am using, or if there is a problem in the ICs.

To test this, I calculated the density myself (I binned up the particles, and calculated the density in x-y projection):

<img src="{{ site.baseurl }}/assets/plots/20200323_snapshot_000_new.png">

This looks good, so the grid-like structure does seem to be an issue with the plotting function.



## Transfer Functions

I went through the calculation for the halo mass function (HMF) in
<a href="https://ndrakos.github.io/blog/mocks/Halo_Mass_Function/">this post</a> and used the transfer function from <a href="https://ui.adsabs.harvard.edu/abs/1986ApJ...304...15B/abstract">BBKS</a>.

For the ICs, I am using the Eisenstein transfer function (Equation 29 of <a href="https://ui.adsabs.harvard.edu/abs/1998ApJ...496..605E/abstract">Eisenstein & Hu 1998</a>), and here I have updated my theoretical HMF to include this.

The difference in the theoretical HMF is minimal:

<img src="{{ site.baseurl }}/assets/plots/20200323_HMF_wfirst128_TFs.png">




## Power Spectrum

I am guessing that the power spectrum of the ICs is just by chance a little too high. In the next post I'll go through how to measure the power spectrum, and compare it to theory.
