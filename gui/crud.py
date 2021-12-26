from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class Principal(BoxLayout):
    pass


class Crud(App):
    def build(self):
        return Principal();


Crud().run()
