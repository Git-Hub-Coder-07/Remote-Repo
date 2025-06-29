import yt_dlp

yt_dlp.YoutubeDL({'format': 'best', 'outtmpl': '%(title)s.%(ext)s'}).download(
    ['https://youtu.be/Ez8F0nW6S-w?si=lNSbi9n1OmHMRp0L'])