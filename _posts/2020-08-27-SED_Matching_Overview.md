---
layout: post
title:  "SED Matching Overview"
date:   2020-08-27
categories: mocks
---

This is a summary of the method used in <a href="https://ui.adsabs.harvard.edu/abs/2018ApJS..236...33W/abstract"> Williams et al. 2018</a> to assign SEDs to each galaxy.

## The Galaxies

First, they assign galaxy masses and type (star-forming/quiescent). For the star-forming galaxies, they also assign absolute UV magnitude and UV continuum slope.

By construction, the galaxies follow known $$M_{UV}--M_*$$ and $$\beta--M_{UV}$$ trends.

The goal is to assign SEDs that are consistent with these galaxy properties.

## SED Parent Catalog


They used BEAGLE to create a parent catalog; this is a tool for modeling and interperating spectrophotometric galaxy SEDs. Self-consistent approach that describes stellar emission and its transfer through the ISM and IGM.

If available, they used BEAGLE to fit SED models to known observations; I will skip this step.

When the properties extend beyond the current measurements of real sources, they use BEAGLE to produce theoretical SEDs covering a range of parameters that can be matched to the redshift, stellar mass and integrated properties of the galaxies.


They altered:

$$z$$: redshift

$$M_*$$ stellar mass

$$\tau$$: time scale of stellar mass formation

$$\hat{tau}_V$$: $$V$$ band attenuation optical depth

$$\log U_S$$: effective gas ionization parameter

$$Z$$: metallicity

$$t$$: age of oldest stars in the galaxy


Section 3.4.3 outlines how they constrain these parameters, to make sure they have reasonable SEDs. From my understanding, they create a grid in mass and redshift; based on the mass--metallicity relationship, they assign a range of realistic metallicities. Then based on the mass--metallicity--star formation history relation, they assign realistic SFHs, ect.

For quiescent galaxies (section 4.2), they do not need to assign all of these properties; they just assign $$t$$, $$\tau$$ and $$Z$$.

This creates a grid of SEDs.

## Matching to sample

They match the galaxy to the closest SED in terms of $$z$$, $$M_*$$, $$M_{UV}$$ and $$\beta$$ (its not clear to me how thet determine which is the "closest").

They then shift the redshift of the SED to match.
