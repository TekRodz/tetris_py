import pygame
from tetris import Tetris

#verifie si tout les modules sont charges
module_charge = pygame.init()
print(module_charge)

colors = [(0, 0, 0),(120, 37, 179),(100, 179, 179),(80, 34, 22),(80, 134, 22),(180, 34, 22),(180, 34, 122)]

#creee une fenetre 
#petit ecran
ecran = pygame.display.set_mode((500,500))
pygame.display.set_caption("Tetris")
#boucle de jeu
loop = True
tetris = Tetris(20, 10)
fps = 25
clock = pygame.time.Clock()
counter = 0
pressing_down = False

while loop:
    # pygame event
    if tetris.tetriminos is None:
        tetris.new_figure()
    counter += 1
    if counter > 100000:
        counter = 0

    if counter % (fps // 2) == 0 or pressing_down:
        if tetris.state == "start":
            tetris.go_down()
    
    for event in pygame.event.get():
        # event input clavier 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                tetris.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                tetris.go_side(-1)
            if event.key == pygame.K_RIGHT:
                tetris.go_side(1)
            if event.key == pygame.K_SPACE:
                tetris.go_bottom()
            if event.key == pygame.K_ESCAPE:
                tetris.__init__(20, 10)
            if event.key == pygame.K_j:
                loop = False 
        
        if event.type == pygame.QUIT:
            loop = False

    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

    ecran.fill((255,255,255))

    for i in range(tetris.height):
        for j in range(tetris.width):
            pygame.draw.rect(ecran, (128, 128, 128), [tetris.x + tetris.zoom * j, tetris.y + tetris.zoom * i, tetris.zoom, tetris.zoom], 1)
            if tetris.field[i][j] > 0:
                pygame.draw.rect(ecran, colors[tetris.field[i][j]],
                                 [tetris.x + tetris.zoom * j + 1, tetris.y + tetris.zoom * i + 1, tetris.zoom - 2, tetris.zoom - 1])
    
    if tetris.tetriminos is not None:
        for i in range(4):
            for j in range(4):
                if i * 4 + j in tetris.tetriminos.image():
                    pygame.draw.rect(ecran, colors[tetris.tetriminos.color],[tetris.x + tetris.zoom * (j + tetris.tetriminos.x) + 1, tetris.y + tetris.zoom * (i + tetris.tetriminos.y) + 1, tetris.zoom - 2, tetris.zoom - 2])

    font = pygame.font.SysFont('Calibri', 65, True, False)
    text_game_over = font.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font.render("Appuyer sur ESC", True, (255, 215, 0))

    if tetris.state == "gameover":
        ecran.blit(text_game_over, [20, 200])
        ecran.blit(text_game_over1, [25, 265])

    #affichage ecran
    pygame.display.flip()
    clock.tick(fps)

# vide le cache 
pygame.quit()