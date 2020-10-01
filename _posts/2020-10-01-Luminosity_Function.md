---
layout: post
title:  "Luminosity Function"
date:   2020-10-01
categories: mocks
---




In <a href="https://ndrakos.github.io/blog/mocks/Mock_Catalog_Detection_Predictions/">this post</a>, I showed some preliminary predictions for the galaxy catalog.

The luminosity function (LF) didn't look quite right, and I'm exploring that a bit more in this post.


## Results


Here I have plotted it again with the <a href="https://ui.adsabs.harvard.edu/abs/2015ApJ...803...34B/abstract">Bouwens et al. 2015</a> luminosity functions:

<img src="{{ site.baseurl }}/assets/plots/20201001_LF.png">

## $$M_{\rm UV}$$ assignment

First, I want to check if this is due to problems in the $$M_{\rm UV}$$--$$M$$ relation. Here are how our current mock catalog relations compare to the relations in W18:

<img src="{{ site.baseurl }}/assets/plots/20200929_MUV.png">

The $$M_{\rm UV}$$--$$M$$ relation isn't too different, but there are some discrepancies. If instead I draw $$M_{\rm UV}$$ properties from the W18 relations, rather than get from our SEDs, as in <a href="https://ndrakos.github.io/blog/mocks/Integrated_Galaxy_Properties/">this post</a>, I can plot the LF and get

<img src="{{ site.baseurl }}/assets/plots/20201001_LF2.png">

This looks a bit better, but it still doesn't match, so I don't think our $$M_{\rm UV}$$ assignment is the problem.

## Galaxy Completeness

The other possible problem is that the it is because the SMFs are not complete below $$\approx 10^9\,M_{\odot}$$ (e.g. see <a href="https://ndrakos.github.io/blog/mocks/LightCone_Abundance_Matching/">this post</a>).

To test the effect of missing low mass galaxies, I again used $$M_{\rm UV}$$ values drawn from the W18 distribution, but I didn't include galaxies with masses below $$10^10\,M_{\odot}$$.

<img src="{{ site.baseurl }}/assets/plots/20201001_LF3.png">

This makes a very large difference on the SMF, which makes me thing this is the reason we can't reproduce the observational LFs.

## For the presentation

Ideally I would have an estimate for how well we would be able to constrain the faint end of the luminosity function, but right now I don't have enough low mass galaxies to resolved in the simulation, and I don't think I have enough time to analyze the high resolution simulations before the conference.

Since I don't need spatial information from this plot, I can just generate galaxy mass/redshifts from the distributions down to lower mass resolutions, and then run them through my SED assignment code and then plot the LF.

I think W18 used a mass limit of $$M_{\rm min} = 10^6$$, and they were able to reproduce the LFs, so that should be enough. However, I only expect the SMFs for the $$2048^3$$ simulations to be complete to $$\approx 10^7\,M_{\odot}$$, so I will start with that mass limit. If there are issues reproducing the LFs with $$M_{\rm min}=10^7\,M_{\odot}$$, we might need to consider adding subhalos analytically to the catalog.
