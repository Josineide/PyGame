import pygame

#inicializa a aplicaçao
pygame.init()
#cor em rgb
cor = 0, 255, 0
#resolucao da tela
r = lar, alt = 640, 480
#carregamento da tela por meio das informacoes passadas
tela = pygame.display.set_mode(r)
tela.fill(cor)
#loop que mantem a tela aberta
while True:
    pygame.display.flip()