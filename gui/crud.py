from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget

from entidades import cliente
from repositorios import cliente_repositorio


class BotaoListagem(ToggleButton):
    def __init__(self, cliente_id, cliente_nome, cliente_idade, **kwargs):
        super(BotaoListagem, self).__init__(**kwargs)
        self.id_cliente = cliente_id
        self.nome_cliente = cliente_nome
        self.idade_cliente = cliente_idade
        self.text = self.nome_cliente + " " + self.idade_cliente
        self.group = 'clientes'


class Principal(BoxLayout):
    def __init__(self, **kwargs):
        super(Principal, self).__init__(**kwargs)
        self.listar_clientes()

    def listar_clientes(self):
        self.ids.clientes.clear_widgets()
        clientes = cliente_repositorio.ClienteRepositorio.listar_clientes()
        for i in clientes:
            print(i)
            id = str(i[0])
            nome = i[1]
            idade = str(i[2])
            self.ids.clientes.add_widget(BotaoListagem(id, nome, idade))

    def cadastrar_cliente(self):
        nome = self.ids.nome.text
        idade = self.ids.idade.text

        cli = cliente.Cliente(nome, idade)
        cliente_repositorio.ClienteRepositorio.inserir_cliente(cli)
        self.ids.nome.text = ''
        self.ids.idade.text = ''
        self.listar_clientes()


class Crud(App):
    def build(self):
        return Principal()


Crud().run()
