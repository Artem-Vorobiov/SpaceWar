# 	Turtle Graphics Game

import turtle 
import time 
import math
import random
import os

turtle.fd(0)
turtle.speed(0)
turtle.bgcolor('black')
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)

class Sprite(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 1

	def move(self):
		self.fd(self.speed)

	def turn_left(self):
		self.lt(45)

	def turn_right(self):
		self.rt(45)

	def accelerate(self):
		self.speed += 1

	def decelerate(self):
		self.speed -= 1


class Player(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 4
		self.lives = 3

# Create my sprites
player = Player('triangle', 'white', 0, 0)



turtle.listen()
turtle.onkey(player.turn_left, 'Left')
turtle.onkey(player.turn_right, 'Right')
turtle.onkey(player.accelerate, 'Up')
turtle.onkey(player.decelerate, 'Down')
while True:
	player.move()


time.sleep(5)
