---
layout: page
permalink: /neutrinos/
title:  "Massive Neutrinos"
---


<p style="text-align:justify">
In this project, I will look into modifying cosmological initial conditions to include neutrinos.
</p>



<h2 class="page-heading">Related Posts</h2>

<ul class="post-list">
  {% for post in site.categories.neutrinos %}

  <li>
    <span>{{ post.date | date: "%b %-d, %Y" }}</span> &nbsp; <a href="{{ post.url | prepend: site.baseurl }}">{{post.title }}</a>
  </li>

  {% endfor %}
</ul>
