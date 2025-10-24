import os 
from dataclasses import dataclass
os.system("cls")
def limpar_tela():
    os.system("cls")
@dataclass
class Pessoa: 
    nome: str
    idade:int
    peso: float
    altura: float
    
    def mostrar_dados(self):
        print("====EXIBINDO DADOS====")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.idade}")
        print(f"Altura: {self.altura}")
    
lista_de_pessoas = []    
for i in range(4):
    print("Insira seus dados {i+1}: ")
    dados_pessoa = Pessoa(
        nome=input("Digite seu nome: "),
        idade=input("Digite a sua idade: "),
        peso=input("Digite o seu peso: "),
        altura=input("Digite a sua altura: ")
    )
    lista_de_pessoas.append(dados_pessoa)
    limpar_tela()
os.system("cls")

print("Dados cadastrados: ")
for uma_pessoa in lista_de_pessoas:
    uma_pessoa.mostrar_dados()    
    
    