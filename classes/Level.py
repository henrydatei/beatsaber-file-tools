import dataclasses
import hashlib
import os
import json
from typing import List, Optional

@dataclasses.dataclass
class Level:
    foldername: str
    beatsaver_id: Optional[str] = dataclasses.field(init = False)
    files: List[str] = dataclasses.field(init = False)
    hash: str = dataclasses.field(init = False)
    
    def __post_init__(self):
        self.beatsaver_id = self.foldername.split("\\")[-1].split(" ")[0]
        if self.beatsaver_id == "Beat":
            self.beatsaver_id = None
            
        # calc hash
        hasher = hashlib.sha1()
        self.files = os.listdir(self.foldername)
        if "Info.dat" in self.files:
            f = open(os.path.join(self.foldername, "Info.dat"), "rb")
        elif "info.dat" in self.files:
            f = open(os.path.join(self.foldername, "info.dat"), "rb")
        else:
            raise FileNotFoundError("Info.dat or info.dat not found")
        
        hasher.update(f.read())
        f.seek(0)
        info = json.load(f)
        for difficultyBeatmapSet in info["_difficultyBeatmapSets"]:
            for difficultyBeatmap in difficultyBeatmapSet["_difficultyBeatmaps"]:
                beatmapFile = difficultyBeatmap["_beatmapFilename"]
                hasher.update(open(os.path.join(self.foldername, beatmapFile), "rb").read())
        self.hash = hasher.hexdigest().upper()