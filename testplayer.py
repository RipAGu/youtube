import vlc
  
# importing time module
import time
  
# creating Instance class object
player = vlc.Instance()

# creating a new media
media = player.media_new("https://www.youtube.com/watch?v=QrZ-A4Ja8rk")
  
# creating a media player object
media_player = player.media_player_new()


# setting video scale
media_player.video_set_scale(0.6)
  
# start playing video
media_player.play()
  
  
# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(100)

