from tube_converter import VideoDownloader
import argparse
import pytube

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="The YouTube URL of the video to be downloaded")
    parser.add_argument("--info", help = "Get more information about the URL ", action="store_true")
    parser.add_argument("--video", help = "Specify this if you want to download a single video only ", action="store_true")
    parser.add_argument("--playlist", help = "Specify this if you want to download videos from a playlist ", action="store_true")
    parser.add_argument('--audio-only', help="Get the audio track only", action="store_true")
    parser.add_argument('--video-only', help="Get the video only", action="store_true")
    
    args = parser.parse_args()
    if args.video:
        if not args.url:
            print("ERROR: No URL found. Please provide URL")
        else:
            try:
                videoDownloader = VideoDownloader(args.url)
                if args.info:
                    videoDownloader.print_info()
                
            
                if args.audio_only:
                    videoDownloader.download_audio_track_only()

                if args.video_only:
                    videoDownloader.download_video()
           
            except pytube.exceptions.PytubeError:
                print("ERROR: There seems to be an error with the specified URL. Please try another one")
        
    elif args.playlist:
        print("playlist")
    
    
            
    print("\n\nBYE!!!\n")
            
    
        
    
        
    