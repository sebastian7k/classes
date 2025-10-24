from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    email: str
    telefone: str
    endereco: str
    
    def mostrar_dados(self):
        print("\n=== EXIBINDO DADOS ===")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")


print("=== SOLICITANDO DADOS ===")
usuario1 = Usuario(
    nome=input("Digite seu nome: "),
    email=input("Digite seu E-mail: "),
    telefone=input("Digite seu telefone: "),
    endereco=input("Digite seu endereço: ")
)

print("\n=== EXIBINDO DADOS ===")
usuario1.mostrar_dados()
