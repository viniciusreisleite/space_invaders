import pygame
import random
import os
import math

# Inicializando o Pygame
pygame.init()

# Configurações da tela
tela_largura = 800
tela_altura = 600
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Space Invaders Simplificado")

# Configurações de cores
preto = (0, 0, 0)
branco = (255, 255, 255)

# Função para carregar imagens
def carregar_imagem(nome_arquivo):
    caminho_completo = os.path.join(os.path.dirname(__file__), nome_arquivo)
    if not os.path.exists(caminho_completo):
        raise FileNotFoundError(f"Arquivo '{nome_arquivo}' não encontrado no diretório '{caminho_completo}'")
    return pygame.image.load(caminho_completo)

# Configurações do jogador
player_img = carregar_imagem('player.png')
player_x = 370
player_y = 480
player_x_mudanca = 0

# Configurações do invasor
invasor_img = carregar_imagem('invader.png')
invasor_x = []
invasor_y = []
invasor_x_mudanca = []
invasor_y_mudanca = 40
num_invasores = 6

for i in range(num_invasores):
    invasor_x.append(random.randint(0, 736))
    invasor_y.append(random.randint(50, 150))
    invasor_x_mudanca.append(0.3)

# Configurações do laser
laser_img = carregar_imagem('laser.png')
laser_x = 0
laser_y = 480
laser_y_mudanca = 0.5
laser_visivel = False

# Pontuação
pontuacao = 0
fonte = pygame.font.Font('freesansbold.ttf', 32)

# Vidas
vidas = 3

# Pontuação necessária para vencer
pontuacao_vitoria = 50

def mostrar_pontuacao(x, y):
    texto = fonte.render(f"Pontuação: {pontuacao}", True, branco)
    tela.blit(texto, (x, y))

def mostrar_vidas(x, y):
    texto = fonte.render(f"Vidas: {vidas}", True, branco)
    tela.blit(texto, (x, y))

# Função para desenhar o jogador
def jogador(x, y):
    tela.blit(player_img, (x, y))

# Função para desenhar o invasor
def invasor(x, y, i):
    tela.blit(invasor_img, (x, y))

# Função para disparar o laser
def disparar_laser(x, y):
    global laser_visivel
    laser_visivel = True
    tela.blit(laser_img, (x + 16, y + 10))

# Função para detectar colisão
def colisao(invasor_x, invasor_y, laser_x, laser_y):
    distancia = math.sqrt(math.pow(invasor_x - laser_x, 2) + math.pow(invasor_y - laser_y, 2))
    return distancia < 27

# Função para mostrar a tela inicial
def tela_inicio():
    tela.fill(preto)
    fonte_inicio = pygame.font.Font('freesansbold.ttf', 64)
    texto_inicio = fonte_inicio.render("Pressione ENTER para Jogar", True, branco)
    tela.blit(texto_inicio, (50, 250))
    pygame.display.update()
    
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    esperando = False

# Função para mostrar a tela de fim de jogo
def tela_fim_jogo():
    tela.fill(preto)
    fonte_fim = pygame.font.Font('freesansbold.ttf', 64)
    texto_fim = fonte_fim.render("GAME OVER", True, branco)
    texto_pontuacao_final = fonte.render(f"Pontuação Final: {pontuacao}", True, branco)
    tela.blit(texto_fim, (250, 250))
    tela.blit(texto_pontuacao_final, (250, 350))
    pygame.display.update()
    
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    esperando = False

# Função para mostrar a tela de vitória
def tela_vitoria():
    tela.fill(preto)
    fonte_vitoria = pygame.font.Font('freesansbold.ttf', 64)
    texto_vitoria = fonte_vitoria.render("VOCÊ VENCEU!", True, branco)
    texto_pontuacao_final = fonte.render(f"Pontuação Final: {pontuacao}", True, branco)
    tela.blit(texto_vitoria, (200, 250))
    tela.blit(texto_pontuacao_final, (250, 350))
    pygame.display.update()
    
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    esperando = False

# Função principal do jogo
def jogo():
    global player_x, player_x_mudanca, laser_x, laser_y, laser_visivel, invasor_x, invasor_y, invasor_x_mudanca, pontuacao, vidas, num_invasores

    # Loop do jogo
    rodando = True
    while rodando:
        # Fundo da tela
        tela.fill(preto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            # Movimento do jogador
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    player_x_mudanca = -0.3
                if evento.key == pygame.K_RIGHT:
                    player_x_mudanca = 0.3
                if evento.key == pygame.K_SPACE:
                    if not laser_visivel:
                        laser_x = player_x
                        disparar_laser(laser_x, laser_y)

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    player_x_mudanca = 0

        # Atualizar posição do jogador
        player_x += player_x_mudanca
        if player_x <= 0:
            player_x = 0
        elif player_x >= 736:
            player_x = 736

        # Atualizar posição dos invasores
        for i in range(num_invasores):
            invasor_x[i] += invasor_x_mudanca[i]
            if invasor_x[i] <= 0:
                invasor_x_mudanca[i] = 0.3
                invasor_y[i] += invasor_y_mudanca
            elif invasor_x[i] >= 736:
                invasor_x_mudanca[i] = -0.3
                invasor_y[i] += invasor_y_mudanca

            # Verificar se o invasor chegou à linha inferior
            if invasor_y[i] > player_y:
                vidas -= 1
                invasor_y[i] = random.randint(50, 150)
                if vidas == 0:
                    tela_fim_jogo()
                    return

            # Verificar colisão
            if colisao(invasor_x[i], invasor_y[i], laser_x, laser_y):
                laser_y = 480
                laser_visivel = False
                pontuacao += 1
                invasor_x[i] = random.randint(0, 736)
                invasor_y[i] = random.randint(50, 150)
                # Aumentar dificuldade ao longo do tempo
                if pontuacao % 10 == 0:
                    for j in range(num_invasores):
                        invasor_x_mudanca[j] += 0.1
                # Verificar vitória
                if pontuacao >= pontuacao_vitoria:
                    tela_vitoria()
                    return

            invasor(invasor_x[i], invasor_y[i], i)

        # Movimento do laser
        if laser_y <= 0:
            laser_y = 480
            laser_visivel = False
        if laser_visivel:
            disparar_laser(laser_x, laser_y)
            laser_y -= laser_y_mudanca

        jogador(player_x, player_y)
        mostrar_pontuacao(10, 10)
        mostrar_vidas(10, 50)
        pygame.display.update()

# Mostrar tela de início
tela_inicio()

# Iniciar o jogo
jogo()

# Sair do Pygame
pygame.quit()
