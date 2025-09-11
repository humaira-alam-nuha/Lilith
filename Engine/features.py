from playsound import playsound
import eel

#Playing Assistant Sound Function
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\computer-startup-sound-effect-312870.mp3"
    playsound(music_dir)