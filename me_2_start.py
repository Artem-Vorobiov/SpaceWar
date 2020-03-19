# Borders, Object, listen(), move down if border cange direction to 180 degrees.

# 	Turtle Graphics Game

import turtle 
import time 
import math
import random
import os

# Some useful variables
speed 		= 3
shapes =  ['triangle','square', 'circle']
colors =  ['darkorange', 'black', 'red', 'white', 'purple']
player =  []
missile = []
# friction 	= 0.98


# Set up the Screen
def screen_here():
	global wn
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
	for unit in range(5):
		unit = turtle.Turtle()
		# unit.color(colors[random.randint(0,4)])
		unit.color('red')
		unit.shape('circle')
		unit.penup()				# remove the Trace
		unit.setposition(random.randint(-280,280),random.randint(-100, 90))
		unit.speed(0)
		unit.right(random.randint(55,125))
		player.append(unit)

def player_ship():
	global ship
	ship = turtle.Turtle()
	ship.color('black')
	ship.shape('triangle')
	ship.penup()
	ship.speed(0)


def turnleft():
	ship.left(20)


def turnright():
	ship.right(20)

def incresespeed():
	global speed
	speed += 1




def boundary_checking(val):
	if type(val) == list:

		for unit in val:
			unit.forward(8)
			if unit.ycor() > 300:
				print('TOP BEFORE->',  unit.heading())
				if unit.heading() > 90:
					print('IF')
					unit.right(180 + 2*abs(90 - unit.heading()))
				else:
					print('ELSE')
					unit.right(180 - 2*abs(90 - unit.heading()))
				print('TOP AFTER->',  unit.heading())



			elif unit.ycor() < -300:
				# print('BOTTOM ->',  player.heading())
				if unit.heading() > 90:
					unit.right(180 + 2*abs(90 - unit.heading()))
				else:
					unit.right(180 - 2*abs(90 - unit.heading()))



			if unit.xcor() > 300:
				# print('LEFT BEFORE ->',  player.heading())
				if unit.heading() > 180:
					unit.right(180 + 2*abs(180 - unit.heading()))
				else:
					unit.right(180 - 2*abs(180 - unit.heading()))
				# player.right(180)
				# print('LEFT AFTER ->',  player.heading())


			if unit.xcor() < -300 :
				# print('LEFT BEFORE ->',  player.heading())
				if unit.heading() > 180:
					unit.right(180 + 2*abs(180 - unit.heading()))
				else:
					unit.right(180 - 2*abs(180 - unit.heading()))
				# player.right(180)
				# print('LEFT AFTER ->',  player.heading())
	else:
		ship.forward(speed)
		if ship.ycor() > 300:
			if ship.heading() > 90:
				ship.right(180 + 2*abs(90 - ship.heading()))
			else:
				ship.right(180 - 2*abs(90 - ship.heading()))



		elif ship.ycor() < -300:
			if ship.heading() > 90:
				ship.right(180 + 2*abs(90 - ship.heading()))
			else:
				ship.right(180 - 2*abs(90 - ship.heading()))



		if ship.xcor() > 300:
			if ship.heading() > 180:
				ship.right(180 + 2*abs(180 - ship.heading()))
			else:
				ship.right(180 - 2*abs(180 - ship.heading()))


		if ship.xcor() < -300 :
			if ship.heading() > 180:
				ship.right(180 + 2*abs(180 - ship.heading()))
			else:
				ship.right(180 - 2*abs(180 - ship.heading()))
				
def blast():
	ship.color(colors[random.randint(0,4)])
	global missile
	vector = ship.heading()
	blast = turtle.Turtle()
	blast.color('white')
	blast.shape('classic')
	blast.penup()
	blast.setposition(ship.xcor(),ship.ycor())
	blast.speed(0)
	blast.setheading(vector)
	missile.append(blast)




def if_collision(blasts_all, units):
	for b in blasts_all:
		for u in units:
			try:
				dis = b.distance(u.xcor(), u.ycor())
				# print('\n\n\t\t ---> ', dis)
				if dis <= 20.0:
					print('\n\n --->>> BBBAAAAMMMM \n\n')
					b.hideturtle()
					u.hideturtle()
					blasts_all.remove(b)
					units.remove(u)
			except:
				pass 


def boundary_missile_ch(smth):
	for b in smth:
		if b.ycor() > 300:
			b.hideturtle()
			smth.remove(b)

		elif b.ycor() < -300:
			b.hideturtle()
			smth.remove(b)

		elif b.xcor() > 300:
			b.hideturtle()
			smth.remove(b)

		elif b.xcor() < -300:
			b.hideturtle()
			smth.remove(b)







# Set up keyboard bindings
def listen_keyboard():
	
	turtle.listen()
	# turtle.onkey(www, 'Down')
	turtle.onkey(turnleft, 'Left')
	turtle.onkey(turnright, 'Right')
	turtle.onkey(incresespeed, 'Up')
	turtle.onkey(blast, 'space')
######################### 		Start the game  	#########################
#########################							#########################
screen_here()
draw_borders()
player_ship()
main_object()
listen_keyboard()


# if_collision()

print('LAPS')

while True:
	# плюс добавить Хединг
	wn.update()
	boundary_checking(player)
	boundary_checking(ship)
	boundary_missile_ch(missile)
	if_collision(missile,player)
	for b in missile:
		b.forward(7)
	



		# # Boundary Checking
		# if unit.ycor() > 300:
		# 	print('TOP BEFORE->',  unit.heading())

		# 	if unit.heading() > 90:
		# 		print('IF')
		# 		unit.right(180 + 2*abs(90 - unit.heading()))

		# 	else:
		# 		print('ELSE')
		# 		unit.right(180 - 2*abs(90 - unit.heading()))
		# 	print('TOP AFTER->',  unit.heading())


		# elif unit.ycor() < -300:
		# 	# print('BOTTOM ->',  player.heading())

		# 	if unit.heading() > 90:
		# 		unit.right(180 + 2*abs(90 - unit.heading()))
		# 	else:
		# 		unit.right(180 - 2*abs(90 - unit.heading()))



		# if unit.xcor() > 300:
		# 	# print('LEFT BEFORE ->',  player.heading())
		# 	if unit.heading() > 180:
		# 		unit.right(180 + 2*abs(180 - unit.heading()))
		# 	else:
		# 		unit.right(180 - 2*abs(180 - unit.heading()))
		# 	# player.right(180)
		# 	# print('LEFT AFTER ->',  player.heading())


		# if unit.xcor() < -300 :
		# 	# print('LEFT BEFORE ->',  player.heading())
		# 	if unit.heading() > 180:
		# 		unit.right(180 + 2*abs(180 - unit.heading()))
		# 	else:
		# 		unit.right(180 - 2*abs(180 - unit.heading()))
		# 	# player.right(180)
		# 	# print('LEFT AFTER ->',  player.heading())

































time.sleep(5)