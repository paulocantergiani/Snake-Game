import turtle
import time
import random

DELAY_TIME = 0.1
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SQUARE_SIZE = 20

class SnakeGame:
    def __init__(self):
        self.screen = self.setup_screen()
        self.snake = self.create_snake()
        self.apple = self.create_apple()
        self.score = 0
        self.direction = "right"
        self.setup_controls()

    def setup_screen(self):
        screen = turtle.Screen()
        screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        screen.bgcolor("black")
        screen.title("Snake Game")
        screen.tracer(0)
        return screen

    def create_snake(self):
        snake = []
        for i in range(4):
            segment = turtle.Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(-i * SQUARE_SIZE, 0)
            snake.append(segment)
        return snake

    def create_apple(self):
        apple = turtle.Turtle("circle")
        apple.color("red")
        apple.penup()
        self.move_apple(apple)
        return apple

    def move_apple(self, apple):
        while True:
            x = random.randint(-14, 14) * SQUARE_SIZE
            y = random.randint(-14, 14) * SQUARE_SIZE
            if [x, y] not in [(segment.xcor(), segment.ycor()) for segment in self.snake]:
                apple.goto(x, y)
                break

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(lambda: self.change_direction("right"), "Right")
        self.screen.onkey(lambda: self.change_direction("left"), "Left")
        self.screen.onkey(lambda: self.change_direction("up"), "Up")
        self.screen.onkey(lambda: self.change_direction("down"), "Down")

    def change_direction(self, new_direction):
        if new_direction == "right" and self.direction != "left":
            self.direction = "right"
        elif new_direction == "left" and self.direction != "right":
            self.direction = "left"
        elif new_direction == "up" and self.direction != "down":
            self.direction = "up"
        elif new_direction == "down" and self.direction != "up":
            self.direction = "down"

    def move_snake(self):
        head = self.snake[0]
        x, y = head.xcor(), head.ycor()

        if self.direction == "right":
            x += SQUARE_SIZE
        elif self.direction == "left":
            x -= SQUARE_SIZE
        elif self.direction == "up":
            y += SQUARE_SIZE
        elif self.direction == "down":
            y -= SQUARE_SIZE

        # Move the existing head to the new position
        head.goto(x, y)

        # Move the rest of the body
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i-1].xcor(), self.snake[i-1].ycor())

        if self.snake[0].distance(self.apple) < SQUARE_SIZE:
            self.move_apple(self.apple)
            self.score += 1
            # Add new segment
            new_segment = turtle.Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            self.snake.append(new_segment)

    def check_collision(self):
        head = self.snake[0]
        x, y = head.xcor(), head.ycor()
        
        # Wall collision
        if (abs(x) > (SCREEN_WIDTH / 2 - SQUARE_SIZE / 2) or
            abs(y) > (SCREEN_HEIGHT / 2 - SQUARE_SIZE / 2)):
            print(f"Wall collision detected: x={x}, y={y}")
            return True
        
        # Self collision (start checking from the 4th segment)
        for segment in self.snake[3:]:
            if head.distance(segment) < 10:
                print(f"Self collision detected at x={x}, y={y}")
                return True
        
        return False

    def reset_game(self):
        for segment in self.snake:
            segment.goto(1000, 1000)  # Move off-screen
        self.snake.clear()
        self.snake = self.create_snake()
        self.move_apple(self.apple)
        self.setup_controls()
        self.score = 0
        self.direction = "right"

    def game_loop(self):
        while True:
            self.screen.update()
            self.move_snake()
            
            if self.check_collision():
                print(f"Game over! Score: {self.score}")
                answer = self.screen.textinput("Game Over", f"YOU LOST! YOUR SCORE WAS {self.score}. Would you like to play again? (Yes/No): ")
                if answer and answer.lower() == "yes":
                    self.reset_game()
                else:
                    break
            
            # Add debug print for snake head position
            print(f"Snake head position: x={self.snake[0].xcor()}, y={self.snake[0].ycor()}")
            
            time.sleep(DELAY_TIME)

    def run(self):
        self.game_loop()
        self.screen.exitonclick()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()