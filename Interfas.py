import pygame
import sys
from AlgoritmoGenetico import genetic_algorithm

# Inicializar Pygame
pygame.init()

# Configuración de ventana
size = width, height = 480, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("8 Reinas")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
QUEEN_COLOR = (255, 0, 0)

# Cargar imagen de reina o dibujar una simple
queen = pygame.Surface((50, 50))
pygame.draw.circle(queen, QUEEN_COLOR, (25, 25), 20)

def draw_board(solution):
    block_size = width // 8
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * block_size, row * block_size, block_size, block_size))
            if solution[row] == col:
                screen.blit(queen, (col * block_size + 5, row * block_size + 5))

def main(solution):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        draw_board(solution)
        pygame.display.flip()

if __name__ == "__main__":
    sol = genetic_algorithm()
    print("Solución encontrada:", sol)
    main(sol)
