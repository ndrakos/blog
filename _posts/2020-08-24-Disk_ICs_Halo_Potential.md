---
layout: post
title:  "Disk ICs with Halo Potential"
date:   2020-08-24
categories: cholla
---

In my <a href="https://ndrakos.github.io/blog/Disk_ICs/">last post</a> I outlined how to set up ICs for a isolated disk, following <a href="https://ui.adsabs.harvard.edu/abs/1993ApJS...86..389H/abstract"> Hernquist 1993</a>.

In this post, I'll add in a fixed potential for the halo.

## The Halo Model

The halo will be NFW:

$$\rho(r) = \dfrac{\rho_0 r_s^3}{r(1+r_s)^2}$$,

and the gravitational potential is given by:

$$\Phi(r) = - \dfrac{4 \pi \rho_0 r_s^3}{r} \ln \left( 1 + \dfrac{r}{r_s}\right)$$

## Including the Halo Potential in the ICs

The potential of the halo can be added to the potential of the disk when calculating the particle velocities.

This alters the calculations of $$\kappa$$ and $$\Omega$$, and therefore the radial and azimuthal velocities.


## Simulating

I checked this by evolving the ICs in a modified form of Gadget, which includes a fixed NFW background potential.

The NFW halo was given the parameters: $$M_{\rm vir} = 5.8$$, $$r_{vir}=10$$ and $$r_s=1$$.

Here is how it evolved:

<img src="{{ site.baseurl }}/assets/plots/20200824_Sim_xy.png">


<img src="{{ site.baseurl }}/assets/plots/20200824_Sim_xz.png">

It's not perfectly stable, but OK... it might be that my gravitational softening length is too big, or I have an error somewhere. It could also be that I didn't add in the softening of the radial dispersion, as suggested in Hernquist 1993.
