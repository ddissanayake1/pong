#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 19:10:33 2020

@author: dylandissanayake
"""


import turtle



wn = turtle.Screen()
wn.title("Dyl's Pong")
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Scoring
score_a = 0
score_b = 0

hit_counter=0

#Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0) # Speed of animation
paddle_a.shape("square") # Default size is 20x20 pixels
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # Stretch object by x5
paddle_a.color('green')
paddle_a.penup() # Turtles draw a line when they move, penup() stops this
paddle_a.goto(-350,0) # Coordinates


#Paddle B

paddle_b = turtle.Turtle()
paddle_b = turtle.Turtle()
paddle_b.speed(0) # Speed of animation
paddle_b.shape("square") # Default size is 20x20 pixels
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # Stretch object by x5
paddle_b.color('green')
paddle_b.penup() # Turtles draw a line when they move, penup() stops this
paddle_b.goto(350,0)

#Ball

ball = turtle.Turtle()
ball = turtle.Turtle()
ball.speed(0) # Speed of animation
ball.shape("circle") # Default size is 20x20 pixels
ball.color('red')
ball.penup() # Turtles draw a line when they move, penup() stops this
ball.goto(0,0)

ball.dx = 2 #ball moves 2 pixels at a time (dx and dy means change in x and y)
ball.dy = 2

# Pen for scoreboard

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

#Functions
#Paddle A functions

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
#Paddle B functions
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
#Assign functions to keyboard strokes
    
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


#Main game loop

while True:
    wn.update()
    

    #Ball movement
    ball.setx(ball.xcor() + ball.dx) #Each time loop is run through ball moves dx and dy
    ball.sety(ball.ycor() + ball.dy)
    
    #Border detection
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #Reverse direction of ball movement if hits border
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = 2 #Reset speed due to speed up
        ball.dy = 2 #Reset speed due to speed up
        ball.dx *= -1 #Reverse direction of ball movement if hits border, remove # if speed up is removed
        score_a += 1
        pen.clear()
        pen.penup()
        pen.goto(0,260)
        pen.color("white")
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        hit_counter=0
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = 2 #Reset speed due to speed up
        ball.dy = 2 #Reset speed due to speed up
        ball.dx *= -1 #Reverse direction of ball movement if hits border, remove # if speed up is removed
        score_b += 1
        pen.clear()
        pen.penup()
        pen.goto(0,260)
        pen.color("white")
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        hit_counter=0
        
    #Paddle ball collision
    if 350 > ball.xcor() > 340 and paddle_b.ycor()+60 > ball.ycor() > paddle_b.ycor()-60:
        ball.setx(340)
#        if abs(ball.dx) < 9: # Stop ball glitching through the paddle
#            ball.dx += 1 #Speed up each bat
#            if ball.dy < 0: # Speed up but accomodate + or - values of ball.dy due to border collisions
#                ball.dy -= 1
#            else:
#                ball.dy += 1
        ball.dx *= -1
        hit_counter += 1
        if hit_counter > 4: # Hot streak text
            pen.clear()
            pen.penup()
            pen.goto(0,220)
            pen.color("red")
            pen.write("{} HIT STREAK!".format(hit_counter), align="center", font=("Courier", 24, "normal"))
            pen.penup()         # Must repeat scoreboard as pen.clear() removes it 
            pen.goto(0,260)
            pen.color("white")
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
       
    if -350 < ball.xcor() < -340 and paddle_a.ycor()+60 > ball.ycor() > paddle_a.ycor()-60:
        ball.setx(-340)
        if abs(ball.dx) < 9: # Stop ball glitching through the paddle
            ball.dx -= 1 #Speed up each bat
            if ball.dy < 0: # Speed up but accomodate + or - values of ball.dy due to border collisions
                ball.dy -= 1
            else:
                ball.dy += 1
        ball.dx *= -1
        hit_counter += 1
        if hit_counter > 4: # Hot streak text
            pen.clear()
            pen.penup()
            pen.goto(0,220)
            pen.color("red")
            pen.write("{} HIT STREAK!".format(hit_counter), align="center", font=("Courier", 24, "normal"))
            pen.penup()         # Must repeat scoreboard as pen.clear() removes it
            pen.goto(0,260)
            pen.color("white")
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    #Paddle border detection
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    
        
    
turtle.done()        
wn.bye()