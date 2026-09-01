import math
import time


print("""BEM VINDO AOS TESTES DE MIGUEL LUCAS EM PYTHON, esse e o começo de uma nova linguagem de progamação
    onde meu foco no final de tudo e saber
    ciencias de dados""")

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
def maravilhoso():
    print("-"*30)
    print("====cadastro da pessoa====")
    print("-"*30)
    maior18 =     totalHomens = totalmulheras20 = 0


    while True:
        idade = int(input("qual sua idade? "))
        genero = str(input("qual seu genenro [M/F] ")).upper()
        if idade >= 18:
            maior18 +=1
        if genero == 'M':
            totalHomens+=1
        if genero == 'F' and idade < 20:
            totalmulheras20+=1
        
        print("-"*20)
        condicao = str(input("qual continuar? [S/N]? ")).upper()
        if condicao == 'N':
            print(f"foram no total {maior18} pessoas maiores de 18 anos")
            print(f"o total de homens registrados e de {totalHomens}")
            print(f"o total de mulheres com menos de 20 anos e de {totalmulheras20}")
            break
def setenta():
    total = maisdemill = maisbarato = contador = menor = 0
    print("__"*50)
    print("LOJA SEU PREÇO")
    print("__"*50)
    while True:
        protudo = str(input("qual o produto? "))
        contador+=1
        preco = int(input("valor: "))
        condicao = str(input(" quer continuar? [S/N] ")).upper()
        total += preco
        if preco > 1000:
            maisdemill+=1
        if contador ==1:
            menor = preco
        else:
            if preco < menor:
                menor = preco
        if condicao == 'N':
            print("VOLTE SEMPRE ")
            print(f""" o total da compra foi de {total}
            temos {maisdemill} produtos custanto mais de 1000 reais
            o protudo mais barato foi {menor} reais""")
            break














if Desafio == 66:
    sesentaseis()
elif Desafio == 67:
     maltido()
elif Desafio == 68:
    print("o desafio 68 e um jogo por isso nao existe ele nessa pagina")
elif Desafio == 69:
    maravilhoso()
elif Desafio == 70:
    setenta()