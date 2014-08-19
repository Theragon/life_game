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
	for x in xrange(universe.x):
		#print('_x: ' + str(_x))
		#print('universe.x: ' + str(universe.x))
		for y in xrange(universe.y):
			#print('_y: ' + str(_y))
			#print('universe.y: ' + str(universe.y))
			print(universe.world[x][y]),
			if y == universe.y-1:
				print('')
			

def update():
	pass


def get_random(lower_bound, upper_bound):
	return random.randint(lower_bound, upper_bound)


def print_character(universe, x, y):
	for entity in universe.entities:
		if entity.x == x:
			if entity.y == y:
				print('x')



class Universe:
	def __init__(self, x, y):
		print('creating universe')
		self.x = x
		self.y = y
		#self.end_of_world = x - 1
		self.entities = self.create_entities()

		self.world = [['_' for i in xrange(y)] for j in xrange(x)]

	def make_world(self, x, y):
		world = []
		for row in range(x):
			world.append([])
			for column in range(y):
				grid[row].append(0)
		#for row in xrange(int(x)): world += [[0]*int(y)]
		return world

	def create_entities(self):
		entities = []
		for x in xrange(self.x):
			for y in xrange(self.y):
				rand = get_random(0,9)
				print('rand: ' + str(rand))
				if rand < 3:
					entity = Entity(x, y)
					print('creating entity at ' + str(x) + ',' + str(y))
					entities.append(entity)

		return entities

class Position:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.contains_entity = False

class Entity:
	def __init__(self, x, y):
		self.x = x
		self.y = y


if __name__ == '__main__':
	main()