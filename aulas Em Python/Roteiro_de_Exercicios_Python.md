# Roteiro dos seus exercícios JavaScript para refazer em Python

Analisei os arquivos da pasta `aulas de JavaScript`. A melhor ordem para estudar/refazer em Python não é exatamente a ordem alfabética: ela deve seguir a dificuldade dos conceitos.

Arquivos que não entram como exercício principal:
- `CSS fudido de bom.css`: estilo visual, não lógica JS.
- `aa.html` e `escolhedor de pagina.html`: parecem páginas de menu.
- `ordenação.html` e `xadrez.html`: estão vazios.

## Ordem recomendada

| Ordem | Arquivo JS | Conceito principal | Versão em Python |
|---:|---|---|---|
| 1 | `js1casa.html` | variáveis, operações e mensagens | `print`, variáveis, soma, multiplicação |
| 2 | `jsaula4.html` | `prompt`, fórmulas matemáticas | `input`, `int`, `float`, delta, IMC, área |
| 3 | `jsaula5.html` | pegar valores de campos e calcular | funções recebendo parâmetros |
| 4 | `jsaula6.html` | médias e conversões | média de 2, 3, 4 números; km/m |
| 5 | `jsaula7.html` | juntar nome e idade | concatenação e f-string |
| 6 | `jsaula8.html` | tamanho, maiúscula/minúscula, replace, slice | métodos de string |
| 7 | `jsaula10.html` | formatar data e números | `split`, `replace`, fatias de string |
| 8 | `jsaula11.html` | cortar texto, trocar palavra, formatar hora | `texto[inicio:fim]`, `replace` |
| 9 | `jsaula12.html` | usuário, CPF, login e senha | normalização de strings |
| 10 | `jsaula13.html` | iniciais de nome completo | `split` e índice `[0]` |
| 11 | `jsaula9.html` | contador/carrinho com regras | estado, preço total, validação |
| 12 | `jsaula14.html` | quiz com pontuação | lista de respostas e contador |
| 13 | `jsaula16.html` | criar elementos dinamicamente | criar lista de HTML/textos |
| 14 | `jsaula17.html` | `for` e par/ímpar | `range`, `%` |
| 15 | `jsaula18.html` | montar card e filtrar nome | função que retorna dicionário/string |
| 16 | `jsaula19.html` | repetir texto várias vezes | `for` acumulando linhas |
| 17 | `jsaula20.html` | sequências com `for` | contagens, intervalo, bingo/par |
| 18 | `jsaula21.html` | classificação por `if/elif` | IMC com faixas |
| 19 | `jsaula22.html` | número positivo/negativo e inteiro | comparações e checagem de decimal |
| 20 | `jsaula23.html` | fatorial e soma de intervalo | acumuladores |
| 21 | `jsaula24.html` | percorrer string e tabuada | loop em caracteres |
| 22 | `jsaula25.html` | classificar horário | slice de hora e `if` |
| 23 | `jsaula26.html` | trocar/remover/inserir em lista | `list[index]`, `pop`, `insert` |
| 24 | `jsauta26parte2.html` | operações completas de lista | `append`, `pop`, `insert`, `clear`, `len` |
| 25 | `jsaula27.html` | maior e menor da lista | loop procurando extremos |
| 26 | `jsaula28.html` | contar pares e ímpares | loop + `%` |
| 27 | `jsaula29.html` | dobrar, filtrar, contar, remover repetidos | transformação e filtro de lista |
| 28 | `trabalho_FINAL_PRA_for.html` | validação de e-mail | regras com string |
| 29 | `trabalho_final_pra_LISTA.html` | validador de senha | loop, ASCII/tipos de caractere |
| 30 | `trianguloDoCaceteDosInfernosDaPorraInfernar.html` | triângulo de Pascal | desafio com listas/loops |

## Como traduzir a lógica de JS para Python

| JavaScript | Python |
|---|---|
| `alert("oi")` | `print("oi")` |
| `prompt("digite")` | `input("digite: ")` |
| `parseInt(x)` | `int(x)` |
| `parseFloat(x)` | `float(x)` |
| `if (...) {}` | `if ...:` |
| `else if` | `elif` |
| `for(i=0; i<10; i++)` | `for i in range(10):` |
| `texto.length` | `len(texto)` |
| `texto.slice(a,b)` | `texto[a:b]` |
| `texto.includes("x")` | `"x" in texto` |
| `texto.replaceAll("a","b")` | `texto.replace("a", "b")` |
| `lista.push(x)` | `lista.append(x)` |
| `lista.pop()` | `lista.pop()` |
| `lista.shift()` | `lista.pop(0)` |
| `lista.unshift(x)` | `lista.insert(0, x)` |
| `lista.splice(i, 0, x)` | `lista.insert(i, x)` |
| `lista.splice(i, 1)` | `lista.pop(i)` |

## Exercícios equivalentes em Python

Use o arquivo `exercicios_python.py` como caderno de treino. Ele tem funções com `TODO` para você completar. A ideia é manter a mesma lógica dos seus exercícios, mas sem depender de HTML, botão ou `innerHTML`.

Sugestão de estudo:
1. Faça 3 a 5 exercícios por dia.
2. Teste cada função no final do arquivo.
3. Quando uma função funcionar, passe para a próxima.
4. Depois que terminar tudo, transforme as funções em um menu de terminal.

