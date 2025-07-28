from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button,Label


class slamano(App):
    def text(self):
        self.textos = ["Lançamentos Financeiros","Categorias","Orçamento","Mostrar Gráficos","Saldo","Exportar Dados"] 
    def cores(self):
        self.cor = [
            (225/255, 88/255, 88/255, 1),(127/255, 194/255, 45/255, 1),(29/255, 177/255, 93/255, 1),(31/255, 153/255, 159/255, 1),(31/255, 46/255, 159/255, 1),(74/255, 31/255, 159/255, 1)
        ]
    def build(self):
        self.text()
        self.cores()
        layout = GridLayout(cols=2)
        for i in range(len(self.cor)):
            layout.add_widget(Button(text=self.textos[i],background_color=self.cor[i]))
        return layout
    
    def qualquercoisa(self,instancia):
        self.mensagem.text = self.inputizin.text
slamano().run()