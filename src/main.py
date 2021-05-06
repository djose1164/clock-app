"""
A simple clock app with some basical features, these are: stop and reset
a timer.

author:
    djose1164
"""

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

from time import strftime

kivy.require("1.11.1")


class ClockApp(App):
    """Here's where the execution starts

    Args:
        App (App): The app class to inheretance.
    """

    # To know when the clock is running or stopped.
    sw_started: bool = False
    # The seconds to show in the timer.
    sw_seconds: bool = 0

    def on_start(self):
        """Start to counting the hours, minutes, and seconds.

        This method will be called automatically after
        the build method has finished. This will update the current time.
        """
        Clock.schedule_interval(self.update, 0)

    def update(self, nap):
        """To update the time show in the clock.

        Args:
            nap (number): The time suministrated fro Clock.schedule_interval(self)
        """

        # If the clock is already running; update the time.
        if self.sw_started:
            self.sw_seconds += nap

        # Show the updated time in the clock.
        self.root.ids.time.text = strftime("[b]%H[/b]: %M: %S")

        # For the timer; assign the minutes and seconds.
        minutes, seconds = divmod(self.sw_seconds, 60)
        # Update the stopwatch (timer).
        self.root.ids.stopwatch.text = (
            f"[b]{int(minutes):02}[/b]: {int(seconds)}.{int(seconds * 100 % 100)}"
        )

    def start_stop(self):
        """To start or stop the stopwatch."""
        # If the clock is already running; Start will be diplayed, otherwise Stop.
        self.root.ids.start_stop.text = "Start" if self.sw_started else "Stop"
        # If the stopwatch was running; will be chante to False, otherwise True.
        self.sw_started = not self.sw_started

    def reset(self):
        """Set the stopwatch to count from 0 again."""
        # If the clock is already running, it can be reseted.
        if self.sw_started:
            self.root.ids.start_stop.text = "Start"
            self.sw_started = False

        # Put the counter to 0.
        self.sw_seconds = 0


if __name__ == "__main__":
    Window.clearcolor = get_color_from_hex("#101216")

    LabelBase.register(
        name="Roboto",
        fn_regular="fonts/roboto/Roboto-Thin.ttf",
        fn_bold="fonts/roboto/Roboto-Medium.ttf",
    )

    app = ClockApp()
    app.run()
