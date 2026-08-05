from random import randint
from time import sleep

while True:
    print("rodando denovo..")
    sleep(3)
    escolha = int(input("""qual dos trem buxa? 
    [1] randomizar de 1 a 20 (melhorado)
    [2] randomizar de -1 a -20
    [3] randomizar 2 numeros de 1 a 20 e tenha uma surpresa
    [4]  10 numeros aleatorios de 1 a 10
    [q] sair
    """))

    def randomizarumavinte():
        aleatorio = randint(10,20)
        print(aleatorio)

    def randomizarumavintenegativo():
        aleatorio = randint(10,20)
        print(aleatorio * -1)

    def doisnumeros():
        valorum =  randint(10,20)  
        valordois =  randint(10,20) 
        print(f"seu primeiro numero e {valorum} " )
        sleep(2)
        print(f"seu primeiro numero e {valordois} " )
        sleep(2)
        soma = valorum + valordois
        print(f"a soma dos 2 valores são de {soma}")
    def umadez():
        a = 0
        i = 0
        for i in range(0,10):
            a = randint(1,10)
            print(f"{a}",end= ",")
        print("")

    if escolha == 1:
        randomizarumavinte()
    elif escolha == 2:
        randomizarumavintenegativo()
    elif escolha == 3:
        doisnumeros()
    elif escolha == 4:
        umadez()

    else:
        break


