---
layout: post
title:  "SED Assignment on Pleiades"
date:   2020-12-03
categories: mocks
---

Here are my notes on getting the SED assignment working on Pleiades.

First of all, I decided to run it on the Lou data analysis nodes instead of Pleaides, even though this means I can't request as many processes.


I installed FSPS according to <a href="https://ndrakos.github.io/blog/mocks/FSPS/">these instructions</a>. I also included the roman filters, as detailed <a href="https://ndrakos.github.io/blog/mocks/Roman_Filters/">here</a>

To install the python version, this required loading the python module, and remembering the <code>--user</code> flag during the python install step. At first I got an error of "Your FSPS version does not seem to be under git version control." in the python installation... this was because when I ran the make file for the fsps code, I had the wrong path in LD_LIBRARY_PATH, which resulted in a bunch of "no version information available" warnings during installation.

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
setenv SPS_HOME /u/ndrakos/Software/fsps/

cd /u/ndrakos/MockCat/Analysis

mpiexec -np 8 python MakeCatalog.py > runMakeCatalog.out

```

## Problems with Pandas

### Pickle Files

I ran into a problem with reading in the pandas files on Pleiades (they were created in python 3.9, and Pleiades only has up to version 3.7). The error message was: "unsupported pickle protocol: 5"

Since it seems like saving pandas objects to pickle files can run into all sorts of compatibility issues, I decided to use csv files instead, e.g:

```
import pandas as pd
halocat = pd.read_pickle(myfile)
halocat.to_csv(filename)
```
and then to read in the csv file,

```
halocat = pd.read_csv(filename,index_col=0)
```

### Pandas Version

The pandas version on Pleiades is outdated, and the function <code>to_numpy()</code> does not exist.

I was having trouble updating the package on Pleiades, so instead I just replaced all uses of that panda function in the code. I.e., everywhere I had something like <code>x = halocat.x.to_numpy()</code> it became <code>x = np.array(halocat.x)</code>. I don't think this introduces any problems.
