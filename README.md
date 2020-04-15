# TubeConverter
An app for downloading videos and/or playlists from youtube and converting them other file formats

## About
This is a CLI Interface that uses pytube to download videos from YouTube and also provides to users an ability to convert the videos to other formats, mainly audio formats.


## Usage
```
Install the requirements first:

$ pip install -r requirements.txt

To download a single video (mp4 format):

$ python main.py --video --url URL --video-only

To download a single video (audio track format):

$ python main.py --video --url URL --audio-only

```

### TODO:
- [x] Handle Error Exceptions (e.g video from URL DNE):rage:
- [] Convert videos after download to mp3 [Will make use of andyp123's class](https://github.com/andyp123/mp4_to_mp3) 
- [] Add feature to delete video after conversion
- [] Add feature for downloading playlists
- [] Add feauture for converting videos in a playlist into other formats (start with mp3 first)
- [] Add feauture for listing the videos in a playlist and only downloading only the videos that are selected by the user
- [] Will probably think of other cool stuff along the way :stuck_out_tongue_winking_eye:
