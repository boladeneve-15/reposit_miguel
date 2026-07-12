from random import randint

print("carregando arquivo")
for i in range(5):
    print("preparando arquivo ({}Mb/4Mb)".format(i))
    for j in range(101):
        print("carregando arquivos ({}Kb/100Kb) arquivos preparados ({}Mb/4Mb)".format(j,i))
        for k in range(1001):
                print("carregando dados ({}B/1000B) carregado arquivos ({}/100Kb) terminando arquivos ({}Mb/4Mb)".format(k,j,i))

print("python pronto, Bem vindo aos desafios de miguel lucas em python")
print("====desafios====")
Desafio = int(input("qual o desafio? (de 28 a 35) "))

# def vinteoito():
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("vou pensar em um numero de 0 a 10...")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
pc = randint(0, 10)
resposta = int(input("Qual Numero eu pensei?? "))
if resposta == pc:
    print("voce ganhou")
else: 
    print("voce perdeu feio, eu tinha pensado em {}".format(pc))