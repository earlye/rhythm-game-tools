import configparser
import glob
import json
import os
import sys

from rhythmLib import *

def arrangeSongs(path):
    result = {}
    for song in findSongs(path):
        artist = fixArtist(song.get('song',{}).get('artist',"{unknown}"))
        name = song.get('song',{}).get('name',"{unknown}")
        if not 'song' in song:
            song['song'] = {}
        song['song']['artist'] = artist
        if not artist in result:
            result[artist] = {}
        if not name in result[artist]:
            result[artist][name]= []
        result[artist][name].append(song)
    return result

def main():
    database =    {
        "$type" : "rhythm-game-content",
        "artists" : arrangeSongs('repo')
    }
    print(json.dumps(database,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
