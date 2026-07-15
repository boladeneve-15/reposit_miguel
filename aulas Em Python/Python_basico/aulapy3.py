Saldo = 100
def sacar():
        global Saldo
        Quanto = int(input("Quanto sacar? "))
        Saldo -= Quanto
        print()
        print("Voce retirou ", Quanto, "Reais ", "seu novo saldo É", Saldo)
        print()
        if Quanto > Saldo:
              print("ERRO, VOCE NAO PODE SACAR MAIS DOQUE TEM")
              print("Saindo Do Banco...")
              


def depositar():
        global Saldo
        Quanto = int(input("Quanto depositar? "))
        Saldo += Quanto
        print()
        print("Voce depositou ", Quanto, "Reais ", "seu novo saldo É", Saldo)
        print()

def Versaldo():
        print()
        print("Bem Vindo o Seu Saldo É", Saldo, "reais ")
        print()


while True:
        print("==== BANCO ====")
        print()
        print()
        print("Bem Vindo, Oque Deseja Hoje?")
        print()
        print()
        valor = input("(1- Ver Saldo 2 - Depositar 3 - Sacar 4 - Sair )")

        if valor == '1':
            Versaldo()

        elif valor == '2':
            depositar()
        elif valor == '3':
            sacar()
        elif valor == '4':
            print("Saindo Do Banco...")
            break