import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str

@dataclass
class Cliente:
    nome: str
    idade: str
    email: str 
    endereco: Endereco
    
    def mostrar_dados(self):
        print("\n--- Dados do Cliente ---")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco.logradouro}, Nº {self.endereco.numero}, {self.endereco.cidade}")

# Entrada de dados
logradouro = input("Digite o logradouro: ")
numero = int(input("Digite o número: "))      
cidade = input("Digite a sua Cidade: ")
endereco = Endereco(logradouro, numero, cidade)

nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
email = input("Digite o seu E-mail: ")
cliente = Cliente(nome, idade, email, endereco)

# Saída de dados
cliente.mostrar_dados()     
