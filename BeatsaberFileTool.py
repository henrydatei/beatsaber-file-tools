import dataclasses
import os
import requests
import re
from zipfile import ZipFile
import json
from typing import List

from classes.Level import Level
from classes.Playlist import Playlist

@dataclasses.dataclass
class BeatsaberFileTool:
    path: str
    
    def __post_init__(self):
        self.customSongsPath = os.path.join(self.path, "Beat Saber_Data\CustomLevels")
        self.votedSongsPath = os.path.join(self.path, "UserData\\votedSongs.json")
        self.playlistPath = os.path.join(self.path, "Playlists")
        self.playerDataPath = os.path.join(os.getenv("APPDATA"), "..\\LocalLow\\Hyperbolic Magnetism\\Beat Saber\\PlayerData.dat")
        
    def downloadMapFromBeatsaver(self, hash: str) -> None:
        r = requests.get("https://eu.cdn.beatsaver.com/{}.zip".format(hash))
        r.raise_for_status()
        d = r.headers['content-disposition']
        fname = re.findall("filename=(.+)", d)[0].split('"')[1]
        path = os.path.join(self.customSongsPath, fname)
        f = open(path, "wb")
        f.write(r.content)
        f.close()
        with ZipFile(path, "r") as zip:
            zip.extractall(path[:-4])
        os.remove(path)
        
    def addMapToUpvotedSongs(self, hash: str) -> None:
        with open(self.votedSongsPath, "r+") as votedSongsFile:
            idx = str(votedSongsFile.read()).index("{")
            votedSongsFile.seek(idx)
            votedSongs = json.load(votedSongsFile)

            newData = {hash: {"hash": hash, "voteType": "Upvote"}}
            votedSongs.update(newData)
            votedSongsFile.seek(0)
            json.dump(votedSongs, votedSongsFile)
            
    def addMapToFavedSongs(self, hash: str) -> None:
        with open(self.playerDataPath, "r+") as playerDataFile:
            playerData = json.load(playerDataFile)
            string = "custom_level_" + hash.upper()
            playerData["localPlayers"][0]["favoritesLevelIds"].append(string)
            playerDataFile.seek(0)
            json.dump(playerData, playerDataFile)
            
    def id2hash(id: str) -> str:
        r = requests.get("https://api.beatsaver.com/maps/id/{}".format(id))
        r.raise_for_status()
        hash = r.json()["versions"][0]["hash"]
        return hash
    
    def getSongs(self) -> List[Level]:
        songList = []
        for folder in os.listdir(self.customSongsPath):
            if not "(Built in)" in folder:
                songList.append(Level(os.path.join(self.customSongsPath, folder)))
                
        return songList
    
    def getPlaylists(self) -> List[Playlist]:
        playlistList = []
        for file in os.listdir(self.playlistPath):
            if file.endswith(".bplist"):
                playlistList.append(Playlist(os.path.join(self.playlistPath, file)))
                
        return playlistList