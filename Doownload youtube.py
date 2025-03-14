import yt_dlp

def download_youtube(url):  # Options for downloading the video
    ydl_opts= {
        'format': 'bestvideo[height<=1080]', # Download the best quality up to 1080p
        'noplaylist': True, # Avoid downloading playlists

    }
    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__=="__main__":
    # Ask the user for the YouTube video URL
    video_url=input("Enter a yotube video")
    download_youtube(video_url)