---
layout: post
title:  "A Closer Look At Beta Part III"
date:   2020-01-06
categories: mocks
---

This is a continuation of the <a href="https://ndrakos.github.io/blog/mocks/A_Closer_Look_At_Beta_Part_II/">previous post</a>.

## The Problem

Considering the example from the previous post. I assigned the example galaxy an age of $$a = 0.037$$ and a SFR of $$\log10(\psi)=-0.40$$.

The e-folding time should be related as follows:

$$\psi = \dfrac{M}{x} \dfrac{a}{\tau^2 - (\tau^2 + a \tau) e^{-a/\tau}} e^{-a/\tau}$$,

where $$M$$ is the mass of the galaxy, and $$x$$ is the surviving stellar mass fraction.

This means the sample galaxy should have an e-folding time of $$0.004$$ Gyr. However, since I am imposing a minimum e-folding time of $$\tau_{\rm min} = 0.1$$ Gyr, this actually means I am implementing a SFR of $$\log10(\psi)=1.87$$, which explains why it has such a high magnitude.


## The Solution?

One possible way to fix this is to check if $$\tau=\tau_{\rm min}$$, and if it does, reassign an age. This will ensure that the SFR are imposed correctly in the SPS modelling, but it is still possible that age distributions are not reasonable.

I will implement this to check the $$\beta$$ and $$M_{\rm UV}$$ relations. Hopefully the correct SFRs will correct most of the problem. If not, I can look further into how to appropriately assign stellar ages.
