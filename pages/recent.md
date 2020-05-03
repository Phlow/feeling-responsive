---
layout: page
header:
  image_fullwidth: 1tza.png
permalink: "/recent/"
last_update: "2019-10-15"
---
{% comment %}

What we want here is *new* pages or new additions to collections including
the blog. You don't want recently *modified* pages. However, the only way
to ask Jekyll about the date of a page is via its *StaticFiles* module and
there the only method available returns *modification* time, not creation
time.

For example, you might have a page that renders a collection. The members
of the collection itself are not rendered but a page about the collection is.


{% endcomment %}

{% assign products = "milk, egg, cheese, bacon, lettuce, tomato" | split: "," %}
{% assign prices = "2, 7, 4, 8.50, 1.75, 0.99" | split: "," %}

<table>
{% tablerow product in products cols:2 %}
{{ product }}
{% endtablerow %}
</table>

**Product**|**Price**
:---|---:
{% for product in products -%}
{{ product }}|{{ prices[forloop.index0] }}
{% endfor %}


{% assign lastsecs = page.last_update | date: "%s" %}
{% assign skips = "pages/recent.md pages/examples.md pages/gallery.md pages/contributors.md" %}

{% capture newline %}
{% endcapture %}

{% assign hspace32 = "" %}
{% for i in (1..32) %}
  {% assign hspace32 = hspace32 | append: "&nbsp;" %}
{% endfor %}

<h3>Recent Additions</h3>

**Date**|**Title**{{ hspace32 }}|**Excerpt**
:---|---|---
{% for page in site.pages -%}
  {%- assign pagedate = page.path | file_date | date_to_string -%}
  {%- assign pagesecs = pagedate | date: "%s" -%}
  {%- if pagesecs <= lastsecs -%}
    {%- continue -%}
  {%- endif -%}
  {%- if page.path contains "blog" -%}
    {%- continue -%}
  {%- endif -%}
  {%- if skips contains page.name -%}
    {%- continue -%}
  {%- endif -%}
{{ pagedate | date: "%d%b" }}|{{ page.title }}|{{ page.content | strip_html | truncatewords: 30 }}
{% endfor %}

{% for page in site.pages -%}
  {%- assign pagedate = page.path | file_date | date_to_string -%}
  {%- assign pagesecs = pagedate | date: "%s" -%}
  {%- if pagesecs <= lastsecs -%}
    {%- continue -%}
  {%- endif -%}
  {%- if page.path contains "blog" -%}
    {%- continue -%}
  {%- endif -%}
  {%- if skips contains page.name -%}
    {%- continue -%}
  {%- endif -%}
* {{ pagedate | date: "%d%b" }}: {{ page.title }}
  * *{{ page.content | strip_html | truncatewords: 30 }}*
{% endfor %}





{% comment %}

<ul>
{% for file in site.static_files %}
<li>{{ file.modified_time | date: "%s" }}: {{ file.path }}</li>
{% endfor %}
</ul>

<h1>Collections</h1>

{% for coll in site.collections %}
<h2>{{ coll.label }}</h2>
<ul>
  {% for doc in coll.docs %}
  <li>{{ doc.date | date: "%s" }}: {{ doc.path }}</li>
  {% endfor %}
</ul>
{% endfor %}

{% endcomment %}
