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
        self.active_alarm=False
        self.sensing=False
        self.ring_duration=5
        # Replace '/dev/cu.usbmodem1101' with your Arduino's serial port
        self.ser = serial.Serial('/dev/ttyACM0', 9600)
        self.th_0=120
        self.lo=0
    
    def get_lightIn(self):
        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').rstrip()
            return line
        else:
            return '0'
        
    def set_lo(self,new_lo):
        self.lo = new_lo
        return None

    def set_th(self,new_th):
        self.th_0=new_th
    
    def set_targ_time(self,hour,min):
        self.targ_hour=hour
        self.targ_min=min
    
    def calc_light_difference(self, lo):
        difference = abs(lo - self.li)
        return difference
    
    #make_sound() need some improvements
    def run(self):
        while True:
            if self.ser.in_waiting > 0:
                line1 = self.ser.readline().decode('utf-8').rstrip()
                print("Light Ser1: {}".format(line1))  # Print the message received from Arduino
                #convert serial from str to int.
                #wrap by try block because it sometimes fails
                try:
                    self.li=int(line1)
                except:
                    self.li=self.lo
                diff=self.calc_light_difference(self.lo)
                print("diff light: {}".format(self.calc_light_difference(self.lo)))
                if diff>=self.th_0:
                    self.active_alarm=True
                else:
                    self.active_alarm=False
            #time.sleep(1)
    
    #legacy function. not in use
    def track_lightIn(self):
        while True:
            if self.ser.in_waiting > 0:
                line1 = self.ser.readline().decode('utf-8').rstrip()
                print("Light Ser1: {}".format(line1))  # Print the message received from Arduino
                #convert serial from str to int.
                #wrap by try block because it sometimes fails
                try:
                    self.li=int(line1)
                except:
                    self.li=self.lo

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
                if int(self.light_difference())>=self.th_0:
                    print('ring!!!! {}'.format(delta.total_seconds()))
                    self.make_sound()
    
    def hold_beep(self):
        while True:
            if self.active_alarm==True:
                self.make_sound()
            time.sleep(0.01)
    
    def make_sound(self):
        sound = AudioSegment.from_mp3("sound0.mp3")
        play(sound)