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


{% for pilot in site.pilots %}
<div class="pilot">
<h2><a href="{{ pilot.url }}">{{ pilot.title }}</a></h2>
</div>
{% endfor %}