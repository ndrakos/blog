---
layout: post
title:  "MIRISim Updates Part II"
date:   2022-12-08
categories: cosmos_web
---


## Work Flow

1. Run the full scene - I will do it for the full DREaM area, and update as needed.

2. I need to add a step that for every visit I (a) read in the pointing file (b) make a dither.dat file (c) make a cutout of the scene, and save it as a 3D data cube . This will be the main topic of this post!

3.  Before this script just makes the configuration file (config.ini). Now I'll also save the scene.ini file


4. Run MiriSim - This I'll have to loop through the different visits, and make sure the wcs information is correct for each. I'll address this in a later post.

## Step 1: Create Scene

I ran this on lux, and have the full scene. I can update this later as needed, but only need to run this once for all visits. See <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Scene_Part_II/">this post</a> for the code to do this.

##  Step 2: Configure

Daizhong has sorted out how to do a lot of this. I will look through his notebook and try and adapt it to my code.


### a) Read in APT pointing

I will use the values in the “*.pointing” file. Here is my chunk of code to read in the visits

```
##################################
# a) Read APT Pointing File
##################################
  
lookup = 'Observation'
visit_linenum = [] #save which line in the pointinf file each visit starts on
obs_num = [] # This is where I'll store the Observation number

#Read through file and save visit_linenum and obs_num
with open(pointing_file) as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            visit_linenum.append(num)
            obs_num.append(int(line.split()[-1]))
num_visits = len(visit_linenum)

#Save a list of dataframes for each observation
data_frames = []
for visit in visit_linenum:
    df = pd.read_csv(pointing_file, skiprows = visit+1, nrows=num_dithers,delim_whitespace=True,index_col=False)
    data_frames.append(df)

#Make a folder for each pointing
for obs in obs_num:
    path = miri_path + 'Obs' + str(obs)
    if not os.path.exists(path):
        os.makedirs(path)

#Save list of observations for this ATP File
myobsfile = pointing_file.split('/')[-1].split('.')[0]
np.savetxt(miri_path + myobsfile+ '.obs', obs_num, fmt='%i')


```

### b) Make dither.dat File

You can read in the dither pattern from the APT file (DithX and DithY), but you need to convert these to be "defined in the Imager detector plane" and in units of pixels. I mostly just copied Daizhong's code here, and made sure I got the same answer as him. I don't entirely understand this, but I am going to assume it is the correct dither pattern for now.

```
##################################
# b) Make Dither Files
##################################
import pysiaf
from mirage.utils import siaf_interface

#Loop through visits
for i in range(num_visits):
    obs = obs_num[i]
    df = data_frames[i]
    mypath = miri_path + 'Obs' + str(obs)
    telescope_v1_ra = df['RA'].iloc[0] # all RA must be the same in a dither sequence
    telescope_v1_dec = df['Dec'].iloc[0] # all Dec must be the same in a dither sequence

    #Only take Miri info and first exposure
    df = df [(df['Aperture']=='MIRIM_ILLUM') &  (df['Exp']==1)]

    #Dithers
    dithers =  df[['DithX','DithY']].to_numpy() #arcsec

    #convert to pixel coordinates
    MIRI_SIAF = pysiaf.siaf.Siaf('MIRI')
    MIRIM_FULL_SIAF = MIRI_SIAF.apertures['MIRIM_FULL']
    local_roll, attitude_matrix, fullframesize, subarray_boundaries = \
        siaf_interface.get_siaf_information(
            MIRI_SIAF, 'MIRIM_FULL', telescope_v1_ra, telescope_v1_dec, telescope_v3_pa,
            v2_arcsec = MIRIM_FULL_SIAF.V2Ref,
            v3_arcsec = MIRIM_FULL_SIAF.V3Ref, # v2 v3 ref of MIRI FULL center
    )
    dithers_pix = MIRIM_FULL_SIAF.idl_to_sci(dithers[:,0],dithers[:,1])
    X = dithers_pix[0] - MIRIM_FULL_SIAF.idl_to_sci(0,0)[0]
    Y = dithers_pix[1] - MIRIM_FULL_SIAF.idl_to_sci(0,0)[1]

    #save
    np.savetxt(mypath + '/dither.dat', np.array([X,Y]).T)
```

### c) Make Cutout of Scene

Here is my code for cutting out the scene for each observation. Note that I assumed an area of 0.01x0.01 degrees around the centre would be big enough.

```
from astropy.nddata import Cutout2D
from astropy import units as u
from astropy.coordinates import SkyCoord

#Load full scene
hdu = fits.open(source_file)[0]
wcs = astropy.wcs.WCS(hdu.header)
image_data = hdu.data


for i in range(num_visits):
    #Get info
    obs = obs_num[i]
    df = data_frames[i]
    mypath = miri_path + 'Obs' + str(obs) + '/'
    telescope_v1_ra = df['RA'].iloc[0] # all RA must be the same in a dither sequence
    telescope_v1_dec = df['Dec'].iloc[0] # all Dec must be the same in a dither sequence
    pos = SkyCoord(telescope_v1_ra ,telescope_v1_dec,unit='deg')

    #Cut out
    cut_im = Cutout2D(image_data,wcs=wcs,position=pos,size=(scene_size*u.deg),mode="trim",copy=False)

    hdu_cutout = fits.PrimaryHDU(np.array([cut_im.data,cut_im.data,cut_im.data]))
    hdu_cutout.header = hdu.header
    hdu_cutout.header.update(cut_im.wcs.to_header())
    hdu_cutout.header['CRVAL3']=7.7; hdu_cutout.header['UNIT3']='um'; hdu_cutout.header['CTYPE3']='WAVE'
    hdu_cutout.header['CDELT3']=0.1; hdu_cutout.header['CRPIX3']=1.0
    hdu_cutout.writeto(mypath + 'sources.fits', overwrite=True)
```

### Step 3: Configure

Here I can read in the observation numbers, then loop through and save a scene.ini and config.ini in each directory as follows:

```
myobsfile = pointing_file.split('/')[-1].split('.')[0]
myobsfile = miri_path + myobsfile+ '.obs'
obs_num = np.loadtxt(myobsfile)


for obs in obs_num:
    mypath = miri_path + 'Obs' + str(obs)

    ##################################
    #Save scene.ini
    ##################################

    ##################################
    #Save config.ini
    ##################################
```

### a) Save the scene.ini file

Saving the scene.ini file is straightforward

```
bg = Background(level = 'low', gradient = 5., pa = 45.,centreFOV=(3600*ra_offset,3600*dec_offset))
s = Skycube(mypath+'sources.fits')
s.fitsFilename = 'sources.fits' #give local path, because Google Drive has a space in the path which messes things up
targetlist = [s]
scene_config = SceneConfig.makeScene(loglevel=0,background=bg,targets = targetlist)
scene_config.write(mypath+'scene.ini',overwrite=True)
```

### b) Save the config.ini file

This is pretty much the same as before.

```
sim_config = SimConfig.makeSim(
name = "mirisim",    	# name given to simulation
scene = "scene.ini", 				# name of scene file to input
rel_obsdate = 0.0,          				# relative observation date (0 = launch, 1 = end of 5 yrs)
POP = 'IMA',                				# Component on which to center (Imager or MRS)
ConfigPath = 'IMA_FULL', 					# Configure the Optical path (MRS sub-band)
Dither = True,             				    # Dither
StartInd = 1,               				# start index for dither pattern
DitherPat = 'dither.dat', 	# dither pattern to use
filter = 'F770W',          					# Imager Filter to use
ima_mode = 'FAST',         					# Imager read mode (default is FAST ~ 2.3 s)
ima_frames = 45,            				# number of groups (for MIRI, # Groups = # Frames)
ima_integrations = 2,      					# number of integrations
NDither = 4,                				# number of dither positions
ima_exposures = 8,         					# number of exposures
readDetect = 'FULL',         				# Portion of detector to read out
disperser = 'SHORT',        # [NOT USED HERE]
detector = 'SW',            # [NOT USED HERE]
mrs_mode = 'SLOW',          # [NOT USED HERE]
mrs_exposures = 2,          # [NOT USED HERE]
mrs_integrations = 3,       # [NOT USED HERE]
mrs_frames = 5,             # [NOT USED HERE]
)

#Save to file
sim_config.write(mypath+'config.ini',overwrite=True)
```

### Step 4: Run MiriSim

This needs to be changed so that (1) we loop through the observations and (2) we fix the WCS information. This will be the topic of a future post.


## Stars

We need to add the star catalog. The one in Mirage was interpolated fluxes from known stars.



## To-do/check
1. Get Step 3 running

2. Are the units correct in BUNIT?

3. Is the pixel resolution of the FITS image fine, or should i make it more precise?

4. Right now I am just repeating the same image to make a data cube. How does MIRISIM interpolate between images in the cube?

5. How to add stars?

6. I am cutting out 0.01x0.01 degrees of the scene around the centre of the visit. Is this enough?
