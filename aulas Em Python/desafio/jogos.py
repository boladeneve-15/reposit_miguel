from random import randint
from time import sleep
print("-=" *30 )
print("jogos")
print("-=" *30 )
print(''' escolher o jogo 
            [1] contra a maquina 0 a 10
            [2]JO-KEN-PO''')
qualjogo = int(input("QUAL JOGO   "))
def zeroadez():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("vou pensar em um numero de 0 a 10... ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    pc = randint(0, 10)
    resposta = int(input("Qual Numero eu pensei?? "))
    print("pensando...")
    if resposta == pc:
        print("voce ganhou ")
    else: 
        print("voce perdeu feio, eu tinha pensado em {}".format(pc))


def jokenpo():
    itens = ('pedra' , 'papel' , 'tesoura')
    print("-="*30)
    jogador = int(input('''sua escolha
                    [0] PEDRA
                    [1] PAPEL
                    [2] TESOURA    
                        '''))
    print("-="*30)
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")
    sleep(1)

    pc = randint(0,2)
    if pc == 0: # 0 = PEDRA
        if jogador == 0: # 0 = PEDRA
            print("EMPATE")
        elif jogador == 1: # 1 = PAPEL
            print("JOGADOR VENCE")
        elif jogador == 2: # 2 = TESOURA
            print("PC VENCE")
        else:
            print("ERRO,JOGADA INVALIDA")

    if pc == 1: # 1 = PAPEL
        if jogador == 0: # 0 = PEDRA
            print("PC VENCE")
        elif jogador == 1: # 1 = PAPEL
            print("EMPATE")
        elif jogador == 2:  # 2 = TESOURA
            print("JOGADOR VENCE")
        else:
            print("ERRO,JOGADA INVALIDA")

    if pc == 2: # 2 = TESOURA
        if jogador == 0: # 0 = PEDRA
            print("JOGADOR VENCE")
        elif jogador == 1: # 1 = PAPEL
            print("PC VENCE")
        elif jogador == 2:  # 2 = TESOURA
            print("EMPATE")
        else:
            print("ERRO,JOGADA INVALIDA")

    print()
    print()
    print()
    print() 
    print("-=" *20)
    print("o pc escolheu  {} ".format(itens[pc]))
    print("voce  escolheu  {} ".format(itens[jogador]))
    print("-=" *20)
    print("FIM DE JOGO")

if qualjogo == 1:
    zeroadez()

elif qualjogo ==2:
    jokenpo()