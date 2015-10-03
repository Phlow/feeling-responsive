---
layout: page-fullwidth
subheadline: "Barra de herramientas para estudiantes de medicina de la Universidad Católica del Norte"
title: "LibX - Edición Medicina UCN"
teaser: "Es una extensión de navegador que facilita la búsqueda y el acceso a indexadores y motores de búsqueda de revistas, artículos de investigación e incluso sitio como UpToDate, PubMed, Harrison Online y muchos más"
header:
    image_fullwidth: /LibX/libx_header.jpg
permalink: /libx/
---

<div class="row features">
      <div class="medium-4 columns">
        <div class="round-icon">
          <span class="icon-globe"></span>
        </div>
        <h3>Acceso a todo tipo de buscadores médicos</h3>
        <hr>
        <p class="text-justify">Busca en indexadores como PubMed, libros como el "Harrison de Medicina Interna", metabuscadores de evidencia como Trip Database y muchos otros, además del Metabuscador para una búsqueda simultánea en 13 revistas electrónicas.</p>
      </div>
      <div class="medium-4 columns">
        <div class="round-icon">
          <span class="icon-cloud"></span>
        </div>
        <h3>Conexión instantánea a la Biblioteca UCN</h3>
        <hr>
        <p class="text-justify">Quieres pedir un libro que acabas de ver en internet? solo debes buscarlo desde el menú de la extensión o mejor aún, resalta su título o autor y con tan solo 2 clicks búscalo en el catálogo de la Biblioteca.</p>
      </div>
      <div class="medium-4 columns">
        <div class="round-icon">
          <span class="icon-rocket"></span>
        </div>
        <h3>Agiliza tu estudio o investigación</h3>
        <hr>
        <p class="text-justify">Haciendo click derecho sobre un enlace o una página que requiere comprar el artículo puedes usar EZproxy para acceder al artículo. También analiza los códigos de identificación (DOI, ISBN y otros) para facilitar su acceso.</p>
      </div>     
    </div>

<h2 class="text-center">¡Descárgalo!</h2>
<ul class="button-group even-2">
  <li><a href="http://libx.org/releases/ff/libx2-latest.xpi?edition=C2D48715" class="button large warning">Mozilla Firefox</a></li>
  <li><a href="http://libx.org/releases/gc/install.php?edition=C2D48715" class="button large info">Google Chrome</a></li>
</ul>

---------

<div class="row">
  <div class="large-6 columns">
      <img src="{{ site.urlimg }}LibX/1.gif">
  </div>
  <div class="large-6 columns">
      <img src="{{ site.urlimg }}LibX/2.gif">
  </div>
  <div class="large-6 columns">
      <img src="{{ site.urlimg }}LibX/3.gif">
  </div>
  <div class="large-6 columns">
      <img src="{{ site.urlimg }}LibX/4.gif">
  </div>
</div>

---------

<div class="row">
<div class="medium-4 medium-push-8 columns" markdown="1">
<div class="panel radius" markdown="1">
**Tabla de Contenidos**
{: #toc }
*  TOC
{:toc}
</div>
</div><!-- /.medium-4.columns -->


<div class="medium-8 medium-pull-4 columns" markdown="1">

# Documentación #
LibX es una extensión para Firefox y Chrome que facilita el acceso a los recursos de la biblioteca. Permite buscar en el Catálogo de la Biblioteca de Coquimbo, el Metabuscador, en bases de datos y revistas, además de conectarlo con las suscripciones de la universidad para ver o descargar artículos de pago, todo esto directamente a través del click-derecho o el icono de la UCN en su navegador.

## Barra de herramientas ##
Seleccione el buscador a utilizar <span class="round warning label">1</span> en la lista desplegable en la parte superior. Seleccione el campo (palabra clave, autor, título, ISBN / ISSN, etc.) que está buscando <span class="round warning label">2</span> en la lista desplegable a la izquierda del cuadro de búsqueda. Introduzca los términos de su búsqueda. Puede añadir más cuadros de búsqueda haciendo click en la flecha hacia abajo <span class="round warning label">3</span>, creando una búsqueda con múltiples términos en diferentes campos.
![]({{ site.urlimg }}LibX/barra_de_herramientas.png)

## Menú contextual ##
Seleccione texto en una página web y haga clic derecho para acceder al menú contextual <span class="round warning label">1</span> que permite la búsqueda en el Catálogo de la Biblioteca, PubMed, y Google Académico (*puede añadir o quitar opciones de búsqueda en las preferencias de LibX*). También hay una opción para abrir un enlace <span class="round warning label">2</span> o recargar la página <span class="round warning label">3</span> a través de EZproxy, así podrás identificarte como usuario y acceder al recurso electrónicos suscrito por la UCN cuando el acceso a un artículo está restringido. Además, en lugar de hacer clic derecho, el texto se puede arrastrar y soltar en el buscador de la barra de herramientas LibX, o sobre el icono del logotipo UCN.
<a class="th" href="{{ site.urlimg }}LibX/menu_contextual.png">
![]({{ site.urlimg }}LibX/menu_contextual-th.png)
</a>

## Soporte para el acceso fuera de la universidad a través de EZProxy ##
EZproxy es un servicio de proxy, que permite conectarse desde fuera de la universidad. La búsqueda parece originarse desde un computador de la universidad, lo que permite el acceso a los recursos autorizados sólo para estudiantes de la UCN.
![]({{ site.urlimg }}LibX/ezproxy_login.png)

## Rápido acceso al texto completo de artículos de las revistas ##
LibX utiliza Google Académico y las suscripciones de la UCN para buscar los artículos y dirige al usuario a la copia electrónica suscrita por la Biblioteca. Seleccione una cita, a continuación, arrastre y suelte en el icono del logotipo UCN en la barra de herramientas. Es posible utilizar esta función incluso desde dentro de un archivo PDF.

## Autolinks ##
LibX reconoce códigos de identificación ISSN, ISBN, PubMed ID y DOI, convirtiéndolos en enlaces que conducen a libros y revistas específicas.

## Soporte para señales integradas ##
LibX coloca "señales" (como esta ![]({{ site.urlimg }}LibX/ucn_cue.png) y esta ![]({{ site.urlimg }}LibX/sfx_cue.gif)) en las páginas web para buscar si la biblioteca tiene recursos relacionados con esa página. Cada vez que vea una señal, haga clic en esta para ver lo que la Biblioteca tiene para ofrecer. Por ejemplo: las páginas de libros en Amazon o Barnes & Noble incluirán señales que enlazan con la entrada del libro en el catálogo, y páginas como Wikipedia contienen estas "señales" al final del artículo, en la sección de referencias)
![]({{ site.urlimg }}LibX/referencias.png)

## Soporte de xISBN ##
El título de un libro puede tener diferentes códigos ISBN para la edición de bolsillo, la de tapa dura, incluso para distintas ediciones. LibX soporta el servicio xISBN de OCLC: podrá encontrar un libro, dado un ISBN, incluso si la biblioteca tiene este libro con un código ISBN diferente.

## Buscadores ##

#### Catálogo Biblioteca UCN - Coquimbo ####
![]({{ site.urlimg }}LibX/biblioteca.jpg)

Permite buscar libros, artículos, revistas, etc. en la Biblioteca UCN de Coquimbo usando varios términos de búsqueda: palabra clave, título, autor, materia, ISBN/ISSN y n° de pedido.

#### Metabuscador ####
![]({{ site.urlimg }}LibX/metabuscador.gif)

Realiza una búsqueda simultánea en 13 indexadores y revistas del área de la salud: *[videos informativos](https://www.youtube.com/user/MetabuscadorUCN/videos)*

1. MEDLINE (Ovid)
2. ScienceDirect (Elsevier)
3. Nature.com
4. Journals@Ovid Full Text (Ovid)
5. MEDLINE In-Process (Ovid)
6. Annual Reviews
7. Oxford Journals
8. Electronic Collections (OCLC)
9. Wiley InterScience - Journals
10. WOS - Science Citation Index Expanded
11. WOS - Social Sciences Citation Index
12. WOS - Arts & Humanities Citation Index
13. HVC Medicina - Revistas Impresas

#### AccessMedicine ####
![]({{ site.urlimg }}LibX/logo_acm.png)

Accede a [más de 85 libros](http://accessmedicine.mhmedical.com/readings.aspx) en inglés de la editorial McGraw-Hill, incluyendo obras como *Harrison’s Principles of Internal Medicine* y *CURRENT Medical Diagnosis & Treatment*

#### Harrison Medicina ####
![]({{ site.urlimg }}LibX/logo_harrison.png)

El sitio Web de Harrison Medicina se actualiza semanalmente y ofrece el texto completo, todas las ilustraciones y las características ampliadas en referencia a la 18ª edición de Harrison Principios de Medicina Interna. La base de datos permite una búsqueda completa y recoge los contenidos nuevos y revisados de los editores y coautores de Harrison Medicina.

#### UpToDate ####
![]({{ site.urlimg }}LibX/logo_uptodate.png)

UpToDate® es un recurso de apoyo para la toma de decisiones clínicas basado en evidencia y está creado por profesionales en el que confían los médicos para tomar decisiones en el centro de atención al paciente.

#### Trip Database ####
![]({{ site.urlimg }}LibX/logo_trip.png)

Trip es un motor de búsqueda clínico diseñado para permitir a los usuarios encontrar y utilizar rápida y fácilmente evidencia de investigaciones de alta calidad para apoyar su práctica y / o atención de salud.

#### PubMed ####
![]({{ site.urlimg }}LibX/logo_pubmed.png)

PubMed comprende más de 25 millones de referencias de literatura biomédica de MEDLINE, revistas de ciencias biológicas, y libros online. Las citaciones y los resúmenes incluyen los campos de la biomedicina y la salud, abarcando porciones de ciencias biológicas, ciencias conductuales, ciencias químicas, y Bioingeniería.

#### Web of Science ####
![]({{ site.urlimg }}LibX/logo_webofscience.png)

Web of Science contiene bases de datos de información bibliográfica y recursos de análisis de la información que permiten evaluar y analizar el rendimiento de la investigación. Su finalidad no es proporcionar el texto completo de los documentos que alberga sino proporcionar herramientas de análisis que permitan valorar su calidad científica. Permite acceder a diferentes bases de datos a través de una única interfaz de consulta pudiéndose acceder a una sola base de datos o a varias de forma simultánea. 

#### ScienceDirect ####
![]({{ site.urlimg }}LibX/logo_sciencedirect.png)

Es una base de datos multidisciplinaria líder que alberga casi una cuarta parte del contenido mundial de revistas y libros en texto completo, con más de 2.500 revistas y cerca de 20.000 libros, incluyendo artículos en prensa y contenido de acceso abierto de las revistas de Elsevier.

## Preferencias ##
Puedes personalizar las opciones de LibX, activar o desactivar sus funciones, y especificar las preferencias de visualización haciendo click en el icono de la UCN para activar la barra de herramientas desplegable, a continuación seleccione la opción "Preferencias" en el menú lateral (se abrirá una nueva pestaña en su navegador).

### Menú contextual ###
Visita la pestaña de "Context Menu" en las preferencias para añadir más opciones a tu menú contextual botón derecho del ratón (además de las opciones por defecto para volver a cargar o seguir un enlace a través de EZproxy). Marque las casillas para incluir la capacidad de buscar palabras clave, títulos y autores en las suscripciones o el Catálogo de la Biblioteca UCN, todo con sólo utilizar el menú contextual.

## Copyright ##
LibX es distribuido bajo la "Mozilla Public License". Copyright Annette Bailey y Virginia Tech.
Esta edición, dirigida a los estudiantes de Medicina de la UCN es mantenida por Víctor Tapia Jiménez (vtj001@alumnos.ucn.cl).

----------

## Privacidad ##

De acuerdo con la Política de Privacidad de LibX, al usar activamente los buscadores de la extensión, se enviará la URL de las páginas que estás visitando actualmente al servidor del catálogo de la Biblioteca UCN y al servidor EZproxy UCN.

El Proyecto LibX y sus desarrolladores utilizan Google Analytics para aprender cómo LibX está siendo utilizado en las distintas bibliotecas académicas que proporcionan a sus usuarios con una edición. 
El tipo de datos recolectados incluye cosas como el número de veces que se realiza una búsqueda en el catálogo de la biblioteca mediante la barra de herramientas (de acuerdo con la Política de privacidad de LibX, únicamente se registra el evento, no los términos de búsqueda).

Para desactivar el seguimiento del uso de Google Analytics, debes ir a la pestaña Browser en Preferences y desmarca las siguientes opciones:

* Enviar datos del uso de la extensión (por ejemplo, edición instalada, catálogos utilizados en las búsquedas) [Nota: LibX utiliza Google Analytics].
* Enviar dato de uso de las LibApp (por ejemplo, LibApps utilizados frecuentemente) [Nota: LibX utiliza Google Analytics]

</div><!-- /.medium-8.columns -->
</div><!-- /.row -->

<style>
.features {
  text-align: center; }
  .features hr {
    width: 50%;
    margin: 1rem auto; }
  .features .round-icon {
    background-color: #E87E04;
    border-radius: 50%;
    display: table;
    height: 100px;
    margin: 0px auto 1rem;
    width: 100px;
    font-size: 3rem; }
    .features .round-icon span {
      color: #fff;
      display: table-cell;
      text-align: center;
      vertical-align: middle; }
  @media only screen and (max-width: 40em) {
    .features .columns {
      margin-bottom: 5rem; } }
</style>
