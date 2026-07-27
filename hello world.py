import os
import pygame

# Initialize Pygame and screen dimensions
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Base path for assets in the same directory as this script
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Initialize display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

# Load and scale images directly with fallback assets

def load_image(name, size, alpha=False, fallback_color=None):
    path = os.path.join(BASE_PATH, name)
    if os.path.exists(path):
        image = pygame.image.load(path)
        image = image.convert_alpha() if alpha else image.convert()
        return pygame.transform.scale(image, size)

    surface = pygame.Surface(size, pygame.SRCALPHA if alpha else 0)
    if fallback_color is not None:
        surface.fill(fallback_color)
    return surface

background_image = load_image(
    'background.png', (SCREEN_WIDTH, SCREEN_HEIGHT), alpha=False,
    fallback_color=pygame.Color('skyblue'))

penguin_image = load_image(
    'penguin.png', (200, 200), alpha=True,
    fallback_color=pygame.Color('white'))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2,
    SCREEN_HEIGHT // 2 - 30))

# Initialize font, render text, and set text position
text = pygame.font.Font(None, 36).render('Hello World ', True,
    pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()