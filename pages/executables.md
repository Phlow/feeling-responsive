---
layout: page
title: "VisIt Releases"
permalink: "/executables/"
---
VisIt is supported by the Department of Energy with funding from the Advanced
Simulation and Computing Program, the Scientific Discovery through Advanced
Computing Program, and the Exascale Computing Project.

If you use VisIt to generate images and/or movies please help us by
[citing](./visit-citation.md) VisIt in your paper or in the credits of your movie.
Doing so helps us sustain funding for future improvements and on going maintenance.

### [Latest](#series-31)&nbsp;&nbsp;&nbsp;[Series 3.1](#series-31)&nbsp;&nbsp;&nbsp;[Series 3.0](#series-30)
### [Older releases](https://wci.llnl.gov/simulation/computer-codes/visit/executables)

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Series 3.1
### Series 3.1

* Links to checksums and file sizes are provided for confirming download integrity.
* Hover over a link to reveal additional details about a download.
* For linux, the [`visit-install`][vm2] script is needed to complete an *install*.

Date | Feb 2020 | Dec 2019
---:|:---:|:---:
Version     |[3.1.1] | [3.1.0]
Windows 10/8/7<br>For developers|[exe][311w]<br>[exe][311wd]|[exe][310w]<br>[exe][310wd]
Mac 10.14<br>10.13|[dmg][311m1014dmg]/[tgz][311m1014tgz]<br>[dmg][311m1013dmg]/[tgz][311m1013tgz]|&nbsp;<br>[dmg][310m1013dmg]/[tgz][310m1013tgz]
19<br>Ubuntu 18<br>16 |[tgz][311u19]<br>[tgz][311u18]<br>[tgz][311u16]|[tgz][310u19]<br>[tgz][310u18]<br>[tgz][310u16]
RedHat EL 7<br>with Mesa|[tgz][311rh]<br>[tgz][311rhwm]|[tgz][310rh]<br>[tgz][310rhwm]
Fedora 27   | [tgz][311f27]|[tgz][310f27]
Debian 9    | [tgz][311d9]|[tgz][310d9]
Centos 8    | [tgz][311c8]|[tgz][310c8]
Java client | [tgz][311j]| [tgz][310j]
[visit-install][vm1]|[sh][311vi]|[sh][310vi]
[build_visit][vm2] |[sh][311bv]|[sh][310bv]
Source      | [zip][311szip]/[tgz][311stgz]|[zip][310szip]/[tgz][310stgz]
Release notes<br>Install notes | [txt][311rn]<br>[txt][311in]|[txt][310rn]<br>[txt][310in]
Checksums<br>File sizes   |[md5][311md5]/[sh1][311sha1]/[sh256][311sha256]<br>[txt][311fs]|[md5][310md5]/[sh1][310sha1]/[sh256][310sha256]<br>[txt][310fs]
Manuals     |[html][311doc]/[pdf][311pdf]|[html][310doc]/[pdf][310pdf]

[vm1]: https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/gui_manual/Intro/Installing_VisIt.html?highlight=visit-install#installing-on-linux "Use to install Linux binaries"
[vm2]: https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/gui_manual/Building/index.html?highlight=build_visit "Using build_visit to build and install VisIt from sources."

<!-- 3.1.1 release asset links -->
[3.1.1]: https://github.com/visit-dav/visit/releases/tag/v3.1.1 "All GitHub release assets"
[311w]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit3.1.1_x64.exe "Windows 10/8/7, 64-bit Visual Studio 2017"
[311wd]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visitdev3.1.1.exe "Windows 10/8/7 for VisIt development, 64-bit Visual Studio 2017"
[311m1014dmg]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit3.1.1.darwin-x86_64-10_14.dmg "Darwin 10.14, Darwin Kernel Version 18.7.0, clang-1000.11.45.5, MPICH"
[311m1014tgz]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit3.1.1.darwin-x86_64-10_14.tar.gz "Darwin 10.14, Darwin Kernel Version 18.7.0, clang-1000.11.45.5, MPICH"
[311m1013dmg]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit3.1.1.darwin-x86_64-10.13.dmg "Darwin 10.13, Darwin Kernel Version 17.7.0, clang-900.39.2, MPICH"
[311m1013tgz]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit3.1.1.darwin-x86_64-10.13.tar.gz "Darwin 10.13, Darwin Kernel Version 17.7.0, clang-900.39.2, MPICH"
[311u19]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit3_1_1.linux-x86_64-ubuntu19.tar.gz "Ubuntu 19, 4.9.184-linuxkit #1 SMP, gcc 8.3"
[311u18]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit3_1_1.linux-x86_64-ubuntu18.tar.gz "Ubuntu 18, 4.9.184-linuxkit #1 SMP, gcc 7.4"
[311u16]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit3_1_1.linux-x86_64-ubuntu16.tar.gz "Ubuntu 16, 4.9.184-linuxkit #1 SMP, gcc 5.4"
[311rh]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit3_1_1.linux-x86_64-rhel7.tar.gz "Redhat Enterprise Linux 7.5, 4.18.9-1.el7.elrepo.x86_64 #1 SMP, gcc 4.8.5"
[311rhwm]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit3_1_1.linux-x86_64-rhel7-wmesa.tar.gz "Redhat Enterprise Linux 7.5, 4.18.9-1.el7.elrepo.x86_64 #1 SMP, gcc 4.8.5 (Includes Mesa support for rendering without a display. Only use on servers without a display.)"
[311f27]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit3_1_1.linux-x86_64-fedora27.tar.gz "Fedora 27, 4.9.184-linuxkit #1 SMP, gcc 7.3.1"
[311d9]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit3_1_1.linux-x86_64-debian9.tar.gz "Debian 9/10, 4.9.184-linuxkit #1 SMP, gcc 6.3"
[311c8]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit3_1_1.linux-x86_64-centos8.tar.gz "CentOS 8, 4.9.184-linuxkit #1 SMP, gcc 8.2.1"
[311j]: https://github.com/visit-dav/visit/releases/download/v3.1.1/jvisit3.1.1.tar.gz "VisIt client only: Java(TM) SE Runtime Environment (build 1.6.0_161-b13) Java HotSpot(TM) 64-Bit Server VM (build 20.161-b13, mixed mode)"
[311vi]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit-install3_1_1 "Linux installer script needed to install linux binaries"
[311bv]: https://github.com/visit-dav/visit/releases/download/v3.1.1/build_visit3_1_1 "Download *only* this script to build VisIt from sources"
[311szip]: https://github.com/visit-dav/visit/archive/v3.1.1.zip
[311stgz]: https://github.com/visit-dav/visit/archive/v3.1.1.tar.gz
[311rn]: https://wci.llnl.gov/simulation/computer-codes/visit/releases/release-notes-3.1.1
[311in]: https://github.com/visit-dav/visit/releases/download/v3.1.1/INSTALL_NOTES.txt
[311sha256]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit_sha256_checksums.txt
[311sha1]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit_sha1_checksums.txt
[311md5]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit_md5_checksums.txt
[311fs]: https://github.com/visit-dav/visit/releases/download/v3.1.1/visit_filesizes.txt
[311doc]: https://visit-sphinx-github-user-manual.readthedocs.io/en/v3.1.1/
[311pdf]: https://visit-sphinx-github-user-manual.readthedocs.io/_/downloads/en/v3.1.1/pdf/

<!-- 3.1.0 release asset links -->
[3.1.0]: https://github.com/visit-dav/visit/releases/tag/v3.1.0 "All GitHub release assets"
[310w]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit3.1.0_x64.exe "Windows 10/8/7, 64-bit Visual Studio 2017"
[310wd]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visitdev3.1.0.exe "Windows 10/8/7 for VisIt development, 64-bit Visual Studio 2017"
[310m1013dmg]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit3.1.0.darwin-x86_64-10.13.dmg "Darwin 10.13, Darwin Kernel Version 17.7.0, clang-900.39.2, MPICH (Works on Mac OS X 10.13 and later.)"
[310m1013tgz]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit3.1.0.darwin-x86_64-10.13.tar.gz "Darwin 10.13, Darwin Kernel Version 17.7.0, clang-900.39.2, MPICH (Works on Mac OS X 10.13 and later.)"
[310u19]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit3_1_0.linux-x86_64-ubuntu19.tar.gz "Ubuntu 19, 4.9.184-linuxkit #1 SMP, gcc 8.3"
[310u18]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit3_1_0.linux-x86_64-ubuntu18.tar.gz "Ubuntu 18, 4.9.184-linuxkit #1 SMP, gcc 7.4"
[310u16]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit3_1_0.linux-x86_64-ubuntu16.tar.gz "Ubuntu 16, 4.9.184-linuxkit #1 SMP, gcc 5.4"
[310rh]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit3_1_0.linux-x86_64-rhel7.tar.gz "Redhat Enterprise Linux 7.5, 4.18.9-1.el7.elrepo.x86_64 #1 SMP, gcc 4.8.5"
[310rhwm]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit3_1_0.linux-x86_64-rhel7-wmesa.tar.gz "Redhat Enterprise Linux 7.5, 4.18.9-1.el7.elrepo.x86_64 #1 SMP, gcc 4.8.5 (Includes Mesa support for rendering without a display. Only use on servers without a display.)"
[310f27]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit3_1_0.linux-x86_64-fedora27.tar.gz "Fedora 27, 4.9.184-linuxkit #1 SMP, gcc 7.3.1"
[310d9]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit3_1_0.linux-x86_64-debian9.tar.gz "Debian 9/10, 4.9.184-linuxkit #1 SMP, gcc 6.3"
[310c8]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit3_1_0.linux-x86_64-centos8.tar.gz "CentOS 8, 4.9.184-linuxkit #1 SMP, gcc 8.2.1"
[310j]: https://github.com/visit-dav/visit/releases/download/v3.1.0/jvisit3.1.0.tar.gz "VisIt client only: Java(TM) SE Runtime Environment (build 1.6.0_161-b13) Java HotSpot(TM) 64-Bit Server VM (build 20.161-b13, mixed mode)"
[310vi]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit-install3_1_0 "Linux installer script needed to install linux binaries"
[310bv]: https://github.com/visit-dav/visit/releases/download/v3.1.0/build_visit3_1_0 "Download *only* this script to build VisIt from sources"
[310szip]: https://github.com/visit-dav/visit/archive/v3.1.0.zip
[310stgz]: https://github.com/visit-dav/visit/archive/v3.1.0.tar.gz
[310rn]: https://wci.llnl.gov/simulation/computer-codes/visit/releases/release-notes-3.1.0
[310in]: https://github.com/visit-dav/visit/releases/download/v3.1.0/INSTALL_NOTES.txt
[310sha256]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit_sha256_checksums.txt
[310sha1]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit_sha1_checksums.txt
[310md5]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit_md5_checksums.txt
[310fs]: https://github.com/visit-dav/visit/releases/download/v3.1.0/visit_filesizes.txt
[310doc]: https://visit-sphinx-github-user-manual.readthedocs.io/en/v3.1.0/
[310pdf]: https://visit-sphinx-github-user-manual.readthedocs.io/_/downloads/en/v3.1.0/pdf/

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Series 3.0
### Series 3.0

* Links to checksums and file sizes are provided for confirming download integrity.
* Hover over a link to reveal additional details about a download.
* For linux, the [`visit-install`][vm2] script is needed to complete an *install*.

Date | Sep 2019 | Jul 2019 | Apr 2019
---:|:---:|:---:|:---:
Version     |[3.0.2] | [3.0.1] | [3.0.0]
Windows     |[use][302w]/[dev][302wd]|[use][301w]/[dev][301wd]|[use][300w]/[dev][300wd]
OSX 10.13   |[dmg][302m1013dmg]/[tgz][302m1013tgz]|[dmg][301m1013dmg]/[tgz][301m1013tgz]|[dmg][300m1013dmg]/[tgz][300m1013tgz]
Ubuntu 19   |[tgz][302u19]|[tgz][301u19]|[tgz][300u19]
Ubuntu 18   |[tgz][302u18]|[tgz][301u18]|[tgz][300u18]
Ubuntu 16   |[tgz][302u16]|[tgz][301u16]|[tgz][300u16]
RedHat EL 7 |[tgz][302rh]|[tgz][301rh]|[tgz][300rh]
RedHat EL 7 w/ Mesa |[tgz][302rhwm]|[tgz][301rhwm]|[tgz][300rhwm]
Fedora 27   |[tgz][302f27]|[tgz][301f27]|[tgz][300f27]
Debian 9    |[tgz][302d9]|[tgz][301d9]|[tgz][300d9]
Centos 8    |[tgz][302c8]|[tgz][301c8]|[tgz][300c8]
Java client |[tgz][302j]|[tgz][301j]|[tgz][300j]
[visit-install][vm1]|[sh][302vi]|[sh][301vi]|[sh][300vi]
[build_visit][vm2]|[sh][302bv]|[sh][301bv]|[sh][300bv]
Source      |[zip][302szip]/[tgz][302stgz]|[zip][301szip]/[tgz][301stgz]|[zip][300szip]/[tgz][300stgz]
Release notes |[txt][302rn]|[txt][301rn]|[txt][300rn]
Install notes |[txt][302in]|[txt][301in]|[txt][300in]
Checksums   |[md5][302md5]/[sh1][302sha1]/[sh256][302sha256]|[md5][301md5]/[sh1][301sha1]/[sh256][301sha256]|[md5][300md5]/[sh1][300sha1]/[sh256][300sha256]
File sizes  |[txt][302fs]|[txt][301fs]|[txt][300fs]
Manuals     |[html][302doc]/[pdf][302pdf]|[html][301doc]/[pdf][301pdf]|[html][300doc]/[pdf][300pdf]

<!-- 3.0.2 release asset links -->
[3.0.2]: https://github.com/visit-dav/visit/releases/tag/v3.0.2 "All GitHub release assets"
[302w]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit3.0.2_x64.exe "Windows 10/8/7, 64-bit Visual Studio 2017"
[302wd]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visitdev3.0.2.exe "Windows 10/8/7 for VisIt development, 64-bit Visual Studio 2017"
[302m1013dmg]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit3.0.2.darwin-x86_64-10.13.dmg "Darwin 10.13, Darwin Kernel Version 17.7.0, clang-900.39.2, MPICH (Works on Mac OS X 10.13 and later.)"
[302m1013tgz]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit3.0.2.darwin-x86_64-10.13.tar.gz "Darwin 10.13, Darwin Kernel Version 17.7.0, clang-900.39.2, MPICH (Works on Mac OS X 10.13 and later.)"
[302u19]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit3_0_2.linux-x86_64-ubuntu19.tar.gz "Ubuntu 19, 4.9.184-linuxkit #1 SMP, gcc 8.3"
[302u18]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit3_0_2.linux-x86_64-ubuntu18.tar.gz "Ubuntu 18, 4.9.184-linuxkit #1 SMP, gcc 7.4"
[302u16]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit3_0_2.linux-x86_64-ubuntu16.tar.gz "Ubuntu 16, 4.9.184-linuxkit #1 SMP, gcc 5.4"
[302rh]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit3_0_2.linux-x86_64-rhel7.tar.gz "Redhat Enterprise Linux 7.5, 4.18.9-1.el7.elrepo.x86_64 #1 SMP, gcc 4.8.5"
[302rhwm]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit3_0_2.linux-x86_64-rhel7-wmesa.tar.gz "Redhat Enterprise Linux 7.5, 4.18.9-1.el7.elrepo.x86_64 #1 SMP, gcc 4.8.5 (Includes Mesa support for rendering without a display. Only use on servers without a display.)"
[302f27]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit3_0_2.linux-x86_64-fedora27.tar.gz "Fedora 27, 4.9.184-linuxkit #1 SMP, gcc 7.3.1"
[302d9]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit3_0_2.linux-x86_64-debian9.tar.gz "Debian 9/10, 4.9.184-linuxkit #1 SMP, gcc 6.3"
[302c8]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit3_0_2.linux-x86_64-centos8.tar.gz "CentOS 8, 4.9.184-linuxkit #1 SMP, gcc 8.2.1"
[302j]: https://github.com/visit-dav/visit/releases/download/v3.0.2/jvisit3.0.2.tar.gz "VisIt client only: Java(TM) SE Runtime Environment (build 1.6.0_161-b13) Java HotSpot(TM) 64-Bit Server VM (build 20.161-b13, mixed mode)"
[302vi]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit-install3_0_2 "Linux installer script needed to install linux binaries"
[302bv]: https://github.com/visit-dav/visit/releases/download/v3.0.2/build_visit3_0_2 "Download *only* this script to build VisIt from sources"
[302szip]: https://github.com/visit-dav/visit/archive/v3.0.2.zip
[302stgz]: https://github.com/visit-dav/visit/archive/v3.0.2.tar.gz
[302rn]: https://wci.llnl.gov/simulation/computer-codes/visit/releases/release-notes-3.0.2
[302in]: https://github.com/visit-dav/visit/releases/download/v3.0.2/INSTALL_NOTES.txt
[302sha256]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit_sha256_checksums.txt
[302sha1]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit_sha1_checksums.txt
[302md5]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit_md5_checksums.txt
[302fs]: https://github.com/visit-dav/visit/releases/download/v3.0.2/visit_filesizes.txt
[302doc]: https://visit-sphinx-github-user-manual.readthedocs.io/en/v3.0.2/
[302pdf]: https://visit-sphinx-github-user-manual.readthedocs.io/_/downloads/en/v3.0.2/pdf/

<!-- 3.0.1 release asset links -->
[3.0.1]: https://github.com/visit-dav/visit/releases/tag/v3.0.1 "All GitHub release assets"
[301w]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit3.0.1_x64.exe "Windows 10/8/7, 64-bit Visual Studio 2017"
[301wd]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visitdev3.0.1.exe "Windows 10/8/7 for VisIt development, 64-bit Visual Studio 2017"
[301m1013dmg]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit3.0.1.darwin-x86_64-10.13.dmg "Darwin 10.13, Darwin Kernel Version 17.7.0, clang-900.39.2, MPICH (Works on Mac OS X 10.13 and later.)"
[301m1013tgz]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit3.0.1.darwin-x86_64-10.13.tar.gz "Darwin 10.13, Darwin Kernel Version 17.7.0, clang-900.39.2, MPICH (Works on Mac OS X 10.13 and later.)"
[301u19]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit3_0_1.linux-x86_64-ubuntu19.tar.gz "Ubuntu 19, 4.9.184-linuxkit #1 SMP, gcc 8.3"
[301u18]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit3_0_1.linux-x86_64-ubuntu18.tar.gz "Ubuntu 18, 4.9.184-linuxkit #1 SMP, gcc 7.4"
[301u16]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit3_0_1.linux-x86_64-ubuntu16.tar.gz "Ubuntu 16, 4.9.184-linuxkit #1 SMP, gcc 5.4"
[301rh]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit3_0_1.linux-x86_64-rhel7.tar.gz "Redhat Enterprise Linux 7.5, 4.18.9-1.el7.elrepo.x86_64 #1 SMP, gcc 4.8.5"
[301rhwm]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit3_0_1.linux-x86_64-rhel7-wmesa.tar.gz "Redhat Enterprise Linux 7.5, 4.18.9-1.el7.elrepo.x86_64 #1 SMP, gcc 4.8.5 (Includes Mesa support for rendering without a display. Only use on servers without a display.)"
[301f27]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit3_0_1.linux-x86_64-fedora27.tar.gz "Fedora 27, 4.9.184-linuxkit #1 SMP, gcc 7.3.1"
[301d9]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit3_0_1.linux-x86_64-debian9.tar.gz "Debian 9/10, 4.9.184-linuxkit #1 SMP, gcc 6.3"
[301c8]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit3_0_1.linux-x86_64-centos8.tar.gz "CentOS 8, 4.9.184-linuxkit #1 SMP, gcc 8.2.1"
[301j]: https://github.com/visit-dav/visit/releases/download/v3.0.1/jvisit3.0.1.tar.gz "VisIt client only: Java(TM) SE Runtime Environment (build 1.6.0_161-b13) Java HotSpot(TM) 64-Bit Server VM (build 20.161-b13, mixed mode)"
[301vi]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit-install3_0_1 "Linux installer script needed to install linux binaries"
[301bv]: https://github.com/visit-dav/visit/releases/download/v3.0.1/build_visit3_0_1 "Download *only* this script to build VisIt from sources"
[301szip]: https://github.com/visit-dav/visit/archive/v3.0.1.zip
[301stgz]: https://github.com/visit-dav/visit/archive/v3.0.1.tar.gz
[301rn]: https://wci.llnl.gov/simulation/computer-codes/visit/releases/release-notes-3.0.1
[301in]: https://github.com/visit-dav/visit/releases/download/v3.0.1/INSTALL_NOTES.txt
[301sha256]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit_sha256_checksums.txt
[301sha1]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit_sha1_checksums.txt
[301md5]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit_md5_checksums.txt
[301fs]: https://github.com/visit-dav/visit/releases/download/v3.0.1/visit_filesizes.txt
[301doc]: https://visit-sphinx-github-user-manual.readthedocs.io/en/v3.0.1/
[301pdf]: https://visit-sphinx-github-user-manual.readthedocs.io/_/downloads/en/v3.0.1/pdf/

<!-- 3.0.0 release asset links -->
[3.0.0]: https://github.com/visit-dav/visit/releases/tag/v3.0.0 "All GitHub release assets"
[300w]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit3.0.0_x64.exe "Windows 10/8/7, 64-bit Visual Studio 2017"
[300wd]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visitdev3.0.0.exe "Windows 10/8/7 for VisIt development, 64-bit Visual Studio 2017"
[300m1013dmg]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit3.0.0.darwin-x86_64-10.13.dmg "Darwin 10.13, Darwin Kernel Version 17.7.0, clang-900.39.2, MPICH (Works on Mac OS X 10.13 and later.)"
[300m1013tgz]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit3.0.0.darwin-x86_64-10.13.tar.gz "Darwin 10.13, Darwin Kernel Version 17.7.0, clang-900.39.2, MPICH (Works on Mac OS X 10.13 and later.)"
[300u19]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit3_0_0.linux-x86_64-ubuntu19.tar.gz "Ubuntu 19, 4.9.184-linuxkit #1 SMP, gcc 8.3"
[300u18]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit3_0_0.linux-x86_64-ubuntu18.tar.gz "Ubuntu 18, 4.9.184-linuxkit #1 SMP, gcc 7.4"
[300u16]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit3_0_0.linux-x86_64-ubuntu16.tar.gz "Ubuntu 16, 4.9.184-linuxkit #1 SMP, gcc 5.4"
[300rh]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit3_0_0.linux-x86_64-rhel7.tar.gz "Redhat Enterprise Linux 7.5, 4.18.9-1.el7.elrepo.x86_64 #1 SMP, gcc 4.8.5"
[300rhwm]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit3_0_0.linux-x86_64-rhel7-wmesa.tar.gz "Redhat Enterprise Linux 7.5, 4.18.9-1.el7.elrepo.x86_64 #1 SMP, gcc 4.8.5 (Includes Mesa support for rendering without a display. Only use on servers without a display.)"
[300f27]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit3_0_0.linux-x86_64-fedora27.tar.gz "Fedora 27, 4.9.184-linuxkit #1 SMP, gcc 7.3.1"
[300d9]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit3_0_0.linux-x86_64-debian9.tar.gz "Debian 9/10, 4.9.184-linuxkit #1 SMP, gcc 6.3"
[300c8]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit3_0_0.linux-x86_64-centos8.tar.gz "CentOS 8, 4.9.184-linuxkit #1 SMP, gcc 8.2.1"
[300j]: https://github.com/visit-dav/visit/releases/download/v3.0.0/jvisit3.0.0.tar.gz "VisIt client only: Java(TM) SE Runtime Environment (build 1.6.0_161-b13) Java HotSpot(TM) 64-Bit Server VM (build 20.161-b13, mixed mode)"
[300vi]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit-install3_0_0 "Linux installer script needed to install linux binaries"
[300bv]: https://github.com/visit-dav/visit/releases/download/v3.0.0/build_visit3_0_0 "Download *only* this script to build VisIt from sources"
[300szip]: https://github.com/visit-dav/visit/archive/v3.0.0.zip
[300stgz]: https://github.com/visit-dav/visit/archive/v3.0.0.tar.gz
[300rn]: https://wci.llnl.gov/simulation/computer-codes/visit/releases/release-notes-3.0.0
[300in]: https://github.com/visit-dav/visit/releases/download/v3.0.0/INSTALL_NOTES.txt
[300sha256]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit_sha256_checksums.txt
[300sha1]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit_sha1_checksums.txt
[300md5]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit_md5_checksums.txt
[300fs]: https://github.com/visit-dav/visit/releases/download/v3.0.0/visit_filesizes.txt
[300doc]: https://visit-sphinx-github-user-manual.readthedocs.io/en/v3.0.0/
[300pdf]: https://visit-sphinx-github-user-manual.readthedocs.io/_/downloads/en/v3.0.0/pdf/
