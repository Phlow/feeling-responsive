---
layout: startpage
title: "Tools & Data"
permalink: "/tools_data/"
header: no
---


<div class="page__wrap tools-data">

  <section class="tools-data__header row row__wrap">
    <div class="large-9 columns">
      <p class="tools-data__subheading">Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat sediam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
      </p>
    </div>
    <div class="columns tools-data__img">
      <img src="{{ site.url }}{{ site.baseurl }}/images/open_ego_tool-chain_150dpi.png" alt="Image about open ego tool chain">
    </div>
  </section>

  <section class="tools-data__tools row row__wrap">
    <div class="columns tools-data__tools-heading">
      <h2>Our tools</h2>
    </div>

    {% include _tools.html %}

  </section>


  {% include openego_data.html %}

</div>





