import vlc
  
# importing time module
import time
  
# creating Instance class object
player = vlc.Instance()


# creating a new media
media_player = player.media_player_new()
media = player.media_new("./testmp.mp4")
media_player.set_media(media)
media_player.play()
time.sleep(10)
# wait so the video can be played for 5 seconds
# irrespective for length of video


