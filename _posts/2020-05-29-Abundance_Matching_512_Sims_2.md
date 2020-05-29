---
layout: post
title:  "Abundance Matching 512 Sims 2"
date:   2020-05-29

categories: mocks
---

This is a continuation of <a href="https://ndrakos.github.io/blog/mocks/Abundance_Matching_512_Sims/">this post</a>. I have performed abundance matching on the final snapshot of the $$512^3$$ simulation, with the updated stellar mass functions, and with the scatter model working.

I am using the halo $$v_{\rm peak}$$ function (HVF) from <a href="https://ui.adsabs.harvard.edu/abs/2017MNRAS.469.4157C/abstract">Comparat et al 2017</a>. I flipped back and forth between using a parameterization or the simulation results. I think it works a lot better with a parameterization, but I will have to use our simulations to fit the parameterization for the range of redshifts we need.

## Scatter Mapping


As outlined in <a href="https://ndrakos.github.io/blog/mocks/Adding_Scatter/">this post</a>, we will add scatter to $$v_{\rm peak}$$ before the abundance matching step to get the required scatter in the galaxy masses $$M_{\rm gal}$$.

Here is how the scatter in $$M_{\rm gal}$$ varies with the scatter in $$v_{\rm peak}$$ as a function of $$v_{\rm peak}$$.

<img src="{{ site.baseurl }}/assets/plots/20200529_scatter_mapping.png">


## Abundance Matching

Here are the results... The parameterized SMF and HVF are shown with dotted black lines. For this resolution, the simulations match the parameterizaiton at roughly $$v_{\rm peak} > 2.2$$ and $$M_{\rm gal}>9.5$$.

<img src="{{ site.baseurl }}/assets/plots/20200529_AbundanceMatching.png">


## Next Steps

I am pretty happy with the set-up I have. The improvements I want to make are to (1) fit the HVF function from our simulations up to redshifts $$z>10$$ and (2) rather than perform this on the snapshot, perform it on the halo lightcone in different redshift bins.
