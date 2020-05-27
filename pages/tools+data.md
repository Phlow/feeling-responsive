---
layout: startpage
title: "Tools & Data"
permalink: "/tools_data/"
header: no
---


<div class="page__wrap tools-data">

  <section class="tools-data__header row row__wrap">
    <div class="columns">
      <p class="tools-data__subheading">
        In the context of <a href="https://openegoproject.wordpress.com">open_eGo</a>, several models and applications have been developed resulting in a toolchain. These data and tools provide the basis for eGo<sup>n</sup>. The data and data models were created and processed in different modules named <i>data processing</i> and <i>ding0</i>. Additional external open source tools such as <i>osmTGmod</i> and <i>SciGrid</i> were applied. Two modular planning tools (<i>eTraGo</i> and <i>eDisGo</i>) focusing on different grid levels were developed. They are combined in the inter-grid-level planning tool eGo to investigate viable grid expansion scenarios. All data sets are open data and made available on the open energy database (oedb) as part of the open energy platform - <a href="https://openenergy-platform.org/">OEP</a>. The grid planning tools access the oedb to retrieve and store data. The codes of the developed tools are open source and available on <a href="https://github.com/openego">GitHub</a>. 
      </p>
    </div>
    <div class="columns tools-data__img">
      <picture>
        <source srcset="../images/Toolchain_web_desktop.svg" media="(min-width: 641px)">
        <img srcset="../images/Toolchain_web_mobile.svg" alt="Toolchain picture">
      </picture>
    </div>
  </section>

  <section class="tools-data__tools row row__wrap">
    <div class="columns tools-data__tools-heading">
      <h2>Our tools</h2>
    </div>
    <div class="columns tools-data__tools-text">
      <p>
      Within open_eGo, we've created a family of three grid planning tools for interlinked modeling of transmission and distribution grid level
    </p>
    </div>

    {% include _tools.html %}

  </section>


  <section class="tools-data__table row row__wrap">
    <div class="columns tools-data__table-heading">
      <h2>Our data</h2>
    </div>
    <div class="columns tools-data__table-text">
      <p>
        The data is characterized by a high spatial resolution suitable for energy system modeling. It is available through the oedb. You can find the most important data sets listed in the following table.
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
    <div class="columns medium-9 tools-data__oep-right">
      <div class="row">
        <h2 class="tools-data__oep-heading">Open&shy;Energy&shy;Platform</h2>
        <p class="tools-data__oep-text">
          The OpenEnergy Platform is an open data platform used by energy researchers to publish data in an accessible manner.
        </p>
        <div class="tools-data__oep-btn">
          <a href="https://openenergy-platform.org/" class="button">Visit OEP</a>
      </div>
      </div>
    </div>
  </section>

</div>





