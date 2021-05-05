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
    sw_started = False
    sw_seconds = 0

    def on_start(self):
        Clock.schedule_interval(self.update, 0)

    def update(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
            
        self.root.ids.time.text = strftime("[b]%H[/b]: %M: %S")
        
        minutes, seconds = divmod(self.sw_seconds, 60)
        self.root.ids.stopwatch.text = (
            f"[b]{int(minutes):02}[/b]: {int(seconds)}.{int(seconds * 100 % 100)}"
        )

    def update_clock(self, nap):
        if self.sw_started:
            self.sw_seconds += nap

    def start_stop(self):
        self.root.ids.start_stop.text = "Start" if self.sw_started else "Stop"
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = "Start"
            self.sw_started = False

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
