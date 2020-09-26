---
layout: post
title:  "SED Methods"
date:   2020-09-28
categories: mocks
---

I am generating SEDs for each galaxy in the mock catalog. I have gone through how to do this in numerous previous posts. Originally, I was going to fit the age and metallicity of the galaxies using UV properties generated from distributions. However, I decided it will be more straightforward to generate all of the free parameters from distributions, and then get the resulting UV properties.


This will give me a working method to get results for the conference; later I will check that the mass-$$M_{\rm UV}$$ and $$M_{\rm UV}$$--$$\beta$$ relations are consistent with observations. If not, I plan on first generating parameters from the distributions, and then accepting/rejecting them based on the probabilty given the UV relations.


## Method

Here is the current implementation. It has changed slightly from <a href="https://ndrakos.github.io/blog/mocks/SEDs_from_Mean_Relations/">this post</a>.

To begin, each galaxy has a mass, $$M$$ and a redshift $$z$$. Given the cosmology, we can calculate $$t_{\rm age}$$ which is the cosmological time at redshift $$z$$.

### Age

First, we choose the age of the galaxy, $$a$$. I am closely following the age distribition suggested in W18. Unlike W18, I used this for both star-forming and quiescent galaxies

The age, $$a$$ is sampled from from a truncated gaussian in $$\log_{\rm 10}(a/{\rm yr})$$ centered on 9.3 with a standard deviation of 0.7. It is truncated so that the minimum age is $$\log_{\rm 10}(a/{\rm yr})=7$$ (i.e. 10 Myr), and the maximum age is the minimum of $$\log_{\rm 10}(a/{\rm yr})=10.5$$ and $$log_{\rm 10}((t_{\rm age}-1e7)/{\rm yr})$$; this ensures star formation couldn't have started earlier than 10 Myr.

Then FSPS parameter <code>sf_start</code> is then $$t_{\rm age}-a$$



### SFR

The SFR, $$\psi$$ is described using a delayed tau model, in which

$$\psi(t) \propto t \exp{-t/\tau}$$

FSPS normalizes this, such that the total mass created over the star formation history is $$1\, M_{\odot}$$. This means that the current star formation rate of the galaxy is:

$$\psi_{\rm N} = \dfrac{a}{\tau^2 -(\tau^2+ a \tau)\exp^{-a/\tau} }  \exp{-a/\tau}$$

To scale this to the galaxy, we need to know (1) $$M$$ and (2) the fraction of the mass we expect to survive at time $$t_{\rm age}$$.

To get this, I am following <a href="https://ui.adsabs.harvard.edu/abs/2017A%26A...602A..96S/abstract">Shreiber et al. 2017</a> (equations 10 and 12 for star-forming (SF) and quiescent (Q) galaxies, respectively).


 $$\psi$$ not explicitly set in FSPS, but it is related to the age, e-folding time and mass of the galaxy



### Metallicity

As in W18, we set the stellar and ISM metallicity to be equal, $$Z$$


We get $$Z$$ for SF galaxies from the fundamental metallicity relation (eq 15 in W18). I am also following their scatter model (eqs 16-17).


For Q galaxies, $$Z$$ is sampled uniformly from the range $$-2.2<Z<0.24$$.

The FSPS parameters are <code>logzsol</code> and <code>gas_logz</code>.


### Gas Ionization

for SF galaxies, $$U_S$$ is selected from $$Z$$--$$U_S$$ relation  (eq 18 in W18), with a scatter of 0.3 dex sampled from a student's t-distribution. It is set to 0 for quiescent galaxies.

The FSPS parameter is  <code>gas_logu</code>.


### Dust Attenuation



I plan on following W18 for this; since this parameter actually depends on the size and inclination of the galaxy, which I haven't assigned yet, I have a simplified version of this working (see <a href="https://ndrakos.github.io/blog/mocks/SEDs_from_Mean_Relations/">this post</a>.)


As in W18, I neglect dust for quiescent galaxies. I am not sure how justified this is.


The FSPS parameter is  <code>dust2</code> (with the dust model we are using, <code>dust1</code> must be set to zero).



### Star-formation time


Finally, we get the e-folding time, $$\tau$$. Since this is dependent on the surviving stellar mass fraction, $$x$$ (<code>stellar_mass</code> in FSPS) this has to be calculated last.

To get this, I iterativly solved for $$\tau$$ from $$\psi(\tau) = \psi_N(\tau) \times\dfrac{M}{x}$$, updating $$x$$ on every iteration. In practice, it only takes a couple of iterations for $$\tau$$ to converge.


## Parameters to Save to Catalog

I will save the parameters needed to reproduce the SEDs; $$a$$, $$\tau$$, $$Z$$, $$\hat{\tau}_V$$ and $$U_S$$.
Additionally, I'll save the SFR $$\log_{10} \psi$$.

I will also save $$M_{\rm UV}$$ and $$\beta$$, as calculated in <a href="https://ndrakos.github.io/blog/mocks/FSPS_UV_Properties/">this post</a>.

Finally, I'll calculate the magnitude in each filter, as outlined in <a href="https://ndrakos.github.io/blog/mocks/Galaxy_Detection/">this post</a>


## Parallelizing the code

It is looping through each galaxy to assign the properties. Each galaxy takes about 0.1-60 seconds; I'm not sure why some are longer (though it seems to be in the sps.stellar_mass calculation), the time did not correlate with the values of any of the free parameters. On average, it takes about 0.4 second per galaxy. For the $$512^3$$ simulations, I have about half a million galaxies. This means I expect it to take about 2-3 days to generate SEDs for every galaxy using the current implementation.

Since it is this slow, and does not require any communitcation between iterations, I am going to parallelize it.

## Scaling Relations

### Imposed

plot distributions for each step above... check that they are what I implemented, and whether they agree with observations

### Recovered

check MUV, beta relations (fig 8,9 in W18)

check SFRs (figures 17,18 in W18)

check mass-metallicity relation (fig 20 in W18 )

check quiescent classification in UVJ color-color diagram


## To-Do

1. Include proper filters

2. Check the imposed distributions against the observations. W18 a good starting place.. Are all of these models/assumptions consistent with available data? Should I update anything?

3. Do the recovered distributions make sense with observations, or do I need to update my methods?
