---
layout: page
title: "Release Notes for VisIt 3.1"
header:
   image_fullwidth: "gallery_05a.png"
permalink: "/releases/release-notes-3.0.0/"
---

Welcome to VisIt's release notes page. This page describes the important
enhancements and bug-fixes that were added to this release.

### General features added in version 3.0

* VisIt has been enhanced to support outputting Cinema databases. Cinema is an image-based database that offers low-cost interaction with simulation data. When viewing a Cinema database through a Cinema viewer, the viewer merely changes the image from the database in response to changes in camera angle and other visualization parameters rather than performing potentially expensive I/O, computational and rendering operations. Viewers and more information about Cinema can be found at [CinemaScience](https://cinemascience.org).

    Images can consist of RGB pixel images and composite images that enable VisIt to bring together multiple plots independently in the Cinema viewer. Cinema databases can be created using the *Save Cinema wizard*, accessible by selecting *Save to Cinema...* from the *File* pulldown menu on the main control panel.
  
* VisIt has been enhanced to support rendering 3D images using the OSPRay. OSPRay features interactive CPU rendering capabilities geared towards scientific visualization applications. Advanced shading effects such as ambient occlusion, shadows, and transparency can be rendered interactively, enabling new insights into data exploration. OSPRay rendering is only available if VisIt has been compiled with OSPRay support. OSPRay is currently supported on Linux and Windows platforms.

    To enable OSPRay rendering bring up the *Rendering options* window by selecting *Rendering...* from the *Options* pulldown menu, switch to the *Advanced* tab and select *OSPRay rendering* at the bottom of the tab. All plots except for the *Volume* will use OSPRay for 3D rendering when enabled through the *Rendering options*. OSPRay rendering for the *Volume* plot is enabled through the *Volume plot attributes* window by setting the *Rendering Method* to *Ray casting: OSPRay*.

    Note that panning and zooming doesn't currently work with OSPRay rendering.
  
* The CLI now provides a *DatabasePlugins()* function that returns a dictionary containing a tuple of the available database plugins for a host.
* VisIt has been enhanced so plots can provide custom animation behaviors. These behaviors are plot-specific and are independent of the time slider animation controls. For example, the Vector plot can alter the length of its glyphs periodically lengthening and shortening them. Plot animation is enabled for the Curve and Vector plugins and can be activated by right-clicking on a plot in the Main window's plot list area and selecting *Animate* from the context menu. Note, this features works best for plots and data that can be rendered quickly.
* Some of VisIt's expressions can be built with support for OpenMP, letting them parallelize over multiple threads. This is available when passing *-fopenmp* to the C++ compiler when building VisIt. The observed speedups are between 2x and 10x when using the serial compute engine. These expressions are enhanced with OpenMP support:

    * *addition +*
    * *multiplication **
    * *vector decompose []*
    * *magnitude()*
    * *lambda2()*
    * *q_criterion()*
    * *gradient() (for logical gradient case only)*
  
* Libsim's *VisItRestoreSession()* function will now attempt to broadcast the session file contents to other MPI ranks rather than having all ranks read the file.
* When exporting to *Curve2D* or saving the Window in *curve* format, a comment style can be selected, with choices being Ultra *("#")*, and Matlab *("%")*. Ultra style is the default.
* VisIt has been enhanced to leverage VTK-m for some operations. VTK-m is a version of VTK that has been rewritten to support multi-core architectures. It is based on a recent version of VTK-m. VTK-m support will only be available if it has been built with VTK-m support. VTK-m support can be enabled in one of two ways.

    When using the graphical user interface, bring up the *Preferences* window by selecting *Preferences...* from the *Options* menu and change the *Parallel Computation Library:* to *VTKm*. This setting will be directly below the *Floating point precision:* setting and will only be visible if VisIt has been built with VTK-m support.

    When using the Python scripting interface, make the following call:

        SetBackendType("VTKm")

    When VTK-m support is enabled, VisIt will use VTK-m for all operations that support it. The following operators currently support VTK-m.

    * Contour plot: Restrictions - Only supports node centered variables.
    * Isosurface operator: Restrictions - Only supports node centered variables.
    * Slice operator: Restrictions - Only works when *Project to 2D* is disabled.

    VTK-m functionality is currently enabled for 3D rectilinear, curvilinear and unstructured grids with only hexahedral elements. VTK-m supports both single block and multi-block grids.

    In order for VTK-m filters to perform better than VTK filters the number of cells in a block must be fairly large, typically at least 1 million cells. Furthermore, there is some overhead in converting between VTK and VTK-m representations that will impact performance. Lastly, checks have been put in to make sure that the data sets being processed are supported by VTK-m and these can impact performance as well. Checking if a variable is node centered or 3D is inexpensive, whereas checking if an unstructured grid contains only hexahedra is expensive.
  
* Due to lack of availability of C++11 compliant compilers, support for OSX 10.8 has been dropped.
* The *Remote Profiles* tab in the *Host profiles* will now allow importing profiles from the currently running release as well as from the trunk.
* VisIt now has a Remap operator under the Geometry menu. This operator supports datasets of single- and multi-domain cell-centered scalars on structured and unstructured grids. It converts the data to a rectlinear grid with user-defined resolution and span. Variables can be specifed as intrisic (like density) or extrinsic (like mass).

### Changes in GUI behavior in version 3.0

* The *Set Save options* window has been enhanced with a section that lets the user select which pixel data will be saved when an image is saved. The usual RGB data can be selected as well as alpha, depth, luminance, and value data. When alpha data are requested, VisIt's images will feature a transparent background that simplifies compositing of VisIt-generated images in other tools. Depth information results in a *filename.depth.Z* file being saved. Luminance information saves a separate image file with gray-scale luminance values. Value images save a 32-bit floating point image with plot scalars; this works with Pseudocolor plots.
* VisIt can now save images into OpenEXR format via the *Set save options* window. OpenEXR files save additional precision and let images contain RGBA data and other image data such as depth, value, and luminance.

### File format reader changes in version 3.0

* The Image reader plug-in was extended to expose a *depth* variable. The depth variable serves up data from the *filename.depth.Z* file if it exists, enabling depth data to be plotted in addition to color data. A depth file is a zlib-compressed file of 32-bit floating point numbers storing the Z-buffer for the image. The depth file can be requested by selecting depth pixel data in the *Set save options* window.
* An OpenEXR reader was added to VisIt.
* An ffp database reader was added to VisIt courtesy of Olivier Cessenat.
* The Curve2D reader can now read curve files with Matlab-style comments.
* The Vista plugin was removed.
* The VTK writer was enhanced to optionally triangulate (2D) or tetrahedralize (3D) any UNstructured mesh output.
* Corrected a bug plotting Nek5000 data, where VisIt displayed an error message indicating that the plot yielded no data when plotting the result of an expression involving a gradient with 2D data.

### Changes to VisIt's plots in version 3.0

* The ray-casting volume renderer in VisIt's Volume plot was sped up in many instances. For rectilinear data, the speed increase can be over 2x, depending on the opacities in the transfer function.
* The Vector plot supports plot animation. The vector glyphs alternate between 50% and 100% of their glyph length while the plot animates, helping to see features in the vector field.
* The Curve plot supports plot animation. The line and time cue features in the plot can respond to plot animation and they advance from left to right while the plot animates.
* When Min or Max is chosen for Pseudocolor plot, a color can now be chosen for those values below the minimum or above the maximum.
* The setting for the Label plot's *Label height* has been replaced with a *Font scale*.  Other options affecting font that were added include *Font name*, *Bold*, and *Italic*. We attempt to ensure old settings from python scripts, session files and configuration files are replicated as closely as possible, however the new label size may not exactly match how things looked in previous versions of VisIt.

### Changes to VisIt's operators in version 3.0

* A new *Grid Information* query was added so the individual types, sizes, and extents of domains in a multidomain mesh can be obtained. This feature is useful in scripts.

### Changes to VisIt's expression language in version 3.0

* The *conn_cmfe* expression was enhanced to handle mapping cell data between point meshes and polygonal or polyhedral meshes where the number of points and polygons or polyhedra match. This didn't work previously in the case of polygons because while the number of cells matched the number of points didn't. Now the number of points is ignored. It didn't work in the case of polyhedral meshes because polyhedra are split into zoo elements, which results in the number of cells not matching. Now the splitting is taken into account.
* Improved the pos_cmfe expression so that it better handles pyramid and wedge cells in the donor mesh.

### Changes to VisIt's picks and queries in version 3.0

* The *Pick Operator* now supports swivelling the camera focus to center on the current pick. This can be accessed through the GUI by checking the *Swivel focus* check box. If you are using the python interface, you can turn this ability on and off by setting the boolean variable *swivelFocusToPick* within the pick attributes.
* Two related features have been added to the *Pick* operator, and these are the ability to force a user-defined pick label and the ability to remove all previous picks that have the same label as the current pick. When used in conjunction, you can create a specialized pick operator that, with every new pick, removes all previous picks that contain the same user-defined label. As of now, these options are only accessible through the python interface pick attributes. To force a user-defined label, set the boolean variable *overridePickLabel* to True, and set *forcedPickLabel* to your chosen label. To remove all previous picks with the same label, set *removeLabelTwins* to True.
* The *Pick* operator now supports highlighting node picks.
* Default index for *Onion Peel* operator was changed from 1 to 0.

### Other bugs fixed in version 3.0

* Corrected a bug where VisIt would crash rendering transparent geometry on the Cooley system at the Argonne Leadership Computing Facility.
* Corrected a bug where VisIt would randomly crash rendering transparent geometry due to memory corruption.
* *ANNOTATION_INT* facelists with faces appearing in more than one sublist are now handled correctly.
* Corrected a bug that caused empty plots when using the *Onion Peel* operator with data containing enumerated subsets.
* Corrected a few usability issues for the *Save movie wizard* including: 

    * The ability to save a movie template file.
    * The ability to set start and end frames when creating a movie template.
    * Pressing the enter key while modifying will no longer advance to the next page.

* Corrected a bug in creating expressions with curves read from multi-domain silo files. 
* Fixed parallel engine hang when attempting to plot data from VTU (.vtu) files.
* Fixed viewer crash when using the *Transparent Color* option for an *Image* annotation object.

### Configuration changes in version 3.0

* Host profiles were added for the Lawrence Livermore National Laboratories' Shark system.
* Host profiles were added for the Lawrence Livermore National Laboratories' Lassen and Sierra systems.
* Host profiles were added for the Argonne National Laboratories' Theta system.
* Enhanced the Lawrence Livermore National Laboratories' custom launcher so that VisIt would display to VNC displays.

### Build changes in version 3.0

* Added the ability to create RPM packages via --create-rpm in build_visit.
* Improved checksum checking of downloads such that python sub-modules are also checked.
* Ensure md5 and shasum checksum commands are handled correctly on OSX.
* Added checksum variables for most packages thereby triggering checksum verifcation upon download.

### Changes for VisIt developers in version 3.0

* VisIt has been ported to use the git/master branch of the IceT compositing library.
* avtGenericDatabase now dumps some intermmediate results of its dataset collection when -dump is in effect.
* The command line option *-svn_revision* was replaced with *-git_version*.
