from random import randint # aleatoriadade
from time import sleep  # tempo de espera



print("python pronto, Bem vindo aos desafios de miguel lucas em python")
print("====desafios====")
Desafio = int(input("qual o desafio? (de 28 a 35) "))

def vinteoito():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("vou pensar em um numero de 0 a 10...")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    pc = randint(0, 10)
    resposta = int(input("Qual Numero eu pensei?? "))
    print("pensando...")
    for i in range(5):
        print("preparando arquivo ({}Mb/4Mb)".format(i))
        for j in range(55):
            print("carregando arquivos ({}Kb/54Kb) arquivos preparados ({}Mb/4Mb)".format(j,i))
            for k in range(260):
                    print("carregando dados ({}B/260B) carregado arquivos ({}/54Kb) terminando arquivos ({}Mb/4Mb)".format(k,j,i))
    if resposta == pc:
        print("voce ganhou")
    else: 
        print("voce perdeu feio, eu tinha pensado em {}".format(pc))

def vintenove():
     velocidade = int(input("qual a velocidade do seu carro? "))
     valor = (velocidade-80)*7
     if velocidade > 80:
          print("VAGABUNDO, PASSOU DE 80 KM AGORA VOCE FOI MULTADO")
          print("o valor de sua multa e de {}R$".format(valor))
     else:
        print("de boa")

def trinta():
     numero = int(input("digite um valor: "))
     calculo = numero%2
     if calculo == 0:
          print("par")
     else: 
          print("impar")

def trintaum():
     numero = int(input("qual a distancia da viagem? "))
     formula = numero * 0.45
     if numero >= 200: 
          print("o custo da sua viagem sera de {}R$".format(formula))
     else:
          novaformula = numero * 0.50
          print("o custo da viagem sera de {}R$".format(novaformula))
def trintaedois():
     ano = int(input("qual o ano?? "))
     if ano%4 == 0:
          print("ano bixesto")
     else:
          print("ano nao bixesto")
def trintatres():
     a = int(input("primeiro valor"))
     b = int(input("segundo valor"))
     c = int(input("terceiro valor"))
     menor = a
     if b<a and b<c:
        menor = b
     if c<a and c<b:
          menor = c
     maior = a
     if b>a and b>c:
          maior = b
     if c>a and c>b:
          maior = c
     print("o menor valor e {}".format(menor))
     print("o maior valor e {}".format(maior))

def trintaquatro():
     salario = float(input("qual o salario? " ))
     if salario <= 1500:
        salario = salario + (salario*25/100)
        print("o seu salario fudido recebeu um bonus de 25% e seu total ficou em {}".format(salario))

     elif salario >= 3000 and salario < 7000:   
           salario = salario + (salario*15/100)
           print("o seu salario mediano recebeu um bonus de 15% e seu total ficou em  {}".format(salario))     
     elif salario > 7000:
        salario = salario + (salario*5/100)
        print("o seu otimo salario recebeu um bonus de 5% e seu total ficou em {}".format(salario))
def trintacinco():
        r1 = float(input("primeiro segmento "))
        r2 = float(input("segundo sequimento "))
        r3 = float(input("terceiro segmento "))
        if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
             print(" os sequimentos formam um triangulo")
        else:
             print("os sequimentos nao formam um triangulo")
          
          
if Desafio == 28:
     vinteoito()
elif Desafio == 29:
     vintenove()
elif Desafio == 30:
     trinta()

elif Desafio == 31:
     trintaum()
elif Desafio == 32: 
     trintaedois()
elif Desafio == 33:
     trintatres()
elif Desafio == 34:
     trintaquatro()
elif Desafio == 35:
     trintacinco()
     