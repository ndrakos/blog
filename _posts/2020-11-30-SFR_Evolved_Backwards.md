---
layout: post
title:  "SFR Evolved Backwards"
date:   2020-11-30
categories: mocks
---

In this post, I evolve the SFR backwards as a consistency check (i.e if I evolve the galaxies backwards by some time, $$dt$$, do the SFRs still fall on the right relation?). This will help me determine whether my age assignments are reasonable.

Currently, SFR assignments only depend on the redshift and mass of the galaxies, where ages are just drawn from a Gaussian.

## Methods
The SFR of each galaxy is given by a delayed-tau model:

$$\Psi_1 \propto t \exp(-t/\tau)$$,

where $$t$$ is the age of the galaxy, and $$\tau$$ is the e-folding time.

If we want to consider the SFR of the galaxy at a time $$dt$$ earlier,

$$\Psi_2 = \dfrac{t-dt}{t} {\rm e}^{dt/\tau} \Psi_1$$

I evolved things backwards by various  (only including galaxies where $$t>dt$$),

To correct for the change in mass, I did abundance matching between the SMFs at the current redshift, and the redshift at time $$t-dt$$ (just by directly solving for when $$n(z,<M)=n(z+dz,<M')$$).

## Results

### dt = 0.0 Gyr

<img src="{{ site.baseurl }}/assets/plots/20201130_SFR_vs_M_evolution_0.png">


### dt = 0.1 Gyr

<img src="{{ site.baseurl }}/assets/plots/20201130_SFR_vs_M_evolution_0p1.png">


### dt = 0.5 Gyr

<img src="{{ site.baseurl }}/assets/plots/20201130_SFR_vs_M_evolution_0p5.png">


### dt = 1 Gyr

<img src="{{ site.baseurl }}/assets/plots/20201130_SFR_vs_M_evolution_1.png">

### dt = 5 Gyr

<img src="{{ site.baseurl }}/assets/plots/20201130_SFR_vs_M_evolution_5.png">


## Conclusions

The star-forming galaxies look pretty good, though the Quiescent galaxies don't match very well (though the Quiescent galaxies might be okay, since they would not necessarily be classified as Quiescent at a time $$dt$$ earlier).
