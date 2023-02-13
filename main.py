from pytube import YouTube
 
from sys import argv

def video():
    yt = YouTube(input("what is the link of the video: "))
    yd = yt.streams.get_highest_resolution()
    yd.download("E:\yt_vodep")
    return

video()