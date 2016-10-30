---
layout: page
show_meta: false
title: "Past Events"
permalink: "/past_events/"
---

<!-- {% capture sorted_events %}{{ site.categories.events | sort: 'start-time' }}{% endcapture %} -->

<!-- get current time  -->
{% capture nowunix %}
   {{ 'now' | date: '%s' }}   		
{% endcapture %}
<!-- decrement by one day in seconds -->
{% assign yesterday = nowunix | minus: 86400 %}

{% assign flag = false %}
<ul>
    {% for event in site.categories.events reversed %}
    	{% capture eventtime %}
			{{ event.date | date: '%s' }}
		{% endcapture %}
		{% assign eventtime = eventtime | plus: 0 %}
	<!-- only show events later than yesterday  -->
	{% if eventtime < yesterday %}
    {% assign flag = true %}

    <li><a href="{{ site.url }}{{ event.url }}">{{ event.date | date_to_long_string }}, {{ event.start_time | date: '%R' }} [{{ event.subheadline }}]: {{ event.title }}</a></li>
    {% endif %}
    {% endfor %}
 </ul>   


