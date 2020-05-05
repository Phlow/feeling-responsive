---
layout: page
title: "Release Notes for VisIt 3.1"
header:
   image_fullwidth: "gallery-05a.png"
permalink: "/releases/release-notes-3.1.0/"
---
Welcome to VisIt's release notes page. This page describes the important
enhancements and bug-fixes that were added to this release.

* TOC 
{:toc} 

### General features added in version 3.1

* Added binary distributions for CentOS 8 and Ubuntu 19.

### Changes in GUI behavior in version 3.1

* Modified the VCR play/reverse play buttons so that they are now inactive when there are no active drawn plots.
* Restructured several windows to reduce their height and allow for better usage on laptops. These include the Pick, Preference, Host profiles configuration setup, Poincare operator, LCS operator, Limit Cycle operator and Integral Curve operator windows.
* Modified the help menu to refer to the VisIt Sphinx manual.

### Changes in CLI behavior in version 3.1

* Added error checking of the arguments to View3DAttributes.RotateAxis().

### File format reader changes in version 3.1

* Corrected a bug with the VTK reader parsing .vtm files when the 'DataSet' tag doesn't have a 'file' attribute.
* Added the OpenPMD reader to VisIt. OpenPMD files are automatically recognized when they have the "pmd" or "opmd" extensions.
* Updated the ADIOS2 reader to use ADIOS2 2.5.
* Improved and corrected the handling of 2/3D tensor and symmetric tensor data in the Silo reader.

### Changes to VisIt's plots in version 3.1

* Enhanced the Pseudocolor plot so that it can now render lines as tubes and ribbons and points as glyphs in mixed-topology unstructured grids and poly data.
* Enhanced the Pseudocolor plot so that it can now glyph points when *Draw objects as* is set to *Points*.

### Changes to VisIt's expression language in version 3.1

* Added the *divide* expression to allow users to specify a divide by zero value and a tolerance for zero.
* Enhanced the *min* and *max* expressssions to support more than two input variables.

### Changes to VisIt's picks and queries in version 3.1

* Corrected a bug where sometimes it wasn't possible to pick on a glyphed point lying near the dataset bounds.

### Other bugs fixed in version 3.1

* Changing the opacity for a Pseudocolor plot no longer affects the glyph type of glyphed points.
* Corrected an issue with installing host profiles after deleting or moving the .visit folder while VisIt is running.
* Removed the visual artifacts of the Expressions window that were present when the window was first rendered.
* Corrected a memory leak with Pseudocolor plots.
* Corrected a bug with MPEG movies being generated upside down with incorrect colors.
* Corrected a memory leak associated with reading ghost cells and nodes in the LibSim reader.
* Corrected a bug with the Pick 'output object' output for tensor variables.
* Corrected a bug with Pick where array variables were sometimes erroneously treated as vectors or tensors.

### Build changes in version 3.1

* Enhanced build_visit to enable OpenSSL by default since Python depends on OpenSSL and Python is enabled by default.
* Corrected a bug in build_visit that prevented OSMesa and MesaGL from building from within a Git checkout.
* Added a patch to build_visit so that Qt builds on CentOS 8 and Ubuntu 19.
* Modified build_visit so that it would build Adios2 on Mac OS X.
* Modified build_visit to correct a compile error with LLVM compiling with icc 19.0.4.
* Modified build_visit to include Python3 and Sphinx-2.2.1.
* Modified build_visit so that Conduit would properly pick up the Fortran compiler.

### Changes for VisIt developers in version 3.1

* Suppressed the Qt warning 'Empty filename passed to function'. Also added additional context information to the Qt log message if available.
* Corrected compile errors when using Open MPI 1.6.5.
* Re-factored sections of the Silo reader for recognizing variable types in metadata to a single function.
* Corrected problems compiling Adios2 on Mac OS X 10.13.6

### Changes to VisIt documentation in version 3.1

* Tensor expression functions have been fully documented.
* Documentation now supports collapsible sections. For examples, see sections to show/hide code in the documentation of tensor expression functions.
* Corrected compile issues with some of the Fortran LibSim examples.
