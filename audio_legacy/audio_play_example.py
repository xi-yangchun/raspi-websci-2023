from pydub import AudioSegment
from pydub.playback import play
import time

while(1):
    sound = AudioSegment.from_mp3("sound0.mp3")
    play(sound)
    time.sleep(1)