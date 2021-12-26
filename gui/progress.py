from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('progress.kv')


class MyLayout(Widget):

    def press_it(self):
        # captura o valor corrente da barra de progresso
        current = self.ids.my_progress_bar.value
        # comecar de novo apos 100
        if current == 1:
            current = 0
        # Incrementea em 25% a barra de tarefa
        current += .25
        # Atualiza a barra de progresso
        self.ids.my_progress_bar.value = current
        # Atualiza o Label
        self.ids.my_label.text = f'{int(current*100)}% Progress'


class Progress(App):
    def build(self):
        return MyLayout()


if __name__=='__main__':
    Progress().run()
