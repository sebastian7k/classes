import os
from dataclasses import dataclass
os.system("cls")
#Fução para limpar a tela 
def limpar_tela():
    os.system("cls")
# Criar uma classe
@dataclass
class Pessoa:
    nome: str
    cpf: str
    telefone: str

    def mostrar_dados(self):
        print("\nSeus Dados:")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")

    def dados_sms(self):
        print(f"Seu Número: {self.telefone}")

# Vetor (lista de pessoas)
lista_de_pessoas = []

for i in range(3):
    print(f"\nCadastro {i+1}:")
    dados_pessoa = Pessoa(
        nome=input("Digite seu nome: "),
        cpf=input("Digite seu CPF: "),
        telefone=input("Digite seu telefone: ")
    )
    lista_de_pessoas.append(dados_pessoa)
    limpar_tela()
os.system("cls")

print("=== Dados cadastrados ===")
for uma_pessoa in lista_de_pessoas:
    uma_pessoa.mostrar_dados()

print("\n=== Números cadastrados ===")
for uma_pessoa in lista_de_pessoas:
    uma_pessoa.dados_sms()
