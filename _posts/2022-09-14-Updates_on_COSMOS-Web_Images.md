---
layout: post
title:  "Updates on COSMOS-Web Images"
date:   2022-09-14
categories: cosmos_web
---


## Status of Project

### What I've Done So Far

1.  I have the input catalog, DREaM. I have also calculated <a href="https://ndrakos.github.io/blog/cosmos_web/Add_Filters_to_DREaM/">photometry</a> for a number of other bands too.

2.  I have run a <a href="https://ndrakos.github.io/blog/cosmos_web/Add_Catalog_to_Mirage/">Mirage image</a> on a reduced catalog (only taking the brightest objects) for one December visit

3. I sorted out how to run the <a href="https://ndrakos.github.io/blog/cosmos_web/JWST_Pipeline_Stage_3/">basic reduction pipeline</a> to check my simulated images, and also added the <a href="https://ndrakos.github.io/blog/cosmos_web/JWST_Pipeline_1_over_f_noise/">1/f noise fix</a>

4. I made a "COSMOS-Web Image Catalog". This is the full 1 deg^2 DREaM catalog, but I removed anything that wasn't brighter than at least 32 mag in one of the bands. This reduced the size of the catalog a factor of two. This will be the catalog I use for this project.


### Immediate Next Steps (Complete before November 1)

1. Parallelize the code (this post)

2. Double check galaxy positions are correct (this post)

3. Make sure I can get things running on CANDIDE (this post)

4. Get star list to add

5. Run Mirage on the full "COSMOS-Web Image" Catalog for all 6 December visits.

6. Look into simulating MIRI images



### Longer Term

1. Get images for the full data release (not just the December visits)

2. Look into lensing effects (talk to lensing group, maybe revisit galsim)



## Parallelization

### Mirage A - Make Mirage Catalog

This I can just do on my laptop, and take as the input catalog.

### Mirage B - Run Mirage

There are two steps: the first creates yaml files, and the second makes an image for each yaml file. The first step runs very quickly, and the second step is trivial to parallelize.

I'll just use the Pool function in Python, as they suggest

```
skip=False
yaml_files = glob(output_dir+'/*yaml')

def make_sim(yfile):
    if yfile ==(output_dir+'observation_list.yaml'):
        return

    myfile = yfile.replace(output_dir,simdata_output_dir)
    myfile = myfile.replace('.yaml', '_uncal.fits')

    if exists(myfile) and skip:
        print(myfile + ': already exists, skipping')
        return

    img_sim = imaging_simulator.ImgSim()
    img_sim.paramfile = yfile
    img_sim.create()

if __name__ == "__main__":
    pool = Pool(cpu_count())
    pool.map(make_sim, yaml_files)
    pool.close()
```

##Pipeline Steps 1 and 2

Steps 1 and 2 of the pipeline are run separately on each file. Therefore, I will parallelize these in the same way as above.

### Pipeline Step 3

As far as I can tell, this is not a step that is straight-forward to parallelize. I'll leave it for now, and check in with what others are doing.


## Double Checking Galaxy Positions


Note that I rearranged my work flow. Now my test catalog includes all galaxies with masses $$10^{10}$$ solar masses. I also updated the <code>jwst</code> python package to the newest release (1.6.2 -> 1.7.2).

I reran my code to make Mirage images and the JWST pipeline (also checking my parallelization code was working fine)

Here are the images (1 visit)

<img src="{{ site.baseurl }}/assets/plots/20220914_Mosaic_nosources.png">

Here are the objects that should be in it:

<img src="{{ site.baseurl }}/assets/plots/20220914_Mosaic.png">

Looks good!


## Using CANDIDE

These are my notes on getting Mirage running on <a href="https://candideusers.calet.org/">CANDIDE</a>, a computer cluster at IAP. This is the cluster I will be using for COSMOS-Web image related tasks.

I have a directory in home in which I'll put my scripts, and I will create a directory in "n23data1" where I will store all the data

I will use the path Henry gave for the CRDS files, so I don't have to redownload them.

I am waiting to hear if I should download the Mirage reference files, or if someone already has them on CANDIDE.

### Conda environment

I am going to use conda enviornments to install my python packages.

I can downloaded:
```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
```

Then, whenever I want to use this, I need to type <code>source ~/miniconda3/etc/profile.d/conda.sh</code> first (I added this to my .bashrc file)

To create an environment named jwst: <code>conda create -n jwst</code>
To use this environment: <code>source activate jwst</code>
To download packages: <code>conda install -n jwst [package]</code>



### Job Script

Here is my job script:
```
#!/bin/env zsh
#PBS -S /bin/zsh
#PBS -j oe
#PBS -l nodes=1:ppn=24,walltime=8:00:00

# Set variables
export MIRAGE_DATA=/n23data1/ndrakos/Mirage/
export CRDS_PATH=/n23data1/hjmcc/jwst/mirage/crds_cache
export CRDS_SERVER_URL=https://jwst-crds.stsci.edu


# Load modules
module () {
  eval $(/usr/bin/modulecmd bash $*)
}
module load openmpi/4.1.4
source ~/miniconda3/etc/profile.d/conda.sh
conda activate jwst

# Run Program
cd /home/ndrakos/COSMOS-Web/MIRAGE
mpirun -np 24 python MirageB-RunMirage.py
```

This seems to be running, except I need the Mirage reference files downloaded. Once I have those, I'll return to this.
