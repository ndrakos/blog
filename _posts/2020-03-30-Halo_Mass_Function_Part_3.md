---
layout: post
title:  "Halo Mass Function Part 3"
date:   2020-03-30

categories: cosmo_sims
---


In my $$128^3$$ <a href="https://ndrakos.github.io/blog/cosmo_sims/Test_Simulation/">test run</a>, I found that the halo mass function (HMF) measured from the simulation was higher than the theoretical curve. I want to sort this out before running larger simulations, to make sure there is no problem with how I have set up the initial conditions.

For more information on calculating HMFs, see the previous posts: <a href="https://ndrakos.github.io/blog/mocks/Halo_Mass_Function/">Part 1</a> and <a href="https://ndrakos.github.io/blog/mocks/Halo_Mass_Function_Continued/">Part 2</a>.



## Previous Tests

One possibility was that the random realization of initial conditions was by chance slightly too high. To test this, I generated another set of ICs, and looked at the power spectrum. While I still need to sort out the normalization of the power spectrum, it does seem that the two different realizations match each other, and therefore this is not likely the source of the discrepancy.

<img src="{{ site.baseurl }}/assets/plots/IC_PowerSpectrum_wfirst128.png">


I also checked how using different transfer functions affected the halo mass function in <a href="https://ndrakos.github.io/blog/cosmo_sims/Initial_Conditions/">this post</a> but found it didn't make much of a difference.

## Including Subhalos

One possibility for the discrepancy is that I am including all of the halos from the simulation data. However, when I remove these, it makes little difference at this resolution:

<img src="{{ site.baseurl }}/assets/plots/HMF_wfirst128_sub.png">


## Check Theoretical Prediction


I used the python package <a href="https://bdiemer.bitbucket.io/colossus/lss_mass_function.html">Colossus</a> to double check my HMF calculation:

<img src="{{ site.baseurl }}/assets/plots/HMF_wfirst128_col.png">

And it seems that there is an issue with my HMF calculation, and that the simulation is okay!



## Conclusions

The simulation looks okay; my theoretical calculation was off. I am going to get my halo finder working on Pleiades, and start running a $$512^3$$ version, to check everything scales okay, and that I am managing file storage okay (I'll also do a lot of time outputs for these, and start looking into some science questions). Hopefully that all goes smoothly, and I can request more space on Pleiades. Then I can move on to the $$2048^3$$ simulations!

However, at some point I should figure out what is wrong with my calculations of both the HMF and power spectrum. *Sigh*.
