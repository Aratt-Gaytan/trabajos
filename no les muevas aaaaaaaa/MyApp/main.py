import kivy

from kivy.app import App
from kivy.uix.button import Button

from functools import partial




class MainApp(App):
    def disable(self, instance, *args):
        instance.disabled = True
        instance.size_hint = (.25,.18)
        instance.pos = (300,300)
        instance.font_size = "30"
        instance.text = "mori"

    def build(self):
    	mybtn = Button(text = "puchame")
    	mybtn.bind(on_press = partial(self.disable, mybtn))
    	return mybtn


if __name__ == "__main__":
    MainApp().run()
