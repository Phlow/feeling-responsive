---
layout: page
show_meta: false
title: "IoT Pilots"
subheadline: "Experimenting with IoT"
show_meta: false

header:
    title: "iot.ed.ac.uk"
    image_fullwidth: "lopy_cropped.jpg"
permalink: "/pilots/"
---

During the initial phase of rolling out the IoT infrastructure, we are encouraging different teams across the University to experiment with different ways of using infrastructure. As they develop, we will post brief descriptions of these pilot projects here.

<ul>
    {% for post in site.categories.pilot %}
    <li><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>