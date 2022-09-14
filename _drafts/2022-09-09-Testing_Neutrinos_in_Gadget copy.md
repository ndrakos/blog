---
layout: post
title:  "Testing Neutrinos in Gadget"
date:   2022-09-09
categories: neutrinos
---

I have been working IC code with dark matter particles. I also have sorted out how to add neutrinos as a second species. In this post I'll go through adding the neutrinos, and check what they look like in Gadget.

As an overview, neutrinos will be on a coarse grid... at each point of the grid will have Nshell neutrinos that sample the fermi dirac distribution, and for each of these velocities, will have 12 Nside^2 different directions. Therefore there are Nsidex12xNshell^2 neutrinos at every coarse grid point...

## Position Assignment

Here is the overview of the position assignment method:

1. Get the power spectrum
- For the CDM I was using the total power spectrum (CDM + baryons + massive neutrinos)
- Now I will use the massive neutrino power spectrum for the neutrinos, and the CDM + baryons power spectrum for the DM.
2. Calculate density field from the power spectrum
- This I will leave exactly the same, but the neutrino density field will be calculated from its own power spectrum
3. Calculate the displacement field from the density field + growing mode
- The displacement field will be different for neutrinos, because it will depend on its own density field.
- The growing mode is also different for both
4. Calculate the positions from displacement field + growing mode (using Zeldovich approximation)
- Again, the positions for neutrinos will be calculated from their own displacement field, and the growing mode will be different for both


### The Growing Mode


### Tests

Testing this, here are the powersectrum...

PLOT

Looks good



## Velocity Assignment

Here is the overview of the velocity assignment method:

1. Calculate the bulk velocities from the displacement field + growing modes
- This will be the same for CDM and neutrinos, but with their own displacement field.
2. For neutrinos: add extra velocity component
- This is something that was detailed in previous posts... Essentially there will be Nsidex12xNshell^2 neutrinos at each point, and each will have a different velocity vector added to the bulk velocity.

## Mass Assignment

Neutrino masses are typically expressed as the sum of neutrino masses in eV. I need to convert this to a density paramter $$\Omega_nu$$. To do this, I followed the notes here: <a href="https://pdg.lbl.gov/2020/mobile/reviews/pdf/rpp2020-rev-sum-neutrino-masses-m.pdf">. I then can convert $$\Omega_nu$$ to mass per particle in the same way I did for the dark matter particles.


## IC Code

Here is the updated IC Code with the neutrino ICs added...

CODE







## Testing in Gadget

I ran this in Gadget... Left neutrinos as a separate particle...

### Density Field

<img src="{{ site.baseurl }}/assets/plots/20220909_Snapshot.png">


### Power Spectrum


<img src="{{ site.baseurl }}/assets/plots/20220909_PowerSpectrum_DM.png">



## Next Steps

-
