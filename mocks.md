---
layout: page
permalink: /mocks/
title:  "Mock Galaxy Catalogs"
---


<p style="text-align:justify">
Mock galaxy catalogs are used to test analysis and processing tools for surveys, as well as helping understanding various observational biases in order to interpret scientific results. I will be leading the creation on the mock galaxy catalogues for the ultra deep field in <i>WFIRST</i>, which will probe galaxies out to redshift 10 and probe the epoch of reionization.
</p>


<h2> Related Publications: </h2>
<ul>
<li> <a href="https://ui.adsabs.harvard.edu/abs/2022ApJ...926..194D/abstract">Drakos et al 2022</a> </li>
</ul>

<h2 class="page-heading">Related Posts</h2>

<ul class="post-list">
  {% for post in site.categories.mocks %}

  <li>
    <span>{{ post.date | date: "%b %-d, %Y" }}</span> &nbsp; <a href="{{ post.url | prepend: site.baseurl }}">{{post.title }}</a>
  </li>

  {% endfor %}
</ul>
