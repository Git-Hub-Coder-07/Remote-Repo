from pytube import YouTube

# Function to download YouTube video
def download_video(url):
    try:
        # Create YouTube object
        yt = YouTube(url)

        # Display video title
        print(f"Title: {yt.title}")

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        print("Downloading...")
        video_stream.download()
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Provide the YouTube video URL
video_url = input("Enter the YouTube video URL: ")
download_video(video_url)
