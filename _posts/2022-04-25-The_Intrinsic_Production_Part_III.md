---
layout: post
title:  "The Intrinsic Production Rate Part III"
date:   2022-04-25
categories: reion
---

Here is a new update on the intrinsic production rate calculation for the galaxies
(continuation from <a href="https://ndrakos.github.io/blog/reion/The_intrinsic_production_rate/">Part I</a> and <a href="https://ndrakos.github.io/blog/reion/The_intrinsic_production_rate/">Part II</a>).


## Spectra Parameters

Dust: I played around with these a bit, and verified setting <code>dust_type=0</code>; <code>dust_index=0</code> is equivalent to keeping <code>dust_type=2</code> and setting <code>dust2=0</code>.

Really, to fix things I had to turn the nebular emission model off
- <code>add_neb_emission=0</code>

What seems to be happening is that the ionizing photons were being absorbed by gas around stars.

## Updated Plots

Here is what the spectra looks like now:

<img src="{{ site.baseurl }}/assets/plots/20220425_Example_Spectra.png">

And here are the xi_ion values

<img src="{{ site.baseurl }}/assets/plots/20220425_xi_ion_scatter.png">


These look *much* better.

There looks like there is some discretization in the second plot (similar to what Mark Dickinson found when looking at emission lines). I think this is probably due to some sort of discretization in how FSPS is creating the spectra, or where the spectral lines are, but I should dig into this more, to make sure it isn't an unwanted discreteness in the redshift values of the galaxies.
