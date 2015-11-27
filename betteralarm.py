import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.label import Label
import winsound
import time

class AlarmClock(Widget):
       
    def __init__(self):
        super(AlarmClock, self).__init__()

        h = int(input("Hour: "))
        m = int(input("Minute: "))
        self.alarm = time.gmtime(h * 3600 + m * 60)
        self.playing = False
                 
        self.ids.next.text = time.strftime("Next Alarm: %I:%M %p", self.alarm)
        
    def update_time(self, dt):

        now = time.localtime()
        self.ids.current.text = time.strftime("%I:%M:%S %p", now)
        
        if (now.tm_hour == self.alarm.tm_hour and now.tm_min == self.alarm.tm_min and self.playing == False):
            print("ALARM NOW");

            # windows only - plays sound for 5 seconds
            winsound.PlaySound("alarm.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            self.playing =  True
            # time.sleep(5)
            # winsound.PlaySound(None, 0)
            # time.sleep(60)
            #using pygame - not tested
            #pygame.mixer.init()
            #pygame.mixer.music.load("alarm.wav")
            #pygame.mixer.music.play()
            #while pygame.mixer.music.get_busy() == True:
            #    continue
    
class AlarmApp(App):
    def build(self):
        alarmClock = AlarmClock()
        Clock.schedule_interval(alarmClock.update_time, 1.0)
        return alarmClock

if __name__ == '__main__':
    AlarmApp().run()
