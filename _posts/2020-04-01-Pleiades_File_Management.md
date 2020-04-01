---
layout: post
title:  "Pleiades File Management"
date:   2020-03-31

categories: cosmo_sims
---

As discussed in the <a href="">previous post</a>, by default you get 8 GB on your home directory, but for long-term storage you can use the <a href="https://www.nas.nasa.gov/hecc/support/kb/the-lou-mass-storage-system_371.html">Lou Mass Storage System</a>, which has no disk quota limits.



## Lustre File System

You can store 1 TB  of data on the Lustre nobackup filesystem (hard limit of 2 TB).

To check the quota:

<code>
lfs quota -h -u username /nobackup/username
</code>



## Transfering Files

It is recommended that rather than <code>scp</code>, you use the <code>shiftc</code> command for transferring files. See
<a href="https://www.nas.nasa.gov/hecc/support/kb/entry/300">this </a> link for more information, but it works pretty much the same as scp, e.g.:

<code>
shiftc -r mydir lfe:/u/username/
</code>


## Lou Data Analysis Nodes

You can do post-processing on the <a href=
"https://www.nas.nasa.gov/hecc/support/kb/lou-data-analysis-nodes_413.html">Lou data analysis nodes</a> (LDANs).

To use the LDANs, submit your jobs to the <code>ldan</code> queue. Each job can use only one LDAN for up to three days, and each user can have a maximum of two jobs running simultaneously.

You can submit interactive PBS jobs to the LDANs from either the LFEs or the PFEs. You can submit PBS job scripts from either your Lustre home filesystem (/nobackup/username) or your Lou home filesystem (/u/username).  


## Work Flow

1) Write output from simulations to the Lustre nobackup directory; I should be able to store at least 200 snapshots with $$512^3$$ particles, and at least 5 snapshots with $$2048^3$$ particles.

2) Transfer to the lou mass storage system

3) Do post-processing (halo finders and merger trees) on LDANs

I am going to try this on the $$512^3$$ simulations, and see if I run into any problems.
