print("""BEM VINDO AOS TESTES DE MIGUEL LUCAS EM PYTHON, esse e o começo de uma nova linguagem de progamação
    onde meu foco no final de tudo e saber
    ciencias de dados, eng de dados, automoção em python, e criação de IAs""")

print("====desafios====")
Desafio = int(input("qual o desafio? (de 72 a 78) "))

def setentadois():
    contador = (
    "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze",
    "dezesseis")
    while True:
        num = int(input("digite um numero entre 0 a 20: "))
        if 0<=num <=20: 
            break
        print(f"voce digitou o numero {contador[num-1]}")
        condicao = str(input("quer continuar?: [S/N]: ")).upper()
        if condicao == 'S':
            num = int(input("digite um numero entre 0 a 20: "))
            if 0<=num <=20: 
                break
            
            else:
                print("saindo...")
                break

if Desafio == 72:
    setentadois()