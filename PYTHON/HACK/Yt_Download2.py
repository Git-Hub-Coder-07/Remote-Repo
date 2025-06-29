import os
from yt_dlp import YoutubeDL

def download_video():
    url = input("Enter the video URL: ").strip()
    if not url:
        print("URL cannot be empty.")
        return

    # Directory to save the video
    output_dir = 'downloads'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # yt-dlp options
    options = {
        'format': 'best',  # Download the best quality available
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',  # Save the video with its title
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convert to MP4 format if necessary
        }],
    }

    try:
        with YoutubeDL(options) as ydl:
            print(f"Downloading from: {url}")
            ydl.download([url])
            print(f"Download completed! Saved in '{output_dir}' folder.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_video()