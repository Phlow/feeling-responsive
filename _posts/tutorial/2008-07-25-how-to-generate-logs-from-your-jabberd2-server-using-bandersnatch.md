---
title: Generate logs from your jabberd2 server using Bandersnatch
author: David
excerpt: This tutorial attempts to guide the reader through the process of installing Bandersnatch for use with an existing Jabberd2 server.
layout: page
permalink: /how-to/generate-logs-from-your-jabberd2-server-using-bandersnatch/
redirect_from: /tutorial/how-to-generate-logs-from-your-jabberd2-server-using-bandersnatch/
categories:
  - how-to
tags:
  - bandersnatch
  - jabber
---
This tutorial attempts to guide the reader through the process of installing Bandersnatch for use with an existing Jabberd2 server.<!--more-->

## Get the sources

We need the following:  
* [Bandersnatch][1]  
* [Perl 5.8.x][2]
* [Perl POE][3]
* Perl module: XML::Stream  
* Perl module: Net::Jabber 2.x  
* [Perl module: DBI (mysql)][4]  
* Perl module: POE::Component-Jabber  
* Perl module: POE::Filter-XML

Extract the Bandersnatch installation into a working directory. Install all the above modules, with their dependencies.

## Configure database

Ensure that you have a working mySQL server installation. To automatically create the database permissions / structure, run the following command (as a priviledged mySQL user) from the Bandersnatch working directory:

    mysql -p < bandersnatch.sql

Then restart the mysql server (we have changed permissions, must reload), by running :

    kill -HUP `pidof mysqld`

(If this doesn't work, restart mySQL manually. This may depend on your distribution)

## Config files

### router-users.xml

This file is where the router gets its component and secret information from for component authentication. We want to tell it about a component called &#8220;bandersnatch&#8221;, whose secret is also &#8220;bandersnatch&#8221;&#8230;

Add the following lines:

    <name>bandersnatch</name>
    <secret>bandersnatch</secret>

...between the new tags. i.e., a file modified from default will now look like this:

    <users>
    <user>
    <name>jabberd</name>
    <secret>secret</secret>
    </user>
    <user>
    <name>bandersnatch</name>
    <secret>bandersnatch</secret>
    </user>
    </users>

### router.xml

Now that we have defined our component (above), we need to give it access to connect to the router, and log messages. Edit router.xml, and at the bottom, uncomment the log type ACL, as follows:

    <acl type='log'>
    <user>bandersnatch</user>
    </acl>

### config.xml

Finally, we edit bandersnatch's config.xml, make sure the following are set:

    <server>
    <connectiontype>tcpip</connectiontype>
    <hostname>localhost</hostname>
    <port>5347</port>
    <secret>bandersnatch</secret>
    </server>
    <component>
    <name>bandersnatch</name>
    </component>

Double-check the port (you may have to change it from 5526 to 5347), and the component name. Also, as per the Bandersnatch documentation, make sure that is set to the name of your jabber server, else you won't log anything :)

## Run it

Finally, once you've confirmed that:

1. Jabberd is running properly
2. MySQL is running properly
3. Bandersnatch tables have been created in mySQL
4. The bandersnatch2.pl script is executable (“chmod 755 bandersnatch2.pl” if it’s not)

run:

    ./bandersnatch2.pl

The output should be something like this:

{% highlight perl %}
Use of uninitialized value in substitution (s///) at /usr/local/share/perl/5.8.4/POE/Component/Jabber/Client/J2.pm line 293.
Use of uninitialized value in subroutine entry at /usr/local/share/perl/5.8.4/POE/Component/Jabber/Clien t/J2.pm line 294.  
Connected to MySQL database (bandersnatch@localhost) ... Bandersnatch is listening! ;)
{% endhighlight %}

I ignore the errors. I think they have to do with the Jabber component, and they aren't fatal. If anybody wants to enlighten me, please go ahead :)

 [1]: https://github.com/funkypenguin/bandersnatch
 [2]: http://www.cpan.org/
 [3]: http://poe.perl.org/
 [4]: http://search.cpan.org/%7Etimb
