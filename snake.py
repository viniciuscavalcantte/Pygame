import pygame
from pygame.locals import *
import random

tamanho_tela = (600, 600)
passo = 10


def colisao(pos1, pos2):
    return pos1 == pos2


def off_limits(pos):
    if 0 <= pos[0] < tamanho_tela[0] and 0 <= pos[1] < tamanho_tela[1]:
        return False
    else:
        return True


def random_on_grid():
    x = random.randint(0, tamanho_tela[0])
    y = random.randint(0, tamanho_tela[1])
    return x // passo * passo, y // passo * passo


pygame.init()
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Jogo da Cobrinha')

cobrinha_pos = [(250, 50), (260, 50), (270, 50)]
cobrinha_sup = pygame.Surface((passo, passo))
cobrinha_sup.fill((255, 255, 255))
cobrinha_dir = K_LEFT

maca_sup = pygame.Surface((passo, passo))
maca_sup.fill((255, 0, 0))
maca_pos = random_on_grid()


def restart_game():
    global cobrinha_pos
    global maca_pos
    global cobrinha_dir
    cobrinha_pos = [(250, 50), (260, 50), (270, 50)]
    cobrinha_dir = K_LEFT
    maca_pos = random_on_grid()


while True:
    pygame.time.Clock().tick(15)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                cobrinha_dir = event.key

    tela.blit(maca_sup, maca_pos)

    if colisao(maca_pos, cobrinha_pos[0]):
        cobrinha_pos.append((-10, -10))
        maca_pos = random_on_grid()

    for pos in cobrinha_pos:
        tela.blit(cobrinha_sup, pos)

    for i in range(len(cobrinha_pos) - 1, 0, -1):
        if colisao(cobrinha_pos[0], cobrinha_pos[i]):
            restart_game()
            break
        cobrinha_pos[i] = cobrinha_pos[i - 1]

    if off_limits(cobrinha_pos[0]):
        restart_game()

    if cobrinha_dir == K_UP:
        cobrinha_pos[0] = (cobrinha_pos[0][0], cobrinha_pos[0][1] - passo)
    elif cobrinha_dir == K_DOWN:
        cobrinha_pos[0] = (cobrinha_pos[0][0], cobrinha_pos[0][1] + passo)
    elif cobrinha_dir == K_LEFT:
        cobrinha_pos[0] = (cobrinha_pos[0][0] - passo, cobrinha_pos[0][1])
    elif cobrinha_dir == K_RIGHT:
        cobrinha_pos[0] = (cobrinha_pos[0][0] + passo, cobrinha_pos[0][1])

    pygame.display.update()