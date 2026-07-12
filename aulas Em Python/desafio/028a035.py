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
     if velocidade >= 80:
          print("VAGABUNDO, PASSOU DE 80 KM AGORA VOCE FOI MULTADO")
          print("o valor de sua multa e de {}R$".format(valor))
     else:
        print("de boa")
if Desafio == 28:
     vinteoito()
elif Desafio == 29:
     vintenove()