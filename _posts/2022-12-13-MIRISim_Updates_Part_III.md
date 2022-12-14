---
layout: post
title:  "MIRISim Updates Part III"
date:   2022-12-13
categories: cosmos_web
---


In this post I'm going to get my MIRISim pipeline working (see previous post <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Updates_Part_II/">here<>)


## Updates to MiriB

There are a couple small updates I made to the MiriB script described in the previous post.

### Save pointing information

Now, for each visit, I save all the information needed to fix the wcs, i.e. <code>np.savetxt(mypath + '/pointing.dat',np.array([telescope_v1_ra,telescope_v1_dec,local_roll]))</code>.


### Dithering pattern

MIRISim was not able to read in the dither pattern properly. I made sure to have the proper format/delimiter, <code>np.savetxt(mypath + '/dither.dat', np.array([X,Y]).T, fmt='%+.4f',delimiter=',')</code>


## MiriD

This post is mostly about running MiriSim. The base code is as follows. Note that I replaced the mirisim run command with a function that I define (<code>run_miri</code>). This code uses Daizhong's script to call all the steps that are inside Miri's run function separately, and fixes the WCS at the appropriate place.


```
##################################
# Loop through visits
##################################
from mirisim.config_parser import SimulatorConfig
from mirisim.obssim import ObservationSimulation
import mirisim.config_parser as c

for obs in obs_num:

    ##################################
    #Set up simulation
    #################################

    #Go to currect folder
    mypath = miri_path + 'Obs' + str(int(obs)) + '/'
    os.chdir(mypath)

    #set up simulation
    simulator = SimulatorConfig.from_default()
    config = c.SimConfig('config.ini')
    scene = c.SceneConfig('scene.ini')

    #fix RA, Dec, Pointing
    mydata = np.loadtxt(mypath+'pointing.dat')
    telescope_v1_ra,telescope_v1_dec,telescope_v3_pa,local_roll  = mydata
    config['Pointing_and_Optical_Path']['Pointing_Centre'] = {}
    config['Pointing_and_Optical_Path']['Pointing_Centre']['RA'] = telescope_v1_ra
    config['Pointing_and_Optical_Path']['Pointing_Centre']['DEC'] = telescope_v1_dec
    config['Pointing_and_Optical_Path']['Pointing_Centre']['PosAng'] = -local_roll
                                                                         ## needs minus here
    mysim = ObservationSimulation(config,scene,simulator,mypath,path_cbp)

    ##################################
    #Run Simulation
    #################################


    run_miri(mysim,mydata)
```



### Error 1

Was getting some error "Validator' object has no attribute 'comment_stack" at the line <code> exposure.write_illum_model(illum_model, fn_part) </code> in Daizhong's script. This looks like a problem with one of the dependancies.

Attempt 1: I reinstalled the mirisim enviornment. The original version of run_miri also needs mirage, so I downloaded to the mirisim environment in the same way Daizhong did:
pip install --upgrade git+https://github.com/spacetelescope/mirage.git. This did not fix it.

Attempt 2: I moved all of the mirage dependant steps into MiriB (i.e. just saved more things in the pointing file), and then reinstalled mirisim. This worked!


## To-do/check

My code seems to run now, and generate output for all the expected visits. I need to check (1) the sources are in the right place, and (2) the observations are in the right place/at the right angle

Other things to check (from previous post):

1. Are the units correct in BUNIT?

2. Is the pixel resolution of the FITS image fine, or should i make it more precise?

3. Right now I am just repeating the same image to make a data cube. How does MIRISIM interpolate between images in the cube?

4. How to add stars?

5. I am cutting out 0.01x0.01 degrees of the scene around the centre of the visit. Is this enough?
