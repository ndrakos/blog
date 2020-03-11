---
layout: post
title:  "Installing and Running MUSIC"
date:   2020-03-11

categories: cosmo_sims
---


I will be running some cosmological simulations with a high number of time outputs for various applications. This will require generating initial conditions, which I plan to do using <a href="https://ui.adsabs.harvard.edu/abs/2011MNRAS.415.2101H/abstract"> MUSIC </a> which can be downloaded <a href="https://www-n.oca.eu/ohahn/MUSIC/">here</a>. Here are my notes on getting it running.


## Installation (debugging notes)

I am installing the package on my laptop (macOS Catalina) according to the User's Guide. Here are the issues I ran into:

### Problem 1

```
clang: error: unsupported option '-fopenmp'
```

This seems to be a problem on my Mac. For now, I just turned off <code>MULTITHREADFFTW</code> in the Makefile.

### Problem 2

```
fatal error: 'fftw3.h' file not found
```

I ran <code>brew install fftw</code> and now this is fine (I had already followed the instructions in the User's Guide for installing fftw3, but guess I missed something).

### Problem 3

A bunch of errors with cmath that look like:

```
Library/Developer/CommandLineTools/usr/bin/../include/c++/v1/cmath:327:9: error: no member named 'islessequal' in the global
      namespace
 ```

When installing  <span style="font-variant:small-caps;">AHF</span> I ran into similar problems and fixed it by changing the compiler in the Makefile from gcc to gcc-9 (I don't remember why I had to did this). So anyway, changing from g++ to g++-9 seems to fix things. Bonus: it also fixes Problem 1, so now I can turn multi-threading back on.



## Running the Code

The code comes with an example <ics_example.conf>. I un-commented the lines corresponding to <span style="font-variant:small-caps;">gadget-2</span> output and ran:

```
./MUSIC ics_example.conf
```

and it all seems to work fine!



## Configuration Parameters

There are numerous parameters that you can set in the config file. Here I'll try and go through what seem to be the more important ones (and ignore the ones that seem fine to leave as default).

### Setup

For the given simulation, you need to specify: <boxlength>, <zstart> (and <baryons> if including those)

<code>use_2LPT</code>: I will set this to yes since second-order lagrangian perturbation theory is more accurate (<a href="https://ui.adsabs.harvard.edu/abs/2010MNRAS.403.1859J/abstract"> Jenkins 2010 </a>)


For unigrid simulations, set <levelmin> = <levelmax>. This value should be $$\log_2 N^3$$, where $$N^3$$ is the number of particles.

In principle, <levelmin_TF> could be set higher than <levelmin>, but I will just keep it equal.


### Cosmology

Cosmological parameters: <code>Omega_m</code>, <code>Omega_L</code>, <code>Omega_b</code>, <code>H0</code>, <code>sigma_8</code> and <code>nspec</code>
Transfer function: I'll use the <eisenstein> option

### Random

Can specify seeds. Doesn't matter for my purposes.


### Output

Specify <code>format</code> and <code>filename</code>

### Poisson

This I will leave to default...

## Next Steps

Okay, so as far as I can tell, I have MUSIC working on my machine. Next I'll run a really small simulation with them and check everything looks right. I should also get all of this working on Pleiades.
