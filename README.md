# Rhythm-Game Library Management Tools

These are just some quick tools I threw together for managing a
library of rhythm game songs.

The intent is to make it easy to serve them via http to rhythm games
that have been updated to support downloading them. Currently none
have this support, although I am working on adding it to Performous.

I also intend to write some tools to help organize the library so
that directory structure is sensible, according to the contents
of song.ini files.

# Usage

Currently, there's just two tools, the cache builder, and the http server.

The cache-builder is `build-cache.py`. It is started by running `make
cache`, and expects all songs to be visible in a directory called
`repo`. This needs to be a directory located inside wherever your
clone this git repository. Or you could havk on `build-cache.py` to
let it look elsewhere.

In _my_ `repo`, I have symlinks to all of my actual repositories, but
you could move all your files to your `repo` if you want.

The other tool is the http server. It's just `SimpleHTTPServer` from python,
and is invoked using `make server`.

# Caveats

Song.ini that have unicode characters often trip up the json encoder
because the python configparser apparently reads those files as blobs
instead of as UTF-8. I've tried to get the python code to be smart
enough to decode them, but ultimately it was easier to get an emacs
macro to just convert all the files that were causing me pain from DOS
encoding to unix-utf-8. `build-cache.py` will at least print out the
names of any files that are problematic for you.  If you're better
with Python unicode suport, please fix that when it hits you and
submit a PR.

`build-cache.py` also has a hack for fixing song.ini files so that
they organize better. In particular, it standardizes a bunch of band
names where there would otherwise be ambiguity. It does this by
looking for certain patterns and fixing the names accordingly. Your
mileage may vary and you may want a better solution. I was
intentionally not trying to provide a great solution here.
