---
layout: post
title:  "SFR Evolved Backwards"
date:   2020-11-30
categories: mocks
---

In this post, I evolve the SFR backwards as a consistency check (i.e if I evolve the galaxies backwards by some time, $$x$$, do the SFRs still fall on the right relation?). This will help me determine whether my age assignments are reasonable.

Currently, SFR assignments only depend on the redshift and mass of the galaxies, where ages are just drawn from a Gaussian.

## Methods
To do this, note the SFR is:

$$\Psi_1 \propto t \exp(-t/\tau)$$,

where $$t$$ is the age of the galaxy, and $$\tau$$ is the e-folding time.

If we want to consider the SFR of the galaxy at a time $$dt$$ earlier,

$$\Psi_2 = \dfrac{t-dt}{t} \e^{x/\tau} \Psi_1$$

I evolved things backwards by various  (only including galaxies where $$t>x$$),

## Results

### dt = 0.1 Gyr

<img src="{{ site.baseurl }}/assets/plots/20201130_SFR_vs_M_evolution_0p1.png">


### dt = 0.5 Gyr

<img src="{{ site.baseurl }}/assets/plots/20201130_SFR_vs_M_evolution_0p5.png">


### dt = 1 Gyr

<img src="{{ site.baseurl }}/assets/plots/20201130_SFR_vs_M_evolution_1.png">


## Conclusions

Once I evolve these back further than 0.1 Gyr, they really don't match anymore (though the Quiescent galaxies are a bit better than the star forming ones). This indicates that my age assignment has problems. I plan to go through some papers, and get a better idea of what observational constraints and/or models there are on galaxy age distributions.

If I am unable to assign galaxy ages directly, I can either constrain age distributions by forcing the mass-SFR relation at earlier redshifts, or assigning UV properties and then using this to constrain ages.
