---
layout: page
title: Examples Gallery
header:
    image_fullwidth: "summit_and_sierra-fs8.png"
permalink: "/examples/"
---

{% capture newline %}
{% endcapture %}

{%- for ex in site.examples -%}
{%- assign split_url = ex.image | split: '.' -%}
{%- capture thumb_url -%}{{split_url[0]}}-thumb.{{split_url[1]}}{%- endcapture -%}
|[![]({{ site.urlimg }}{{ thumb_url }})]({{ site.baseurl }}{{ ex.url }}){%- cycle "", "", "", newline -%}{%- endfor -%}
