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
      <img src="{{ site.url }}{{ site.baseurl }}/images/open_ego_tool-chain_noBorder.svg" alt="Image about open ego tool chain">
    </div>
  </section>

  <section class="tools-data__tools row row__wrap">
    <div class="columns tools-data__tools-heading">
      <h2>Our tools</h2>
    </div>

    {% include _tools.html %}

  </section>


  <section class="tools-data__table row row__wrap">
    <div class="columns tools-data__table-heading">
      <h2>Our data</h2>
    </div>
    <div class="large-9 columns">
      <p class="tools-data__table-text">Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat sediam voluptua.
      </p>
    </div>
    <div class="columns tools-data__table-content">
      {% include openego_data.html %}
    </div>
  </section>

  <section class="tools-data__oep row row__wrap">
    <div class="columns medium-3 tools-data__oep-logo">
      <img src="{{ site.url }}{{ site.baseurl }}/images/OEP_logo.svg" alt="Logo oedb">
    </div>
    <div class="columns medium-7 tools-data__oep-right">
      <div class="row">
        <h2 class="tools-data__oep-heading">OpenEnergyPlatform</h2>
        <p class="tools-data__oep-text">Lorem ipsum dolor sit amet, consetetur sadipscing elitr dolor sit amet, consetetur sadipscing elitr</p>
        <div class="tools-data__oep-btn">
          <a href="#" class="button">To Platform</a>
      </div>
      </div>
    </div>
  </section>

</div>





