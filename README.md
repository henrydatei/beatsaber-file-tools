# Beatsaber File Tools
A Python package to interact with Beatsaber (it's not a Beatsaber mod!)

### Usage
Clone the repo and place a file with the following content in it.
```python
from BeatsaberFileTool import BeatsaberFileTool

# path is mostly "C:\Program Files (x86)\Steam\steamapps\common\Beat Saber"
bs = BeatsaberFileTool("path to your Beatsaber files")

hash = bs.id2hash("49ae") # https://beatsaver.com/maps/49ae
bs.downloadMapFromBeatsaver(hash)
bs.addMapToUpvotedSongs(hash)
bs.addMapToFavedSongs(hash)
```
When working with different tools, the CustomLevels folder can get full of duplicate songs. You can clean it up with the following code.
```python
from BeatsaberFileTool import BeatsaberFileTool

# path is mostly "C:\Program Files (x86)\Steam\steamapps\common\Beat Saber"
bs = BeatsaberFileTool("path to your Beatsaber files")
duplicateSongs = bs.listDuplicateSongs()
print(duplicateSongs)
bs.removeDuplicateSongs()
```
When you use [BSManager](https://github.com/Zagrios/bs-manager) to manage different version of Beat Saber, you'll likely have a folder for all songs which get synced through different version of Beatsaber. To work with this CustomLevels folder, do:
```python
from BeatsaberFileTool import BeatsaberFileTool

# path is mostly "C:\Program Files (x86)\Steam\steamapps\common\Beat Saber"
bs = BeatsaberFileTool("path to your Beatsaber files")
bs.useBS_Manager()
print(bs.customSongsPath)
# ...
```

### Features
- download a map from Beatsaver
- add a map to upvoted songs (_Please note that the "Upvote" requests to Beatsaver won't be executed. The map will just be added to a file._)
- add a map to favourite songs
- convert an ID from Beatsaver to a hash