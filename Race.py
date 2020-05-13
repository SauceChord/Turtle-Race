from turtle import *
from random import randint
import time

class Racer():
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.turtle = None
    
    def ready(self, pos): 
        turtle = self.turtle or Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.color(self.color)
        turtle.shape('turtle')
        turtle.goto(pos)
        turtle.pendown()
        turtle.showturtle()
        self.turtle = turtle
    
    def spin(self):
        for turn in range(10):
            self.turtle.right(36)

    def go(self):
        self.turtle.forward(randint(1,5))

    def xpos(self):
        return self.turtle.xcor()

    def clear(self):
        self.turtle.clear()
        self.turtle.hideturtle()

    def victorydance(self):
        self.spin()
        self.spin()
        self.spin()
        self.spin()

class Track():
    def __init__(self, legs):
        self.legs = legs
        self.leg_distance = 20
        self.lane_height = 20
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.color('black')
        turtle.shape('arrow')
        self.turtle = turtle
    
    def draw(self, lanes):
        turtle = self.turtle
        turtle.speed(0)
        turtle.showturtle()
        turtle.penup()
        pos = (-self.leg_distance * self.legs / 2, self.lane_height * lanes / 2)
        turtle.goto(pos)
        
        for leg in range(self.legs):
            turtle.write(leg + 1, align='center')                        
            turtle.right(90) 
            for lane in range(lanes): 
                turtle.penup()
                turtle.forward(self.lane_height / 2)
                turtle.pendown()
                turtle.forward(self.lane_height / 2)
            turtle.penup()
            turtle.backward(lanes * self.lane_height)
            turtle.left(90)
            turtle.forward(self.leg_distance)

        turtle.hideturtle()
    
    def start_pos(self, lane, lanes):
        pos = (-self.leg_distance * self.legs / 2 - 20, self.lane_height * lanes / 2 - lane * self.lane_height - 2 * self.lane_height / 3)
        return pos
    
    def goal(self):
        return self.leg_distance * (self.legs - 1.5) / 2

class Race():
    def __init__(self, legs):
        self.track = Track(legs)
        self.racers = []
        self.winner = -1
        # text_turtle used for displaying winner name
        # not yet impl.
        self.text_turtle = Turtle()
        self.text_turtle.hideturtle()
        self.text_turtle.penup()
        self.text_turtle.goto(0, 0)
    
    def join(self, color, name):
        self.racers.append(Racer(color, name))

    def draw_track(self):
        self.track.draw(len(self.racers))
    
    def ready_set_go(self):
        # ready / set
        self.winner = -1
        num_racers = len(self.racers)
        for i in range(num_racers):
            startpos = self.track.start_pos(i, num_racers)
            self.racers[i].ready(startpos)
        for i in range(num_racers):
            self.racers[i].spin()

        # go
        while self.winner == -1:
            for i in range(num_racers):
                racer = self.racers[i]
                racer.go()
                if racer.xpos() > self.track.goal():
                    # subtle glitch, if two racers 
                    # cross line, one is picked 
                    # arbitrarily, which may look
                    # like the wrong racer won
                    # (Another racer came further)
                    self.winner = i 
        
    def honour_winner(self):
        # todo; write winners name above race track
        self.racers[self.winner].victorydance()
        time.sleep(2)

    def clear_racers(self):
        for racer in self.racers:
            racer.clear()