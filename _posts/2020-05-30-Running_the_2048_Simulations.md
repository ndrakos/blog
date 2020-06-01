---
layout: post
title:  "Running the 2048 Simulations"
date:   2020-05-30

categories: cosmo_sims
---

I ran into some problems running the $$2048^3$$ simulations, so here I am going to document my issues and how I solved them.

## Initial Conditions

### Memory Requirements

MUSIC requires about 500GB of memory to run the $$2048^3$$ simulations (which I figured out through trial and error), which is more than is available on the regular Pleiades nodes. There is documentation <a href="https://www.nas.nasa.gov/hecc/support/kb/how-to-get-more-memory-for-your-pbs-job_222.html">here</a> on how to run higher memory jobs.

Here is the jobscript I ended up using:

```

#PBS -lselect=1:ncpus=16:ompthreads=16:model=ldan:mem=700GB
#PBS -l walltime=2:00:00
#PBS -q normal

module load comp-intel/2018.3.222

cd /nobackup/ndrakos/MUSIC/

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/nasa/pkgsrc/sles12/2016Q4/lib:/u/ndrakos/install_to_here/gsl_in/lib

./MUSIC /nobackup/ndrakos/wfirst2048/wfirst2048_ics.conf > /nobackup/ndrakos/wfirst2048/MUSIC_output

```

One thing to note is that MUSIC creates some large files when generating the ICs, so I had to move MUSIC to the nobackup drive.



### Code Crashed While Writing File

After fixing the memory problem, I kept getting this error (this is the point of the code where the ICs have been generated, and are being printed to the output file):

```

MUSIC: src/plugins/output_gadget2.cc:128: void gadget2_output_plugin<T_store>::distribute_particles(unsigned int, std::vector<std::vector<unsigned int> >&, std::vector<unsigned int>&) [with T_store = float]: Assertion `n2dist[i]==0' failed.

/var/spool/pbs/mom_priv/jobs/8833017.pbspl1.nas.nasa.gov.SC: line 11: 53443 Aborted (core dumped) ./MUSIC /nobackup/ndrakos/wfirst2048/wfirst2048_ics.conf > /nobackup/ndrakos/wfirst2048/MUSIC_output

```


I tried a few different things to try and debug this. Eventually, I found the <a href="https://groups.google.com/forum/#!forum/cosmo_music">user group</a> for the code, and after reading through some of the posts found the following:
```
for the Gadget-2 output plugin multiple output files are needed since any single standard Gadget-2 IC file can only hold up to 2**32 particles = (~ 1600**3).
```
I hadn't realized this, and had left the parameter <code>gadget_num_files = 1</code> in the MUSIC configuration file. After increasing this parameter, the code ran fine.


## Gadget Simulation

I also ran into problems with the Gadget Simulation.


### Reading in IC files

The relevant output for the error is:

```
Allocated 1872.46 MByte for particle storage. 72


reading file `/nobackup/ndrakos/wfirst2048/wfirst2048_ics.dat.0' on task=0 (con\
tains 134217728 particles.)
distributing this file to tasks 0-14
Type 0 (gas):          0  (tot=     0000000000) masstab=0
Type 1 (halo):  134217728  (tot=     0000000000) masstab=0.00152861
Type 2 (disk):         0  (tot=     0000000000) masstab=0
Type 3 (bulge):        0  (tot=     0000000000) masstab=0
Type 4 (stars):        0  (tot=     0000000000) masstab=0
Type 5 (bndry):        0  (tot=     0000000000) masstab=0

too many particles
task 497: endrun called with an error level of 1313
```

I tried increasing the number of cores and increasing the number of IC files, but that didn't work.

I then recompiled MUSIC and Gadget, making sure there were no warnings, and all the modules were loaded properly. I then regenerated the ICs, and tried rerunning. This seemed to fix this error.

### Memory Issues

After that I ran into memory issues. There are two different places this occurs: (1) internally, when Gadget throws an error, or (2) because there is not enough memory available on Pleiades.

The former gives the following eror "No domain decomposition that stays within memory bounds is possible", and can be fixed by increasing TreeAllocFactor/PartAllocFactor or by running on more processors. Currently, I am using TreeAllocFactor=1.5 and PartAllocFactor=2.0 and 1024 mpiprocesses. That seems to be working so far; if the job dies at some point I might have to increase those parameters more. Note that if you ask for too many mpiprocs, Gadget throws the following error:

```
We are out of Topnodes. Increasing the constant MAXTOPNODES might help.task 1287: endrun called with an error level of 13213
```

To get enough memory on Pleiades, I ended up requesting less cores per node. Eventually I got the code working with the following job script:

```
#PBS -l select=32:ncpus=16:model=bro
#PBS -l walltime=120:00:00
#PBS -q long

module load mpi-sgi/mpt
module load comp-intel/2018.3.222

cd /u/ndrakos/Gadget2/

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/nasa/pkgsrc/sles12/2016Q4/lib:/u/ndrak\
os/install_to_here/gsl_in/lib

mpiexec -np 512 ./Gadget2 /nobackup/ndrakos/wfirst2048/wfirst2048_gadget.param\
 > /nobackup/ndrakos/wfirst2048/output
```

<!---
### Other errors

I got the above running fine on the devel queue (which you can only run for 2 hours). Then, when running it on the long queue, it died after a few hours, with the following errors:

```

MPT: --------stack traceback-------
MPT ERROR: Rank 874(g:874) received signal SIGSEGV(11).
        Process ID: 93911, Host: r583i5n4, Program: /home6/ndrakos/Gadget2/Gadget2
        MPT Version: HPE MPT 2.17  11/30/17 08:08:29

MPT: --------stack traceback-------
MPT ERROR: MPI_COMM_WORLD rank 170 has terminated without calling MPI_Finalize()
        aborting job
MPT: Received signal 11
```
-->
