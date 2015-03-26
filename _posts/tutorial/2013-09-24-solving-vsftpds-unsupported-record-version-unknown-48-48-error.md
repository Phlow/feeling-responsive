---
title: 'Solving vsftpd&#8217;s unsupported record version unknown 48.48 error'
author: David
layout: page
permalink: /note/solving-vsftpds-unsupported-record-version-unknown-48-48-error/
wp-to-buffer-log:
  - 'O:8:"WP_Error":2:{s:6:"errors";a:1:{s:19:"http_request_failed";a:1:{i:0;s:65:"Operation timed out after 5000 milliseconds with 0 bytes received";}}s:10:"error_data";a:0:{}}'
wp-to-buffer:
  - 'a:1:{s:7:"publish";s:1:"1";}'
categories:
  - Note
tags:
  - ssl
  - vsftpd
---
I use FTPS with vsftpd to update my WordPress plugins. This means that the wordpress files don&#8217;t need to be writeable by the webserver user, which adds another layer of protection and separation. I make FTPS available to localhost only, and force SSL encryption end-to-end.

This makes debugging a bit of a PITA though. The simplest way to debug is to REMOVE all that extra security, and allow unencrypted connections from a trusted host, using an FTP GUI (Cyber Duck, in my case), and see any error logs.

In my case, once I stripped away all the encryption, instead of the unsupported record version unknown 48.48 error, I got a succinct error telling me that a chroot was not supported in a directory where my user had write access. Simple fix, turn the encryption back on, and I&#8217;m away!
