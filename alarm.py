import datetime
import time

class alarmclock:
    def __init__(self):
        self.targ_hour=0
        self.targ_min=0
        self.now_hour=0
        self.now_min=0
        self.sensing=False
        self.ring_duration=5
    
    def ring(self):
        ok=False
        if self.now_hour==self.targ_hour and self.now_min>=self.targ_min\
        and self.now_min<=self.targ_min+self.ring_duration:
            ok=True
        
        if ok and self.sensing==True:
            self.make_sound()
    
    def make_sound(self):
        pass

while(True):
    dt_now = datetime.datetime.now()
    hour=dt_now.hour
    minute=dt_now.minute
    time.sleep(1)