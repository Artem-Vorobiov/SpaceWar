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

		# Boundary detection
		if self.xcor() > 290:
			self.setx(290)
			self.rt(60)

		if self.xcor() < -290:
			self.setx(-290)
			self.rt(60)

		if self.ycor() > 290:
			self.sety(290)
			self.rt(60)

		if self.ycor() < -290:
			self.sety(-290)
			self.rt(60)

	def is_collision(self, others):
		if (self.xcor() >= (others.xcor()-20)) and \
		(self.xcor() <= (others.xcor()+20)) and \
		(self.ycor() >= (others.ycor()-20)) and \
		(self.ycor() <= (others.ycor()+20)):
			return True
		else:
			return False

	def turn_left(self):
		self.lt(45)

	def turn_right(self):
		self.rt(45)

	def accelerate(self):
		self.speed += 1

	def decelerate(self):
		self.speed -= 1


class Enemy(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 6
		self.setheading(random.randint(0,360))



class Player(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 4
		self.lives = 3


class Game():
	def __init__(self):
		self.level = 1
		self.score = 0 
		self.state = 'playing'
		self.pen = turtle.Turtle()
		self.lives = 3 

	def drow_border(self):
		self.pen.speed(0)
		self.pen.color('white')
		self.pen.pensize(3)
		self.pen.penup()
		self.pen.goto(-300,300)
		self.pen.pendown()
		for side in range(4):
			self.pen.fd(600)
			self.pen.rt(90)
		self.pen.penup()
		self.pen.ht()



# Create my sprites
player = Player('triangle', 'white', 0, 0)
enemy  = Enemy('circle', 'red', -100, 0)
game   = Game()

game.drow_border()



turtle.listen()
turtle.onkey(player.turn_left, 'Left')
turtle.onkey(player.turn_right, 'Right')
turtle.onkey(player.accelerate, 'Up')
turtle.onkey(player.decelerate, 'Down')
while True:
	player.move()
	enemy.move()

	# check for a collision:
	if player.is_collision(enemy):
		x = random.randint(-250, 250)
		y = random.randint(-250, 250)
		enemy.goto(x,y)


time.sleep(5)















