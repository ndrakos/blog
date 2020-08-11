---
layout: post
title:  "Integrated Galaxy Properties"
date:   2020-08-12
categories: mocks
---

In <a href="https://ndrakos.github.io/blog/mocks/Assigning_Galaxy_Properties/">this post</a>, I outlined the general method for assigning galaxy properties to the galaxy catalog. Here is the first step of the process: assigning integrated galaxy properties to the star-forming galaxies.

## Star-Forming Versus Quiescent

To determine which galaxies were star-forming, I used the SMFs (right now just using the Williams SMFs---I still need to update these) to get the probabilty of a galaxy being star-forming as a function of mass and redshift, and then randomly decided whether it was star-forming based on this probability.

Here are the recovered SMFs of the two populations:

<img src="{{ site.baseurl }}/assets/plots/20200812_SMF_Catalog.png">

I don't know if there are properties that correlate strongly with queiscence (e.g. halo properties or environment) that I should be including. I need to look into this.


## UV

The UV magnitude, $$M_{UV}$$, and UV continuum slope, $$\beta$$ were assigned from the linear relations given in <a href="https://ui.adsabs.harvard.edu/abs/2018ApJS..236...33W/abstract"> Williams et al. 2018</a>.

I realized their Equation 11 is not correct. To my best reasoning, their parameters should be $$(a,b,c)=(-0.08,-0.12,9.43)$$ **not** $$(a,b,c)=(0.12,0.08,9.41)$$.

Here are the assigned properties:

<img src="{{ site.baseurl }}/assets/plots/20200812_MUV.png">
