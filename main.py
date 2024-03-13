"""

    HydroPulse
    --------------------
    Challenge assignment
    BMA1020 - Mathematics for programming

    @author   :  Luna Sofie Bergh

    @date     :  12/03/2024

    @brief    :  Hydropulse is a Python-based application designed to simulate a dynamic grid of
                 interactive elements, akin to a water ripple effect. Primarily developed using
                 Pyglet and math libraries, it offers users a visually engaging experience through
                 smooth animations and responsive interactions.

    @features :  > Grid Simulation: Creates a dynamic grid of interactive elements.
                 > Mouse Interaction: Reacts to real-time mouse movements and clicks.
                 > Ripple Effect: Initiates ripple effects from selected elements.
                 > Interpolation: Ensures smooth transitions and visual effects.
                 > Platform Compatibility: Support for Windows, macOS, and Linux.

"""

# Module Imports
from Modules.grid import Grid

# Pyglet Imports
from pyglet.window import Window, FPSDisplay, mouse, key
from pyglet.resource import image
from pyglet.app import run


def user_exit(symbol):
    if symbol == key.ESCAPE:
        exit()


class MainWindow(Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid = Grid(self.width, self.height)
        self.grid.render(amount=20)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print(f"Left mouse button pressed at ({x}, {y})")
            self.grid.handle_interaction(x=x, y=y)

    def on_draw(self):
        self.clear()
        fps_display.draw()

        for ball in self.grid.balls:
            ball.shape.draw()


if __name__ == '__main__':

    # Window Properties
    window = MainWindow(
        caption="HydroPulse  <>  BMA1020 Challenge Assignment 1",
        width=1000,
        height=1000,
        resizable=False
    )
    window_width, window_height = window.get_size()
    window_loc_x, window_loc_y = window.get_location()

    # Window Icon
    image = image("Assets/Images/waterdrop.png")
    window.set_icon(image)

    # Window FPS
    fps_display = FPSDisplay(window)

    # Window Checkpoint
    print(
        f"\n\t Debug Checkpoint"
        f"\n\t ----------------"
        f"\n\t {window}"
        f"\n"
        f"\n\t Coordinate X: {window_loc_x}"
        f"\n\t Coordinate Y: {window_loc_y}"
        f"\n"
        f"\n\t Width: {window_width}"
        f"\n\t Height: {window_height}"
        f"\n"
        f"\n\t FPS: {fps_display}"
        f"\n\t Image: {image}"
    )

    run()
