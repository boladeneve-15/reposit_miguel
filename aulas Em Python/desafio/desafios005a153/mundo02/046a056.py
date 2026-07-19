from time import sleep
from datetime import date
print("""BEM VINDO AOS TESTES DE MIGUEL LUCAS EM PYTHON, esse e o começo de uma nova linguagem de progamação
    onde meu foco no final de tudo e saber
    ciencias de dados, eng de dados, automoção em python, e criação de IAs""")


print("====desafios====")
Desafio = int(input("qual o desafio? (de 46 a 56) "))

def quarentaseis():
    for i in range(10, -1, -1):
        sleep(1)
        print(i)
    print("parabens pela paciencia pra ver nada acontecer")

def quarentasete():
    for i in range(0, 52, 2):
        print(i, end=' ')
def quarentaoito():
    soma = 0
    contador = 0
    for i in range(1,501):
        if i % 2 != 0 and i % 3 == 0:
            soma += i
            contador += 1
    print("A soma de todos os {} valores solicitados é {}.".format(contador, soma))
def quarentanove():
    numero = int(input("digite um numero "))
    for i in range(1 ,11):
        print("{}x{} = {}".format(numero, i, (numero*i)))

def cinquenta():
    soma = 0
    contador = 0
    print("-="*20)
    print("ESPECIAL DE 50 EXERCICIOS FEITOS")
    print("-="*20)
    for i in range(1,7):
        numero = int(input("digite o {} numero ".format(i)))
        if numero % 2 == 0:
            soma += numero
            contador += 1
    print("voce informou {} numeros PARES, e a soma deles foi {}".format(contador, soma))
def cinquentaum():
    print("="*20)
    print("10 TERMOS DE UMA PA")
    print("="*20)
    termo = int(input("PRIMEIRO TERMO: "))
    razao = int(input("RAZAO: "))
    decimo = termo + (10-1)*razao
    for i in range(termo, decimo + razao, razao):
        print("{} ".format(i), end='-> ')
    print("FIM")
def cinquentadois():
    numero = int(input("digite um numero: "))
    total = 0
    for i in range(1, numero, 1):
        if numero % i == 0:
            print('\033[31m', end=' ')
            print("{}".format(i),end=' ')
            total += 1
        else:
            print('\033[32m', end=' ')
    print("{} ".format(i),end=' ')
    print('\n\033[mO numero {} foi divivel {} vezes'.format(numero, total))
    if total == 2:
            print('NUMERO PRIMO')
    else:
        print("NÃO PRIMO")    
def cinquentatres():
    frase = str(input("digite uma frase: ")).strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = ''
    for i in range(len(junto)-1, -1, -1):
        inverso += junto[i]
    if junto == inverso:
        print('FRASE PALÍNDROMO')
    else:
        print("frase nao palíndromo")    

def cinquentaquatro():
     contadornovo = 0
     contadorveio = 0
     morto = 0
     for i in range(1,8):
        atual = date.today().year
        nasceu = int(input("Qual o ano que a {}° pessoa nasceu? ".format(i)))
        idade =    (nasceu - atual)*-1
        if idade >= 21:
            contadorveio += 1
        elif idade <=20:
            contadornovo += 1
        elif idade >= 100:
            morto += 1
     print("ao todo temos {} pessoas velhas e {} pessoas novas e {} mortos".format(contadorveio, contadornovo,morto))
def cinquentacinco():
    for i in range(1,7):
        peso = float(input("qual o peso da {}° pessoa? ".format(i)))
        maior = 0
        menor = 0
        if i == 1:
            maior = i
            menor = i
        else:
            if peso > maior:
                maior = peso
            if peso < menor:
                menor = peso
    print("o maior peso lido foi {}".format(maior))
    print("o menor peso lido foi {}".format(menor))
def cinquentaseis():
    for i in range(1,4):
        print("---{}° PESSOA---".format(i))
        nome = str(input("NOME "))
        idade = int(input("IDADE "))
        genero = str(input("GENERO(M/F) "))
if Desafio == 46:
    quarentaseis()
elif Desafio == 47:
    quarentasete()
elif Desafio == 48:
    quarentaoito()
elif Desafio == 49:
    quarentanove()
elif Desafio == 50:
    cinquenta()
elif Desafio == 51:
    cinquentaum()
elif Desafio == 52:
    cinquentadois()
elif Desafio == 53:
    cinquentatres()
elif Desafio == 54:
    cinquentaquatro()
elif Desafio == 55:
    cinquentacinco()
elif Desafio == 56:
    cinquentaseis()
else:
    print("ERRO")