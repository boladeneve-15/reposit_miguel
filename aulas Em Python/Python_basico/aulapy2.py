# objetivo calculadora
# REGRAS
# 1. A calculadora deve somar dois números
# 2. A calculadora deve subtrair dois números
# 3. A calculadora deve multiplicar dois números
# 4. A calculadora deve dividir dois números

print("==== CALCULADORA ==== ")
oqueFazer = input (""
"1 - Somar" \
" "

"2 - Subtrair" \
" "
"3 - Multiplicar" \
" "
"4 - Dividir")


if oqueFazer == '1':
    def somar(): 
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 + numero2
        print("O resultado da soma é:", resultado)  
        somar()

if oqueFazer == '2':
       def subtrair():
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 - numero2
        print("O resultado da subtraição é:", resultado)  
        subtrair()
if oqueFazer == '3':
    def multiplicar():
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 * numero2
        print("O resultado da multiplicação é:", resultado)  
        multiplicar()
if oqueFazer == '4':
    def dividir():
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 / numero2
        print("O resultado da divisao é:", resultado)  
        dividir()