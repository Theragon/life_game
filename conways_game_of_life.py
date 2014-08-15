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
		for _y in xrange(universe.y):
			print(universe.world[_x][_y]),
			if _y == universe.end_of_world:
				print('')

def maxItemLength(a):
    maxLen = 0
    rows = len(a)
    cols = len(a[0])
    for row in xrange(rows):
        for col in xrange(cols):
            maxLen = max(maxLen, len(str(a[row][col])))
    return maxLen


def update():
	pass

class Universe:
	def __init__(self, x, y):
		print('creating universe')
		self.x = x
		self.y = y
		self.end_of_world = x - 1

		self.world = [[0 for i in xrange(x)] for j in xrange(y)]

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