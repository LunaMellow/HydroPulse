"""

    Grid Module
    ------------
    Contains classes and functions related to managing the grid of balls.

"""

# Pyglet imports
from pyglet.graphics import Batch
from pyglet.shapes import Circle


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.balls = []

    def add_ball(self, ball):
        self.balls.append(ball)

    def remove_ball(self, ball):
        self.balls.remove(ball)

    def update(self):
        for ball in self.balls:
            ball.update()

    def render(self, amount):
        radius = min(self.width, self.height) // (amount * 4)
        distance_x = self.width // (amount + 1)
        distance_y = self.height // (amount + 1)

        for i in range(amount):
            x = (i + 1) * distance_x
            for j in range(amount):
                y = (j + 1) * distance_y
                ball = Ball(x, y, radius)
                self.add_ball(ball)

    def handle_interaction(self, x, y):
        clicked_ball = None

        for ball in self.balls:
            if (ball.x - ball.radius <= x <= ball.x + ball.radius
                    and ball.y - ball.radius <= y <= ball.y + ball.radius):
                clicked_ball = ball
                break

        if clicked_ball:
            clicked_ball.interaction("active")

            range_multiplier = 50  # Range multiplier for surrounding balls
            range_x = range_multiplier * self.width / len(self.balls)
            range_y = range_multiplier * self.height / len(self.balls)

            # Change color of surrounding balls
            for ball in self.balls:
                if (abs(ball.x - clicked_ball.x) <= range_x
                        and abs(ball.y - clicked_ball.y) <= range_y):
                    ball.interaction("active")


class Ball:
    batch = Batch()

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (255, 255, 255)
        self.state = "idle"  # Default state

        self.shape = Circle(
            x=x,
            y=y,
            radius=radius,
            color=self.color,
            segments=6,
            batch=Ball.batch
        )

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_color(self, color):
        self.color = color

    def interaction(self, state):
        if state == "idle":
            self.shape.color = (255, 255, 255)
        elif state == "active":
            self.shape.color = (255, 0, 0)

