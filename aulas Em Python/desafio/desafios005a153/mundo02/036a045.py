from datetime import date
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
    if escolha == 1:
        print("O {} CONVERTIDO EM BINARIO E {} ".format(numero, bin(numero)[2:]))
    elif escolha == 2: 
        print(" o {} convertito em octal e {} ".format(numero, oct(numero)[2:]))
    elif escolha == 3:
        print("o {} convertito em hexadecimal e {} ".format(numero, hex(numero)[2:]))

def trintaoito():
    primeiro = int(input("digite o primeiro numero "))
    segundo = int(input("digire o segundo numero "))
    maior = primeiro
    if segundo > primeiro:
        maior = segundo
        print(" o segundo e o maior ")
    elif primeiro > segundo:
        print(" o primeiro e maior ")
    elif primeiro == segundo:
        print("os dois numeros sao iguais ")

def trintanove():
    atual = date.today().year
    ano = int(input("que ano voce nasceu? "))
    idade = (ano-atual )*-1
    print("quem nasceu em {}, tem {} anos, em {} ".format(ano,idade,atual))
    if  idade < 18:
        print("voce nao tem +18 anos daqui a  {} anos".format((idade-18)*-1))
    elif idade > 18:
        print("voce tem mais de 18 anos voce fez o alistamento a {} anos atras".format((idade-18)))
    elif idade == 18:
        print("vai trabalhar no exercito vagabundo da silva")
def quarenta():
    nota1 = float(input("qual sua primeira nota: "))
    nota2 = float(input("qual sua segunda nota: "))
    media = (nota1+nota2)/2
    print(" o aluno com a primeira nota de {} e a segunda nota de {} tem a media de {}".format(nota1,nota2,media))
    if media < 5.9:
        print("sua nota esta abaixo de 6.0 sua nota de {} estude mais".format(media))
    elif media >= 6.0:
        print("sua nota esta acima de 6.0 sua nota de {}, esta otimo".format(media)) 
def quarentaum():
    ano = int(input("qual seu ano de nascimento? "))
    atual = date.today().year
    idade = (ano-atual )*-1
    print("o/a atleta tem {} anos.".format(idade))
    if idade > 0 and idade <= 14:
        print("sua classificação e mirim")
    elif idade >= 15 and idade <= 22:
        print("sua classificação e junior")
    elif idade > 23:
        print("sua clasificação e senior")
def quarentadois():
    t1 = float(input("primeiro segmento"))
    t2 = float(input("segundo segmento"))
    t3 = float(input("terceiro segmento"))
    if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
        print("os segmentos formam um triangulo")
        if t1 == t2 == t3:
            print("TRIANGULO EQUILATERO")
        elif t1 != t2 != t3 != t1:
            print("TRIANGULO ESCALENO")
        else:
            print("TRIANGULO ISOCELES")
    else:
        print("os sequimentos NÃO FORMAM UM TRIANGULO")
# quarenta e treis feito em aulapy1

def quarentaquatro():
    preco = float(input("qual o total das compras? "))
    print('''formas de pagamento
          [1] pagamento a vista dinheiro/cheque (10%of)
          [2] pagamento a vista no cartão (5%of)
          [3] parcelado em  2x no cartão (preço normal)
          [4] parcelado em 3x ou mais no cartão (20% de juros)''')
    forma = int(input("qual sera a forma? "))
    if forma == 1:
        descontocheck = preco - (preco*10/100)
        print("o seu preço de {} foi para {} com 10% de desconto com o pagamento em dinheiro/cheque".format(preco, descontocheck))
        comfi = input("vai pagar? S/N? ")
        if comfi == 'S' or comfi == 's':
            print("COMPRA FEITA " )
        else:
            print("COMPRA NEGADA " )
    elif forma == 2:
            descontocard = preco - (preco*5/100)
            print("o seu preço de {} foi para {} com 5% de desconto com o pagamento a vista no cartão".format(preco, descontocard))
            comfi = input("vai pagar? S/N? ")
            if comfi == 'S' or comfi == 's':
                print("COMPRA FEITA " )
            else:
                print("COMPRA NEGADA " )
    elif forma == 3:
        parcela = preco/2
        print("voce irar pagar duas parcelas de {}".format(parcela))
        comfi = input("vai pagar? S/N? ")
        if comfi == 'S' or comfi == 's':
            print("COMPRA FEITA " )
        else:
            print("COMPRA NEGADA " )
    elif forma == 4:
        preco2 = preco
        total = preco2 +preco*20/100
        quantarparcelas = int(input("quantas vezes vai parcelar?"))
        parcela = total/quantarparcelas
        print("voce irar pagar {} parcelas de {}".format(quantarparcelas,parcela))
        comfi = input("vai pagar? S/N? ")
        if comfi == 'S' or comfi == 's':
                print("COMPRA FEITA " )
        else:
                print("COMPRA NEGADA " )



 
if Desafio == 36:
    trintaseis()
elif Desafio == 37:
    trintasete()
elif Desafio == 38:
    trintaoito()
elif Desafio == 39:
    trintanove()
elif Desafio == 40:
    quarenta()
elif Desafio == 41:
    quarentaum()
elif Desafio == 42:
    quarentadois()
elif Desafio == 44:
    quarentaquatro()