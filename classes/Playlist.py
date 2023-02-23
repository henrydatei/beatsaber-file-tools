import dataclasses
import json

from .Level import Level

@dataclasses.dataclass
class Playlist:
    filename: str
    playlistTitle: str = dataclasses.field(init = False)
    playlistAuthor: str = dataclasses.field(init = False)
    songs: dict = dataclasses.field(init = False)
    
    def __post_init__(self):
        with open(self.filename, "r") as f:
            playlist = json.load(f)
            self.playlistAuthor = playlist["playlistAuthor"]
            self.playlistTitle = playlist["playlistTitle"]
            self.songs = playlist["songs"]
            
    def addSong(self, level: Level) -> None:
        with open(self.filename, "r+") as f:
            playlist = json.load(f)
            playlist["songs"].append({"hash": level.hash, "key": level.beatsaver_id, "songName": level.songName, "levelAuthorName": level.levelAuthor})
            f.seek(0)
            json.dump(playlist, f, indent = 4)