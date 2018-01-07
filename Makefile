server: cache.json
	python -m SimpleHTTPServer 6969

cache.json : build-cache.py
	python3 build-cache.py > $@
	head $@

.PHONY : cache
cache :
	rm -f cache.json
	$(MAKE) cache.json
