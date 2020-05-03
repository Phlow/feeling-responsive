---
layout: page
title: "Source Code"
header:
   image_fullwidth: "gallery-05a.png"
permalink: "/sources/"
---

## Automatically Build VisIt with the [build_visit](https://github.com/visit-dav/visit/releases/download/v3.1.1/build_visit3_1_1) Script

VisIt can be built automatically using the [build_visit](https://github.com/visit-dav/visit/releases/download/v3.1.1/build_visit3_1_1) script on MacOS X and many Linux platforms. The [build_visit](https://github.com/visit-dav/visit/releases/download/v3.1.1/build_visit3_1_1) script takes care of downloading relevant VisIt and 3rd party source code, configuring, and building it all using your C++ compiler. We encourage users to build VisIt using the [build_visit](https://github.com/visit-dav/visit/releases/download/v3.1.1/build_visit3_1_1) script when our binary distributions have trouble running on some systems. We also recommend using the [build_visit](https://github.com/visit-dav/visit/releases/download/v3.1.1/build_visit3_1_1) script on your system if you plan to:

* Modify the VisIt source code. 
* Build a parallel version on an advanced platform that we don't provide executables for.
* Create your own VisIt plugins. Building VisIt on your system ensures that it is built with the same C++ compiler that you will use to develop your plugin, minimizing the chance for runtime library incompatibilities.

For instructions on building VisIt on MacOS X and Linux systems using [build_visit](https://github.com/visit-dav/visit/releases/download/v3.1.1/build_visit3_1_1), go to the [Building](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/gui_manual/Building/index.html) chapter of the VisIt GUI Manual. For instructions on building VisIt on Windows, go to the [Building on Windows](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/gui_manual/BuildingOnWindows/index.html) chapter of the VisIt GUI Manual. Links to download the Unix source code, the Windows source code, the md5 and sha1 checksums, and file sizes are below, organized by release starting with the most recent release. The checksums and file sizes are for checking that the files were properly downloaded if corruption of the files is suspected during the download process.

If you use VisIt to generate images and/or movies please cite VisIt in your paper and the credits of your movie. Doing so helps us sustain funding for future improvements and on going maintenance. Please use the following acknowledgement and send us references to any publications, presentations, or successful funding applications that make use of DOE software.

* VisIt Citation [bibtex citation](visit-citation.md)

VisIt is supported by the Department of Energy with funding from the Advanced Simulation and Computing Program, the Scientific Discovery through Advanced Computing Program, and the Exascale Computing Project.

## Releases

Series | First Date | Releases
3.1 | Dec 29, 2019 | [3.1.0](https://github.com/visit-dav/visit/releases/download/v3.1.0/build_visit3_1_0) | [3.1.1](https://github.com/visit-dav/visit/releases/download/v3.1.1/build_visit3_1_1)
3.0 | Mar 01, 2019 | [3.0.1](https://github.com/visit-dav/visit/releases/download/v3.0.1/build_visit3_0_1) | [3.0.2](https://github.com/visit-dav/visit/releases/download/v3.0.1/build_visit3_0_2)
2.13 | Jun 15, 2018 | [2.13.0](https://github.com/visit-dav/visit/releases/download/v2.13.0/build_visit2_13_0) | [2.13.1](https://github.com/visit-dav/visit/releases/download/v2.13.1/build_visit2_13_1) | [2.13.2](https://github.com/visit-dav/visit/releases/download/v2.13.2/build_visit2_13_2) | [2.13.3](https://github.com/visit-dav/visit/releases/download/v2.13.3/build_visit2_13_3)
