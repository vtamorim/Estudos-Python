import yt_dlp

link = input("Enter: ")
filename = input("")
options = {
    'outtmpl': filename,  # Your filename
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([link])
