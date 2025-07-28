from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button,Label


class slamano(App):

    def build(self):
        layout = GridLayout(cols=3)
        layout.add_widget(Label(text="primeirooooo"))
        layout.add_widget(Label(text="segundo '-' "))
        layout.add_widget(Label(text="terceirinho ,0, "))
        self.mensagem = Label(text="")
        layout.add_widget(Button(text="parapapa 4 ",on_press = self.qualquercoisa))
        self.inputizin = TextInput(hint_text="alguma coisa kkkkk")
        layout.add_widget(self.inputizin)
        layout.add_widget(self.mensagem)
        return layout
    
    def qualquercoisa(self,instancia):
        self.mensagem.text = self.inputizin.text
slamano().run() 