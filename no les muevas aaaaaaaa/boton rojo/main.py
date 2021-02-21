import kivy
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout


from kivy.config import Config

Config.set('graphics','width',500)
Config.set('graphics','height',700)

class contenedor01(BoxLayout):
	None

class boton_rojoApp(App):
	title = "olaaaaaaaaaaaaaa"
	def build(self):
		return contenedor01()


if __name__ == "__main__":
    boton_rojoApp().run()
