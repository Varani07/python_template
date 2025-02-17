from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from app.dao.jogador_dao import JogadorDAO
from app.services.jogador_service import JogadorService

class JogadorKivyApp(App):
    def build(self):
        self.dao = JogadorDAO()
        self.service = JogadorService(self.dao)
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.name_input = TextInput(hint_text="Nome do Jogador", multiline=False)
        self.points_input = TextInput(hint_text="Pontos (inteiro)", multiline=False)
        
        create_button = Button(text="Criar Jogador")
        create_button.bind(on_press=self.criar_jogador)
        
        self.result_label = Label(text="")
        
        layout.add_widget(self.name_input)
        layout.add_widget(self.points_input)
        layout.add_widget(create_button)
        layout.add_widget(self.result_label)
        
        return layout

    def criar_jogador(self, instance):
        nome = self.name_input.text
        pontos_str = self.points_input.text
        
        try:
            pontos = int(pontos_str)
        except ValueError:
            pontos = 0  
        
        jogador = self.service.criar_jogador(nome, pontos)
        
        self.result_label.text = f"Jogador criado: {jogador.nome} com {jogador.pontos} pontos."
        
        self.name_input.text = ""
        self.points_input.text = ""

if __name__ == '__main__':
    JogadorKivyApp().run()
