---
layout: post
title:  "Consistent Trees"
date:   2021-02-02
categories: cosmo_sims
---

Now that I have switched to using Rockstar for the halo finder, I am going to use <a href="https://bitbucket.org/pbehroozi/consistent-trees/src/main/">consistent trees</a> for the merger trees (this is required to get $$V_{\rm peak}$$ for the abundance matching step).


## Install

I downloaded the code and ran make.

(When trying to install on my laptop I ran into problems with gcc compiler, but fixed it by specifying the compiler in the file src/Makefile (I set CC = gcc-10))

## Run

Go to the folder with the config file (mine was rockstar_param.cfg). Make sure <code>OUTBASE</code> is where halofinder output is, and that <code>NUM_SNAPS</code> and <code>STARTING_SNAP</code> are set properly.

Then, run

<code>perl /path/to/rockstar/scripts/gen_merger_cfg.pl rockstar.cfg </code>

and follow the instructions.

On Pleiades, I can run submit a job script to run the trees:

```
#PBS -S /bin/csh
#PBS -j oe
#PBS -l select=1:ncpus=1:mem=100MB
#PBS -l walltime=2:00:00
#PBS -q ldan

module load mpi-sgi/mpt
module load comp-intel/2018.3.222
module load python3/3.7.0

setenv MPI_SHEPHERD true

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/nasa/pkgsrc/sles12/2016Q4/lib:/pleiades/u/ndrakos/insta\
ll_to_here/gsl_in/lib

cd /pleiades/u/ndrakos/consistent_trees

perl /pleiades/u/ndrakos/Rockstar/scripts/gen_merger_cfg.pl /u/ndrakos/wfirst128/HaloFinder/rockstar_param.cfg
perl do_merger_tree.pl /u/ndrakos/wfirst128/HaloFinder/outputs/merger_tree.cfg > outputTrees
perl halo_trees_to_catalog.pl /u/ndrakos/wfirst128/HaloFinder/outputs/merger_tree.cfg > outputTrees2
```
