---
layout: post
title:  "Annihilation Signal Scaling"
date:   2024-04-06
categories: tidal_stripping
---

For edits on my annihilation paper, I have a problem with how I'm rescaling my profiles, so I'm going to record my calculation here.

## Rescale profiles

In particular, my annihilation signal is in units $$M_{\rm unit}^2 / r_{\rm unit}^3$$, where $$r_{\rm unit}=r_s$$ and $$M_{\rm unit}=M(<10 r_s)$$ (assuming an NFW profile).

Therefore

$$\dfrac {M_{\rm unit}^2} {r_{\rm unit}^3} = \dfrac {M (10 r_s)^2 } {r_s^3} = \dfrac {M (10 r_s)^2 c^3 } {r_{\rm vir}^3} $$

And then, using $$200 \rho_c = M_{\rm vir} / (4/3 \pi r_{\rm vir}^3)$$,


$$\dfrac {M_{\rm unit}^2} {r_{\rm unit}^3} = \dfrac {4\pi \times 200 \rho_c M (10 r_s)^2 c^3 } {3 M_{\rm vir}} = \dfrac {4}{3}\pi \times 200 \rho_c M_{\rm vir} c^3   \left(  \dfrac {M(10 r_s)} {M_{\rm vir}}  \right)^2$$



## Concentration--mass relation

Now I need a way to choose a concentration for a halo of a given mass. I'm going to just assume it lies on the concentration--mass relation. I'll use one of the Colossus functions. <a href="https://bdiemer.bitbucket.io/colossus/halo_concentration.html">here</a>. I chose the Ishiyama 2021 model, with the $$200\rho_c$$ definition.
