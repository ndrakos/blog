---
layout: post
title:  "Mock Catalog August Progress Report"
date:   2020-08-28
categories: mocks
---

This is a summary of our progress with the mock catalog. The plan is to have some rough results for the October meeting. Therefore, I am trying to get the methods roughly sorted out from start to finish.

I also have the draft of the paper on github that I've slowly been writing and adding plots to.

## Title

I was a bit distracted the other day trying to come up with a name for our mock catalog. Here were some rough ideas:


MUSINGS: Mock Ultradeep Survey ... Nacy Grace...

ARTEMIS: A Roman Telescope Extragalactic Mock ... Survey

MUSE: Mock Ultradeep Survey for Extragalactic...

AMUSEMENT: A Mock Ultadeep Survey for Extragalactic ...  Nacy Telescpope


## Simulations

The $$2048^3$$ simulations are almost complete (redshift 0.1), and I have set up code to do a second realization.

We have currently used 78 percent of computational time on Pleaides, which expires September 30. I'm not sure if we have enough time to complete a second realization, so I will focus on getting halo catalogs before starting the second realization


##  Halo finder

I am using AHF as a halo finder. This step (and all of the following) have been done with the $$512^3$$ simulations.
A while back, I had started to create halo catalogs for the $$1024^3$$ simulations, but it was going very slowly. AHF has an MPI option that I will need to use, but I first have to recompile the code for MPI and figure out what values to set in the parameter file for the MPI decomposition.

I want to get this done before Sept 30 (since that's the project end date on Pleiades). I will focus on getting this running next week.

## Halo lightcone

This is mostly done. There are two small details to look into:

1) Right now we are possibly allowing the same halo to cross the light cone more than once. I still need to check if the same halos get included multiple times, and possibly prune things.

2) I'm assigning all halo properties from snapshot $$j+1$$, it is probably better to have some way of deciding whether it should be from snapshot $$j$$ or $$j+1$$

Other than that, I just need to run it on the higher resolution simulations, and edit the plots so that they are more visually appealing.

## Galaxy Masses

I have code set up to assign galaxy masses using abundance matching. See <a href="https://ndrakos.github.io/blog/mocks/LightCone_Abundance_Matching/">this post</a> for the latest report on this.

The biggest problem is that the scatter model isn't working at high redshifts. I think I will need to change how I am doing this, but I have some ideas. I think I will assume a functional form for how the stellar-mass--halo-mass scatter depends on the scatter on $$v_{\rm peak}, and then fit the parameters in the functional form. If this doesn't work, I can do the more traditional de-convolution method.

Additionally, the SMFs from Williams et al. are shaped a bit funny, so I should update the parameterization for these.

Finally, want to check the galaxy clustering (and maybe bias) of the galaxy catalog to verify that the results are realistic. I started to look at the galaxy clustering, but realized the number of galaxies at low redshifts is way too small in our survey volume to get a good clustering signal. I am going to repeat the abundance matching on the entire box, rather than just galaxies in the survey volume to check this.

## Integrated Galaxy Properties

After assigning galaxy masses, our next step is to assign integrated galaxy properties: namely, whether galaxies are star-forming or quiescent, as well as their UV magnitude and UV continuum slope.

This step is done (unless we decide to improve upon it), and outlined in <a href"https://ndrakos.github.io/blog/mocks/Integrated_Galaxy_Properties/">this post</a>.


## Galaxy SEDs

This is the next step I really want to sort out, to make sure I have SEDs for the October meeting.

The plan for assigning SEDs to each galaxy is to first create a mock parent catalog of SEDs, and then match galaxies to these SEDs, based on their assigned properties.

In  <a href="https://ndrakos.github.io/blog/mocks/SED_Matching_Overview/">this post</a> I outlined roughly how this is done in Williams et al. I'm not sure whether we need BEAGLE. It's a bit difficult for me to determine what exactly we need, without going through and actually trying things. I might muddle around with things a bit, and build up a deeper understanding of what actually goes into SED assignments.

There are many softwares available for SED fitting, as summarized <a href="http://www.sedfitting.org/Fitting.html">here</a>. Brant--do you have experience/knowledge of any of these?


## Galaxy Morphologies

I also want to assign galaxy morphology, including galaxy size, shape, Sersic index and position angle.

In <a href="https://ui.adsabs.harvard.edu/abs/2018ApJS..236...33W/abstract"> Williams et al. 2018</a>, they assigned these properties based on their distributions, or their mass/redshift dependence. However, some of these properties may correlate strongly halo properties; unlike Williams et al, we do have halo properties to check this.

For now I'm just going to follow Williams (which should be pretty straightforward), and check the trends with halo properties after. If we are worried our results are unrealistic, we can change the way we are doing it.

## Galaxy Images

We might also make galaxy images. I want to look into GalSim, to see how straightforward it is to use. I tried installing it, but got an error wihen pip installing the dependant package, LSSTDESC.Coord. I need to try and troubleshoot this.
