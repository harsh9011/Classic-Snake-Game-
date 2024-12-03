from turtle import Turtle,Screen
START_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP =90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

# to create a snake
    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)


    def add_segment(self,position):
        new_segments = Turtle("square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)


    def extend(self):
        self.add_segment(self.segments[-1].position())






# to move the snake
    def move(self):
        # logic
        for seg_num in range(len(self.segments) - 1, 0, -1):  # 1,2,3
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # to move snake up

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)











