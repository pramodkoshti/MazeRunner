import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Runner")
wn.setup(700,700)
possible_direcetion = ["Left","Up","Right","Down"]

turtle.register_shape("Maze_Block.gif")
turtle.register_shape("player.gif")
turtle.register_shape("Enter.gif")
turtle.register_shape("Exit.gif")


class Pen(turtle.Turtle):    
    def __init__(self):        
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(10)

class Player(turtle.Turtle):    
    def __init__(self):        
        turtle.Turtle.__init__(self)
        self.shape("player.gif")
        self.penup()
        self.speed(1)
        self.direction = "Left"
        self.current_direction = possible_direcetion[0]       
    
    
    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        if(move_to_x,move_to_y) not in walls:            
            self.goto(move_to_x,move_to_y)
            self.direction = "Left"                        
        else:
            self.direction = "Right"
        self.Move()
        
    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        if(move_to_x,move_to_y) not in walls:            
            self.goto(move_to_x,move_to_y)
            self.direction = "Right"
        else:
            self.direction = "Down"
        self.Move()
        
    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        if(move_to_x,move_to_y) not in walls:
            self.direction = "Up"
            self.goto(move_to_x,move_to_y)               
        else:
            self.direction = "Down"
        self.Move()
        
    def go_left(self):
        move_to_x = self.xcor() -24
        move_to_y = self.ycor()
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)                        
        else:
            self.direction = "Up"
        self.Move()
        
    def Move(self):
        if(self.direction == "Left"):                        
            self.go_left()
        elif(self.direction == "Up"):
            self.go_up()
        elif(self.direction == "Right"):
            self.go_right()
        else:            
            self.go_down()                            
        
class In(turtle.Turtle):    
    def __init__(self):        
        turtle.Turtle.__init__(self)
        self.shape("Enter.gif")        
        self.penup()
        self.speed(0) 
        
class Out(turtle.Turtle):    
    def __init__(self):        
        turtle.Turtle.__init__(self)
        self.shape("Exit.gif")
        self.penup()
        self.speed(0)
        
levels = [""]

level_1 = ["XXXXXXXXXXXXXXXXXXXXXXXXX",
           "X              X XXXXXXXX",
           "X      XXXX             O",
           "XXX XX XXX       X XXXXXX",
           "X       XXXXX X  X  XX XX",
           "X X XX XXXXXXX      XXXXX",
           "X X XXX  XXXXX   XXXXXXXX",
           "X        XXXXXX XX   XXXX",
           "X X X XX XXXXXX X   XXXXX",
           "X XXX XX        XXX XXXXX",
           "X   X XXX  XX XX XX XXXXX",
           "X X X    XX      XX XXXXX",
           "X X X XXX    XXX   XXXXXX",
           "X  XX XXXX       XXXXXXXX",
           "X X X XXX  XXXXX  XXXXXXX",
           "X  XX XXXX XXXX  XXX    X",
           "XX           XXX XXXXXXXX",
           "XX XX XXXXXX XXX XXXXXXXX",
           "XX XX  XXXXX  XX     XXXX",
           "XX  XX  X XXXX   XX  XXXX",
           "XX  XX XXXXX   XXXX  XXXX",
           "X  XXX       X X XX    XX",
           "X   XX   XXX X      X   X",
           "XX         X           PX",
           "XXXXXXXXXXXXXXXXXXXXXXXIX"
          ]
levels.append(level_1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x *24)
            screen_y = 288 - (y*24)
            if(character == "X"):
                pen.goto(screen_x,screen_y)
                pen.shape("Maze_Block.gif")
                pen.stamp()                
                walls.append((screen_x,screen_y))
            if(character == "P"):
                player.goto(screen_x,screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))
            if(character == "O"):
                out.goto(screen_x,screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))
            if(character == "I"):
                inway.goto(screen_x,screen_y)                
                pen.stamp()
                walls.append((screen_x,screen_y))

pen = Pen()
player = Player()
inway = In()
out = Out()

walls = []

setup_maze(level_1)
player.Move()
# turtle.listen()
# turtle.onkey(player.go_left,"Left")
# turtle.onkey(player.go_down,"Down")
# turtle.onkey(player.go_right,"Right")
# turtle.onkey(player.go_up,"Up")
wn.tracer(0)

while True:
    wn.update()
    
turtle.done()        
