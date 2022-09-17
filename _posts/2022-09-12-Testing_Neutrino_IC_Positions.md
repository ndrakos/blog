---
layout: post
title:  "Testing Neutrino IC Positions"
date:   2022-09-12
categories: neutrinos
---

I have been working IC code with dark matter particles. I also have sorted out how to add neutrinos as a second species. In this post I'll go through adding the neutrino positions.

As an overview, neutrinos will be on a coarse grid. at each point of the grid will have $$N_{shell}$$ neutrinos that sample the Fermi Dirac distribution, and for each of these velocities, they will have $$12 N_{side}^2$$ different directions. Therefore, there are $$N_{side} \times 12 N_{shell}^2$$ neutrinos at every coarse grid point.

## Position Assignment

Here is the overview of the position assignment method:

1. Get the power spectrum
- For the CDM I was using the total power spectrum (CDM + baryons + massive neutrinos)
- Now I will use the massive neutrino power spectrum for the neutrinos, and the CDM + baryons power spectrum for the DM.
2. Calculate density field from the power spectrum
- This I will leave exactly the same, but the neutrino density field will be calculated from its own power spectrum
3. Calculate the displacement field, $$\Psi from the density field (Zeldovich approx)
- The displacement field will be different for neutrinos, because it will depend on its own density field.
- Otherwise it is exactly the same - I went through the perturbation theory derivations and checked this was correct
4. Calculate the positions from displacement field
- Again, the positions for neutrinos will be calculated from their own displacement field

Therefore the neutrino positions are set exactly the same as the dark matter particles, but using their own power spectrum.

## Initial Test

Initially testing this (using 128 grid points for both the DM and the neutrinos, and not currently putting multiple neutrinos per grid point), I found the following power spectrum:

<img src="{{ site.baseurl }}/assets/plots/20220912_test1.png">


Clearly, the neutrinos don't match. However, if you look at the power spectrum of just the initial grid point positions (red), you find

<img src="{{ site.baseurl }}/assets/plots/20220912_test2.png">

I think there is some power that comes from the discretization/density field measurement. (I'm not sure how to measure ahead of time what this is)


If I test this code on a larger box size (1000 Mpc/h rather than 100 Mpc/h), where we can see the smaller k modes, we can see that the power spectrum matches pretty well for small scales:

<img src="{{ site.baseurl }}/assets/plots/20220912_test3.png">

I imagine this will look better as I go to higher resolutions, but for now I think it is fine.



## Next Steps

I have already mostly coded in the velocity assignment. I'll have a post up soon showing the velocity distributions, and the stability in Gadget. Then I'll run it at higher resolution and write up a report.
