import math
import time


print("""BEM VINDO AOS TESTES DE MIGUEL LUCAS EM PYTHON, esse e o começo de uma nova linguagem de progamação
    onde meu foco no final de tudo e saber
    ciencias de dados, eng de dados, automoção em python, e criação de IAs""")

print("====desafios====")
Desafio = int(input("qual o desafio? (de 66 a 71) "))

def sesentaseis():
    contador = 0
    soma = 0
    while True:
        numero = int(input("digite um valor: [digite 999 para sair] "))
        soma += numero
        contador +=1
        if numero == 999:
            break
    print(f" a soma dos {contador-1} valores foi de {soma-999}")

def maltido():
    while True:
        print("~"*30)
        valor = int(input("qual valor da tabuada? [0 para sair] "))
        print("~"*30)
        for i in range(1 ,11):
            print(f"{valor}x{i} = {valor*i}")
        if valor == 0:
            break















if Desafio == 66:
    sesentaseis()
if Desafio == 67:
    maltido()
if Desafio == 68:
    print("o desafio 68 e um jogo por isso nao existe ele nessa pagina")