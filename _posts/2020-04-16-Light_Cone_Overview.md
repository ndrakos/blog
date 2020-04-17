---
layout: post
title:  "Light Cone Overview"
date:   2020-04-16

categories: mocks
---

This post outlines my plan for making the light cone for our mock galaxy catalogue.


## Overview of Mock Catalogues

Here is the current plan for the mock catalogue generation; this is so I can decide where in the methods the light cone generation fits.

We will start the catalogue from a dark matter only simulation, and then do abundance matching (alternatives include hydrodynamic simulations, HOD modeling and semi-analytic models; see the <a href="https://ui.adsabs.harvard.edu/abs/2018ARA%26A..56..435W/abstract">Wechsler and Tinker 2018</a> review for an overview of different methods).

### 1) Simulation

We decided to run a simulation with a box size of $$115 {\rm Mpc}\, h^{-1}$$ with $$2048^3$$ particles (see <a href="https://ndrakos.github.io/blog/mocks/Box_Size/">this post</a>). This a mass resolution of $$1.5 \times 10^7$$ solar masses per particle. We have created the ICs using MUSIC, and will run it in Gadget-2.


Note that the <a href="http://hipacc.ucsc.edu/Bolshoi/MergerTrees.html">Bolshoi-Planck</a> simulations are somewhat similar (volume of $$250 {\rm Mpc}\, h^{-1}$$, with a mass resolution of $$10^{10}$$) and we could potentially use these for another realization, or for a comparison.



### 2) Halo Catalogue and Merger Trees

I have everything setup to create halo catalogue and merger trees using AHF. Rockstar and Consistent-Trees seem to be more popular though, so I maybe need to justify using AHF (or switch). I should review the <a href="https://ui.adsabs.harvard.edu/abs/2011MNRAS.415.2293K/abstract">Haloes Gone MAD</a> papers.


### 3) Light Cone Generator

I plan to assign the halos positions on the light cone (rather than creating a lightcone out of the particles, and running a halo finder after). I will outline this more below.

I was debating whether to do the light cone generation or abundance matching first, but I think this makes more sense to make the light cone first for two reasons (1) many of the halos will be outside the light cone, so abundance matching will be faster if I do this step first and (2) if I do this first, each galaxy will have a unique redshift, rather than being assigned the redshift of the current snapshot (which may matter when assignment galaxy properties).


### 4) Abundance Matching

There were various choices associated with SHAM (e.g. which stellar mass/luminosity function, halo property, and scatter model to use). I have mostly sorted these things out in previous posts (though there were issues I blamed on resolution, and I need to check if things work with the higher resolution simulations). I also need to extend my abundance matching codes to work for redshifts out to about $$z=10$$.


### 5) Galaxy Properties

Once we have our galaxies, we need to assign galaxy properties (SEDs and galaxy sizes to start with). For this, I will closely follow <a href="https://ui.adsabs.harvard.edu/abs/2018ApJS..236...33W/abstract"> Williams et al. 2018</a>.

### 6) Mock Images

I will eventually look into making mock images, using <a href="https://ui.adsabs.harvard.edu/abs/2015A%26C....10..121R/abstract">GALSIM</a> (see also <a href="https://ui.adsabs.harvard.edu/abs/2019arXiv191209481T/abstract">Troxel et al. 2020</a>).




## Light Cone Generation

### Literature

I plan to follow a procedure similar to that for generating the CosmoDC2 sky catalog for LSST (<a href="https://ui.adsabs.harvard.edu/abs/2019ApJS..245...26K/abstract">Korytov et al. 2019</a>; these methods are  also outlined in the pedagogical notes by <a href="https://ui.adsabs.harvard.edu/abs/2019arXiv190608355H/abstract"> Hollowed 2019 </a>). The general idea is summarized nicely in this plot:

<img src="{{ site.baseurl }}/assets/plots/Korytov_LightCone.png">


Other key references for making light cones are: <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...573....7E/abstract">Evrard et al. 2002</a>, <a href="https://ui.adsabs.harvard.edu/abs/2005MNRAS.360..159B/abstract">Blaizot et al. 2005</a>, <a href="https://ui.adsabs.harvard.edu/abs/2007MNRAS.376....2K/abstract">Kitzbichler & White 2007</a>,  <a href="https://ui.adsabs.harvard.edu/abs/2013MNRAS.429..556M/abstract">Merson et al. 2013</a> and <a href="https://ui.adsabs.harvard.edu/abs/2017MNRAS.470.4646S/abstract">Smith et al. 2017</a>.


### Methods

Here is the current plan:

1) Start with the most recent snapshot, and find all isolated halos (ignore subhalos; these will be kept with their hosts).

2) For each halo, trace back the most massive progenitor and calculate $${\rm d}s^2$$ in each snapshot (Robertson-Walker metric). Assume that the observer is in the corner of the box, at (0,0,0).

3) Find the snapshots at times $$t_{j+1}$$ and $$t_j$$ at which $${\rm d}s^2$$ changes from positive to negative: the halo crossed the light cone at time $$t_j<t_e<t_{j+1}$$ (if  $${\rm d}s^2$$ doesn't change signs, this halo is not observable on the light cone, and all halos on this main progenitor branch can be discarded).

4) Solve for the cosmic time, $$t_e$$, and the comoving position at which the halo crossed (See equations 27-29 in <a href="https://ui.adsabs.harvard.edu/abs/2019ApJS..245...26K/abstract">Korytov et al. 2019</a>)

5) This can be used to determine the redshift and angular position of the halo

6) Assign the halo properties (mass, substructure, ect) from snapshot $$j+1$$ to this time and position---there are other alternatives to decide whether to assign properties from time $$t_j$$ or $$t_{j+1}$$, but I am following this simpler approach from <a href="https://ui.adsabs.harvard.edu/abs/2019ApJS..245...26K/abstract">Korytov et al. 2019</a>.

7) Remove all halos that are progenitors/descendants of this snapshot $$j+1$$ halo from further consideration (so they aren't double counted; though it is unlikely these would have crossed the light cone anyway)

8) Repeat this with all isolated halos in the next (earlier) snapshot that haven't been thrown away; this will include halos that have become disrupted, and halos that were not on the main progenitor branches.
