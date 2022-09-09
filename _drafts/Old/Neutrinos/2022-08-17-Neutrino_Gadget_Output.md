---
layout: post
title:  "Neutrino Gadget Output"
date:   2022-08-17
categories: neutrinos
---

Here are my notes on modifying <code>src/plugins/output_gadget2.cc</code> to include functions for writing out neutrino information.



## Modifications to output code

https://ndrakos.github.io/blog/neutrinos/MUSIC_code_breakdown/


6 fields... first is for gas, second is for dark matter particels... gonna store the neutrinos in the next field. in Gadget this is labelled "Disk", but it doesn't matter, it is treated the same as the dark matter particles.



Add
id_nu_mass, id_nu_vel, id_nu_pos

assemble_gadget_file



### Particle Numbers

The function <code>determine_particle_numbers</code> takes in the grid structure and returns the number of particles, and sets the header for the Gadget file.



### Masses

<code>write_dm_mass</code>

### Positions

I basically copied the <code>write_dm_positions</code> function, with the following modifications

The code should get the number of neutrinos from the grid structure that is passes. For neutrinos, there are multiple particles at *each* grid point.

id_dm_pos

### Velocities

## Testing

Code runs fine?
Right number of neutrinos, dark matter particles?
Check distribution of initial neutrinos, dark matter particles?
Check thermal velocities?

## Next Steps

The code is running, creating the right number of neutrinos and dark matter particles, and assigning them  velocities and positions that at first glance seem reasonable. Here are my next steps...


1. Make sure initial positions of the neutrinos are right. I will plot the power spectrum of the MUSIC ICs, and make sure this matches the input.

2. Finish implementing the neutrino velocity code. All neutrinos should have a bulk velocity, plus an extra thermal velocity. Right now I only have the thermal velocity coded in. I need to look into how to implement the bulk velocity, and test that the velocities are reasonable.

3. Test in Gadget. Check the evolution of the power spectrum, and that it makes sense
