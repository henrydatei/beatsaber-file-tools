# Beatsaber File Tools
A Python package to interact with Beatsaber (it's not a Beatsaber mod!)

### Usage
Download `beatsaber-file-tools.py` and place it in the same location as your script. Then
```python
from BeatsaberFileTool import BeatsaberFileTool

# path is mostly "C:\Program Files (x86)\Steam\steamapps\common\Beat Saber"
bs = BeatsaberFileTool("path to your Beatsaber files")

hash = bs.id2hash("49ae") # https://beatsaver.com/maps/49ae
bs.downloadMapFromBeatsaver(hash)
bs.addMapToUpvotedSongs(hash)
bs.addMapToFavedSongs(hash)
```

### Features
- download a map from Beatsaver
- add a map to upvoted songs (_Please note that the "Upvote" requests to Beatsaver won't be executed. The map will just be added to a file._)
- add a map to favourite songs
- convert an ID from Beatsaver to a hash