---
layout: page
header:
  image_fullwidth: gallery_07a.png
permalink: "/contributors/"
---

{% comment %}
This is using Liquid to form a Markdown table. Others would use raw html for same.

Markdown is sensitive to spaces whereas HTML is not. So, one has to go to great lengths
to control the spacing here.

The capture newline is to capture an actual newline character in the newline variable
as Liquid doesn't understand "\n" as a newline.

The long sequence of non-breaking spaces (&nsbp;) is to ensure that the first column
of the table is wide enough to hold reasonably sized pictures.

The person's bio about themselves is truncated to 100 words.
{% endcomment %}

{% capture newline %}
{% endcapture %}

**This page is under construction and does not yet fully reflect all the contributors.**

|**Name**|**Bio**|
|:---|:---|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||
{% for person in site.contributors -%}
|![]({{ person.photo_url }})<br>{{ person.name }}<br>{{ person.affiliation }}|{{ person.content | replace: newline, " " | replace: "<p>", " " | replace: "</p>", " " | strip_newlines | truncatewords: 100 }}|
{% endfor %}
