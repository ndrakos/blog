---
layout: post
title:  "Writing my own IC Code"
date:   2022-08-17
categories: neutrinos
---

Altering the MUSIC code was honestly way more annoying than just writing things myself. Therefore, I'm going to write some basic IC code in python. I think this will be more useful in the long-run, since we want to implement our own code into Cholla.


##Overall Structure


1. Define Cosmology
2. Calculate Density Field
3. Calculate Displacement Field
4. Assign Positions
5. Assign Velocities
6. Assign Masses
7. Write Gadget Output


## 1. Define Cosmology

Which parameters do I need?

note need to specify a scale factor to get power spectrum...

## 2. Calculate Density Field

Need to write a function that will

1. Assign Gaussian amplitudes to each grid point (zero mean and unit variance)
2. Fourier transform
3. Scale with power spectrum

That will output a density field (in fourier space)

For this need power spectrum... I'll use CAMB... see previous post https://ndrakos.github.io/blog/neutrinos/Neutrino_Transfer_Function/

Power spectrum will be different for neutrinos...



## 3. Calculate Displacement Field

The displacement field can be calculated from the density field (in fourier space)

$$s = -i \dfrac{1}{D_+} \dfrac{k_{lmn}}{k^2{lmn}} \delta_{lmn}$$

And then inverse fourier transform...


## 4. Assign positions


Note there will be multiple neutrinos per grid point...

## Assign velocities

Bulk velocity:

Neutrinos have an extra velocity:


## Assign masses

I am only considering equal mass dark matter particles, and equal mass neutrinos (note that we might change this later)

## Gadget Output
