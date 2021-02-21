import kivy

from kivy.app import App
from kivy.uix.button import Button
class MainApp(App):
    def build(self):
        return Button(text="hola mundo")


if __name__ == "__main__":
    MainApp().run()
