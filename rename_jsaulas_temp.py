import os

base = r'c:\Users\mugue\OneDrive\Documentos\GitHub\reposit_miguel\aulas de JavaScript'
mapping = {
    'jsaula4.html': 'formulas.html',
    'jsaula5.html': 'formulas-input.html',
    'jsaula6.html': 'medias-e-conversoes.html',
    'jsaula7.html': 'nome-e-idade.html',
    'jsaula8.html': 'manipulacao-de-texto.html',
    'jsaula9.html': 'contador-de-compras.html',
    'jsaula10.html': 'formatacao-de-data.html',
    'jsaula11.html': 'texto-e-hora.html',
    'jsaula12.html': 'usuario-e-cpf.html',
    'jsaula13.html': 'iniciais.html',
    'jsaula14.html': 'quiz.html',
    'jsaula16.html': 'criar-elementos.html',
    'jsaula17.html': 'for-e-par-impar.html',
    'jsaula18.html': 'card-e-filtro.html',
    'jsaula19.html': 'repeticao-de-texto.html',
    'jsaula20.html': 'sequencias-for.html',
    'jsaula21.html': 'imc-classificacao.html',
    'jsaula22.html': 'tipo-de-numero.html',
    'jsaula23.html': 'fatorial-e-soma.html',
    'jsaula24.html': 'strings-e-tabuada.html',
    'jsaula25.html': 'hora-e-periodo.html',
    'jsaula26.html': 'editar-lista.html',
    'jsauta26parte2.html': 'lista-operacoes.html',
    'jsaula27.html': 'maior-menor-lista.html',
    'jsaula28.html': 'pares-e-impares.html',
    'jsaula29.html': 'transformacoes-de-lista.html',
}

os.chdir(base)
for old, new in mapping.items():
    if os.path.exists(old):
        os.rename(old, new)
        print(f"RENAMED {old} -> {new}")
    else:
        print(f"MISSING {old}")
