---
layout: page
title: "Release Notes for VisIt 3.1.2"
header:
   image_fullwidth: "gallery-05a.png"
permalink: "/releases/release-notes-3.1.2/"
---

Welcome to VisIt's release notes page. This page describes the important
enhancements and bug-fixes that were added to this release.

1. TOC
{:toc}

### Bugs fixed in version 3.1.2

* Fixed a bug with the xml tools where they would fail when the full version was specified (eg xml2cmake -v 3.1.2).
* Fixed a bug printing to printers or PDF files on Windows.
* Fixed a bug where the pick operator would choose ghost zones while picking from mili datasets.
* Fixed several bugs with the Blueprint reader for cases where domain data also exists in the root file.
* Fixed the ability to save a movie template via the <i>Save Movie Wizard</i> on Windows.
* Fixed several bugs with the avtLinesFileFormat reader. The reader now distinguishes between 2D from 3D and will not remove identical consecutive points that exist on different lines.
* Fixed a crash with the generation of ghost zones using global node ids where there were NULL domains.
* Fixed a bug that caused trilinear ray casting to have very harsh lighting.
* Fixed a bug with importing remote hosts.
* Fixed a bug that was preventing VisIt from correctly generating normals for triangle strips.
* Fixed a bug reading files generated with newer Exodus libraries.
* Fixed a bug preventing full removal of the axes when using OSPRay rendering.
* Fixed a bug where 2D axes annotation font settings weren't always saved to config files.
* Fixed a bug where lines starting with !TIME and !ENSEMBLE ".visit" files weren't being processed properly and were interpreted as file names.
* Fixed a bug that was producing bad volumes on datasets with cells of multiple dimensions.
* Reduced the amount of '.' characters written to log files while waiting for processes to connect.
* Fixed a crash when performing a choose center operation when there weren't any non-hidden active plots while in scalable rendering mode. It now prints an error message requesting that the user select a non-hidden plot.
* Forced VisIt to always use <i>Light Mode</i> on macOS until <i>Dark Mode</i> is supported for Qt.
* Fixed a bug where the OpenPMD reader might cause opening an HDF5 file to hang.

### Enhancements in version 3.1.2

* Removed the pbatch launch profile from the Lawrence Livermore National Laboratory's Max host profile.
* Added host profiles for the Lawrence Livermore National Laboratory's Magma and Boraxo systems.
* Enhanced the CGNS reader to support a mesh decomposed across multiple CGNS files, one block per file as might be typical of file-per-processor parallel I/O. This requires that each file contain just a single CGNS mesh block. In addition, if all files do not also contain the same number of time steps, results will be indeterminate. The collection of CGNS files can be grouped together into a .visit file or follow the naming convention "basename.cgns.nblocks.iblock", where basename is any string, cgns is the string "cgns", nblocks is the number of blocks, and iblock is the block index.
* Enhanced the VTK reader to support reading and writing VisIt expressions as non-specific FIELD variable named "VisItExpressions" of type string. To see an example, look at the example file named <code>higher_order_triangles.vtk</code> in <a href="https://github.com/visit-dav/visit/blob/develop/data/vtk_test_data.7z?raw=true">vtk_test_data.7z</a>
* Enhanced the <i>Pick Through Time</i> to use a substantially faster algorithm by default. This algorithm will be enabled when preserving the picked element id. When preserving the picked coordinate, the original algorithm will be used instead.
* Enhanced the new default <i>Pick Through Time</i> algorithm to handle vectors, tensors, and arrays. For vectors, the magnitude is used. For tensors and arrays, the major eigenvalue is used.
* Enhanced the <i>Expression</i> window so that expressions in the expression list will appear alphabetically.
* Enhanced the Blueprint reader to support expressions.
* Enhanced the Blueprint reader to support Ascent outputs with multiple domains per file.
* Changed the variable name <i>Patch/Rank</i> to <i>Patch/ProcId</i> in the Uintah reader.

### Changes for VisIt developers in version 3.1.2

* The build_visit script was enhanced to allow VisIt to build on Ubuntu 19.10 systems using gcc 9.2.
* The build_visit script was enhanced to allow VisIt to build on Debian 10.

### Documentation changes in version 3.1.2

* Added sphinx docs on Visit's Integral Curve System.
* Added sphinx docs for building VisIt on macOS using masonry.
