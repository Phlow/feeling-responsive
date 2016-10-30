# build local Jekyll pages

local: clean
	bundle exec jekyll serve --config _config.yml,_config_dev.yml

clean:
	rm -rf _site/*




