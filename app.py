from flask import  Flask
from tube_converter import VideoDownloader
app = Flask(__name__)


@app.route('/')
def index():
    downloader = VideoDownloader('https://www.youtube.com/watch?v=1S4cXeL1-nc')
    downloader.print_info()
    downloader.download_mp4()
    return 'Hello world'

if __name__ == '__main__':
    app.run(port=8000)