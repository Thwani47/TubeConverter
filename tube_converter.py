from pytube import YouTube, Playlist
import pytube
import os

class VideoDownloader:
    def __init__(self, url):
        self.videoDownloader = YouTube(url)
        self.streams = self.videoDownloader.streams
        self.url  = url

    def print_info(self):
        print("\n[INFO]:\n\ntitle: {0}\n\nThumbnail URL: {1}\n\nLength (seconds): {2}"
              .format(self.videoDownloader.title, self.videoDownloader.thumbnail_url, self.videoDownloader.length))
        print("\nDescription: {0}".format(self.videoDownloader.description))
        
    def download_audio_track_only(self):
        self.streams = self.videoDownloader.streams.filter(only_audio=True)
        
        top_stream = self.streams[0]
        
        print("Getting audio track with highest quality.....")
        for stream in self.streams:
            if stream.resolution:
                if int(stream.resolution.split("p")[0]) >= int(top_stream.resolution.split("p")[0]):
                    top_stream = stream
                    
        print("Downloading audio track......")
        mp4_name = pytube.extract.video_id(self.url)
        mp3_name = self.videoDownloader.title.strip() + '.mp3'
        print(mp4_name)
        print(mp3_name)
        top_stream.download(filename=mp4_name)
        os.rename(mp4_name + ".mp4", mp3_name)
        # os.system("ren {0} {1}".format(mp4_name + ".mp4", mp3_name ))
                
        print("Download complete!")
        
    def download_video(self):
        self.streams = self.videoDownloader.streams.filter(file_extension='mp4')
        
        top_stream = self.streams[0]
        
        print("Getting video with highest quality.....")
        for stream in self.streams:
            if stream.resolution:
                if int(stream.resolution.split("p")[0]) >= int(top_stream.resolution.split("p")[0]):
                    top_stream = stream
                    
        print("Downloading video track......")
        top_stream.download()
        print("Download complete!")
        
        
class PlaylistDownloader:
    def __init__(self, url):
        self.playlistDownloader = Playlist(url)        
        
    def print_info(self):
        print("\nTitle: {0}\n\nNumber of VideosL {1}".format(self.playlistDownloader.title, len(self.playlistDownloader.video_urls)))
