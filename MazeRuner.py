import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Runner")
wn.setup(700,700)

class Pen(turtle.Turtle):    
    def __init__(self):        
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):    
    def __init__(self):        
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        
    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 24)
    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 24)
    def go_right(self):
        self.goto(self.xcor() + 24, self.ycor())
    def go_left(self):
        self.goto(self.xcor() - 24, self.ycor())
        
class In(turtle.Turtle):    
    def __init__(self):        
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("Red")
        self.penup()
        self.speed(0) 
        
class Out(turtle.Turtle):    
    def __init__(self):        
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("Green")
        self.penup()
        self.speed(0)
        
levels = [""]

level_1 = ["XIXXXXXXXXXXXXXXXXXXXXXXX",
           "XP XXXXXXX          XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X                        ",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX          XXXXX",
           "X  XXXXXXX  XXX XXXXXXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "X  XXXXXXX  XX      XXXXX",
           "XXXXXXXXXXXXXXXXXXXOXXXXX"
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
                pen.stamp()
            if(character == "P"):
                player.goto(screen_x,screen_y)
                pen.stamp() 
            if(character == "O"):
                out.goto(screen_x,screen_y)
                pen.stamp()
            if(character == "I"):
                inway.goto(screen_x,screen_y)
                pen.stamp()

pen = Pen()
player = Player()
inway = In()
out = Out()

setup_maze(level_1)

turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_down,"Down")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
wn.tracer(0)

while True:
    wn.update()
    
turtle.done()        