---
layout: post
title:  "Neutrinos in MUSIC"
date:   2022-04-28
categories: cosmo_ics
---


Here is my first attempt to add neutrinos to MUSIC.

<a href="https://ndrakos.github.io/blog/cosmo_ics/MUSIC_code_breakdown/">This post</a> outlines the MUSIC code, and the changes I need to make.


## MUSIC Installation

First, I checked I can still install MUSIC okay. This required a bit of debugging. <a href="https://ndrakos.github.io/blog/cosmo_sims/Installing_and_Running_MUSIC/">Here</a> are my previous notes for installing MUSIC.

### Problem 1

```
clang: error: unsupported option '-fopenmp'
```

Before, changing the compiler from g++ to g++-9 fixed all the problems. But I no longer have g++-9. So I went back to g++

For troubleshooting purposes, I again set <code>MULTITHREADFFTW</code> off to get rid of this error.

### Problem 2

```
error: a space is required between consecutive right angle brackets (use '> >')
```

This I fixed by including the flag <code>-std=c++11</code>

Now it works, but only if I keep the '-fopenmp' option turned off.


### Problem 3

General problems with segfaults in strings... switched to g++-11

## Step 1: Read in parameters

I altered MUSIC to read in a "neutrino" option the configuration file.

1. <code>main.cc</code>
- Reads in the "neutrino" parameter as an option
- Checks other settings are compatible with what I have implemented for neutrino code (i.e. does not allow for baryons or 2LPT)

2. <code>neutrino_test.conf</code>
- I added this example conf file
- This includes extra parameters needed (see <a href="https://ndrakos.github.io/blog/cosmo_ics/MUSIC_code_breakdown/">this post</a>).



## Step 2: Neutrino Displacements


## Step 3: Neutrino Velocities

Bulk velocity from power spectrum + random thermal velocity from Fermi-Dirac power spectrum...

<a href="https://ndrakos.github.io/blog/cosmo_ics/Neutrino_Implementation_in_C/">This post</a> contains my C code for implementing the neutrino ICs. I altered MUSIC to do this.

1. <code>src/nu_directions</code>
- Added this new folder with a lookup table...

2. <code>main.cc</code>



## Step 3: Outputs

1. Check that it is Gadget
2. Cleanup



## Next Steps

1. Check the power spectrum of the ICs look reasonable
2. Run in Gadget, make sure simuation looks good
