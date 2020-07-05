---
layout: page-fullwidth
title: "About"
subheadline: "In this world, a single blade can take you anywhere you want to go"
teaser: "Atemosta is a a group of content creators, engineers, and dreamers who have come together, to bring you together. Through the skills we have mastered and the hobbies we are passionate about, we want to try to give something back..."
permalink: "/about/"
header:
    image_fullwidth: "header_about_1600x300.jpg"
---

<div class="row">
  <div class="large-6 columns">
      <img src="{{site.url}}/images/about_img1_raw.jpg">
  </div>
  <div class="large-6 columns">
      <img src="{{site.url}}/images/about_img2_raw.jpg">
  </div>
</div>

...and learn at the same time.

A self-styled gamers' guild calling itself a small business, **Atemosta** wants to bring into reality all the things you love about the virtual world, *especially* community, one project at a time.

## The Team
{% for author in site.data.about %}
  <h3>{{ author.name }}</h3>
  <img src="{{ site.url }}/{{ author.avi }}" alt="{{ author.name }}" /><br>
  {{ author.info }} <br>
  <img src="{{ site.url }}/images/icon/Twitter_Social_Icon_Circle_Color.png" alt="{{ author.twitter }}" height="20" width="20" />
  <a href="{{ author.twitter_url }}">{{ author.twitter_handle}}</a>
{% endfor %}
