"""

    Grid Module
    ------------
    Contains classes and functions related to managing the grid of balls.

"""

# Math imports
from math import pi, cos, sin

# Pyglet imports
from pyglet.graphics import Batch
from pyglet.shapes import Circle
from pyglet.clock import unschedule, schedule_interval

# Module imports
from Modules.util import lerp


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.balls = []

    def add_ball(self, ball):
        self.balls.append(ball)

    def render(self, amount):
        radius = min(self.width, self.height) // (amount * 2)
        distance_x = self.width // amount
        distance_y = self.height // amount

        for i in range(amount):
            x = (i + 0.5) * distance_x
            for j in range(amount):
                y = (j + 0.5) * distance_y
                ball = Ball(x, y, radius)
                self.add_ball(ball)

    def update(self, dt):
        for ball in self.balls:
            ball.update(dt)

    def handle_click(self, x, y, range_multiplier):
        clicked_ball = next((ball for ball in self.balls if
                             ball.x - ball.radius <= x <= ball.x + ball.radius and
                             ball.y - ball.radius <= y <= ball.y + ball.radius), None)

        if clicked_ball:
            clicked_ball.click(self, range_multiplier)

    def handle_interaction(self, x, y):
        for ball in self.balls:
            if (ball.x - ball.radius <= x <= ball.x + ball.radius
                    and ball.y - ball.radius <= y <= ball.y + ball.radius):
                ball.interaction("active")
                break


class Ball:
    batch = Batch()

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.initial_x = x
        self.initial_y = y
        self.start_x = x
        self.start_y = y

        self.radius = radius

        self.color = (49, 0, 71)
        self.target_color = (49, 0, 71)
        self.start_color = None

        self.state = "idle"
        self.interpolation_duration = 0.4
        self.interpolation_timer = 0.0
        self.interpolation_intensity = 5.0

        self.shape = Circle(
            x=x,
            y=y,
            radius=radius,
            color=self.color,
            segments=20,
            batch=Ball.batch
        )

    def update(self, dt):
        if self.state in {"active"}:
            self.interpolation_timer += dt
            t = self.interpolation_timer / self.interpolation_duration
            if t <= 1.0:
                angle = t * 2 * pi
                interpolation_x = sin(angle) * self.interpolation_intensity
                interpolation_y = cos(angle) * self.interpolation_intensity
                self.x = self.initial_x + interpolation_x
                self.y = self.initial_y + interpolation_y
                self.shape.x = self.x
                self.shape.y = self.y
            else:
                self.state = "idle"
                self.x = self.start_x
                self.y = self.start_y
                self.shape.x = self.x
                self.shape.y = self.y

    def click(self, grid, range_multiplier):
        for ball in grid.balls:
            distance_from_clicked = ((self.initial_x - ball.x) ** 2 +
                                     (self.initial_y - ball.y) ** 2) ** 0.5
            if distance_from_clicked <= range_multiplier * self.radius:
                ball.interaction("active")
                ball.interpolate_color(0)

    def interaction(self, state):
        if state == "active":
            self.target_color = (150, 20, 208)
        elif state == "idle":
            self.target_color = (49, 0, 71)

        if self.state != state:
            self.start_color = self.shape.color
            self.state = state
            self.interpolation_timer = 0.0
            schedule_interval(self.interpolate_color, 1 / 60.0)
        else:
            self.interpolation_timer = 0.0

    def interpolate_color(self, dt):
        t = min(1.0, self.interpolation_timer / self.interpolation_duration)
        if self.state == "active":
            start_color = self.start_color
            target_color = self.target_color
        else:
            start_color = self.target_color
            target_color = self.start_color

        current_color = (
            int(lerp(start_color[0], target_color[0], t)),
            int(lerp(start_color[1], target_color[1], t)),
            int(lerp(start_color[2], target_color[2], t))
        )

        self.shape.color = current_color

        if t >= 1.0:
            unschedule(self.interpolate_color)
