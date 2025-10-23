import os 
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

print (" SOLICITANDO DADOS DO USUARIO ")
pessoa1 = Pessoa (nome=input("Digite seu nome: "), 
                 idade=int(input("Digite a sua idade: ")), 
                 peso=float(input("Digite o seu peso: ")), 
                 altura=float(input("Digite a sua altua: ")))

print ("\nExibindo dados\n")
print(f"Nome: {pessoa1.nome}")
print(f"Idade: {pessoa1.idade}")
print(f"Peso: {pessoa1.peso} kg")
print(f"altuta: {pessoa1.idade} cm")
