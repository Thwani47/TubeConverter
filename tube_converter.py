from pytube import YouTube, Playlist


class VideoDownloader:
    def __init__(self, url):
        self.videoDownloader = YouTube(url)
        self.streams = None

    def print_info(self):
        print("\n[INFO]:\n\ntitle: {0}\n\nThumbnail URL: {1}\n\nLength (seconds): {2}"
              .format(self.videoDownloader.title, self.videoDownloader.thumbnail_url, self.videoDownloader.length))
        print("\nDescription: {0}".format(self.videoDownloader.description))
        

    def download_mp4(self):
        self.streams = self.videoDownloader.streams.filter(file_extension='mp4').all()
        print(len(self.streams))

