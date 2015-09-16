---
layout: page-fullwidth
show_meta: false
subheadline: Links, revisiones, clases, material, recursos y demases
title: Recursos y Referencias
teaser: Todo lo necesario para aprender, actualizar tus conocimientos o hacer tu tarea.
permalink: /recursos/
---

## En Construcción ##

{% comment %}

<div id="blog-index" class="row">
	<div class="small-12 columns t30">
		<h1>{{ page.title }}</h1>
		{% if page.teaser %}<p class="teaser">{{ page.teaser }}</p>{% endif %}

		<dl class="accordion" data-accordion>
			{% assign counter = 1 %}
			{% for post in site.categories.gastroenterologia limit:1000 %}
			<dd class="accordion-navigation">
			<a href="#panel{{ counter }}"><span class="iconfont"></span> {% if post.subheadline %}{{ post.subheadline }} › {% endif %}<strong>{{ post.title }}</strong></a>
				<div id="panel{{ counter }}" class="content">
					{% if post.meta_description %}{{ post.meta_description | strip_html | escape }}{% elsif post.teaser %}{{ post.teaser | strip_html | escape }}{% endif %}
					<a href="{{ site.url }}{{ post.url }}" title="Read {{ post.title escape_once }}"><strong>{{ site.data.language.read_more }}</strong></a><br><br>
				</div>
			</dd>
			{% assign counter=counter | plus:1 %}
			{% endfor %}
		</dl>
	</div><!-- /.small-12.columns -->
</div><!-- /.row -->

{% endcomment %}
