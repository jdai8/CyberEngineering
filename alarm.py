import time
import os
import threading
import winsound

class Alarm(threading.Thread):
    def __init__(self, hours, minutes):
        super(Alarm, self).__init__()
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.keep_running = True

    def run(self):
        try:
            while self.keep_running:
                now = time.localtime()
                if (now.tm_hour == self.hours and now.tm_min == self.minutes):
                    print("ALARM NOW");
                    
                    # windows only - plays sound for 5 seconds
                    winsound.PlaySound("alarm.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    time.sleep(5)
                    winsound.PlaySound(None, 0) 
                    time.sleep(60)
                    #using pygame - not tested
                    #pygame.mixer.init()
                    #pygame.mixer.music.load("alarm.wav")
                    #pygame.mixer.music.play()
                    #while pygame.mixer.music.get_busy() == True:
                    #    continue
                else:
                    time.sleep(1)
            
        except:
            return
            
    def quit(self):
        self.keep_running = False

# hour is in military time: enter 13 for 1 pm
hour = input("Enter the hour you want to wake up at: ")
min = input("Enter the minute you want to wake up at: ")

print("You want to wake up at: {0:02}:{1:02}".format(int(hour), int(min)))

alarm = Alarm(hour, min)
alarm.start()

try:
    while True:
         text = str(input())
         if text == "stop":
            alarm.quit()
            break
except:
    print("Yikes lets get out of here")
    alarm.quit()