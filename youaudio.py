
from pytube import YouTube
import os
import ffmpeg
def video_downloader():
   url=input("please past the url hear to downloade the video :")
   processurl="'"+url+"'"
   my_video=YouTube(processurl)
   print("--------------Details-------------")
   title = my_video.title
   desc = my_video.description
   print(title)
   print(desc)
   choise=str(input("enter (Y) to downloade the video :"))
   choise_=choise.upper()
   print(choise_)
   if choise_ == "Y":
      print("Your audio start downloading...")
      my_video = my_video.streams.filter(only_audio=True).first()
      audio= my_video.download()
      
  

  
# result of success
      print(title," .....sucessfully downloaded.....")
      print("")
      print(" to downloade another audio")
      video_downloader()
   else:
       print(".....thankyou.....")
video_downloader()
       