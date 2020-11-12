---
layout: post
title:  "2048 Simulation Summary"
date:   2020-11-12

categories: cosmo_sims
---

Here is a summary of the 2048 simulations. I had previously documented my workflow <a href="https://ndrakos.github.io/blog/cosmo_sims/Running_the_2048_Simulations/">here</a>, but there were a couple of updates.

## Job Script

Here was the pbs job script I ended up using:

```
#PBS -l select=128:ncpus=8:model=has
#PBS -l walltime=120:00:00
#PBS -q long

%module load mpi-sgi/mpt
%module load comp-intel/2018.3.222

cd $PBS_O_WORKDIR
module load pkgsrc/2018Q3 mpi-sgi/mpt
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/nasa/pkgsrc/sles12/2016Q4/lib


cd /u/ndrakos/Gadget2/
mpiexec -np 1024 dplace -c CS ./Gadget2 /nobackup/ndrakos/wfirst2048/wfirst2048_gadget.param > /nobackup/ndrakos/wfirst2048_2/output


```


## Check Output

Here is a comparison of the 2048 simulation to the 512 simulation (the colour scheme isn't ideal, but it shows they agree).

512:

<img src="{{ site.baseurl }}/assets/plots/20201112_Snapshot_512.png">


2048:

<img src="{{ site.baseurl }}/assets/plots/20201112_Snapshot_2048.png">


## Second Realization

To get a second realization, I changed all the seeds as follows (in the MUSIC .conf file):

```
[random]
seed[7]                 = 11111
seed[8]                 = 11111
seed[9]                 = 11111
seed[10]                = 11111
seed[11]                = 11111
seed[12]                = 11111
```
