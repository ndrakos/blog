---
layout: post
title:  "Writing my own IC Code"
date:   2022-08-25
categories: neutrinos
---

Altering the MUSIC code was honestly way more annoying than just writing things myself. Therefore, I'm going to write some basic IC code in python. I think this will be more useful in the long-run, since we want to implement our own code into Cholla.

For this post, I'll just focus on the dark matter component, and note where I need to add in neutrinos.


## Overall Structure


1. Define Cosmology
2. Calculate Density Field
3. Calculate Displacement Field
4. Assign Positions
5. Assign Velocities
6. Assign Masses
7. Write Gadget Output


### 1. Define Parameters


Cosmology - I will define: Omega_m, Omega_L, Omega_b, H0, sigma_8, nspec (and optionally w0 and wa)
Simulation details - box size, number of particles, redshift

When adding neutrinos, there will need to be additional parameters set (see <a href= "https://ndrakos.github.io/blog/neutrinos/Neutrino_IC_Method_Overview/">this post</a>).

### 2. Calculate Density Field

I need to:

1. Assign Gaussian amplitudes to each grid point (zero mean and unit variance)
2. Fourier transform
3. Scale with power spectrum

That will output a density field (in Fourier space)


For this need power spectrum. I'll use CAMB (see previous <a href="https://ndrakos.github.io/blog/neutrinos/Neutrino_Transfer_Function/">post</a>).

```
import camb
params = camb.CAMBparams()
params.set_cosmology(H0=H0, ombh2=Omega_b, omch2=Omega_m) #check these all in the right units
params.InitPower.set_params(ns=nspec)
params.set_matter_power(redshifts=[z_start])

PK = camb.get_matter_power_interpolator(params,var1='delta_tot',var2='delta_tot')
```

The power spectrum will be different for neutrinos, but camb includes this as well

**Question**: will I want to use delta_tot, delta_cdm or delta_nonu for the CDM particles?


Here is the code to make the density field (in Fourier space):

```

#Make gaussian field
seed(seed1)
density = random.randn(N,N,N) #gaussian field

#Fourier Transform
density = np.fft.fftn(density) #fourier space
ka = 2*np.pi*fft.fftfreq(N, d=boxlength/(N-1))
kx,ky,kz =np.meshgrid(ka,ka,ka)
k = np.sqrt(kx**2 + ky**2 + kz**2)

#scale with powerspectrum in fourier space
P = PK.P(z_start,k)
density = np.sqrt(P)*density
```


### 3. Calculate Displacement Field

The displacement field can be calculated from the density field (in Fourier space)

$$s = -i \dfrac{1}{D_+} \dfrac{k_{lmn}}{k^2{lmn}} \delta_{lmn}$$,

where $$D_+$$ is the growth factor. This can be calculated directly from an integral,  but I am currently using the fitting function from Carroll, Press & Turner (note this assumes a csomological constant). This will be easy to integrate numerically later if I chose to update it. For now I have:
```
H2 = Omega_m*(1+z_start)**3 + Omega_L
w_m =  Omega_m * (1+z_start)**3 /  H2
w_l = Omega_L /  H2
Dp = 5*w_m /(w_m **(4/7) - w_l + (1+w_m/2)*(1 + w_l/70) ) / (2*(1+z_start))

```

The inverse Fourier Transform  of $$s$$ will give the displacement field:


```
k[k==0]=np.inf #This mode can be ignored, because it corresponds to a simple change of a reference frame.
d_x = -1j /Dp * kx/k**2 * density
d_y = -1j /Dp * ky/k**2 * density
d_z = -1j /Dp * kz/k**2 * density

d_x = np.real(np.fft.ifftn(d_x))
d_y = np.real(np.fft.ifftn(d_y))
d_z = np.real(np.fft.ifftn(d_z))
```

This returns the displacement vector at each coordinate.

**Question**: Is it okay to just take the real part and ignore the imaginary part?


### 4. Assign positions

The positions are initially on the grid vertices, and then offset using the displacement field.

```
a = np.linspace(0,boxlength,N)
x,y,z =np.meshgrid(a,a,a)
x += Dp*d_x; y += Dp*d_y; z+=Dp*d_z
x = x.flatten(); y =y.flatten(); z = z.flatten()
```

This exact same procedure can be used to get neutrino points except (1) I will use a coarser grid (2) the power spectrum will be different and (3) there will be multiple neutrinos per grid point.

### Assign velocities

Bulk velocity is straightforward to calculate from the displacement field. I will need to calculate $$dD_+/da$$ first

```
Dp_dot = -3*Omega_m*(1+z_start)**4/2/H2*Dp + 5/2*Omega_m*(1+z_start)**3/H2
```

and then the velocities are

```
vx = Dp_dot*d_x/(1+z_start);
vy = Dp_dot*d_y/(1+z_start);
vz = Dp_dot*d_z/(1+z_start);

vx = vx.flatten(); vy =vy.flatten(); vz = vz.flatten()
```

Neutrinos will also have an extra velocity, which I have calculated previously <a href="https://ndrakos.github.io/blog/neutrinos/Neutrino_Velocity_Assignment_Test/">here</a>


### Assign masses

I am only considering equal mass dark matter particles, and equal mass neutrinos (note that we might change this later). Given the mass density parameter, the box size, and the cosmological parameters, I can calculate the mass per particle.

The mass of each particle should be

$$m = \Omega_m \times \rho_c \times \rm{boxlength}^3 \times N^{-3} $$

and the critical density at redshift $$z$$ is $$3 H(z)^2 / 8 \pi G$$

## Next Steps

1. Check the power spectrum of the particles
2. Check units of all steps
3. Double check the questions raised in this post
4. Write function to make gadget output
5. Check that the ICs runs fine in Gadget
6. Write neutrino part of code
7. Repeat Steps 4 and 5 with neutrinos
