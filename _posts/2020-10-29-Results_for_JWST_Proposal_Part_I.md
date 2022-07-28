---
layout: post
title:  "Results for JWST Proposal Part I"
date:   2020-10-29
categories: cosmos_web
---

We want positions and magnitudes in two snapshots (redshifts 7 and 9) in the F200W Filter.

## Generating magnitudes

I will use snapshot_121 ($$z=9.05$$) and snapshot_159, ($$z=7.02$$).

I plan to read in a snapshot halo catalog, perform abundance matching, assign an SED and get the magnitude in F200W (using the FSPS built-in <code>jwst_f200W</code> band).

There are a couple of things that need to be improved in the SED generation procedure (e.g. ages), but I think that it will probably be fine for now; if there is time I can work on this and incorporate it into the catalog for the proposal figure.



## Mass Resolution

Right now I have $$512^3$$, $$1024^3$$ and $$2048^3$$ simulations. The 512 simulations are complete to galaxy masses above approximately $$10^9\,M_{\odot}$$, and I expect the 2048 simulations to be complete above masses of approximately $$10^7 \,M_{\odot}$$.

First, I want to see what mass resolution I need to resolve most of the galaxies at the given redshift. To do this, I created a "sample mock", in which I generated 1000 galaxy masses at redshift $$z=7$$ from the SMFs above a mass of $$10^{7}\,M_{\odot}$$. I then calculated the F200W magnitude, and found the fraction of galaxies that are brighter than the magnitude limit of $$27.5$$.

Here is the plot:
<img src="{{ site.baseurl }}/assets/plots/20201029_frac_detect.png">


Note that since only tested this on 1000 galaxies, I did not generate many high mass galaxies. However, this demonstrates that at redshift 7, we don't really need to have galaxies with masses above $$10^8$$ therefore I will use the $$1024^3$$ simulations. In the interest of time, I will probably just run AHF directly on the desired snapshots, since I still need to update my code to read in the Rockstar catalogs.
