---
layout: page
title: "Coordination"
permalink: "/coordination/"
---

At present, the {{ site.title }} is organised by an informal Coordination Group, consisting of the following members:

<ul>
{% for coordinator in site.data.coordinators %}
  <li>
  {% if coordinator.url %}
    <a href="{{ coordinator.url }}"> {{ coordinator.name }}</a> 
  {% else %}  
    {{ coordinator.name }}
  {% endif %}

    &mdash; 
   {% if coordinator.job %}
    {{ coordinator.job }}, 
   {% endif %}
    {{ coordinator.affiliation }}
  </li>
{% endfor %}
</ul>

