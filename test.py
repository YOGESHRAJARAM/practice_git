import pytube as pt

yt = pt.YouTube("https://youtu.be/-wG_wCQFjY4")
t = yt.streams.filter(only_audio=True)
t[0].download()