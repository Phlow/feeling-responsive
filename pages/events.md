---
layout: page
show_meta: false
title: "Forthcoming Events"
permalink: "/events/"
---

<!-- {% capture sorted_events %}{{ site.categories.events | sort: 'start-time' }}{% endcapture %} -->

<!-- get current time  -->
{% capture nowunix %}
   {{ 'now' | date: '%s' }}   		
{% endcapture %}
{% assign nowunix = nowunix | plus: 0 %}


<ul>
    {% for event in site.categories.events reversed %}
    	{% capture eventtime %}
			{{ event.date | date: '%s' }}
		{% endcapture %}
		{% assign eventtime = eventtime | plus: 0 %}
	<!-- only show events later than now  -->
	{% if eventtime > nowunix %}
    <li><a href="{{ site.url }}{{ event.url }}">{{ event.date | date_to_long_string }}, {{ event.start_time | date: '%R' }} [{{ event.subheadline }}]: {{ event.title }}</a></li>
    {% endif %}
    {% endfor %}
</ul>
