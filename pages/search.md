---
layout: page
show_meta: false
title: "Search"
permalink: "/search/"
---

{% include google_search.html %}

<form style="padding-bottom: 200px;" onsubmit="google_search()" >
  <input type="text" id="google-search" placeholder="Enter search term and hit enter">
</form>