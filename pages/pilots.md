---
layout: pilot
show_meta: false
title: "IoT Pilots"
subheadline: "Experimenting with IoT"
show_meta: false

header:
    title: "iot.ed.ac.uk"
    image_fullwidth: "lopy.jpg"
permalink: "/pilots/"
---

During the initial phase of rolling out the IoT infrastructure, we are encouraging different teams across the University to experiment with different ways of using infrastructure. As they develop, we will post brief descriptions of these pilot projects here.


{% for pilot in site.pilots %}

<div class="t30">
 
 
 <h3><img src="{{ site.urlimg }}{{ pilot.image }}">{{ pilot.title }}</h3>
 <p>
 {{ pilot.content }}
 </p>
 </div>

 


</div>
{% endfor %}