# Borders, Object, listen(), move down if border cange direction to 180 degrees.

# 	Turtle Graphics Game

import turtle 
import time 
import math
import random
import os

# Some useful variables
speed 		= 2.5
# friction 	= 0.98


# Set up the Screen
def screen_here():
	wn = turtle.Screen()
	wn.bgcolor('lightgreen')
	wn.tracer(3)  


# Draw border
def draw_borders():
	mypen = turtle.Turtle()
	mypen.penup()
	mypen.setposition(-300,-300)
	mypen.pendown()
	mypen.pensize(4)
	for side in range(4):
		mypen.forward(600)
		mypen.left(90)
	mypen.hideturtle()


# Create a main object
def main_object():
	global player
	player = turtle.Turtle()
	player.color('darkorange')
	player.shape('circle')
	player.penup()				# remove the Trace
	player.speed(0)
	player.right(random.randint(0,360))


def turnleft():
	player.left(10)


def turnright():
	player.right(10)

def incresespeed():
	global speed
	speed += 1

# Set up keyboard bindings
def listen_keyboard():
	turtle.listen()
	left  = turtle.onkey(turnleft, 'Left')
	right = turtle.onkey(turnright, 'Right')
	turtle.onkey(incresespeed, 'Up')
	



######################### 		Start the game  	#########################
#########################							#########################
screen_here()
draw_borders()
main_object()
listen_keyboard()
print('LAPS')

while True:
	# плюс добавить Хединг
	player.forward(speed)


	# Boundary Checking
	if player.ycor() > 300:
		# print('TOP BEFORE->',  player.heading())

		if player.heading() > 90:
			# print('IF')
			player.right(180 + 2*abs(90 - player.heading()))

		else:
			# print('ELSE')
			player.right(180 - 2*abs(90 - player.heading()))
		# print('TOP AFTER->',  player.heading())


	elif player.ycor() < -300:
		# print('TOP BEFORE->',  player.heading())

		if player.heading() > 270:
			# print('IF')
			player.right(180 + 2*abs(270 - player.heading()))
		else:
			# print('ELSE')
			player.right(180 - 2*abs(270 - player.heading()))
		# print('TOP AFTER->',  player.heading())



	if player.xcor() > 300:
		# print('LEFT BEFORE ->',  player.heading())
		if player.heading() > 180:
			player.right(180 + 2*abs(180 - player.heading()))
			# print('IF')
		else:
			player.right(180 - 2*abs(180 - player.heading()))
			# print('ELSE')
		# player.right(180)
		# print('LEFT AFTER ->',  player.heading())


	if player.xcor() < -300 :
		# print('LEFT BEFORE ->',  player.heading())
		if player.heading() > 180:
			player.right(180 + 2*abs(180 - player.heading()))
			# print('IF')
		else:
			player.right(180 - 2*abs(180 - player.heading()))
			# print('ELSE')
		# player.right(180)
		# print('LEFT AFTER ->',  player.heading())

































time.sleep(5)