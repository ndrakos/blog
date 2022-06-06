---
layout: post
title:  "IGM Neutral Fraction"
date:   2022-06-07
categories: reion
---

In this post, I calculate the IGM neutral fraction.

## The Ionized Fraction

As outlined in the <a href="">previous post</a> the volume-filling fraction of ionized gas is:

$$ \frac{ dQ_{\rm HII} }{ dt} = \frac{ \dot{n}_{\rm ion} } {\langle n_H \rangle} - \frac{Q}{\bar{t}_{\rm rec}} $$

where:
  - $$\dot{n}_{\rm ion}$$ can be calculated directly from the catalog
  - $$\langle n_H \rangle =1.9\times 10^{-7} cm^{-3}$$
  - $$t_{\rm rec} = [ C_{\rm HII} \alpha_B (1 + (1-X)/4X)  \langle n_H \rangle  (1+z)^3 ]^{-1}$$
  - $$X=0.75$$
  - $$C_{\rm HII} = 3$$ (but I will later replace this with a time dependent value)
  - $$\alpha_B = 2.6 \times 10^{-13} (T/10^4 {\rm K})^{0.76} {\rm cm^3 s^{-1}}$$
  - $$T=10^4$$ K (I will vary this later to see the effects)


For $$\dot{n}_{\rm ion}$$ I will use all the galaxies in the DREaM catalog. Later on, I can decide if I should make a cut in luminosity. I will interpolate this to get $$\dot{n}_{\rm ion}$$ as a function of $$z$$

## Calculation

First, I reframed this in terms of redshift:

$$\frac{ dQ_{\rm HII} }{ dt} = \frac{ dQ_{\rm HII} }{ dz}\frac{ dz}{ dt} =   -(1+z)H(z) \frac{ dQ_{\rm HII} }{ dz}$$

where I can just calculate $$H(z)$$ from some package; I used <code>colossus</code>.

I need a boundary condition. In this case, I will use $$Q_{\rm HII}=0$$ at $$z=12$$

I integrating the equation to $$z=4$$ using <code>odeint</code> and set a maximum $$dQ_{\rm HII}$$ value of 1.

The neutral fraction is simply $$1-dQ_{\rm HII}$$.

## Results

Here are my results, compared to the data compiled by Naidu2020. It looks great! There are a few modelling choices I want to explore later, but this is enough to get started.

<img src="{{ site.baseurl }}/assets/plots/20220607_neutral_fraction.png">
