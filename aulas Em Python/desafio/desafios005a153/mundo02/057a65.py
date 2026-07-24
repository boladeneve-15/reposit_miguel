import math
import time


print("""BEM VINDO AOS TESTES DE MIGUEL LUCAS EM PYTHON, esse e o começo de uma nova linguagem de progamação
    onde meu foco no final de tudo e saber
    ciencias de dados, eng de dados, automoção em python, e criação de IAs""")


print("====desafios====")
Desafio = int(input("qual o desafio? (de 57 a 65) "))

def cintquentasete():
    genero = str(input("qual seu genero [M/F]? ")).upper().strip()[0]
    
    while genero != 'M' or genero != 'F':
        genero = str(input(" ERRO, POR FAVOR FALE UM DOS 2 GENEROS [M/F]: ")).upper().strip()[0]
        if genero == 'M' or genero == 'F':
            print("cadastro feito seu genero e {}".format(genero))
            break


# desafio 58 e um jogo por isso nao esta disponivel nesse arquivo


def cinquentanove():
    Primeiro = int(input("Qual o primeiro valor? "))
    segundo = int(input("Qual e o segundo valor? "))
    funcoes = 0
    maior = 0
    while funcoes != 5:
        funcoes = int(input(''' 
        [1] somar
        [2] multiplicar
        [3] ver o maior numero
        [4] novos numeros
        [5] sair do progama
        >>>>> O QUE DESEJA FAZER? '''))
        if funcoes == 1:
            print(" a soma dos 2 valores e de {}".format(Primeiro + segundo))
        elif funcoes == 2:
            print(" a multiplicaçao dos 2 valores e de {}".format(Primeiro * segundo))
        elif funcoes == 3:
                if Primeiro > segundo:
                   maior = Primeiro
                   print("o maior numero e {}".format(Primeiro))
                else:
                    maior = segundo
                    print("o maior numero e {}".format(segundo))
        elif funcoes == 4:
            print("novos numeros..")
            time.sleep(3)
            Primeiro = int(input("Qual o primeiro valor? "))
            segundo = int(input("Qual e o segundo valor? "))
        elif funcoes == 5:
            print("FINALIZANDO")
        else:
            print("ERRO")


def sesenta():
    numero = int(input("um numero: "))
    i = numero
    fatorial = 1
    print("""calculando o {}!
    """.format(numero), end='')
    while i > 0:
        print("{}".format(i),end=' x ')
        fatorial *= i
        i-= 1
    print('{}'.format(fatorial))        

    



def sesentaum():
    print("="*20)
    print("10 TERMOS DE UMA PA")
    print("="*20)
    primeiro = int(input("PRIMEIRO TERMO: "))
    razao = int(input("RAZAO: "))
    termo = primeiro
    contador = 1
    while  contador <=10: 
        print("{} ".format(termo), end='-> ')
        termo += razao 
        contador +=1
    print("FIM")

def sesentadois():
    print("~="*31)
    print("X TERMOS DE UMA PA(versao melhorada)")
    print("~="*31)
    primeiro = int(input("PRIMEIRO TERMO: "))
    razao = int(input("RAZAO: "))
    termo = primeiro
    contador = 1
    mais = 10
    total = 0
    while mais != 0:
        total = total + mais
        while  contador <=10: 
            print("{} ".format(termo), end='-> ')
            termo += razao 
            contador +=1
        print("PAUSA...")
        mais = int(input("quantos termos a mais voce quer mostrar? "))
    print("FIM")


def sessentatres():
    print("-"*30)
    print("sequencia de Fibonacci")
    print("-"*30)
    numero = int(input('quantos termos voce quer mostrar? '))
    termo1 = 0
    termo2 = 1
    print("~"*30)
    print("{} -> {}".format(termo1, termo2),end='')
    contador = 3
    while contador <= numero:
        termo3 = termo1 + termo2
        print('-> {}'.format(termo3),end='')
        termo1 = termo2
        termo2 = termo3
        contador+=1
    print(" fim")
def umpack():
    num = contador = soma = 0
    while num != 999:
        num = int(input("digite um numero [999 para sair]: "))
        soma += num
        contador +=1
    print("voce digitou {} numeros e a soma entre eles foram de {}".format(contador, soma - 999))


def     sesentacinco():
    condicao = 'S'
    soma  = quantidade = media = 0
    while condicao != 'N':
        numero = int(input("digite um numero: "))
        soma += numero
        quantidade += 1     
        condicao = str(input("qual continuar? [S/N] ")).upper()
    media = soma/quantidade
    print("voce digitou {} numero e a media dele foi de {}  ".format(quantidade, media))
    print("acabou")


if Desafio == 57:
    cintquentasete()
elif Desafio == 58:
    print("desafio 58 e um jogo por isso nao esta disponivel nesse arquivo")
elif Desafio == 59:
    cinquentanove()
elif Desafio == 60:
    sesenta()
elif Desafio == 61:
    sesentaum()
elif Desafio == 62:
    sesentadois()
elif Desafio == 63:
    sessentatres()
elif Desafio == 64:
    umpack()
elif Desafio == 65:
    sesentacinco()