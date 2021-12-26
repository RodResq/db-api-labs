from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from entidades import cliente
from repositorios import cliente_repositorio


class Principal(BoxLayout):
    def cadastrar_cliente(self):
        nome = self.ids.nome.text
        idade = self.ids.idade.text

        cli = cliente.Cliente(nome, idade)
        cliente_repositorio.ClienteRepositorio.inserir_cliente(cli)
        self.ids.nome.text = ''
        self.ids.idade.text = ''


class Crud(App):
    def build(self):
        return Principal();


Crud().run()
