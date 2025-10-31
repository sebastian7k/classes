import os 
os.system("cls")

#rescto que desejo salvar
texto = input("Digite seu nome: ")

#definir  nome do arquivo para slavar 
nome_arquivo="exemplo.txt"

#comando para salvar 
with open(nome_arquivo, "a") as meu_arquivo:
    meu_arquivo.write(f"{texto}\n")
    print("salvo com sucesso ")