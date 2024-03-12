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

# Pyglet Imports
from pyglet.window import Window, FPSDisplay
from pyglet.app import run


class MainWindow(Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window size
        self.width, self.height = self.get_size()

        # Checkpoint
        print(
            f"\n\t Application running"
            f"\n\t Width: {self.width}"
            f"\n\t Height: {self.height}"
            )

    def on_draw(self):
        window.clear()
        fps_display.draw()


if __name__ == '__main__':

    # Window properties
    window = MainWindow(
        caption="HydroPulse  <>  BMA1020 Challenge Assignment 1",
        width=1000,
        height=1000,
        resizable=False
    )
    fps_display = FPSDisplay(window)

    run()
