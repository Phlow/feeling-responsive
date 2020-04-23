# A Responsive Jekyll Theme: *Feeling Responsive*

Do you want to get to know *Feeling Responsive*? Than check it out first and have a look on its home at  <http://phlow.github.io/feeling-responsive/>.

To get to know *Feeling Responsive* check out all the features explained in the [documentation][1].

And what license is *Feeling Responsive* released under? [This one][2].

# Build and serve the site locally

Bot is possible, building the site with a local installation of Jekyll or containing Jekyll in a Docker container.

The site is served at [localhost:4000/feeling-responsive](localhost:4000/feeling-responsive) in both cases.

To work around Jekyll build errors, create to folders which are required

```
mkdir .jekyll-cache _site
```

## Local installation

```
jekyll serve --watch
```

The flag `--ẁatch` sets Jekyll in autoreload mode. Whenever a file is changed, its changed are served immediately.


## Docker container

```
docker run --rm -p 4000:4000 --volume="$PWD/vendor/bundle:/usr/loc/bundle" --volume="$PWD:/srv/jekyll" -it jekyll/jekyll:3.8 jekyll serve --watch
```


 [1]: http://phlow.github.io/feeling-responsive/documentation/
 [2]: https://github.com/Phlow/feeling-responsive/blob/gh-pages/LICENSE
