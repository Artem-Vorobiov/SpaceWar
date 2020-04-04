# 	Turtle Graphics Game

import turtle 
import time 
import math
import random
import os
import time

turtle.fd(0)
turtle.speed(0)
turtle.bgcolor('black')
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(0)

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



class Ally (Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 8
		self.setheading(random.randint(0,360))

	def move(self):
		self.fd(self.speed)

		# Boundary detection
		if self.xcor() > 290:
			self.setx(290)
			self.lt(60)

		if self.xcor() < -290:
			self.setx(-290)
			self.lt(60)

		if self.ycor() > 290:
			self.sety(290)
			self.lt(60)

		if self.ycor() < -290:
			self.sety(-290)
			self.lt(60)




class Player(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.shapesize(stretch_wid = 0.6, stretch_len = 1.2 , outline = None)
		self.speed = 4
		self.lives = 3


class Missile(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.shapesize(stretch_wid = 0.2, stretch_len = 0.6, outline = None)
		self.speed   = 20
		self.status = 'ready'
		# self.goto(-1000,1000)

	def fire(self):
		if self.status ==  'ready':
			self.goto(player.xcor(), player.ycor())
			self.setheading(player.heading( ))
			self.status = 'firing'

	def move(self):

		if self.status == 'ready':
			self.goto(-1000, 1000)


		if self.status == 'firing':
			self.fd(self.speed) 

		# Border Check
		if self.xcor() < -290 or self.xcor() > 290 or \
			self.ycor() < - 290 or self.ycor() > 290:
			self.goto(-1000, 1000)
			self.status = 'ready'



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
		self.pen.pendown()

	def show_status(self):
		self.pen.undo( )
		msg = 'Score: %s' %(self.score)
		self.pen.penup()
		self.pen.goto(-300,310)
		self.pen.write(msg, font=("Arial", 16, "normal"))



# Create my sprites
player  = Player('triangle', 'white', 0, 0)
# enemy   = Enemy('circle', 'red', -100, 0)
missile = Missile('triangle', 'yellow', 0, 0)
# ally    = Ally('square', 'blue', 0, 0)
game    = Game()

enemies = []
for i in range(6):
	enemies.append(Enemy('circle', 'red', -100, 0))

allies = []
for i in range(6):
	allies.append(Ally('square', 'blue', 0, 0))

game.drow_border()
game.show_status()



turtle.listen()
turtle.onkey(player.turn_left, 'Left')
turtle.onkey(player.turn_right, 'Right')
turtle.onkey(player.accelerate, 'Up')
turtle.onkey(player.decelerate, 'Down')
turtle.onkey(missile.fire, 'space')
while True:
	turtle.update()
	time.sleep(0.03)

	player.move()
	# enemy.move()
	missile.move()
	# ally.mov e() 

	for enemy in enemies:
		enemy.move()
		# check for a collision with the player:
		if player.is_collision(enemy):
			x = random.randint(-250, 250)
			y = random.randint(-250, 250)
			enemy.goto(x,y)
			# Increase the score
			game.score += 100
			game.show_status()


		# Check for a collision between the missile and the enemy:
		if missile.is_collision(enemy):
			x = random.randint(-250, 250)
			y = random.randint(-250, 250)
			enemy.goto(x,y)
			missile.status = 'ready'
			# Increase the score
			game.score += 100
			game.show_status()

	for ally in allies:
		ally.move()

		# Check for a collision between the missile and the ally:
		if missile.is_collision(ally):
			x = random.randint(-250, 250)
			y = random.randint(-250, 250)
			ally.goto(x,y)
			missile.status = 'ready'
			# Decrease the score
			game.score -= 50
			game.show_status()



time.sleep(5)















 