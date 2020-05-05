---
layout: page
title: "Release Notes for VisIt 3.1.1"
header:
   image_fullwidth: "gallery-05a.png"
permalink: "/releases/release-notes-3.1.1/"
---

Welcome to VisIt's release notes page. This page describes the important
enhancements and bug-fixes that were added to this release.

1. TOC
{:toc}

### Bugs fixed in version 3.1.1

* Corrected a bug where certain types of mili datasets would cause unexpected crashes.
* Corrected a bug where the Data level comparison wizard would always enter zero for the simulation cycle.
* Corrected a bug where zone pick highlights were incorrect after transforms were applied.
* Corrected a bug summing mesh_quality/volume in a sub-material setting.
* Corrected a bug where VisIt crashes on start-up on some Windows systems when the system OpenGL version is too old. VisIt now determines the OpenGL version during the installation process and uses Mesa3D as a drop-in replacement if needed, with a warning on the installer pages to notify the user that the graphics cards / drivers should be updated.
* Corrected a bug importing remote profiles from a Windows system.
* Corrected a bug performing QueryOverTime with plots involving operator-created expressions.
* Corrected a bug where VisIt would only display a black window when displaying on a Windows system running the XWin-32 X Server.
* Corrected a bug with external surfaces not display with Pseudocolor Plots when the centering is changed from original centering.
* Corrected a bug where makemili_driver was not properly installed, making it unusable.

### Enhancements in version 3.1.1

* Updated the mfem library to version 4.0.
* Added host profiles for Leibniz Supercomputing Centre.
* Enhanced the FFP database plugin and enhanced to use libstripack when it is available, either installed in VisIt's lib dir or the path specified via the VISIT_FFP_STRIPACK_PATH environment variable.
* Removed the host profile for Lawrence Livermore National Laboratory's rzuseq system.
* Removed the use of the rzgw gateway from all the Lawrence Livermore National Laboratory's RZ host profiles.

### Changes for VisIt developers in version 3.1.1

* Updated build_visit to work on macOS 10.14.
* Enhanced build_visit to download the visit source code and third party libraries from GitHub instead of NERSC."
* Updated build_visit to allow the user to disable the building of Sphinx. To disable building Sphinx specify "--no-sphinx".
* Enhanced build_visit to also package VisIt into a tar file after building it so that VisIt is ready to install.
* Enhanced build_visit to also build the VisIt manuals when building VisIt.
* Enhanced build_visit to add checksums for the VisIt source tar file when writing a unified file. It assumes that the tar file containing the VisIt source file is in the current directory. If any errors are encountered and it can't add the checksums a warning is printed.
