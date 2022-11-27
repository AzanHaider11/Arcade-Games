import turtle
STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DIS = 25


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.cont = False

    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = turtle.Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for x in range(len(self.segments)-1, 0, -1):
            self.segments[x].goto(self.segments[x-1].pos())
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for part in self.segments:
            part.reset()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]