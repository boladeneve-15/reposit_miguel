
#    resultado.innerHTML =  ""
#         lista = []
#         inicio =  parseInt(comeco.value)
#         inter =   parseInt(intervalo.value)
#         maximo =  parseInt(quantos.value)

#         for(i= 1; i<maximo; i++){
#         aleatorios = parseInt(Math.random() *(inter - inicio) + inicio)
#         lista.push(aleatorios)
#         resultado.innerHTML =  lista

#     }
import random

lista = []
inicio = int(input("Qual número quer começar? "))
inter = int(input("Qual intervalo ter (passo)? "))
maximo = int(input("Qual a quantidade máxima de números? "))

=
for i in range(1, maximo):
    aleatorio = random.randrange(inicio, 100, inter)  
    lista.append(aleatorio)

print(lista)


    