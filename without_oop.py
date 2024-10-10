from turtle import Turtle, Screen
import time, random

DELAY_TIME = 0.12

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

coordinates = [[0, 0], [-20,0], [-40,0]]
squares = []

for coordinate in coordinates:
    square = Turtle("square")
    square.color("white")
    square.penup()
    square.goto(coordinate)
    squares.append(square)

def move(new_heading):
    x_cor = []
    y_cor = []
    for i in range(1, len(squares)):
        x_cor.append((squares[i-1].xcor()))
        y_cor.append(squares[i-1].ycor())
    
    
    squares[0].setheading(new_heading)
    squares[0].forward(20)
    x_cor = ([squares[0].xcor()] + x_cor)
    y_cor = ([squares[0].ycor()] + y_cor)
    global coordinates
    coordinates = [list(pair) for pair in zip(x_cor, y_cor)]
    
    
    for i, square in enumerate(squares):
        square.goto([x_cor[i], y_cor[i]])
    screen.update()

def apple_coordinates_creator():
    x_cor = random.randint(-14, 14) *20
    y_cor = random.randint(-14, 14) *20
    return x_cor, y_cor

def move_right():
    if squares[0].heading() != 180:
        move(0)

def move_left():
    if squares[0].heading() != 0:
        move(180)

def move_up():
    if squares[0].heading() != 270:
        move(90)
        
def move_down():
    if squares[0].heading() != 90:
        move(270)

def apple_collision_check():
    if squares[0].distance(apple) < 10:
        apple_coordinates = apple_coordinates_creator()
        while apple_coordinates in coordinates:
            apple_coordinates = apple_coordinates_creator()
        apple.goto(apple_coordinates)
        coordinates.append(coordinates[-1])
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(coordinates[-1])
        squares.append(square)


apple_coordinates = apple_coordinates_creator()
x_cor_apple = apple_coordinates[0]
y_cor_apple = apple_coordinates[1]
apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto([x_cor_apple,y_cor_apple])

screen.update()

screen.listen()
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

def game():
    while True:
        screen.update()
        
        apple_collision_check()
        move(squares[0].heading())
        apple_collision_check()
        
        if [squares[0].xcor(), squares[0].ycor()] in coordinates[1:]:
            break
        if abs(squares[0].xcor()) > 280 or abs(squares[0].ycor()) > 280:
            break
        
        print(squares[0].pos())
        
        time.sleep(DELAY_TIME)

while True:
    game()
    answer = screen.textinput("Game Over", "YOU LOST! YOUR SCORE WAS {score}. Would you like to play again?(Yes/No): ")
    if answer.lower() == "no":
        break
    
    screen.clear()
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    
    coordinates = [[0, 0], [-20,0], [-40,0]]
    squares = []

    for coordinate in coordinates:
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(coordinate)
        squares.append(square)
    
    apple_coordinates = apple_coordinates_creator()
    x_cor_apple = apple_coordinates[0]
    y_cor_apple = apple_coordinates[1]
    apple = Turtle("circle")
    apple.color("red")
    apple.penup()
    apple.goto([x_cor_apple,y_cor_apple])
    
    screen.listen()
    screen.onkey(move_right, "Right")
    screen.onkey(move_left, "Left")
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    
    screen.update()


screen.exitonclick()
print("Hello")
