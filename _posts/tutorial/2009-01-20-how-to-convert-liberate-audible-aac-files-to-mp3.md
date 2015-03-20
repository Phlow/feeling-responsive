---
title: How to convert (liberate) Audible AAC files to MP3
author: David
layout: page
permalink: /note/how-to-convert-liberate-audible-aac-files-to-mp3/
bttc_cache:
  - 1291321742:1
aktt_notify_twitter:
  - no
wp-to-buffer-error:
  - 1
categories:
  - Note
---
I was an [Audible][1] subscriber for over 2 years, and although I&#8217;m no longer active on a plan, I still have 50+ books that I&#8217;ve legitimately purchased. Each of them, however, is locked to my Audible username and password. I don&#8217;t tolerate DRM where possible, and I&#8217;ve done enough system reloads / iPod upgrades to be frustrated at the need to authorize my new devices, and de-authorize my old ones. (and get Audible to reset my devices, since it&#8217;s impossible to de-authorize a dead computer!)

Here are the steps required to convert your Audible titles to standard, un-restricted MP3 files, which you can then do what you want with. Note to scurvy pirates: the process still requires your Audible username and password!<!--more-->

  * Download [Audible Manager for Windows][2]
  * Download [dBpoweramp Music Converter][3] (dMC-r10.exe is the last freeware version, newer ones will expire after 30 days)
  * Download the latest &#8220;[lame_enc.dll][4]&#8221; (it&#8217;s in the zipfile version)
  * Download [dBpoweramp DirectShow Decoder][5] (use this direct link, it&#8217;s for the older version)
  * Download the [Audible Media Player Filter][6] (or [search for it][7])
  * Install dBpoweramp and the DirectShow Decoder.
  * Extract lame_enc.dll to C:\Program Files\Illustrate\dBpowerAMP\Compression\Lame\
  * Add &#8220;.aa&#8221; to DSExt.txt by clicking Start -> Programs -> DB Poweramp -> Configure DirectShow..
  * Install Audible Media Player Filter. You may also need to download [msvcr70.dll][8] and [msvci70.dll][9] to get it to install successfully
  * Download one of your Audible books from your Library, and play it in Audible Manager. You will need to enter your Audible username and password. Remember to put the playback position back to the beginning for the book, else conversion will only start where you last stopped playback!
  * Once you&#8217;re able to play a downloaded book, open dBpoweramp Music Converter, choose your source file, and set the following sensible defaults: 
      * Check that you&#8217;re converting to &#8220;MP3 (Lame)&#8221;
      * Set Target to Bit Rate (CBR) : 32kbps
      * Under &#8220;Advanced&#8221;, uncheck the &#8220;Original&#8221; option<figure id="attachment_1112" style="width: 300px;" class="wp-caption aligncenter">

[<img class="size-medium wp-image-1112" title="dBpowerAmp Options" src="http://www.funkypenguin.co.nz/wp-content/uploads/2009/01/TinyXP-Rev08-1-300x150.jpg" alt="dBpowerAmp Options" width="300" height="150" />][10]<figcaption class="wp-caption-text">dBpowerAmp Options</figcaption></figure> 

  * Click &#8220;Convert&#8221; <img src="https://www.funkypenguin.co.nz/wp-includes/images/smilies/icon_smile.gif" alt=":)" class="wp-smiley" /><figure id="attachment_1111" style="width: 300px;" class="wp-caption aligncenter">

[<img class="size-medium wp-image-1111" title="Successfully converted an Audible AAC file to MP3" src="http://www.funkypenguin.info/wp-content/uploads/2009/01/TinyXP-Rev08-300x138.jpg" alt="Successfully converted an Audible AAC file to MP3" width="300][11]<figcaption class="wp-caption-text">Successfully converted an Audible AAC file to MP3</figcaption></figure> 

  * Update [28 July 2009] : Added specific links to download older versions of dBpoweramp and friends, to avoid expiry of MP3 encoder.

 [1]: http://www.audible.com
 [2]: http://www.audible.com/software/
 [3]: http://web.archive.org/web/20110224225448/http://afewbeers.com/stuff/programs/dMC-r10.exe "dBpoweramp Music Converter"
 [4]: http://lame.buanzo.com.ar/ "Latest lame_enc.dll"
 [5]: http://www.dbpoweramp.com/codecs/dBpowerAMP-codec-DirectShowDecoder.exe "dBpoweramp DirectShow Decoder"
 [6]: http://www.coolutils.com/Downloads/AudibleMediaPlayerFilter.exe "Audible Media Player Filter"
 [7]: http://www.google.co.nz/search?q=AudibleMediaPlayerFilter.exe
 [8]: http://www.google.co.nz/search?q=msvcr70.dll
 [9]: http://www.google.co.nz/search?q=msvci70.dll
 [10]: http://www.funkypenguin.co.nz/wp-content/uploads/2009/01/TinyXP-Rev08-1.jpg
 [11]: http://www.funkypenguin.co.nz/wp-content/uploads/2009/01/TinyXP-Rev08.jpg
