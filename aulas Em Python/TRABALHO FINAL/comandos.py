acumulador = 1
base = {
    "id": 1,
    "nome": "",
    "marca": "",
    "tipo": "",
    "modelo": "",
}
informacoes = []


def busca(x):
    possicao = -1
    for i in range(0, len(informacoes), 1):
        if informacoes[i]["id"] == x:
            return i
    return possicao


def CREATE():
    global acumulador
    Nome = str(input("NOME "))
    Marca = str(input("MARCA "))
    Tipo = str(input("TIPO "))
    Modelo = str(input("MODELO "))
    i = acumulador
    for i in range(acumulador, i + 1, i + 1):
        informacoes.append(
            {
                "id": acumulador,
                "nome": Nome,
                "marca": Marca,
                "tipo": Tipo,
                "modelo": Modelo,
            }
        )
        acumulador += 1 
        break


def READ_ALL():
    print(informacoes)
def READ_ID():
    valor = int(input("DIGITE O ID"))
    possicao = busca(valor)
    if possicao == -1:
        print("ERRO ESSE ID NÃO EXISTE")
    if possicao != -1:
        print(informacoes[possicao])
def UPDATE():
    valor = int(input("ID a atualizar: "))
    posicao = busca(valor)
    if posicao == -1:
        print("ERRO ID NÃO EXISTE")
        return

    nome = input("NOVO NOME ")
    marca = input("NOVA MARCA ")
    tipo = input("NOVO TIPO ")
    modelo = input("NOVO MODELO ")

    informacoes[posicao] = {
        "id": valor,  # ID não muda, igual você pediu
        "nome": nome,
        "marca": marca,
        "tipo": tipo,
        "modelo": modelo,
    }


def DELETE():
    valor = int(input("ID a deletar: "))
    posicao = busca(valor)
    if posicao == -1:
        print("ERRO ID NÃO EXISTE")
        return
    informacoes.pop(posicao)