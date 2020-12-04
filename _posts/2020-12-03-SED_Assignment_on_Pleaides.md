---
layout: post
title:  "SED Assignment on Pleiades"
date:   2020-12-03
categories: mocks
---

Here are my notes on getting the SED assignment working on Pleiades.

First of all, I decided to run it on the Lou data analysis nodes instead of Pleaides, even though this means I can't request as many processes.


I installed FSPS according to <a href="https://ndrakos.github.io/blog/mocks/FSPS/">these instructions</a>. This required loading the python module, and remembering the <code>--user</code> flag during the python install step.

Here is my job script:

```                                                                            
#PBS -S /bin/csh
#PBS -j oe
#PBS -l select=1:ncpus=8:mem=10MB
#PBS -l walltime=0:30:00
#PBS -q ldan

module load mpi-sgi/mpt
module load comp-intel/2018.3.222
module load python3/3.7.0

setenv MPI_SHEPHERD true

cd /u/ndrakos/MockCat/Analysis

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/nasa/pkgsrc/sles12/2016Q4/lib:/pleia\
des/u/ndrakos/install_to_here/gsl_in/lib

mpiexec -np 8 python MakeCatalog.py > runMakeCatalog.out

```
