---
layout: page
permalink: /reion/
title:  "Reionization Constraints"
---


<p style="text-align:justify">
In this project, I will use the DREaM catalogs to check how well upcoming surveys will be able to constrain reionization.
</p>



<h2 class="page-heading">Related Posts</h2>

<ul class="post-list">
  {% for post in site.categories.reion %}

  <li>
    <span>{{ post.date | date: "%b %-d, %Y" }}</span> &nbsp; <a href="{{ post.url | prepend: site.baseurl }}">{{post.title }}</a>
  </li>

  {% endfor %}
</ul>
