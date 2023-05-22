---
layout: post
title:  "Bubble Size Troubleshooting Part II"
date:   2023-05-22
categories: reion
---


As discussed in my <a href="https://ndrakos.github.io/blog/reion/Bubble_Size_Troubleshooting/">previous post</a>, my reionization bubbles were growing too slowly. I suspect this is because I need to model the overlap of bubbles.


## Add an ionized background

I attempted to approximate how much individual bubble sizes should increase by adding a background in the calculation; i.e. $$f_{ esc} \dot{N}_{ion}$$ became $$f_{ esc} \dot{N}_{ ion} + \dot{N}_{background}$$,
where
$$\dot{N}_{background} = \dot{n} Q V $$, $$Q$$ is the ionized fraction and $$V$$ is the volume of the bubble.

In the previous post, I said this didn't fix things, however, I made a mistake with my conversion to proper distances, and this actually mostly works!


Here is Case I (dotted line is the expected, solid line is the measured):

<img src="{{ site.baseurl }}/assets/plots/20230522_BubbleFraction_1.png">


While this is much better than before, it still doesn't match the expected curve very well.


## Clumping

I also tried adding in a Clumping term (C=3, as used for the recombination term) to account for inhomogenities in the IGM:

$$\dot{N}_{background} = \dot{n} Q V C$$


This worked even better:

<img src="{{ site.baseurl }}/assets/plots/20230522_BubbleFraction_2.png">


## Conclusions

I'm still not sure if this is the best way to model the bubbles, but I think it looks roughly right. I will proceed with this method, unless I come up with a better idea!

I will run this for Case II as well, and see how it compares. One thing to decide for Case II is whether I should just allow $$f_{\\rm esc}$$ to vary with time. This would require modelling the evolution of the size/shape of the galaxy as well. Initially, I will just treat it as constant.

Then, the next steps will be calculating which galaxies are Lyman Alpha Emitters (I'll start by following Yajima et al. 2018 for this part). 
