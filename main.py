from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.graphics import Color,Line,Rectangle
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.clock import Clock

class Intro(FloatLayout):
	"""docstring for intro"""
	def __init__(self, **kwargs):
		super(Intro, self).__init__(**kwargs)
		
		self.o1 = Label(text="- X -", font_size=500, color=(1,.3,.3,1))
		self.add_widget(self.o1)
		with self.canvas:
			Color(0.8,0.7,.61,1, mode="rgba")
			Rectangle(size=(Window.size[0]*10, Window.size[1]*10))
			Color(0.3,0.4,1,1, mode="rgba")
			Line(width=10, points=(0, 0, Window.size[0], Window.size[1]))
			Line(width=10, points=(0, Window.size[1], Window.size[0], 0))
		
		self.o2 = Label(text="OO", font_size=507, color=(1,.3,.3,1))
		self.add_widget(self.o2)
		
		self.play = Button(text="Play!",font_size=60, color=(.1,0,.1,1), size_hint=(.5,.3), pos_hint={"x":.25,"buttom":1}, background_color=(.8,.6,.4,0))
		self.play.bind(on_press=self.switch)
		self.add_widget(self.play)

	def switch(self, _):
		game.screen_manager.current = "Board"

class Board(GridLayout):
	"""docstring for Board"""
	def __init__(self, **kwargs):
		super(Board, self).__init__(**kwargs)
		self.cols = 3
		self.rows = 3
		
		with self.canvas:
			Color(.8,.1,.6,1, mode="rgba")
			self.rect = Rectangle(size=(Window.size[0]*10, Window.size[1]*10))
	
		self.tics = ["X","O"]
		self.index_blocks = {}		
		self.index_mapping = {}
		self.started = False
		self.win = False
		self.count = 0
		result = False

		self.block1 = Button(on_release=self.draw, background_color=(0,0,0,1), font_size = 200)
		self.block1.filled = False
		self.block1.index = 1
		self.index_blocks[1] = self.block1
		self.add_widget(self.block1)

		self.block2 = Button(on_release=self.draw, background_color=(0,0,0,1), font_size = 200)
		self.block2.filled = False
		self.block2.index = 2
		self.index_blocks[2] = self.block2
		self.add_widget(self.block2)

		self.block3 = Button(on_release=self.draw, background_color=(0,0,0,1), font_size = 200)
		self.block3.filled = False
		self.block3.index = 3
		self.index_blocks[3] = self.block3
		self.add_widget(self.block3)

		self.block4 = Button(on_release=self.draw, background_color=(0,0,0,1), font_size = 200)
		self.block4.filled = False
		self.block4.index = 4
		self.index_blocks[4] = self.block4
		self.add_widget(self.block4)

		self.block5 = Button(on_release=self.draw, background_color=(0,0,0,1), font_size = 200)
		self.block5.filled = False
		self.block5.index = 5
		self.index_blocks[5] = self.block5
		self.add_widget(self.block5)

		self.block6 = Button(on_release=self.draw, background_color=(0,0,0,1), font_size = 200)
		self.block6.filled = False
		self.block6.index = 6
		self.index_blocks[6] = self.block6
		self.add_widget(self.block6)

		self.block7 = Button(on_release=self.draw, background_color=(0,0,0,1), font_size = 200)
		self.block7.filled = False
		self.block7.index = 7
		self.index_blocks[7] = self.block7
		self.add_widget(self.block7)

		self.block8 = Button(on_release=self.draw, background_color=(0,0,0,1), font_size = 200)
		self.block8.filled = False
		self.block8.index = 8
		self.index_blocks[8] = self.block8
		self.add_widget(self.block8)

		self.block9 = Button(on_release=self.draw, background_color=(0,0,0,1), font_size = 200)
		self.block9.filled = False
		self.block9.index = 9
		self.index_blocks[9] = self.block9
		self.add_widget(self.block9)

	def draw(self, block_button):
		print(self.count)
		self.count += 1
		

		if not self.started:
			block_button.color = (0.3,0.4,1,1)
			block_button.text = self.tics[0]
			self.prev_tic = block_button.text
			self.started = True
			block_button.filled = True
			self.index_mapping[block_button.index] = block_button.text
			if self.check_horizontal(block_button.index):
				return
			elif self.check_vertical(block_button.index):
				return
			elif self.check_diagonal(block_button.index):
				return

			return

		while block_button.filled == False:
			if self.prev_tic == self.tics[0]:
				block_button.color = (1,.3,.3,1)
				block_button.text = self.tics[1]
				self.prev_tic = block_button.text 
				block_button.filled = True
				self.index_mapping[block_button.index] = block_button.text
				if self.check_horizontal(block_button.index):
					return
				elif self.check_vertical(block_button.index):
					return
				elif self.check_diagonal(block_button.index):
					return
				elif self.check_even():
					
					return
			else:
				block_button.color = (0.3,0.4,1,1)
				block_button.text = self.tics[0]			
				self.prev_tic = block_button.text
				block_button.filled = True
				self.index_mapping[block_button.index] = block_button.text
				if self.check_horizontal(block_button.index):
					return
				elif self.check_vertical(block_button.index):
					return
				elif self.check_diagonal(block_button.index):
					return
				elif self.check_even():
									
					return
			return

	def check_horizontal(self, index):
		if index in range(1,4):
			if self.index_mapping.get(1) == self.index_mapping.get(2) == self.index_mapping.get(3):
				print(self.index_mapping.get(index), "horizontally wining")
				self.victory(list(range(1,4)))
				#self.stop()
				self.win = True
				return self.win
		elif index in range(4,7):
			if self.index_mapping.get(4) == self.index_mapping.get(5) == self.index_mapping.get(6):
				print(self.index_mapping.get(index), "horizontally wining")
				self.victory(list(range(4, 7)))
				#self.stop()
				self.win = True
				return self.win
		elif index in range(7,10):
			if self.index_mapping.get(7) == self.index_mapping.get(8) == self.index_mapping.get(9):
				print(self.index_mapping.get(index), "horizontally wining")
				self.victory(list(range(7, 10)))
				#self.stop()
				self.win = True
				return self.win
		
	def check_vertical(self, index):
		if index in [1, 4, 7]:
			if self.index_mapping.get(1) == self.index_mapping.get(4) == self.index_mapping.get(7):
				print(self.index_mapping.get(index), "vertically wining")
				self.victory([1, 4, 7])
				#self.stop()
				self.win = True
				return self.win
		elif index in [2, 5, 8]:
			if self.index_mapping.get(2) == self.index_mapping.get(5) == self.index_mapping.get(8):
				print(self.index_mapping.get(index), "vertically wining")
				self.victory([2, 5, 8])
				#self.stop()
				self.win = True
				return self.win
		elif index in [3, 6, 9]:
			if self.index_mapping.get(3) == self.index_mapping.get(6) == self.index_mapping.get(9):
				print(self.index_mapping.get(index), "vertically wining")
				self.victory([3, 6, 9])
				#self.stop()
				return True

	def check_diagonal(self, index):
		if index in [1, 5, 9]:
			if self.index_mapping.get(1) == self.index_mapping.get(5) == self.index_mapping.get(9):
				print(self.index_mapping.get(index), "diagonal wining")
				self.victory([1, 5, 9])
				#self.stop()
				self.win = True
				return self.win
		elif index in [3, 5, 7]:
			if self.index_mapping.get(3) == self.index_mapping.get(5) == self.index_mapping.get(7):
				print(self.index_mapping.get(index), "diagonal wining")
				self.victory([3, 5, 7])
				#Clock. self.stop()
				self.win = True
				return self.win
	def check_even(self):

		if self.count >= 9 and self.win == False:
			game.screen_manager.current = "Finished"
			print("hiiiiii")
			Clock.schedule_once(self.newgame, 1)
			return True
	def victory(self, victory_list):
		game.screen_manager.current = "Finished"
		print(victory_list)
		for i in victory_list:
			self.index_blocks[i].font_size = 204
			del self.index_mapping[i]
		for i in self.index_mapping:
			
			if self.index_mapping[i] == "X":
				self.index_blocks[i].color = (0.3,0.4,1,.2)
			else :
				self.index_blocks[i].color = (1,.3,.3,.2)
		Clock.schedule_once(self.newgame, 1)

	def newgame(self,_):
		
		for i in self.index_blocks:
			self.index_blocks[i].filled = False
			self.index_blocks[i].text=""
			print(self.index_blocks[i].filled)
		self.index_mapping.clear()
		self.count = 0
		self.win = False
		print(self.index_mapping)

	
class Finished(GridLayout):
	"""docstring for Finis"""
	def __init__(self, **kwargs):
		super(Finished, self).__init__(**kwargs)
		self.cols = 1

		with self.canvas:
			Color(.8,.1,.6,1, mode="rgba")
			self.rect = Rectangle(size=(Window.size[0]*10, Window.size[1]*10))


		self.label = Label(text="Good Game ;) ", font_size=60, halign="center")
		self.add_widget(self.label)

		self.button = Button(text="Continue", font_size=40)
		self.button.bind(on_release=self.switch)
		self.add_widget(self.button)

	def switch(self, _):
		game.screen_manager.current = "Intro" 
		
class tictactoe(App):
	def build(self):
		self.screen_manager = ScreenManager()
		self.screen = Screen(name="Intro")
		self.screen.add_widget(Intro())
		self.screen_manager.add_widget(self.screen)

		self.screen = Screen(name="Board")
		self.screen.add_widget(Board())
		self.screen_manager.add_widget(self.screen)
		
		self.screen = Screen(name="Finished")
		self.screen.add_widget(Finished())
		self.screen_manager.add_widget(self.screen)

		return self.screen_manager

if __name__ == "__main__":
	game = tictactoe()
	game.run()

