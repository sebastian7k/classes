import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Usuario:
    nome: str 
    email: str 
    endereco:str

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco}")
        
    def apenas_nomes(self):
        print(f"Nome: {self.nome}")
        

print("Solicitando dados")
lista_usuarios = []
for i in range(2):
    usuario = Usuario(
        nome=input("Digite seu nome: "),
        email=input("Digite seu E-mail: "),
        endereco=input("Digite seu endereço: ")
    )
    lista_usuarios.append(usuario)
os.system("cls")

print("===MOSTRANDO DADOS===")


usuario.exibir_dados()
for pessoa in lista_usuarios:
    print("===MOSTRANDO APENAS NOME===")

for pessoa in lista_usuarios:
    usuario.apenas_nomes()