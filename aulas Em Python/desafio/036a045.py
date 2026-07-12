
print("python pronto, Bem vindo aos desafios de miguel lucas em python")
print("====desafios====")
Desafio = int(input("qual o desafio? (de 36 a 45) "))

def trintaseis():
    valor = float(input("qual o valor da casa??? "))
    salario = float(input("qual o seu salario??? "))
    ano = int(input("quantos anos voce vai financiar a casa? "))
    messes = ano * 12
    prestacao = valor / messes
    limite = salario * 0.30 
    if prestacao <= limite:
        print('compra de casa concedido')
    else:
        print("compra negada")
def trintasete():
    numero = int(input(" digite um numero: "))
    print("escolha")
    print("[1] binario")
    print("[2] octal")
    print("[3] hexadecimal")
    escolha = int(input("escolha "))
if Desafio == 36:
    trintaseis()
elif Desafio == 37:
    trintasete()