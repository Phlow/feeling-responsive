---
layout: page
title: "Release Notes for VisIt 3.0.2"
header:
   image_fullwidth: "gallery-05a.png"
permalink: "/releases/release-notes-3.0.2/"
---

Welcome to VisIt's release notes page. This page describes the important
enhancements and bug-fixes that were added to this release.

1. TOC
{:toc}

### Bugs fixed in version 3.0.2

* Corrected a bug where VisIt would crash when attempting to use python expressions with other expressions as inputs.
* Corrected a launch failure on Windows when 8dot3name (shortnames) is disabled on the system.
* Corrected a bug with the mili plugin not handling integers in scientific notation.
* Corrected a bug with the Uintah reader not being able to read index.xml files.
* Corrected a bug with importing remote profiles, where it looked at the old Subversion repository for remote profiles. Now it looks at the new Git repository.
* Corrected a bug where bringing up the Elevate attributes window would crash the graphical user interface on OSX.
* Corrected a bug with the Uintah reader where it would not load because the libxml2 could not be found.
* Corrected a bug where the GUI plot list goes blank on macOS.
* Corrected a bug where the VTK reader incorrectly set topological dimension of a dataset to 0, making the dataset undrawable by VisIt. This occured in a multiblock case where the first block contained neither points nor cells.
* Corrected a bug with highlighting zones picked by their global ids. The highlighted cells were incorrect or non-existent before.
* Corrected a bug where the OriginalZoneLabels and OriginalNodeLabels variables appeared twice in the menu for Mili files.
* Corrected a viewer crash when glyphed points were scaled by a tensor.

### Enhancements in version 3.0.2

* Host profiles were added for the Oak Ridge National Laboratory's Summit system.
* Tables in the graphical user interface documentation that ran off the edge of the page have been converted to definition lists.
* Modified the batch launching at NERSC to work on Cori after the major operating system upgrade."
* Openssl was added to the list of required libraries in build_visit.
* Added the turbo color table.
* The XYZ writer replaces '?' with UNKNOWN_ATOMIC_ELEMENT and now warns the user if the dataset is not effectively point-centered.
* The Xdmf reader now supports time-varying grid counts via a top-level &lt;Information Name="TimeVaryingMetaData" Value="True"/&gt; node in the Xdmf file.
* Added a reader for Xolotl files. Xolotl is an open-source, high performance plasma-surface interactions simulator that is under development with the DOE's SciDAC program. VisIt will automatically recognize files that end with the extention ".xolotl" as Xolotl files.
* Binary distributions have been added for Ubuntu 16, Ubuntu 18, Debian 9, and Fedora 27.
* Support for reading Uintah files has been added to the Red Hat Enterprise Linux 7, Ubunutu 16, Ubuntu 18, Debian 9 and Fedora 27 binary distributions.

### Changes for VisIt developers in version 3.0.2

* Updated masonry to build adios2 for OSX.
* Corrected the building of plugins against a VisIt install for OSX.
* Corrected an xmledit failure due to missing a Qt cocoa plugin.
* PySide was removed from build_visit until we get a newer version working with VisIt.
* Corrected a bug with build_visit that prevented Uintah from being built with MPICH on Linux. This occured when specifying "--mpich --uintah" on the command line.
