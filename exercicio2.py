from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    email: str
    telefone: str
    endereco: str

print("=== SOLICITANDO DADOS ===")
usuario1 = Usuario(
    nome=input("Digite seu nome: "),
    email=input("Digite seu E-mail: "),
    telefone=input("Digite seu telefone: "),
    endereco=input("Digite seu endereço: ")
)

print("\n=== EXIBINDO DADOS ===")
print(f"Nome: {usuario1.nome}")
print(f"E-mail: {usuario1.email}")
print(f"Telefone: {usuario1.telefone}")
print(f"Endereço: {usuario1.endereco}")
