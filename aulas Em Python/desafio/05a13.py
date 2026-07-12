print("""BEM VINDO AOS TESTES DE MIGUEL LUCAS EM PYTHON, esse e o começo de uma nova linguagem de progamação
    onde meu foco no final de tudo e saber
        ciencias de dados, eng de dados, automoção em python, e criação de IAs""")
print("====desafios====")
Desafio = int(input("qual o desafio? (de 5 a 13) "))

def cinco():
    numero = int(input("qual o numero? "))
    print("o seu numero e {}, o sucessor dele e {}, e o antecesor dele e  {}".format(numero, (numero+1), (numero -1)))

def seis():
    numero = int(input("qual o numero? "))
    print("o seu numero e {}, o dobro do seu numero e {}, o triplo do seu numero e {} e a raiz do seu numero e {:.2f}".format(numero, (numero*2), (numero*3), pow(numero,(1/2))))

def sete():
    numero1 = float(input(" qual a nota da primeira prova?  "))
    numero2 = float(input(" qual a nota da segunda prova?  "))
    media = (numero1 + numero2 )/2
    print(media)

def oito():
    valor = float(input(" qual a distancia em M? "))
    M = valor
    KM = valor/1000
    HM = valor/100
    Dam = valor/10
    Dm = valor*10
    Cm = valor*100
    Mm  =  valor*1000

    print(" a distancia em M e {}".format  (M))
    print(" a distancia em KM e {}".format (KM))
    print(" a distancia em HM e {}".format (HM))
    print(" a distancia em Dam e {}".format(Dam))
    print(" a distancia em Dm e {}".format (Dm))
    print(" a distancia em Cm e {}".format (Cm))
    print(" a distancia em Mm e {}".format (Mm))

def nove():
    valor = int(input("digite um numero para ver a tabuada "))
    print("=========TABUADA=========")
    print("{} x  {}  =  {}".format(valor, 1, valor*1 ))
    print("{} x  {}  =  {}".format(valor, 2, valor*2 ))
    print("{} x  {}  =  {}".format(valor, 3, valor*3 ))
    print("{} x  {}  =  {}".format(valor, 4, valor*4 ))
    print("{} x  {}  =  {}".format(valor, 5, valor*5 ))
    print("{} x  {}  =  {}".format(valor, 6, valor*6 ))
    print("{} x  {}  =  {}".format(valor, 7, valor*7 ))
    print("{} x  {}  =  {}".format(valor, 8, valor*8 ))
    print("{} x  {}  =  {}".format(valor, 9, valor*9 ))
    print("{} x  {}  =  {}".format(valor, 10, valor*10))
    print("=========================")

def dez():
    OqueFazer = int(input("Oque deseja fazer? 1- Real para Dolar 2- Dolar pra real "))
    if OqueFazer == 1:
        reais = float(input("quantos R$ vc tem? "))
        RealParaDolar = reais / 5.20
        print("Voce Tem {:.2f}U$".format(RealParaDolar))
    else: 
        Dolares = float(input("quantos U$ vc tem? "))
        DolarParaReal = Dolares * 5.20
        print("voce tem {:.2f}R$".format(DolarParaReal))
def onze():
    largura = float(input("quantos M tem  a largura da sua parede? "))
    altura  = float(input("quantos M tem a altura da sua parede? "))
    area = largura*altura
    tinta = area/2
    print("sua parede tem a Dimensao de {:.2f}x{:.2f} e a area dela e de {:.2f}m²".format(largura, altura, area))
    print("para pintar essa parede voce ira precisar de {:.2f}L de tinta".format(tinta))

def doze():
    produdo = float(input("qual e o preço de seu produto? "))
    desconto = float(input("quanto de desconto no seu produdo? "))
    valor = produdo - (produdo*desconto/100)
    print("o seu produdo com o descondo de {}% tem o valor de {:.2f}".format(desconto, valor))

def treze(): 
    salario = float(input("qual e o salario do seu empregado? "))
    aumento= float(input("qual e o o bonus em % que o senhor vai dar a ele? "))
    total = salario + (salario*aumento/100)
    print("o seu empregado estava com {:.2f}R$ de salario e com o aumento de {}% ele vai começar a receber {:.2f}R$".format(salario, aumento, total))

if Desafio == 5:
    cinco()

elif Desafio == 6:
    seis()

elif Desafio == 7:
    sete()

elif Desafio == 8:
    oito()

elif Desafio == 9:
    nove()

elif Desafio == 10:
    dez()

elif Desafio == 11:
    onze()

elif Desafio == 12:
    doze()

elif Desafio == 13:
    treze()


else:
    print("ERRO digite um numero de 5 a 13")