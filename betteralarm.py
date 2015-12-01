import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty, ListProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import pygame
import time

class AlarmPopup(Popup):
    pass
        

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
        
        if (now.tm_hour == self.alarm.tm_hour and now.tm_min == self.alarm.tm_min):
            if(self.playing == False):
                print("ALARM NOW")
                
                popup = AlarmPopup(title_size = "0sp", separator_color=[0,0,0,1], auto_dismiss=False)
                popup.ids.off.background_color=[255, 0, 0, 1]
                popup.ids.off.bind(on_press=popup.dismiss)
                popup.bind(on_dismiss=self.turnOffAlarm)
                popup.open()
                
                pygame.mixer.init()
                pygame.mixer.music.load("alarm.wav")
	        pygame.mixer.music.play()

		self.playing = True
                	
        elif(self.playing):
            self.playing = False
    
    def turnOffAlarm(self, arg):
        pygame.mixer.music.stop()
        
    
class AlarmApp(App):
    def build(self):
        alarmClock = AlarmClock()
        Clock.schedule_interval(alarmClock.update_time, 1.0)
        return alarmClock

if __name__ == '__main__':
    AlarmApp().run()
