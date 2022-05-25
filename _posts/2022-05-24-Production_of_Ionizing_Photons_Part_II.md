---
layout: post
title:  "Production of Ionizing Photons Part II"
date:   2022-05-24
categories: reion
---

As described in <a href="https://ndrakos.github.io/blog/reion/Reionization_Modelling/">this post</a>, we want to calculate the production of ionizing photons.

I did a preliminary plot on this in <a href="https://ndrakos.github.io/blog/reion/Production_of_Ionizing_Photons/">Part I</a>, but it did not include the full catalog, and also there were some problems with my $$\xi_{\rm ion}$$ calculation that are now fixed.

In this post, I am running this calculation for the full DREaM catalog, and deciding if it looks reasonable.


## Calculation

The production of ionizing photons is given by:

$$\dot{n}_{\rm ion} = f_{\rm esc} \xi_{\rm ion} \rho_{\rm UV}$$.

where $$\rho_{\rm UV}= \int_0^{\infty} \phi(L) {\rm d}L$$.


Using the values from the catalog this can be rewritten as:

$$ \dot{n}_{\rm ion} = \dfrac{\sum f_{\rm esc} \dot{N}_{\rm ion} }{V}$$,

where $$f_{\rm esc}$$ and $$\dot{N}_{\rm ion}$$ are unique to each galaxy.

- $$f_{\rm esc}$$ is the escape fraction, as calculated <a href="https://ndrakos.github.io/blog/reion/The_Escape_Fraction/">here</a>

- $$\dot{N}_{\rm ion}$$ is the rate of ionizing photons calculated directly from the intrinsic spectrum, as outlined in the $$\xi_{\rm ion}$$ calculations (see <a href="https://ndrakos.github.io/blog/reion/The_Intrinsic_Production_Part_II/">The Intrinsic Production Rate Part II</a> and <a href="https://ndrakos.github.io/blog/reion/The_Intrinsic_Production_Part_III/">Part III</a>)



## Results

### Intrinsic production rate

Here's the intrinsic production rate in the full catalog

<img src="{{ site.baseurl }}/assets/plots/20220524_xi_ion.png">

for comparison, here are the results from Naidu2020:


<img src="{{ site.baseurl }}/assets/plots/20220316_naidufig2.png">

Our values are slightly higher than those in Naidu2020, but that could easily be a difference in spectra modelling. I will dig into this a little deeper later, but for now it seems pretty reasonable.



### Ionizing photons

Here is the ionization production of the full DREaM catalog ($$M_{\rm gal}>10^5 M_{\rm sol}$$) and also truncated at different $$M_{\rm UV}$$ values.

<img src="{{ site.baseurl }}/assets/plots/20220524_ndot.png">


Here are the results from Fig 7 of Naidu2020 (which included galaxies with  $$M_{\rm UV}<-13.5$$)

<img src="{{ site.baseurl }}/assets/plots/20220413_NaiduFig7.png">


These agree quite well!

## Conclusions


This is a great starting point, and what I will consider the ground truth for now. The next broad steps are:

1. Quantify different sources of error. Some of this was included in the original DREaM paper, but I also want to quantify the number of galaxies that are obscured, redshift errors, cosmic variance, ect.

2. Make comparisons for different surveys. The most straightforward comparison is area depth. But I also need to think about what photometry/spectroscopy is included. This basically involves making an estimate of the error on $$\dot{n}_{\rm ion}$$ for each survey.

3. Quantify how well different surveys will be able to quantify $$\dot {n}_{\rm ion}$$ for this "ground truth". Also consider variations in what the Roman Ultra Deep Field could look like.

4. Alter the underlying model. This could be done by changing the underlying model; e.g. assume escape fraction doesn't vary with redshift, or by altering the underlying luminosity function (though this would require remodelling the spectra of these galaxies). It could also be done by just changing the three important quantities plus number counts systematically by e.g. 10 percent, and seeing if the different surveys could distinguish between the different data sets.
