# File name: oldVersion.py
import random
import time
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.graphics import *
from kivy.clock import Clock
# Window.clearcolor = (1, 1, 1, 1)

class MyWidget(Widget):
	def __init__(self, **kwargs):
		self.selected = None
		self.add_seq()
		super(MyWidget, self).__init__(**kwargs)
		self.currButton = self.get_first_button()
		self.currColor = self.currButton.color
		self.completed = False
		
	def change_color(self, dt):
		self.currButton.color=self.currColor
		#print(self.currColor)
	
	def add_seq(self):
		options = ["red", "blue", "green", "yellow"]
		c = random.choice(options)
		i = 1
		self.target_sequence.append(c)
		
		for btn in self.children:
			print(btn.text)
			if btn.text.lower() == c:
				print("Button found", btn)
				self.currColor = btn.color
				self.currButton = btn
				btn.color=(250,235,215,1)
				Clock.schedule_once(self.change_color,1)
				
				break
		
		print("Current sequence:", self.target_sequence)
	
	
	def get_first_button(self):
		for btn in self.children:
			if btn.text.lower() == 'yellow':
				return btn
	
	target_sequence = []
	sequence = []

	def press_button(self, color, obj):
		self.sequence.append(color)
		incorrect = False
		for i in range(len(self.sequence)):
			if self.sequence[i] != self.target_sequence[i]:
				print("Incorrect sequence!")
				self.sequence = []
				incorrect = True
				break
		if len(self.sequence) == len(self.target_sequence):
			# sequence == target_sequence
			print("Wow you did it")
			if(len(self.sequence) == 5)
				self.completed = True
			self.sequence = []
			self.add_seq()
		elif not incorrect:
			left = (len(self.target_sequence) - len(self.sequence))
			print("Okay so far... {} to go".format(left))

class WidgetsApp(App):
	def build(self):
		w = MyWidget()
		return w

if __name__=="__main__":
	WidgetsApp().run()