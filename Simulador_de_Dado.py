# Simulador de Dado
# Simular o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]
  
    def Iniciar(self):
        # Criar uma janela
        self.janela = sg.Window('Simulador de Dado', Layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer alguma coisa com esses valores
        while True:
            try:
                if self.eventos == 'Sim' or self.eventos == 'S':
                    self.GerarValorDoDado()
                elif self.eventos  == 'Não' or self.eventos == 'N':
                    print('Agradecemos sua participação!')
                else:
                    print('Favor digitar Sim ou Não')
            except:
                print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()