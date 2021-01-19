---
layout: post
title:  "Rockstar Part II"
date:   2021-01-19
categories: cosmo_sims
---

As outlined <a href="https://ndrakos.github.io/blog/cosmo_sims/Rockstar/">here</a>, I had decided to switch to Rockstar for the halo finder.


## 1024 HMF

I ran the rockstar halo finder on the $$1024$$ simulations according to the script in the earlier post. First I want to check that the halo mass function looks alright. Note that I am using a slightly different mass definition than earlier; before I was using  $$200\rho_c$$, now I'm using Rockstar's default, which is the formula from Bryan & Norman (1998). Don't think it really matters which I use.

Here is the HMF:

<img src="{{ site.baseurl }}/assets/plots/20210119_HMF.png">


For comparison, see the first plot in <a href="https://ndrakos.github.io/blog/mocks/HMF_Lightcone/">this post</a>, in which I plot the HMF from the 512 simulation... In the 1024 simulations, the HMFs look complete down to $$10^{9.5}$$ solar masses, where the 512 simulations were only complete to $$10^{10.5}$$ solar masses.

## Next Steps

The good news is that the halo mass functions look great for the 1024 simulations. Next, I will run this on the 2048 simulation, and also look into making merger tree using rockstar (since I am using the peak circular velocity in abundance matching, I need merger histories).
