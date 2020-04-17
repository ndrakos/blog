---
layout: post
title:  "LDAN Pipeline"
date:   2020-04-03

categories: cosmo_sims
---

For the simulations, I will be doing post-processing on the <a href=
"https://www.nas.nasa.gov/hecc/support/kb/lou-data-analysis-nodes_413.html">Lou data analysis nodes</a> (LDANs). In this post, I am documenting my workflow and job scripts.


## Overall Plan

You can only request 1 LDAN at a time; I think the easiest approach will be to run multiple serial jobs, with each job analyzing a separate snapshot. In AHF, this will require an input file for each snapshot.



## AHF input files

I have a script on my computer for generating input files for AHF snapshots. These can then be copied over to Pleiades.

<pre><code>
#!/bin/bash

snappath=/u/ndrakos/wfirst128/ #where the snapshots will be located
snapmin=0
snapmax=500
AHFinput_stem=AHF.input #base AHF input file; missing ic_filename and outfile_prefix lines

for (( i=$snapmin; i<=$snapmax; i++ ))
do
    #echo $i

    #current snapshot
    mysnap=snapshot_$( printf '%03d' $i)


    #define lines in input file
    ic_filename=$snappath$mysnap
    outfile_prefix=$snappath$mysnap

    #create input file
    filename=$mysnap.input
    cp $AHFinput_stem $filename

    #add lines to input file
    (echo 1a; echo ic_filename=$ic_filename; echo .; echo w) | ed - $filename
    (echo 3a; echo outfile_prefix=$outfile_prefix; echo .; echo w) | ed - $filename

done


</code></pre>


## Submitting Multiple Serial Jobs

There is information <a href="https://www.nas.nasa.gov/hecc/support/kb/using-sgi-mpt-to-run-multiple-serial-jobs_184.html">here</a> on how to submit multiple serial jobs in one job script.


Here is my job script:



<pre><code>
#PBS -S /bin/csh
#PBS -j oe
#PBS -l select=1:ncpus=16:mpiprocs=16:mem=1GB
#PBS -l walltime=24:00:00
#PBS -q ldan

module load mpi-sgi/mpt
module load comp-intel/2018.3.222

setenv MPI_SHEPHERD true

cd .

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/nasa/pkgsrc/sles12/2016Q4/lib:/pleiades/u/ndrakos/install_to_here/gsl_in/lib

mpiexec -np 16 ./runAHF_wfirst128.zsh

</code></pre>



and the wrapper, <code>runAHF_wfirst128.zsh</code>:



<pre><code>

#!/bin/zsh -f  

cd /pleiades/u/ndrakos/AHF/bin
maxsnap=500
minsnap=0

i=$MPT_MPI_RANK
i=$((i+minsnap))

while ((i<=maxsnap))
do
mysnap=snapshot_$( printf '%03d' $i)
./AHF /u/ndrakos/wfirst128/${mysnap}.input
i=$((i+16))
done
</code></pre>
