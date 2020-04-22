---
layout: page
title: "Release Notes for VisIt 3.0.1"
header:
   image_fullwidth: "gallery_05a.png"
permalink: "/releases/release-notes-3.0.1/"
---

Welcome to VisIt's release notes page. This page describes the important enhancements and bug-fixes that were added to this release.

### Bugs fixed in version 3.0.1

* Corrected a bug where VisIt would crash rendering transparent geometry when processor 0 didn't have any geometry.
* Corrected a bug where VisIt would not switch into scalable rendering mode when it should have when the total number of primitives to render was greater than 2 billion. This typically resulted in VisIt crashing because it ran out of memory.
* Corrected the batch launching on Sierra type systems at Lawrence Livermore National Laboratory.
* Corrected a bug where glyphed points color were rendered in the wrong color when transparency was turned on.
* Corrected a bug with the Expressions window where the 'Type' indicator in the variable definition would become blank when 'Apply' was clicked.
* Corrected the inability to change the opacity attenuation when using ray casting in the Volume plot.
* Updated the language translations in the graphical user interface.
* Added support for cell-centered data with the Pseudocololor plot's line geometry options (tube, ribbon, endpoints).
* Corrected a bug where the tool bar would be rendered with nonsense imagery when an image was zoomed for the first time in *Zoom* mode.

### Enhancements in version 3.0.1

* Rewrote the Mili database reader. Among other things, the plugin now supports a Griz-like menu, material variables, global variables, shared variables, and integration points. At the moment, only the mid integration point is available for visualization and is selected by default. Future updates will allow the user to change which integration point is used. Also, the old .mili file format is no longer valid. You can create new .mili files by using the updated makemili tool, located in visit/bin.
* Added database readers for ADIOS2 version 2.4.0.
* Changed the default for the color table in the Pseudocolor and Surface plots from 'hot' to 'Default' making those plots use the default color map by default.
* Switched to case-insensitive variable name sorting in the graphical user interface.
* Enhanced the default volume renderer to allow adjusting ambient, diffuse, specular, and shininess lighting properties.
* Added host profiles for the Lawrence Livermore National Laboriatories' Cmax system.
* Increased the maximum number of characters allowed in file and dataset names from 1023 to 2047 in the XDMF reader.
* Added ability for internallauncher to launch single-processor parallel engines.
* Removed the host profiles for the NERSC *edison* machine.
* Removed the CCM reader.

### Changes for VisIt developers in version 3.0.1

* The Python command line interface documentation generation has been reversed so that developers now modify the rst files in the Sphinx documentaion first and then automatically generate the MethodDoc.C and MethodDoc.h files.
