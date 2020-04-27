---
layout: page
#
# Content
#
teaser: "All teams have to do it. Now we have a name for it."
subheadline: "BSSw.io blog article re-host"
title: "Continuous Technology Refreshment (CTR)"
categories:
  - design
#
# Styling
#
#    image_fullwidth: "summit_and_sierra-fs8.png"
header:
    image_fullwidth: "https://github.com/betterscientificsoftware/images/raw/master/Blog_0419_CTR_1176_432.png"
    caption: "A NASA astronaut on STS-130 gives the ISS a Tech Refresh"
    caption_url: https://www.nasa.gov/mission_pages/shuttle/shuttlemissions/sts130/main/index.html
image:
    thumb: gallery_27.jpg
author: miller86
---
The practice of
[*Continuous Technology Refreshment (CTR)*](http://info.alphanumeric.com/blog/benefits-establishing-technology-refresh-cycle)
is defined as the *periodic upgrade or replacement of infrastructure to deliver continued reliability, improved speed,
capacity, and/or new features*. The term is used primarily in the IT world when replacing obsolete *hardware*.
However, long-lived software projects often wind up having to engage in equivalent activity.
Examples of CTR in scientific computing software include adoption of new 
language standards, integration of performance portability solutions, application of burst buffers in
workflow, and new revision control systems. The longer lived and bigger a project is, the more
involved technology refresh can be. Using recent work for a major release of
[VisIt](https://wci.llnl.gov/simulation/computer-codes/visit/), 3.0 Beta,
we describe experiences and lessons learned refreshing several technologies
* Wrangling binary content: Subversion to Git [Large File Support (LFS)](https://www.git-tower.com/learn/git/ebook/en/desktop-gui/advanced-topics/git-lfs)
* Revision control: [Subversion](http://visit.ilight.com/svn/visit) to [GitHub](https://github.com/visit-dav/visit)
* Issue tracking: [Redmine](https://visitbugs.ornl.gov/projects/visit) to [GitHub Issues](https://github.com/visit-dav/visit/issues)
* Documentation: [OpenOffice](https://wci.llnl.gov/simulation/computer-codes/visit/manuals) to
  [Sphinx+ReadTheDocs](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/)
* Other Refreshments Completed and Planned

### Wrangling binary content
Because of the lack of alternatives, the VisIt team wound up having to use its Subversion repo for general *hosting*
of content, much of it binary, not really requiring revision control. This included pre-built release
binaries and tar files, PowerPoint presentations, and data ensembles used in tutorials.
Binary content is [problematic](https://hackernoon.com/what-should-be-in-version-control-d5f16e9a2bf2)
for revision control systems. Over many years of development, this and other binary content used in testing grew
in size, making working with the whole repo unwieldy. For example, branch creation could take more than
an hour. In moving to GitHub, we [configured our repository](https://github.com/visit-dav/visit/blob/develop/.gitattributes)
to use [Git Large File Support (LFS)](https://git-lfs.github.com) to better handle binary content. GitHub offers free
LFS with 1 GB of storage and 1 GB/month bandwidth
[limits per repo](https://help.github.com/en/articles/about-storage-and-bandwidth-usage). For $300 per year, 
we purchased upgraded LFS service with 300 GB of storage and 3 TB of bandwidth.

### Revision control
Migrating a few branches of a small project from [Subversion to GitHub](https://blog.axosoft.com/migrating-git-svn/)
is trivial. A Google search of
[*migrate from subversion to git*](https://www.google.com/search?q=migrate+from+subversion+to+git&oq=migrate+from+subversion+to+git&aqs=chrome..69i57j0l5.2131j0j8&sourceid=chrome&ie=UTF-8)
reveals many options. However, there are no tools for migrating many branches, tags, and releases of a large project
with a long development history while also culling and/or LFS'ing unwieldy binary content (described above)
such that the resulting GitHub repo captures all history and looks, more or less, as if all
the development had originally occurred on GitHub. We developed and tested custom Python scripts to basically
*replay* all the changes from the old Subversion repo into the new GitHub repo. The process takes hours.
In addition, these scripts were tested, results examined, and repositories destroyed and re-created, several
times before all the kinks in the process were worked out. [The result](https://github.com/visit-dav/visit)
is that key branches and tags as well as all release and development history are captured on GitHub in what one would
expect to be the GitHub-native way.
Furthermore, unwieldy binary content is properly LSF'd with only the revision history of essential binary
content being captured. We reduced the size of the repository from several tens of gigabytes in Subversion to
under half a gigabyte in Git.

### Issue tracking
A key challenge in migrating issues was deciding upon a mapping from Redmine issue metadata
(e.g., trackers, statuses, and custom fields) to reasonable GitHub equivalents and then
automating the conversion with a script. To capture all issue history, we chose to migrate both open and resolved issues.
We found that capturing Redmine comments as *true* GitHub conversations was not easily possible. All comments from
a Redmine issue were poured into the initial GitHub issue. We also included all Redmine
metadata in the initial GitHub issue as a hedge against unforeseen data loss. A final challenge was attachments.
Fewer than 10% of the issues contained attachments. However, GitHub offered no way to automate adding attachments
to issues. After migrating the issues themselves (which then defined a mapping between the old
Redmine and new GitHub issue ids), we scripted the download of all Redmine attachments renaming
the resulting files with their new GitHub ids. The team then engaged in an *attach-a-palooza* exercise
where each member was assigned about 10% of the attachments to manually attach to the appropriate
GitHub issues.

### Documentation
We migrated VisIt's GUI User Manual from OpenOffice to
[Sphinx](http://www.sphinx-doc.org/en/master/) and
[ReadTheDocs](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/).
This task involved a conversion script to bootstrap the process generating an initial
[restructured text](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) output. Then, the
team engaged in 3-4 documentation sprints, each of length 2-3 hours, manually reviewing, fixing, reorganizing,
and polishing the resulting `.rst` files. VisIt's CLI (Python) User Manual existed as compilable
C code in the form of Python docstrings. This design facilitates in-line help within Python
(e.g., `>>> help(myFunc)`) but is otherwise not the best format for humans to compose documentation. We wrote
a script to automate conversion of the C code Python docstrings to `.rst` files. We plan to reverse this
in the near future, that is, craft the documentation in `.rst` and automate the creation of Python doc-strings
from the `.rst`.

### Other refreshments

When making big changes, it is a good idea to combine as many together as possible rather than
dribble them out over numerous releases. As part of the 3.0 beta release, the VisIt team also refreshed
from VTK-6 to VTK-8 which necessitated refreshing GL infrastructure as well, 
from `.tar.gz` to `.7z`, which reduced storage for binary test data by 50%. Later this year, we plan to refresh
commit hooks (e.g., tab characters, `abort()` calls, file name case clashing, using statements in headers),
do CI testing (we currently test only proper compilation), and move our
[web site](https://wci.llnl.gov/simulation/computer-codes/visit/) and
[test dashboard](https://portal.nersc.gov/project/visit/) to GitHub as well.

### Summary
Most code teams find it necessary to engage in activities similar to those described here on a regular basis, often
in response to changing development workflow needs. For example, in its 25+ year history, the
[PETSc](https://www.mcs.anl.gov/petsc/) project has refreshed revision control systems on four separate occasions.
Each of these changes was motivated by the growing set of distributed developers collaborating on PETSc.
The HPC software community has yet to adopt the term *Continuous Technology Refreshment* to characterize such
activities. However, we hope this article demonstrates that CTR is an essential aspect of sustaining software.
Although technology refresh efforts can be costly, the benefits are improved development workflow and reduced long-term costs.

### Author bios

Mark Miller is a computer scientist supporting the [WSC](https://wci.llnl.gov/about-us/weapon-simulation-and-computing)
program at [LLNL](https://www.llnl.gov) since 1995.
He is a contributor to
[VisIt](https://wci.llnl.gov/simulation/computer-codes/visit)
and the lead developer of
[Silo](https://wci.llnl.gov/simulation/computer-codes/silo). He is also a contributor to the
[IDEAS-ECP](https://ideas-productivity.org/ideas-ecp/) project.

Holly Auten is the Web Content Lead for the Computation Web Team and
routinely contributes articles regarding various aspects of on-going software
development activities within the Computation department at [LLNL](https://www.llnl.gov).
