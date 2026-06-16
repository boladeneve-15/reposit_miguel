import random
import os

# Função para limpar a tela do terminal e deixar o jogo bonito
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Desenha o tabuleiro no terminal
def desenhar_tabuleiro(tabuleiro):
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---|---|---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---|---|---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")

# Verifica se alguém ganhou
def checar_vitoria(tab, jogador):
    condicoes_vitoria = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Colunas
        [0, 4, 8], [2, 4, 6]             # Diagonais
    ]
    for condicao in condicoes_vitoria:
        if tab[condicao[0]] == tab[condicao[1]] == tab[condicao[2]] == jogador:
            return True
    return False

# Jogada do Computador (IA Simples)
def jogada_computador(tabuleiro):
    # 1. Se o computador puder ganhar na próxima jogada, ele ganha
    for i in range(9):
        if tabuleiro[i] == " ":
            copia = tabuleiro.copy()
            copia[i] = "O"
            if checar_vitoria(copia, "O"):
                return i

    # 2. Se o jogador for ganhar na próxima jogada, o computador bloqueia
    for i in range(9):
        if tabuleiro[i] == " ":
            copia = tabuleiro.copy()
            copia[i] = "X"
            if checar_vitoria(copia, "X"):
                return i

    # 3. Se não houver jogada imediata, escolhe um espaço vazio aleatório
    espacos_vazios = [i for i, x in enumerate(tabuleiro) if x == " "]
    return random.choice(espacos_vazios)

# JOGO PRINCIPAL
def jogar():
    # Preenche o tabuleiro com números de 1 a 9 para guiar o jogador
    tabuleiro = [" "] * 9
    
    limpar_tela()
    print("=== JOGO DA VELHA EM PYTHON ===")
    print("Você é o 'X' e o Computador é o 'O'")
    print("Escolha as posições de 1 a 9 baseando-se no teclado numérico.\n")
    
    while True:
        desenhar_tabuleiro(tabuleiro)
        
        # Vez do Jogador
        vez_do_jogador = True
        while vez_do_jogador:
            try:
                jogada = int(input("\nSua vez (1-9): ")) - 1
                if 0 <= jogada <= 8 and tabuleiro[jogada] == " ":