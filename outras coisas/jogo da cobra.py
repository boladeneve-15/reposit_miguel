import turtle
import time
import random

# Configurações iniciais do jogo
atraso = 0.1
pontos = 0
maior_pontuacao = 0

# Configuração da janela (Tela)
janela = turtle.Screen()
janela.title("O Melhor Jogo da Cobrinha em Python")
janela.bgcolor("black")
janela.setup(width=600, height=600)
janela.tracer(0)  # Desliga as atualizações automáticas de tela para evitar lag

# Cabeça da Cobra
cabeca = turtle.Turtle()
cabeca.speed(0)
cabeca.shape("square")
cabeca.color("green")
cabeca.penup()
cabeca.goto(0, 0)
cabeca.direction = "stop"

# Comida da Cobra
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

# Segmentos do corpo da cobra (lista vazia no início)
corpo = []

# Placar de Pontuação
placar = turtle.Turtle()
placar.speed(0)
placar.shape("square")
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Pontuação: 0  |  Recorde: 0", align="center", font=("Courier", 18, "normal"))

# Funções de Movimentação
def ir_para_cima():
    if cabeca.direction != "down":
        cabeca.direction = "up"

def ir_para_baixo():
    if cabeca.direction != "up":
        cabeca.direction = "down"

def ir_para_esquerda():
    if cabeca.direction != "right":
        cabeca.direction = "left"

def ir_para_direita():
    if cabeca.direction != "left":
        cabeca.direction = "right"

def mover():
    if cabeca.direction == "up":
        y = cabeca.ycor()
        cabeca.sety(y + 20)

    if cabeca.direction == "down":
        y = cabeca.ycor()
        cabeca.sety(y - 20)

    if cabeca.direction == "left":
        x = cabeca.xcor()
        cabeca.setx(x - 20)

    if cabeca.direction == "right":
        x = cabeca.xcor()
        cabeca.setx(x + 20)

# Mapeamento do teclado
janela.listen()
janela.onkeypress(ir_para_cima, "Up")
janela.onkeypress(ir_para_baixo, "Down")
janela.onkeypress(ir_para_esquerda, "Left")
janela.onkeypress(ir_para_direita, "Right")

# Loop Principal do Jogo
while True:
    janela.update()

    # 1. Verificar colisão com as bordas da tela (Game Over)
    if cabeca.xcor() > 290 or cabeca.xcor() < -290 or cabeca.ycor() > 290 or cabeca.ycor() < -290:
        time.sleep(1)
        cabeca.goto(0, 0)
        cabeca.direction = "stop"

        # Esconder os segmentos do corpo antigo
        for segmento in corpo:
            segmento.goto(1000, 1000)
        corpo.clear()

        # Resetar pontuação
        pontos = 0
        atraso = 0.1
        placar.clear()
        placar.write(f"Pontuação: {pontos}  |  Recorde: {maior_pontuacao}", align="center", font=("Courier", 18, "normal"))

    # 2. Verificar colisão com a comida
    if cabeca.distance(comida) < 20:
        # Mover a comida para um lugar aleatório
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        comida.goto(x, y)

        # Adicionar um novo segmento ao corpo da cobra
        novo_segmento = turtle.Turtle()
        novo_segmento.speed(0)
        novo_segmento.shape("square")
        novo_segmento.color("lightgreen")
        novo_segmento.penup()
        corpo.append(novo_segmento)

        # Aumentar a velocidade do jogo conforme ganha pontos
        atraso -= 0.003

        # Atualizar a pontuação
        pontos += 10
        if pontos > maior_pontuacao:
            maior_pontuacao = points = pontos

        placar.clear()
        placar.write(f"Pontuação: {pontos}  |  Recorde: {maior_pontuacao}", align="center", font=("Courier", 18, "normal"))

    # 3. Mover o corpo da cobra (em ordem reversa)
    for index in range(len(corpo) - 1, 0, -1):
        x = corpo[index - 1].xcor()
        y = corpo[index - 1].ycor()
        corpo[index].goto(x, y)

    # Mover o primeiro segmento para onde a cabeça estava
    if len(corpo) > 0:
        x = cabeca.xcor()
        y = cabeca.ycor()
        corpo[0].goto(x, y)

    mover()

    # 4. Verificar colisão da cabeça com o próprio corpo
    for segmento in corpo:
        if segmento.distance(cabeca) < 20:
            time.sleep(1)
            cabeca.goto(0, 0)
            cabeca.direction = "stop"
            
            for seg in corpo:
                seg.goto(1000, 1000)
            corpo.clear()

            pontos = 0
            atraso = 0.1
            placar.clear()
            placar.write(f"Pontuação: {pontos}  |  Recorde: {maior_pontuacao}", align="center", font=("Courier", 18, "normal"))

    time.sleep(atraso)

janela.mainloop()