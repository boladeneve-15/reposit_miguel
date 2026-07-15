print("""BEM VINDO AOS TESTES DE MIGUEL LUCAS EM PYTHON, esse e o começo de uma nova linguagem de progamação
    onde meu foco no final de tudo e saber
    ciencias de dados, eng de dados, automoção em python, e criação de IAs""")


print("====desafios====")
Desafio = int(input("qual o desafio? (de 22 a 27) "))

def vinteDois():
    Nome = str(input("QUAL O SEU NOME COMPLETO???: "))
    MAI = Nome.upper()
    Min = Nome.lower()
    quantidade = Nome.replace(" ", "")
    primeiro = Nome.split()
    print("seu nome e {} em maiusculo".format(MAI))
    print("seu nome e {} em minusculo".format(Min))
    print("seu nome tem {} letras".format(len(quantidade)))
    print("seu primeiro nome e {}".format(primeiro[0]))

def vintetres():
    numero = int(input("Digite um numero "))
    numero = str(numero)
    print("o seu numero tem a unidade de {}".format(numero[3]))
    print("o seu numero tem a dezena de {}".format (numero[2]))
    print("o seu numero tem a centena de {}".format(numero[1]))
    print("o seu numero tem a milhar de {}".format (numero[0]))

def VindeQuadro():
    cidade = str(input("em que cidade voce nasceu? "))
    cidade = cidade.lower()
    verificar = ('uberlandia' in cidade)
    print(verificar)

def vintecinco():
    Nome = str(input("QUAL O SEU NOME COMPLETO???: "))
    Nome = Nome.lower()
    verificar = ('silva' in Nome)
    print("seu nome tem silva? {}".format(verificar))

def VinteSeis():
    frase = str(input("digite uma frase pequena: "))
    print("a letra A apareceu {} vezes".format(frase.count('A')))
    print("a letra a apareceu {} vezes".format(frase.count('A')))
    print("a letra A apareceu na possição {}".format(frase.find('A')+1))
    print("a letra a apareceu na possição {}".format(frase.find('a')+1))
    print("a ultima letra A apareceu {} vezes".format(frase.rfind('A')+1))
    print("a ultima letra a apareceu {} vezes".format(frase.rfind('a')+1))

def vintesete():
    nome = str(input("qual e seu nome??: "))
    nome = nome.split()
    print("muito prazer em te conhecer seu primeiro nome e {}".format(nome[0]),) 
    print(" e seu ultimo nome e {}".format(nome[len(nome)-1]))


if Desafio == 22:
    vinteDois()

elif Desafio == 23:
    vintetres()
elif Desafio == 24:
    VindeQuadro()
elif Desafio == 25:
    vintecinco()
elif Desafio == 26:
    VinteSeis()
elif Desafio == 27:
    vintesete()

else: 
    print("ERRO")