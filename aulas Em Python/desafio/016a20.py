import math
import random
import pygame

print("====desafios====")
Desafio = int(input("qual o desafio? (de 16 a 21) (21 e o mais pika) "))

def deseseis():
    valor = float(input("digite um numero que contena ponto(EX:9.595 ) "))
    print("o valor digitado era {} e seu novo valor e {}".format(valor, int(valor)))

def desesete():
    oposto = float(input("comprimento do cateto oposto? "))
    adjacente = float(input("comprimento do cateto adjacente? "))
    hiponenusia = math.sqrt(oposto**2 + adjacente**2)
    print("a hiponenusia vai medir {:.3f}".format(hiponenusia))

def  desoito():
    oposto = float(input("comprimento do cateto oposto? "))
    adjacente = float(input("comprimento do cateto adjacente? "))
    hiponenusia = math.sqrt(oposto**2 + adjacente**2)
    SENO = oposto/hiponenusia
    COSSENO = adjacente/hiponenusia
    Tangente = oposto/adjacente
    print("o angulo do triangulo tem o SENO de     {:.2f}    ".format(SENO))
    print("o angulo do triangulo tem o COSSENO de  {:.2f} ".format(COSSENO))
    print("o angulo do triangulo tem o Tangente de {:.2f}".format(Tangente))
def  desenove():
    aluno1 = (str(input("Qual e o anuluno?  ")))
    aluno2 = (str(input("Qual e o anuluno?  ")))
    aluno3 = (str(input("Qual e o anuluno?  ")))
    aluno4 = (str(input("Qual e o anuluno?  ")))
    lista = [aluno1, aluno2, aluno3, aluno4]
    escolhido = random.choice(lista)
    print("o aluno escolhido foi {}".format(escolhido))

def vinte(): 
    aluno1 = (str(input("Qual e o anuluno?  ")))
    aluno2 = (str(input("Qual e o anuluno?  ")))
    aluno3 = (str(input("Qual e o anuluno?  ")))
    aluno4 = (str(input("Qual e o anuluno?  ")))
    lista = [aluno1, aluno2, aluno3, aluno4]
    random.shuffle(lista)
    print("a ordem de alunos e")
    print(lista)

def  vinteum():
    pygame.init()
    pygame.mixer.music.load('aulas Em Python/desafio/ventaniahippie-ventania-cogumelo-azul.mp3')

if Desafio == 16:
    deseseis()

elif Desafio == 17:
    desesete()

elif Desafio == 18:
    desoito()

elif Desafio == 19:
    desenove()

elif Desafio == 20:
    vinte()

elif Desafio == 21:
    vinteum()
