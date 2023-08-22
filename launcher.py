import pygame
from pygame.locals import *
import sys

from menudicts import *
from screens import *
from guiboard import *
import copy

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WHITE = (255, 255, 255)
BLACK = (0,0,0)
FRAMES_PER_SECOND = 30

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,30)

main_menu = Menu2(window,'main',0,(20,280),['Easy','Medium','Hard'])
in_game_menu = Menu2(window,'in_game',0,(10,450),['Reset','Restart','Exit'])
loser_menu = Menu2(window,'loser',0,(10,400),['Restart'])
winner_menu = Menu2(window,'winner',0,(10,400),['Exit'])

font = pygame.font.SysFont(None,50)
width_label, height_label = font.size('Welcome to Sudoku')
welcome_text = SimpleTexto(window, (int((WINDOW_WIDTH-width_label)/2),int((WINDOW_HEIGHT-height_label)/2)-40), 'Welcome to Sudoku', BLACK,50)

font = pygame.font.SysFont(None,30)
width_label, height_label = font.size('Select Game Mode:')
gamemode_text = SimpleTexto(window, (int((WINDOW_WIDTH-width_label)/2),int((WINDOW_HEIGHT-height_label)/2)), 'Select Game Mode:', BLACK,30)

start_screen = Screen(window,[main_menu,welcome_text,gamemode_text])


width_label, height_label = font.size('Game Over')
game_over_text = SimpleTexto(window, (int((WINDOW_WIDTH-width_label)/2),int((WINDOW_HEIGHT-height_label)/2)), 'Game Over', BLACK,30)
loser_screen = Screen(window,[loser_menu,game_over_text])

width_label, height_label = font.size('Game Won')
game_won_text = SimpleTexto(window, (int((WINDOW_WIDTH-width_label)/2),int((WINDOW_HEIGHT-height_label)/2)), 'Game Won', BLACK,30)
winner_screen = Screen(window,[winner_menu,game_won_text])


screens = {'Start Screen': start_screen}



current_screen = 'Start Screen'


in_game_menu = Menu2(window,'entrada',0,(10,450),['Reset','Restart','Exit'])


screens = {'Start Screen': start_screen}



while True:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		screen_states = screens[current_screen].eventsScreen(event)

		if current_screen == 'Start Screen':
			start_screen_states = screen_states[main_menu]
			if True in start_screen_states.values():
				difficulty = list(start_screen_states.values()).index(True)
				board = Board(window, (20,20),int(30 + (difficulty)*10))
				board_copy = copy.deepcopy(board.boardcode)
				sudoku_screen = Screen(window,[board,in_game_menu])
				current_screen = 'Sudoku'
				screens[current_screen] = sudoku_screen

		elif current_screen == 'Sudoku':

			game_menu_states = screen_states[in_game_menu]
			sudoku_state = screen_states[board]

			if True in game_menu_states.values():

				chosen_option = list(game_menu_states.keys())[list(game_menu_states.values()).index(True)]

				if chosen_option == 'Exit':
					pygame.quit()
					sys.exit()	

				elif chosen_option == 'Reset':
					copy_of_copy = copy.deepcopy(board_copy)
					board = Board(window, (20,20),30 + (difficulty)*10,copy_of_copy)
					sudoku_screen = Screen(window,[board,in_game_menu])
					screens[current_screen] = sudoku_screen	
	
				elif chosen_option == 'Restart':
					current_screen = 'Start Screen'

			if sudoku_state != None:
				if sudoku_state:
					current_screen = 'Game Won'
					screens[current_screen] = winner_screen
				else:
					current_screen = 'Game Over'
					screens[current_screen] = loser_screen

		elif current_screen =='Game Over':
			loser_menu_states = screen_states[loser_menu]

			if True in loser_menu_states.values():
				current_screen = 'Start Screen'

		elif current_screen == 'Game Won':
			winner_menu_states = screen_states[winner_menu]

			if True in winner_menu_states.values():
					pygame.quit()
					sys.exit()	


	screens[current_screen].perFrameScreen()
	pygame.display.update()
	clock.tick(FRAMES_PER_SECOND)

