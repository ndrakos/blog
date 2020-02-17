---
layout: page
permalink: /projects/mocks/
---

<h1>Tidal Stripping</h1>



<h2 class="page-heading">Related Posts</h2>

<ul class="post-list">

{% for post in site.categories.tidal_stripping %}
 <li><span>{{ post.date | date_to_string }}</span> &nbsp; <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}

</ul>
