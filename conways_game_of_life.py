#!/usr/bin/env python

import sys
import random
from array import array

def main():
	
	x = int(sys.argv[1])
	y = int(sys.argv[2])

	universe = Universe(x, y)
	
	#world = [[0 for i in xrange(x)] for j in xrange(y)]
	#world[0][4] = 5

	print('x: ' + str(x))
	print('y: ' + str(y))

	render(universe)
	

def render(universe):
	for _x in xrange(universe.x):
		#print('_x: ' + str(_x))
		#print('universe.x: ' + str(universe.x))
		for _y in xrange(universe.y):
			#print('_y: ' + str(_y))
			#print('universe.y: ' + str(universe.y))
			print(universe.world[_x][_y]),
			if _y == universe.y-1:
				print('')
			

def update():
	pass

class Universe:
	def __init__(self, x, y):
		print('creating universe')
		self.x = x
		self.y = y
		self.end_of_world = x - 1

		self.world = [['_' for i in xrange(y)] for j in xrange(x)]

	def make_world(self, x, y):
		world = []
		for row in range(x):
			world.append([])
			for column in range(y):
				grid[row].append(0)
		#for row in xrange(int(x)): world += [[0]*int(y)]
		return world


if __name__ == '__main__':
	main()