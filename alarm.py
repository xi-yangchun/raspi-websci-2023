import datetime
import time
import serial

from pydub import AudioSegment
from pydub.playback import play
import time

class alarmclock:
    def __init__(self):
        self.targ_hour=0
        self.targ_min=0
        self.now_hour=0
        self.now_min=0
        self.sensing=False
        self.ring_duration=5
        # Replace '/dev/cu.usbmodem1101' with your Arduino's serial port
        self.ser = ""#serial.Serial('/dev/cu.usbmodem1401', 9600)
        self.th_0=30
    
    def get_cds_line(self):
        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').rstrip()
            return line
        else:
            return '0'
    
    def run_alarm_under_lux(self):
        self.targ_hour=1
        self.targ_min=39
        # set target datetime of alarming
        dt_targ=datetime.datetime.now()
        dt_targ=dt_targ.replace(hour=self.targ_hour,
                minute=self.targ_min,second=0,microsecond=0)
        while(1):
            time.sleep(0.1)
            dt_now=datetime.datetime.now()
            delta=(dt_targ-dt_now)
            if delta.total_seconds()<=0 and delta.total_seconds()>=-self.ring_duration*60:
                if int(self.get_cds_line())<=self.th_0:
                    print('ring!!!! {}'.format(delta.total_seconds()))
                    self.make_sound()
    
    def make_sound(self):
        sound = AudioSegment.from_mp3("sound0.mp3")
        play(sound)
        time.sleep(1)