---
layout: post
title:  "Merger Simulation Setup"
date:   2022-01-28
categories: iso_ics
---

I will be running a suite of mergers for Justin (at Waterloo), who is looking at the time oscillations of dark matter halo properties. Here are my notes on the setup.


## Fiducial Case

The fiducial case will be two NFW halos with a mass ratio of 5:1, and orbital parameters $$\eta =1$$ (energy divided by the energy of a circular orbit at the virial radius) and $$\epsilon=0.5$$ (circularity; the angular momentum divided by the angular momentum of a circular orbit with the same energy). We will assume both NFW halos have a concentration of 10, and truncate the ICs at these radii.


## Creating the particle ICs


### Set up ICs for each individual halo

I generated each halo using ICICLE. Each truncated NFW profile needs to be given $$G$$, $$m$$, $$N_0$$, $$r_s$$ and $$r_{\rm vir}$$. I will set $$G=1$$.

Halo A has parameters $$r_{s, A}=1$$, $$r_{\rm cut, A = 10}$$, $$N_{0,A} = 5\times 10^5$$, $$m = 1/N_{0,A} = 2 \times 10^{-6}$$. After truncation, $$N_A=321676$$ and $$M_A\approx0.64$$.

Halo B is intended to have 1/5th of the mass and the same "concentration" as Halo A. The mass of each particle will be kept as $m$. The "virial radius" should scale as $$r_{\rm vir, B} = \left(\frac{M_{B}}{M_{A}} \right)^{1/3}  r_{\rm vir, A}$$. Therefore, I set $$r_{\rm cut, B} = 5.85$$ and $$r_{s, B} = 0.585$$. I begin with $$N_{0,B} = N_{0,A}/5 = 10^5$$ particles, resulting in $N_B=64333$ and $$M_B\approx 0.13$$ after truncation. *(Note for the last test simulation I sent, I just kept $$r_s=1$$ the same for each halo. This would mean that they had different concentrations, though both were truncated at $$r_s=10$$. I think the way I set it up here is more physical).*


### Determine orbital parameters

At time=0 halo A will be placed at the origin, and given no net velocity (i.e. we make no change to the ICs from ICICLE).

Halo B will be given a net velocity, and a radial separation to give the proper orbital parameters (eta and epsilon).


There is some discussion in <a href="">Drakos et al. 2019a</a> about the eta and epsilon parameters, and how they are calculated. Neither is particularly well-suited for describing isolated simulations. Nevertheless, we want mergers that are representative of those found in simulations. Therefore, I'm going to make a number of assumptions to get orbital parameters that seem reasonable (we can update these parameter calculations later if you would like).

I am going to do these calculations assuming Halo B is a point-mass (with mass $$M_B$$) orbiting within the (infinitely extended) Halo A. Halo A will then be described by an NFW profile with mass $$M_{A,untrunc} = N0*m$$ inside $$r_{vir,A}=10$$. The calculated energies will not be the same as if we had calculated them directly from the particles (i.e. Eqs 5 and 6 in Drakos+2019a).


#### 1) Convert eta -> orbital energy and epsilon -> angular momentum

The energy of this orbit is:

```
rvir = 10; G = 1; r_s = 1; N0 = 5e5; m = 2e-6
rho0 =  N0*m / (4.0*pi*r_s*r_s*r_s*(log(1 + rvir/r_s)-rvir/(r_s+rvir)))
E = -2.0*pi*G*rho0*r_s*r_s*r_s*( np.log(rvir/r_s +1.0)/rvir + 1.0/(rvir+r_s)) #relative energy
```


For $$\eta \approx 1$$, this corresponds to an orbital (relative) energy of -0.11 in the simulation units.


The (relative) angular momentum of a circular orbit at the radius with the same energy (for $$\eta=1$$ this is just the virial radius) is:

```
rc = rvir
M = 4.0*pi*rho0*r_s**3 * (np.log(1 + rc/r_s)-rc/(r_s+rc))
Vc = np.sqrt(G*M/rc)
Lc = rc*Vc #relative angular momentum
```

for a circularity of 0.5, this corresponds to a (relative) angular momentum of $$L = 0.5*Lc = 1.58 $$ in the simulation units.


Therefore, we will set the energy of the orbit to -0.11 and the angular momentum to 1.58.


#### 2) Convert (relative) orbital energy and angular momentum to radial separation and initial velocity


```
from scipy import optimize
def NFW_orb_params(E,L,rho0,r_s,G):
    #########################################################
    # given the energy and angular momentum of a point mass Mpoint
    # orbiting in NFW profile with params rho0 and r_s
    # returns v0 and rsep for ICs
    #########################################################


    def myfunc(rsep,E,L,rho0,r_s,G):

        v0 = L/(rsep)

        K =  v0**2/2
        P = - 4* np.pi*G*rho0*r_s**3 * np.log(rsep/r_s +1.0) / rsep
        Eorb = P+K # (relative) orbital energy

        return (E-Eorb)

    rsep = optimize.root(myfunc,r_s,args=(E,L,rho0,r_s,G)).x[0]
    v0 = L/rsep

    return rsep, v0
```


This gives $v0=0.69$ and $rsep = 2.29$ in the simulation units.


### Add ICs together

I add [r_sep, 0, 0, 0, v0 , 0] to the [x,y,z,vx,vy,vz] values of Halo B, and combine the two IC files.

The total number of particles is 386009 particles, each with mass 2e-06.





## Running the Simulation


I used James' "write_single_ICs" program to convert the ICs to the binary gadget format.


I just set these parameters the same as before, with the assumption they should be reasonable:

```
TimeMax 100
TimeBetSnapshot 1
SofteningHalo 0.02
ErrTolIntAccuracy 0.02
```

We can update these if needed. All the other Gadget parameters were pretty standard.


I then ran the simulation on the supercomputer lux.
