import pygame
import random

pygame.init()
screen = pygame.display.set_mode((250, 250))
clock = pygame.time.Clock()

BRANCO = (255, 255, 255)
CINZA = (150, 150, 150)

TAMANHO_QUADRADO = 16

def desenhar_mapa(mapa, imagem):
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):
            tipo_de_arte = mapa[linha][coluna]
            x = coluna * TAMANHO_QUADRADO
            y = linha * TAMANHO_QUADRADO
            if tipo_de_arte.startswith('chao'):
                quadradinho = imagem.subsurface((0, 0, TAMANHO_QUADRADO, TAMANHO_QUADRADO))
            elif tipo_de_arte.startswith('parede'):
                quadradinho = imagem.subsurface((TAMANHO_QUADRADO, 0, TAMANHO_QUADRADO, TAMANHO_QUADRADO))
            screen.blit(quadradinho, (x, y))

def criar_mapa_aleatorio(linhas, colunas):
    return [['chao1' if random.random() < 0.7 else 'parede1' for _ in range(colunas)] for _ in range(linhas)]

def main():
    running = True
    imagem = pygame.image.load('C:\\Users\\julio\\PycharmProjects\\teste\\spritesheet.png')
    current_map = criar_mapa_aleatorio(16, 16)  # Define tamanho

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                current_map = criar_mapa_aleatorio(16, 16)  #Gera um novo aleatório

        screen.fill((0, 0, 0))  #Limpa tela
        desenhar_mapa(current_map, imagem)  #Desenha mapa novo
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
