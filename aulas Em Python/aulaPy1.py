# 1 fazer o delta
# 2 fazer o IMC ja com resultado
EscolherFuncao = input("Escolha Sua Função(Baskara ou IMC): ")

if EscolherFuncao == "Baskara":
    def Baskara():
        import math
        A =  int(input("valor De a "))
        B =  int(input("valor De b "))
        C =  int(input("valor De c "))
        DELTA = B**2 -4*A*C
        if DELTA < 0:
            print("A Equação do Segundo Grau Nâo Aceita Numeros Negativos")
        else:
            Raiz =  math.sqrt(DELTA)
            BaskaraPlus = (-B + Raiz) / (2*A)
        BaskaraNeg = (-B - Raiz) / (2*A)
        print(BaskaraPlus)
        print(BaskaraNeg)
    Baskara()

if EscolherFuncao == "IMC":
    def IMC():
        peso = float(input("qual e seu peso? "))
        Altura = float(input("Qual Sua Altua? "))
        imc = (peso)/(Altura**2)
        if imc <= 18.5:
            print("Esta Muito Magro")
        elif imc <= 24.9:
            print("normal")
        elif imc <= 29.9:
            print("esta Sobrepeso(obesidade grau I)")
        elif imc <= 39.9:
            print("esta em Obeso (Obesidade Grau II)")
        elif imc >= 40.0:
            print("Esta Igual o Davi Gordo, Gigante, nem passa na porta")


IMC()



