---
layout: post
title:  "Consistent Trees"
date:   2020-11-13
categories: cosmo_sims
---

Now that I have switched to using Rockstar for the halo finder, I am going to use <a href="https://bitbucket.org/pbehroozi/consistent-trees/src/main/">consistent trees</a> for the merger trees (this is required to get $$V_{\rm peak}$$ for the abundance matching step).


## Install

Download from above site and run make...

problems with gcc compiler (sigh)

try updating mac...

if not change gcc options in src/Makefile (have gcc-10 installed)


## Run

go to folder with config file (mine was rockstar_param.cfg),
Make sure <code>OUTBASE</code> is where halofinder output is, and that <code>NUM_SNAPS</code> and <code>STARTING_SNAP</code> are set properly...

run
<code>perl /path/to/rockstar/scripts/gen_merger_cfg.pl <rockstar.cfg> </code>

and follow instructions...
