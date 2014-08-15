#!/usr/bin/env python

import sys
import random
from array import array

def main():
	
	x = int(sys.argv[1])
	y = int(sys.argv[2])

	break_line = x - 1
	
	world = [[0 for i in xrange(x)] for j in xrange(y)]
	world[0][4] = 5

	print('x: ' + str(x))
	print('y: ' + str(y))

	for _x in xrange(x):
		for _y in xrange(y):
			print(world[_x][_y])
			if _y == break_line:
				print('')

def render(universe):
	a = []
	for i in xrange(3):
		a.append([])
		for j in xrange(3):
			a[i].append(i+j)

	#rows
	for i in xrange(3):
		
		#columns
		for j in xrange(3):
			if(i % 3 == 0):
				print('')
			else:
				print(a[i][j]),

def maxItemLength(a):
    maxLen = 0
    rows = len(a)
    cols = len(a[0])
    for row in xrange(rows):
        for col in xrange(cols):
            maxLen = max(maxLen, len(str(a[row][col])))
    return maxLen


def print2dList(a):
	if (a == []):
		# So we don't crash accessing a[0]
		print []
		return
	rows = len(a)
	cols = len(a[0])
	fieldWidth = maxItemLength(a)
	#print "[ ",
	for row in xrange(rows):
		if (row > 0): print "\n  ",
		#print "[ ",
		for col in xrange(cols):
			if (col > 0): print ",",
			# The next 2 lines print a[row][col] with the given fieldWidth
			format = "%" + str(fieldWidth) + "s"
			print format % str(a[row][col]),
		#print "]",
	#print "]"


def update():
	pass

class Universe:
	def __init__(self, x, y):
		print('creating universe')
		self.x = x
		self.y = y

		#self.world = self.make_world(x, y)

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