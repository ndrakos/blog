---
layout: page
permalink: /other/
title:  "Other"
---


<ul class="post-list">
  {% for post in site.categories.other %}

  <li>
    <span>{{ post.date | date: "%b %-d, %Y" }}</span> &nbsp; <a href="{{ post.url | prepend: site.baseurl }}">{{post.title }}</a>
  </li>

  {% endfor %}
</ul>
