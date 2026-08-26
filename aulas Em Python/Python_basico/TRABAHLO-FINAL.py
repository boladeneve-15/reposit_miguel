acumulador = 1
base = {
    "id": 1,
    "nome": "",
    "marca":"",
     "tipo": "",
     "modelo": "",
}
informacoes = [

]

def busca(x):
    possicao = -1
    for i in range(0, len(informacoes),1):
        if informacoes[i]["id"] == x:
            return i
    return possicao

def CREATE():
    nome = str(input("NOME "))
    marca = str(input("MARCA "))
    tipo = str(input("TIPO "))
    modelo = str(input("MODELO "))
    for i in range(acumulador, i+1)