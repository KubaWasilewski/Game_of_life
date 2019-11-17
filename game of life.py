import pygame
import sys
import math
import keyboard
import numpy as np

#dead cell becomes alive when 3 neighbour cells are alive
#alive cell with 2,3 neighbours stays alive
#alive cell with 3+ neighbour alive cells dies
#alive cell with 1 or less alive neighbours dies
# j is x 
# i is y

WIDTH = 600
HEIGHT = 600
WHITE = (255,255,255)
BLACK = (0,0,0)
game_over = False
mouse_state = 0


pygame.init()

window = pygame.display.set_mode((WIDTH,HEIGHT))


grid = np.zeros((29,29))
sub_grid = np.zeros((29,29))
print(grid)


def draw_board(win):
	col = 29
	row = 29
	win.fill(BLACK)
	for i in range(row):
		for j in range(col): 
			pygame.draw.rect(win,WHITE,(i*(20+1),j*(20+1),20,20))	

def mutate(grid,sub_grid):
	neighbour_counter = 0
	for i in range(0,29):
		for j in range(0,29):
			if grid[i][j] == 1:
				try:
					if grid[i+1][j] == 1:	
						neighbour_counter += 1
						print('i+1')
				except:
					pass
				try:
					if grid[i-1][j] == 1:
						neighbour_counter += 1
						print('i-1')
				except:
					pass
				try:
					if grid[i][j-1] == 1:
						neighbour_counter += 1
						print('j-1')
				except:
					pass
				try:
					if grid[i][j+1] == 1:
						neighbour_counter += 1
						print('j+1')
				except:
					pass
				try:
					if grid[i+1][j+1] == 1:
						print('i+1 j+1')
						neighbour_counter += 1
				except:
					pass
				try:
					if grid[i+1][j-1] == 1:
						print('i+1 j-1')
						neighbour_counter += 1
				except:
					pass
				try:
					if grid[i-1][j+1] == 1:
						print('i-1 j+1')
						neighbour_counter += 1
				except:
					pass
				try:
					if grid[i-1][j-1] == 1:
						print('i-1 j-1')
						neighbour_counter += 1
				except:
					pass
				if neighbour_counter < 2:
					sub_grid[i][j] = 0
					print('less than 3')
					neighbour_counter = 0
				elif neighbour_counter > 3 :
					sub_grid[i][j] = 0
					neighbour_counter = 0
				else:
					sub_grid[i][j] = 1
					neighbour_counter = 0
			if grid[i][j] == 0:
				try:
					if grid[i+1][j] == 1:	
						neighbour_counter += 1
						print('i+1')
				except:
					pass
				try:
					if grid[i-1][j] == 1:
						neighbour_counter += 1
						print('i-1')
				except:
					pass
				try:
					if grid[i][j-1] == 1:
						neighbour_counter += 1
						print('j-1')
				except:
					pass
				try:
					if grid[i][j+1] == 1:
						neighbour_counter += 1
						print('j+1')
				except:
					pass
				try:
					if grid[i+1][j+1] == 1:
						print('i+1 j+1')
						neighbour_counter += 1
				except:
					pass
				try:
					if grid[i+1][j-1] == 1:
						print('i+1 j-1')
						neighbour_counter += 1
				except:
					pass
				try:
					if grid[i-1][j+1] == 1:
						print('i-1 j+1')
						neighbour_counter += 1
				except:
					pass
				try:
					if grid[i-1][j-1] == 1:
						print('i-1 j-1')
						neighbour_counter += 1
				except:
					pass
				if neighbour_counter == 3:
					sub_grid[i][j] = 1 
					neighbour_counter = 0
				else:
					sub_grid[i][j] = 0
					neighbour_counter = 0




	print('====================================')
	print(sub_grid)
	print('====================================')

	for i in range(0,29):
		for j in range(0,29):
			grid[i][j] = sub_grid[i][j]




def update_board(win,grid):
	for i in range(0,29):
		for j in range(0,29):
			if grid[j][i] == 0:
				pygame.draw.rect(win,(255,255,255),(i*21,j*21,20,20))
			elif grid[j][i] == 1:
				pygame.draw.rect(win,(0,0,0),(i*21,j*21,20,20))

draw_board(window)

pygame.display.flip()
while not game_over:
	x,y = pygame.mouse.get_pos()
	xpos = math.floor(x/21)
	ypos = math.floor(y/21)
	#print(window.get_at((xpos,ypos))[0])
	#print(x,y)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONUP:
			mouse_state = 0
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_state = 1
		if mouse_state == 1:
			pygame.draw.rect(window,BLACK,(xpos*21,ypos*21,20,20))
			pygame.display.flip()
			grid[ypos,xpos]=1
			print('----------------------------')
			print(grid)
			print('----------------------------')
		if keyboard.is_pressed('tab'):
			mutate(grid,sub_grid)
			print('+++++++++++++++++++++++++++++')
			print(grid)
			print('+++++++++++++++++++++++++++++')			
			update_board(window,grid)
			pygame.display.flip()

		





#145,242 right one	
#155,240 right one
#173,237 right one
#195,238 right one 
#195,259 down one
