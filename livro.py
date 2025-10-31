import os 

os.system("cls")

class Autor:
    def __init__(self, nome, biografia):
        self.nome = nome 
        self.biografia =  biografia
    def __str__(self):
        return (f"{self.nome},{self.biografia}")
        

class Livro: 
    def __init__(self, titulo, ano, autor):
        self.titulo= titulo
        self.ano = ano 
        self.autor = autor
        
    def exibir_detalhes(self):
        print(f"Titulo: {self.titulo}")
        print(f"Ano de Publicação: {self.ano}")
        print(f"Autor: {self.autor}")
    
    
#craiando instâncias

autor1 = Autor(nome="Stendhal", biografia="Henri-Marie Beyle, mais conhecido como Stendhal, foi um escritor francês. Seus romances de formação")
livro1 = Livro(titulo="O Vermelho e o Negro", ano="1830", autor=autor1)

#exibindo dados

livro1.exibir_detalhes()