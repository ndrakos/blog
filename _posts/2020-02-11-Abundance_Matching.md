---
layout: post
title:  "Abundance Matching"
date:   2020-02-11
---


In subhalo abundance matching (SHAM), you assume that the abundance of haloes as a function of their mass (or some other mass proxy), $$n(x)$$ is related to the stellar mass function $$ \phi (M_*')$$ as follows:

$$\int_x^\infty n(x') dx' = \int_{M_*}^\infty \phi (M_*') dM_*’$$

While there are different mass proxies, $$x$$, used in the literature, we will adopt $$v_{\rm peak}$$, which is the peak maximum circular velocity, $$v_{\rm max}$$,  a halo reaches in it's accretion history. This mass proxy seems to reproduce clustering results better than other quantities (e.g. <a href="https://ui.adsabs.harvard.edu/abs/2018MNRAS.477..359C/abstract">Campbell et al. 2018</a>). Presumably, $$v_{\rm peak}$$ will be equal to $$v_{\rm max}$$ at the current redshift for host halos, and equal to $$v_{\rm max}$$ at accretion for satellite halos.

Overall, my method is as follows:

(1) Get/run a simulation

(2) Run a halo finder and merger tree generator on the simulation (we use AHF)

(3) Measure $$v_{\rm peak}$$ for every halo (and also construct the halo mass function, $$n(v_{\rm peak})$$)

(4) Calculate the minimum galaxy mass, $$M_{\rm min}$$, by assuming the number of galaxies is equal to the number of halos found in the simulation ($$N_{\rm galaxies}=N_{\rm halos}$$) as:

$$ N_{\rm galaxies} = V \int_{M_{\rm min}}^\infty \phi (M_*') dM_*’$$

where $$V$$ is the simulation volume. The stellar mass function can now be normalized such that it has the same number of galaxies as halos.

(5) Do the abundance matching. Mathematically, for each halo (with a calculated $$v_{\rm peak}$$) solve for $$M_*$$ using:

$$ V \dfrac{\int_{v_{\rm peak}}^\infty n(v_{\rm peak}') d v_{\rm peak}'}{N_{\rm halos}} = \dfrac{\int_{M_*}^\infty \phi (M_*') dM_*’}{\int_{M_{min}}^\infty \phi (M_*') dM_*’}$$

## Test Results

## What's Next

While the current implementation has zero free parameters, it does not contain any scatter in the stellar mass -- halo mass (SMHM) relation. That will be the topic of the next post
