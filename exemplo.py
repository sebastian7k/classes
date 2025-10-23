from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    idade: int
    
    def mostrar_dados(self):
        print("\n=== EXIBINDO DADOS ===")
        print(f"Nome: {self.nome}")
        print(f"idade: {self.idade}")


print("=== SOLICITANDO DADOS ===")
usuario1= Usuario(nome=input("Digite seu Nome: "),
                  idade=int(input("Digite sua idade: ")))

usuario2= Usuario(nome=input("Digite seu Nome: "),
                  idade=int(input("Digite sua idade: ")))

print("\n=== EXIBINDO DADOS ===")
usuario1.mostrar_dados()
usuario2.mostrar_dados()

