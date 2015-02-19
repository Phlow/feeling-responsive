---
layout: page
title: "Change is good!"
subheadline: "Feeling Responsive Theme Changelog"
description: "History and changelog of Feeling Responsive Theme"
header:
   image_fullwidth: "header_unsplash_9.jpg"
permalink: "/changelog/"
---
2015-02-19 // Version 0.99
:   Yes! Now *Feeling Responsive* uses the built-in sass-support by Jekyll. Open `_sass` and dig deeper into customizing this theme using your colors, typography and so on...

2015-02-18 // Version 0.98
:   Now with author-support and [Schema.org microdata](http://schema.org). Edit author(s) in `authors.yml` and use it via front matter like `author: your_author_name`. Added [Disqus-comments]({{ site.url}}/design/comments/#comments) to the mix.

2015-02-17 // Version 0.97
:   Simplicity. Reduced templates. Now there is one page/post-template with two switches via front matter to turn on metadata at the end of the page/post via `show_meta: true/false` and to add a left or right sidebar via `sidebar: left/right`. The defaults are declared in `config.yml`. I also changed the variable `description` to `teaser` because it's more logigally.

2015-02-12 // Version 0.96
:   Added `frontpage`-layout with three widgets-areas. The layout simplifies the process to change content on the frontpage.

2015-02-09 // Version 0.95
:   Now with custom icon font using only entypo icons necessary. Eliminated one one request and reduced the font-file to 9kb. You can easily customize the font yourself using [Font Custom][7] and the included `fontcustom.yml` in `assets/fonts/`.

2015-01-12 // Version 0.94
:   Added Windows 8-Tile in `config.yml` and `header.html`. Added `_config_dev.yml` for easier local development. Use `jekyll serve --config _config.yml,_config_dev.yml` to overwrite `url`-settings of the main configuration. Added `_data/network.yml` to customize links in the footer-area. Now with 404-page and a google-powered search.

2014-12-22 // Version 0.93
:   Improved speed through the use of [webfontloader](https://github.com/typekit/webfontloader). Reduced Volkhov font and only embedded normal weight. Now fonts load asynchronous and the package is 53kb lighter.

2014-12-21 // Version 0.92
:   A new polished version, with a stronger and better color scheme. [Have a look ›]({{ site.url }}/design/grid/#color-scheme-and-colors-codes). Added foundation `.scss-files` to `assets/scss/` for savety.

2014-10-08 // Version 0.91
:   Moved images folder from `assets/img/` to `images` to fasten access to folder. Moved all pages to `pages/`-folder for better organization. Added language-functionality. *Feeling Responsive* is now translation ready.

2014-09-21 // Version 0.9
:   Optimized code, tweaked CSS, added images, deleted `header: "no"` from front matter (because it not necessary), added drafts to the new `_drafts`-folder to begin posts and pages faster and enhanced the documentation. Huh, 1.0 I am coming.

2014-09-16 // Version 0.8
:   Added [video post format][5] for that cinematic flavor. Added URL- and Credit-feature to images and revamped the homepage a little bit to give blog-content more exposure. Optimized some includes, especially the `_include/list-posts.html`-Include which support some nifty parameters.

2014-09-15 // Version 0.7
:   Added an [example of a gallery][4] to show how to use Clearing Lightbox. Meta information is used in posts via `/include/meta_information.html`. To optimize pages/posts for search engines you have now have an extra front matter-variable called `meta_description`. Also the theme supports facebook open graph information.

2014-09-12 // Version 0.6
:   Finally the [blogpage][1] has pagination and an [archive for all blog-posts][2] using the [foundation accordion][3].

2014-08-22 // Version 0.5
:   Better typograpyh, extended [documentation]({{ site.url}}/documentation/) and little subtle css-things to make *Feeling Responsive* a little better.

2014-08-17 // Version 0.4
:   First beta release of »Feeling Responsive« with the current jekyll templates.

2014-08-17 // Version 0.3
:   First release – only *HTML-Version* – of »Feeling Responsive« on Github-Pages with some hickups.

2014-07-26 // Version 0.2
:   Updated Navigation & Social Media-Configuration via custom data in `_data`

2014-07-07 // Version 0.1
:   Start of theme coding and development.

2014-06-23
:   First Ideas and scribbles at the beach in [Bergen/Netherlands][6].





 [1]: {{ site.url }}/blog/
 [2]: {{ site.url }}/blog/archive/
 [3]: http://foundation.zurb.com/docs/components/accordion.html
 [4]: {{ site.url }}/design/gallery/
 [5]: {{ site.url }}/design/video/
 [6]: https://www.google.de/maps/place/Strandpaviljoen+Joep+B.V./@51.9960733,5.830135,6z/data=!4m2!3m1!1s0x47cf5918df69093b:0x7c11ab31102c1c8a
 [7]: fontcustom.com
 [8]: #
 [9]: #
 [10]: #