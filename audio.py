from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("./alarmfiles/alarm.mp3")

play(sound)