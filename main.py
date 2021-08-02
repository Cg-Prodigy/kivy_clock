from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import Clock
from kivy.properties import ObjectProperty
import time


class ClockLayout(BoxLayout):
    l_time = ObjectProperty(None)


class ClockApp(App):
    s_seconds = 0
    s_start = False

    def on_start(self):
        Clock.schedule_interval(self.time_val, 0)

    def time_val(self, nap):
        if self.s_start:
            self.s_seconds += nap
        m, s = divmod(self.s_seconds, 60)
        self.root.ids.time.text = time.strftime("%H:%M:%S")
        self.root.ids.s_time.text = "%02d:%02d:%02d" % (
            int(m),
            int(s),
            int(s * 100 % 100),
        )

    def start_counting(self):
        self.s_start = not self.s_start
        self.root.ids.start_button.text = "PAUSE" if self.s_start else "START"

    def stop_counting(self):
        if self.s_start:
            self.s_start = False
        self.s_seconds = 0


if __name__ == "__main__":
    LabelBase.register(
        name="Roboto",
        fn_bold="fonts/Roboto-Bold.ttf",
        fn_italic="fonts/Roboto-Italic.ttf",
        fn_regular="fonts/Roboto-Regular.ttf",
        fn_bolditalic="fonts/Roboto-BoldItalic.ttf",
    )
    Window.clearcolor = get_color_from_hex("#10434a")
    ClockApp().run()
    print(ClockApp().s_seconds)
