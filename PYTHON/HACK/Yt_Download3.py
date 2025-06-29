import os
from yt_dlp import YoutubeDL

def download_video(url, output_dir='downloads'):
    """
    Downloads a video in Full HD (1080p) quality.
    
    Args:
        url (str): The URL of the video to download.
        output_dir (str): The directory to save the downloaded video.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    options = {
        'format': 'bestvideo[height<=1080]+bestaudio/best',
        'merge_output_format': 'mp4',  # Ensure video and audio are merged into MP4 format
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'postprocessors': [
            {'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}
        ],
    }

    try:
        with YoutubeDL(options) as ydl:
            print(f"Downloading video from: {url}")
            ydl.download([url])
            print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")
    if video_url.strip():
        download_video(video_url)
    else:
        print("No URL provided. Exiting...")
