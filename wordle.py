# import the pygame module
from ast import Or
import time
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((300, 300))
screen_x, screen_y = screen.get_size()
pygame.display.set_caption('Worlde')

words_list = []
for i in open("words.txt", "r").read().split('\n'):
    if len(i) == 5:
        words_list.append(i)

words = []
temp_word = []
rectangles = [[],[],[],[],[],[]]
possible_letters = []
for i in range (97,123):
	possible_letters.append(chr(i))
current_row = 0
guesses = 0
end_word = words_list[random.randint(0,len(words_list))].strip()
# print(end_word)
FONT = pygame.font.SysFont("comicsans", 16)
canPress = True
isWon = False

background_colour = (255,255,255)
rect_color = (0,0,0)
green = (0,255,0)
yellow = (255,255,0)
white = (255,255,255)
black = (0,0,0)
gray = (211,211,211)


class Rectangle:
	def __init__(self,x ,y,color):
		self.x = x
		self.y = y
		self.color = color
		self.rect = pygame.Rect(x, y, screen_x/5, screen_x/6) 
	
	def draw(self):
		pygame.draw.rect(screen,self.color,self.rect)
	
	def __setitem__(self,color):
		self.color = color
		
'''
text = FONT.render(end_word, True, (0,0,255), (255,0,255))
		text_box = text.get_rect()
		text_box.center = ()
'''
def init_Rectangles():
	x_step = screen_x / 5
	y_step = screen_y / 6
	for r in range(6):
		for c in range(5):
			rectangles[r].append(Rectangle(c * x_step, r * y_step, white))

#Rectangle(c * x_step, r * y_step, green)

def text(word, row):
	step_x = screen_x / 5
	multiplier = .5
	for char in word:
		text = FONT.render(char, True, (0,0,0))
		text_box = text.get_rect()
		text_box.center = (step_x * multiplier, (row  + 0.5) * screen_y / 6)
		multiplier += 1
		screen.blit(text, text_box)

def draw_Lines():
	x_diff = screen_x / 5
	for i in range(0, screen_x, int(screen_x / 5)):	
		pygame.draw.line(screen, (0,0,0), (i, 0), (i, screen_y))

	for i in range(0,screen_y, int(screen_y / 6)):
		pygame.draw.line(screen,(0,0,0), (0, i), (screen_x, i))

def draw_Rects():
	for r in range(6):
		for c in range(5):
			rectangles[r][c].draw()

def checkWordExists(word):
	if str.lower(word) not in words_list:
		return False
	return True

def updateColors(row):
	word = str.lower(words[-1])
	letters = list(end_word) #find way to split word into array so I can make sure a letter isnt marked twice
	# print(letters) 

	# print(canPress)
	# print(word)
	# print(end_word)
	for i in range(5):
		#rectangles[row][i].color = green
		if word[i] in end_word and word[i] in letters:
			if word[i] == end_word[i]:
				rectangles[row][i].color = green
			else:
				rectangles[row][i].color = yellow
			letters.remove(word[i])
		else:
			rectangles[row][i].color = gray
			if word[i] in possible_letters:
				possible_letters.remove(word[i])
			

def changeColor(color):
	for r in range(6):
		for c in range(5):
			rectangles[r][c].color = color

def checkWin(word):
	global isWon
	isWon = str.lower(word.strip()) == str.lower(end_word.strip())




# Define the background colour
# using RGB color coding.

# Fill the background colour to the screen
#screen.fill(background_colour)

pygame.display.flip()
init_Rectangles()
# game loop

def reset():
	global words, temp_word, rectangles, current_row, guesses, canPress, running, end_word, isWon
	isWon = False
	words = []
	temp_word = []
	rectangles = [[],[],[],[],[],[]]
	current_row = 0
	guesses = 0
	end_word = words_list[random.randint(0,len(words_list))].strip()
	canPress = True
	running = True
	init_Rectangles()
	screen.fill(white)
	pygame.display.set_caption('Worlde')
	pygame.display.update()

running = True
while running:
	draw_Rects()
	row = 0
	for word in words:
		text(word, row)
		row += 1
	text(temp_word, current_row)
	draw_Lines()
	
	# for loop through the event queue
	for event in pygame.event.get():
	
		# Check for QUIT event	
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_BACKSPACE and len(temp_word) > 0 and canPress:
				temp_word.pop(-1)
			elif event.key == pygame.K_RETURN and len(temp_word) == 5 and checkWordExists(''.join(temp_word)):
				words.append(''.join(temp_word))
				temp_word = []
				guesses += 1
				current_row += 1
				updateColors(current_row - 1)
				canPress = not checkWin(words[-1])
				print(str.lower(" ".join(possible_letters)))
			elif event.key < 123 and event.key >= 97 and len(temp_word) < 5 and canPress:
				temp_word.append(str.upper(chr(event.key)))
			elif event.key == pygame.K_RSHIFT:
				reset()
			if isWon or guesses > 5:
				pygame.display.set_caption("The word was: " + end_word) 

	pygame.display.update()
print("The word was:" + end_word)

