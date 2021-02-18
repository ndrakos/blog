---
layout: post
title:  "Changing to Rockstar"
date:   2021-02-15
categories: mocks
---

As discussed previously, I decided to change from AHF to Rockstar (because it was going to take to long to get the merger trees for the $$2048^3$$ simulations). Here I have updated the lightcone code to read in the outputs from consistent trees for the $$512^3$$ simulations.

## Rockstar and Consistent Trees

In previous posts I outlined how I got <a href="https://ndrakos.github.io/blog/cosmo_sims/Rockstar/">Rockstar</a> and <a href="https://ndrakos.github.io/blog/cosmo_sims/Consistent-Trees/">Consistent Trees</a> running on Pleiades.

These result in a bunch of hlists files that contain all the halos as well as some merger information (their progenitors/descendants as well as peak mass and vmax values). This gives me the information I need to track the halos between snapshots to create the lightcone, and it also directly gives the vpeak values for abundance matching (before I was reading through all the AHF files and mapping out the merger histories to get the vpeak values).

I already checked that HMF of Rockstar looked right (for the 1024 simulations, <a href="https://ndrakos.github.io/blog/cosmo_sims/Rockstar_Part_II/">here</a>). I also want to look at the Halo Vpeak Function (HVF).

Here is the HVF for the 512 simulations. The dotted lines were the fits I had to the AHF catalogs (e.g. <a href="https://ndrakos.github.io/blog/mocks/Fit_HVF/">this post</a>). This is something I may update later, but if I'm leaving off the scatter model we don't actually need the HVF.

<img src="{{ site.baseurl }}/assets/plots/20210215_HVF.png">


Regardless, the HVF seem consistent with what we had before, which means the merger trees are probably working properly

## LightCone

I edited the lightcone code to read in the rockstar files, which meant reorganizing a lot of the code.

I also still need to check if the HMF looks okay once I put it in lightcone:

<img src="{{ site.baseurl }}/assets/plots/20210215_HMF_lightcone.png">


## Galaxy Sizes

I also want to double check that the galaxy sizes are still okay. The galaxy sizes are assigned as specified <a href="https://ndrakos.github.io/blog/mocks/Galaxy_Sizes_Part_II/">here</a>. As detailed in that post, I am now using a different virial radius definition, and need to correct for this when calculating $$R_{\rm eff}$$

<img src="{{ site.baseurl }}/assets/plots/20210215_Reff.png">


The sizes here are actually lower than I had before (I accidently wasn't implementing the virial radius definition correction).

I'm actually not sure whether or not this agrees with W18 though. I need to go through and be careful whether $$R_{\rm eff}$$ is the major axis, or circularized quantity, and whether it is projected or not. Then I need to make sure I am using the correct quantity when calculating the dust parameter. It is possible that my galaxies were too large, resulting in unrealistic dust parameters.

## Check for Double Counting

Another thing I implemented when changing the code to read in these files is a check to make sure a halo doesn't cross the lightcone twice. I'm not sure this is actually possible; physically, it is not possible because it would require the halo travelled faster than the speed of light. However, since I am interpolating the halo positions between snapshots (and also extrapolating when a halo doesn't exist in the previous snapshot), it may be possible that it calculates that the halo crossed the lightcone when it didn't. Also, if the merger trees aren't perfect, it might incorrectly connect two halos.

For each box, I traced the merger history for every halo and subhalo, and made sure none of their *main* progenitors are included in the lightcone catalog---I did not find any instances of a halo being included twice.


## Higher Resolution simulations

Finally, I need to upgrade to the higher resolution simulations.

1024: I have run Rockstar, and am currently running consistent trees---I need to figure out how to (1) restart consistent trees from the output files and (2) use the parallelized version.

2048: I'm in the process of running Rockstar. I had to change from lou to pleaides, since you can request many more nodes. However, this means I have to copy files from lou (unlimited storage) to the nobackup drive (which I have a 5TB limit)... I'm probably just going to copy ~10-20 snapshots over at a time and run the halo finder on those.
