from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label


class Teste(App):
    def build(self):
        return Label(text='Ola, Mundo!!!')


Teste().run()
