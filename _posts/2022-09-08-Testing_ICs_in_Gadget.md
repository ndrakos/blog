---
layout: post
title:  "Testing ICs in Gadget"
date:   2022-09-08
categories: neutrinos
---

My overall goal for this project is to write ICs that have <a href="https://ndrakos.github.io/blog/neutrinos/Neutrino_ICs_Background/">stable massive neutrinos</a>, using the method outlined <a href="https://ndrakos.github.io/blog/neutrinos/Neutrino_IC_Method_Overview/">here</a>. In a <a href="https://ndrakos.github.io/blog/neutrinos/Writing_my_own_IC_Code/"> previous post</a>, I went through how to make my own initial conditions, rather than altering existing code. I wrote code to do this for DM particles, and with the previous work I've done sorting out how to treat neutrinos, it should be trivial to add them after.

The goal of this post is to write the dark matter particles in the current code to Gadget files, and test that the initial conditions are set up correctly (i.e. the power spectrum evolves as expected). Once this is verified, I will add in my code for neutrino particles.

## Current Code

I went through how to write this code in <a href="https://ndrakos.github.io/blog/neutrinos/Writing_my_own_IC_Code/">this post</a>. Here is the current code, with some minor updates/corrections:

<object width="500" height="200" type="text/plain" data="{{site.baseurl}}/assets/files/IC_Code.txt" border="0" >
</object>


## Writing Gadget Output Files

I'm going to run this through Gadget to test my ICs. First, I need to save the ICs as a gadget file. See below my python code for writing Gadget files. Note I fiddled with a couple of things to get this to work, and I don't entirely understand some parts. However, this is just needed for the purpose of testing my ICs, so it doesn't really matter as long as it works properly.


```

def writegadget(filename, data, N_arr, m_arr, time, redshift, boxsize, Omega0, OmegaLam, h):
    '''
    File to write gadget files. For now assume to one file, and equal masses for particles.
    ---------
    filename: base of filename (if split into multiple files, leave off '.x')
    ---------
    data: Nx7 array ID, x, y, z, vx, vy, vz
    N_arr:  number of particles for each species [array of 6]
    mas_arr: mass for each species [array of 6]
    time: time of output, or expansion factor for cosmological simulations.
    redshift: z = 1/a -1, only set for cosmological integrations
    boxsize: boxsize
    Omega0, OmegaLam, h: cosmological parameters
    '''

    #Open file
    f = open(filename, "wb")

    ###############################################################
    #Make Header
    ###############################################################
    myheader = b'\x00\x01\x00\x00' #padding
    myheader += struct.pack(6*"i",*N_arr)
    myheader += struct.pack(6*"d",*m_arr)
    myheader += struct.pack("d",time)
    myheader += struct.pack("d",redshift)
    myheader += struct.pack("i",0) #unused
    myheader += struct.pack("i",0) #unused
    myheader += struct.pack(6*"i",*N_arr)
    myheader += struct.pack("i",0) #unused
    myheader += struct.pack("i",1) #I'll use only 1 file
    myheader += struct.pack("d",boxsize)
    myheader += struct.pack("d",Omega0)
    myheader += struct.pack("d",OmegaLam)
    myheader += struct.pack("d",h)
    myheader += struct.pack("i",0) #unused
    myheader += struct.pack("i",0) #unused
    myheader += struct.pack("iiiiii",0,0,0,0,0,0) #would need to change for N> 2^32 particles
    myheader += struct.pack("i",0) #unused

    padding = 256 + 4 - len(myheader)
    for i in range(int(padding/4)):
        myheader+= struct.pack("i",0)

    f.write(myheader)
    #f.write(struct.pack("ii",0,0)) # 8 bits
    f.write(b'\x00\x01\x00\x00\x00\x00\x80\x01')

    ###############################################################
    #Write particle Info
    ###############################################################

    pos = data[:,1:4].flatten()
    pos = struct.pack(pos.shape[0]*"f",*pos)
    f.write(pos)
    #f.write(struct.pack("ii",0,0)) # 8 bits
    f.write(b'\x00\x00\x80\x01\x00\x00\x80\x01')

    vel = data[:,4:7].flatten()
    vel = struct.pack(vel.shape[0]*"f",*vel)
    f.write(vel)
    #f.write(struct.pack("ii",0,0)) # 8 bits
    f.write(b'\x00\x00\x80\x01\x00\x00\x80\x00')


    ID = data[:,0].astype(int)
    ID = struct.pack(ID.shape[0]*"i",*ID)
    f.write(ID)
    #f.write(struct.pack("i",0)) # 4 bits
    f.write(b'\x00\x00\x80\x00')


    f.close()


    return
```


## Running in Gadget

I made ICs with 128 particles, and a boxsize of 100 Mpc/h at redshift z=20. I saved these as a Gadget file. I then made a Gadget param file making sure the units and cosmological parameters matched. I then ran the code in the normal way.

## Output

### Density Field

<img src="{{ site.baseurl }}/assets/plots/20220908_Snapshot.png">

This looks pretty reasonable. Obviously the resolution is not very good, so it is a bit pixelated. But looks reasonable overall!

### Power Spectrum


<img src="{{ site.baseurl }}/assets/plots/20220908_20220908_PowerSpectrum_DM.png">

This starts to deviate from theory a bit around redshift 2. I suspect this is mostly resolution related though.


## Next Steps


- Add the neutrino particles; I have most of the code to do this already, I just need to integrate it into the IC code I have.
- Run things at a higher resolution (on lux), to make some prettier plots
