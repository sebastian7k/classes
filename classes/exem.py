import os 
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: str
    pet: str
@dataclass
class Pet:
    nome: str
    idade: int
    peso: float
    raca: str
# exemplo usado no data calass 

pessoa = Pessoa ("Alice", 30, "789.654.355.60", "Bob")
pet =  Pet ("Bob", 3, "5kg", "Pastor Alemão")

print("Exibindo dados do dono:")

print(f"Nome: {pessoa.nome}, idade: {pessoa.idade} CPF: {pessoa.cpf}, Nome do pet: {pessoa.pet}")

print("Exibindo dados do pet:")

print(f"Nome: {pet.nome}, idade: {pet.idade} peso: {pet.peso}, Raça: {pet.raca}")

