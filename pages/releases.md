---
layout: page
title: "Archive of VisIt Releases"
header:
   image_fullwidth: "gallery-05a.png"
permalink: "/releases/"
---

## February, 2020 - VisIt 3.1.1 released

VisIt is a distributed, parallel visualization and graphical analysis tool for data defined on two- and three-dimensional (2D and 3D) meshes. Version 3.1.1 is primarily a bug-fix release that resolves about twenty important issues. For a complete list of changes see the [VisIt 3.1.1 Release Notes](release-notes-3.1.1).

## December, 2019 - VisIt 3.1 released

VisIt 3.1 contains many bug-fixes and new features. For a complete list of changes see the [VisIt 3.1 Release Notes](release-notes-3.1.0).

1. Added and enhanced several readers.

    Added readers for Xolotl and openPMD files. Made significant enhancements to the ADIOS2 reader, including basing it on ADIOS 2.5. Rewrote the Mili reader. It now supports a Griz-like menu, material variables, global variables, shared variables, and integration points.

2. VisIt is now available on a greater variety of Linux platforms.

    VisIt is now available on Centos 8, Debian 9, Fedora 27, Ubuntu 16, Ubuntu 18 and Ubuntu 19. These versions include parallel support by way of MPICH.

3. Significantly improved the performance of queries over time.

    The query over time performance has been improved by roughly a factor of 100 due to eliminiting multiple round trip communications between the viewer and compute engine per time step.

## September, 2019 - VisIt 3.0.2 released

VisIt 3.0.2 contains about twenty bug-fixes and new features. For a complete list of changes see the [VisIt 3.0.2 Release Notes](release-notes-3.0.2).

## July, 2019 - VisIt 3.0.1 released

VisIt 3.0.1 contains about twenty bug-fixes and new features. For a complete list of changes see the [VisIt 3.0.1 Release Notes](release-notes-3.0.1).

## April, 2019 - VisIt 3.0 released

VisIt 3.0 contains many bug-fixes and new features. For a complete list of changes see the [VisIt 3.0 Release Notes](release-notes-3.0.0).

1. VisIt now supports outputting Cinema databases.

    Cinema is an image-based database that offers low-cost interaction with simulation data. When viewing a Cinema database through a Cinema viewer, the viewer merely changes the image from the database in response to changes in camera angle and other visualization parameters rather than performing potentially expensive I/O, computational and rendering operations.

2. VisIt now supports rendering 3D images using the OSPRay.

    OSPRay features interactive CPU rendering capabilities geared towards scientific visualization applications. Advanced shading effects such as ambient occlusion, shadows, and transparency can be rendered interactively, enabling new insights into data exploration.

3. VisIt now supports plot animations.

    VisIt has been enhanced so plots can provide custom animation behaviors. These behaviors are plot-specific and are independent of the time slider animation controls. For example, the *Vector* plot can alter the length of its glyphs periodically lengthening and shortening them. Plot animation is enabled for the *Curve* and *Vector* plugins.
