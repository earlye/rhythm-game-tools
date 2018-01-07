import configparser
import glob
import json
import os
import sys

from pprint import pprint

def findSongs(path):
    for filename in glob.iglob(os.path.join(path,'**','song.ini'), recursive=True):
        yield loadSong(filename)

def configToDict(config):
    return config._sections

def loadFile(filename):
    with open(filename,'r') as f:
        return f.read()

def dropComment(l):
    if l.startswith('//'):
        return ''
    return l

def dropComments(s):
    return '\n'.join(dropComment(l) for l in s.split('\n'))

def loadSong(filename):
    config = configparser.ConfigParser(strict=False)
    try:
        config.read_string(dropComments(loadFile(filename)))
        result = config._sections
        result["path"] = os.path.dirname(filename)
        json.dumps(result) # make sure it's encodable
        return result;
    except Exception as e:
        sys.stderr.write("{}\n".format(filename))
        return { "path" : filename , "error" : e }

def fixArtist(artist):
    if artist.lower().endswith("[fof.spain]"):
        artist = artist[:-12]
    if artist.lower().startswith("the "):
        artist = artist[3:]
    artist = artist.strip()

    if artist=="Acro-brats":
        artist = "Acro-Brats"
    if artist=="Alice In Chains":
        artist = "Alice in Chains"
    if artist=="Bob Marley & The Wailers" or artist=="Bob Marley":
        artist = "Bob Marley and the Wailers"
    if artist=="Bullet For My Valentine":
        artist = "Bullet for My Valentine"
    if artist=="Dragonforce":
        artist = "DragonForce"
    if artist=="Honest Bob and the Factory-to-Dealer":
        artist = "Honest Bob and the Factory-to-Dealer Incentives"
    if artist=="J Geils Band":
        artist = "J. Geils Band"
    if artist=="Jimmy Hendrix":
        artist = "Jimi Hendrix"
    if artist=="Megadeath":
        artist = "Megadeth"
    if artist=="Motley Crue":
        artist = "Mötley Crüe"
    if artist=="NickelBack":
        artist = "Nickelback"
    if artist=="NightWish":
        artist = "Nightwish"
    if artist=="Panic at the Disco":
        artist = "Panic! at the Disco"
    if artist=="Panic! At the Disco":
        artist = "Panic! at the Disco"
    if artist=="P.O.D":
        artist = "P.O.D."
    if artist=="Queensryche":
        artist = "Queensrÿche"
    if artist=="REM":
        artist = "R.E.M."
    if artist.lower()=="siouxsie and the banshees":
        artist = "Siouxsie and the Banshees"
    if artist == "Sonata Arctica / FReTs By PAsisTi" or artist == "Sonata Artica":
        artist = "Sonata Arctica"
    if artist.lower() == "sum41":
        artist = "Sum 41"
    if artist.lower().startswith("system of a down"):
        artist = "System of a Down"
    if artist == "T-Rex":
        artist = "T. Rex"
    if artist.lower().startswith("tears for fears"):
        artist = "Tears for Fears"
    if artist == "Timmy & the Lords of the Underworld":
        artist = "Timmy and the Lords of the Underworld"
    if artist.lower() == "vagiant":
        artist = "VAGIANT"
    if artist.lower() == "war":
        artist = "War"
    if artist.lower().startswith("weezer"):
        artist = "Weezer"
    if artist.lower().startswith("white stripes"):
        artist = "White Stripes"
    if artist.lower() == "dc talk":
        artist = "DC Talk"

    return artist.strip()

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
