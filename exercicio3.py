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
        print(f"Endereço: {self.endereco}")
        
    def dados_email_marketing(self):
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco}")

print("Solicitando dados")

usuario1 = Usuario(
    nome=input("Digite seu nome: "),
    email=input("Digite seu E-mail: "),
    endereco=input("Digite seu endereço: ")
)
os.system("cls")

print("exibindo dados de entrega ")


usuario1.exibir_dados()

print("Dados de Marketing e E-email")


usuario1.dados_email_marketing()