#   resultado2.innerHTML = "";
#       contador = 0;
#       x = parseInt(segundonumero.value);
#       divisores = [];
#       for (i = 2; i < x / 2 + 1; i++) {
#         // console.log(i)
#         resto = x % i;
#         if (resto == 0) {
#           contador++;
#           divisores.push(i);
#         }
#       }
#       if (contador == 0) {
#         resultado2.innerHTML = "numero primo";
#       } else if (contador != 0) {
#         resultado2.innerHTML = `numero não primo e seus divisores são ${divisores}`;
#       }
def primos(x):
    contador = 0
    i = 2
    for i in range(2,x, i+1):

        resto = x % i
        if resto == 0:
            contador +1 

    if contador == 2:
      return True
    else:
        return False

def naoprimos():
    lista = []
    contador = 0
    i = 2
    x = int(input("digite um numero e veja se ele e primo ou não "))
    for i in range(2,x, i+1):

        resto = x % i
        if resto == 0:
            contador +1 
            lista.append(i)


    if contador == 2:
        print(f"{x} e um numero primo e seus divisores são {lista}")
    else:
        print(f"{x} não e primo")
naoprimos()