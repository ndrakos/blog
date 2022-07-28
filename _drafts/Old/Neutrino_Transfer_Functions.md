---
layout: post
title:  "Neutrino Transfer Functions"
date:   2022-07-01
categories: cosmo_ics
---

<a href="https://ndrakos.github.io/blog/cosmo_ics/MUSIC_code_breakdown/">This post</a> outlines the MUSIC code, and the changes I need to make to put in neutrinos. I also looked into detail on how to assign velocities.

In this post I'm going into more detail on position assignments.

## Calculating

Effectively, the neutrinos are calculated the same as the CDM particles, and then given an additional thermal velocity.

Important modifications: (1) initial density field of neutrinos should be set by neutrino power spectrum (e.g. using neutrino transfer function) and (2) we are doing the neutrinos on a more coarse grid. The calculation is inserted into <code>main.cc</code> after calculating the dark matter density positions. I will calculate the density field, then the potential, and then the displacements.

## Transfer functions

### Currently in MUSIC


### Transfer function plug-ins

MUSIC takes <code>transfer</code> as an input in the config file. This is the name of the transfer plug-in. The options are
1. BBKS - fit to the transfer function without baryon
features.
2. eisenstein - fit for the CDM transfer function with baryon features
3. CAMB - for CAMB output transfer functions (tabulated). The filename of the additional option transfer_file has to indicate the file from which the tabulated transfer function shall be read.

You can also add your own plugins. "These plugins need to derive from the class transfer_function_plugin, defined in transfer_function.hh. Examples can be found in the plugins directory."


### TF Type

The different tf types in the code are "total, cdm, baryon, vtotal, vcdm, vbaryon, total0". Here, "v" indicates it is in velocity space; these are only used in the 2LPT section of the code

E.g., when setting dark matter displacements, my_tf_type is set to either (1) cdm, if there are baryons or (2) total, if there are no baryons. When setting baryon displacements, my_tf_type is set to baryon.

I should add something for massive neutrinos.

## Adding massive neutrinos


## Compile code

Try compiling code with this..
