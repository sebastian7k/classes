import os 
from dataclasses import dataclass
os.system("cls")

#Creat class

@dataclass
class Cliente: 
    nome: str
    endereco: str
    telefone: str
    
    def mostrar_dados(self):
        print("\nSeus dados:")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")
    
    
#Vetores
lista_clientes = []  
for i in range (3) :   
    dados_cliente = Cliente(nome=input("Digite seu nome: "),
                    endereco= input("Digite seu endereço: "),
                    telefone=input("Digite Seu Telefone: ") )
    lista_clientes.append(dados_cliente)

#solicitando dados 
os.system("cls")
#exibindo nomes
print("DADOS DO CLIENTE")
for um_cliente in lista_clientes:
    um_cliente.mostrar_dados()
    







# print("Exibindo apenas nomes ")

# print(f"Nome: {cliente1.nome}")
# print(f"Nome: {cliente2.nome}")


# #exibindo apenas endereços

# print("Mostrando endereços")
# print(f"Endereço: {cliente1.endereco}")
# print(f"Endereço: {cliente2.endereco}")

# #exibindo informações completas

# print("Dados dos clientes")

# print(f"Nome: {cliente1.nome}")
# print(f"Endereço: {cliente1.endereco}")
# print("================================")
# print(f"Nome: {cliente2.nome}")
# print(f"Endereço: {cliente2.endereco}")