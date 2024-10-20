import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

# Game variables
GRID_SIZE = 4
MARGIN = 20
FPS = 60

CARD_WIDTH = (SCREEN_WIDTH - (MARGIN * (GRID_SIZE + 1))) // GRID_SIZE
CARD_HEIGHT = (SCREEN_HEIGHT - (MARGIN * (GRID_SIZE + 1)) - 100) // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
SOFT_BLUE = (100, 150, 255)
SOFT_RED = (255, 100, 100)
SOFT_GREEN = (100, 255, 100)
SOFT_YELLOW = (255, 255, 150)
SOFT_CYAN = (100, 255, 255)
SOFT_MAGENTA = (255, 100, 255)
SOFT_PURPLE = (150, 100, 255)
SOFT_TEAL = (100, 200, 200)

colors = [SOFT_BLUE, SOFT_RED, SOFT_GREEN, SOFT_YELLOW, SOFT_CYAN, SOFT_MAGENTA, SOFT_PURPLE, SOFT_TEAL]
cards = colors * 2
random.shuffle(cards)

# Fonts
font = pygame.font.SysFont('Arial', 36)
large_font = pygame.font.SysFont('Arial', 72)

# Card class
class Card:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        self.color = color
        self.hidden = True
        self.hovered = False
        self.flip_progress = 0
        self.flipping = False

    def draw(self, surface):
        if self.flipping:
            self.flip_progress += 10
            if self.flip_progress >= 100:
                self.flipping = False
                self.flip_progress = 0
                self.hidden = False

        flip_ratio = abs(50 - self.flip_progress) / 50
        card_width = CARD_WIDTH * flip_ratio

        if self.hidden:
            pygame.draw.rect(surface, GRAY if self.hovered else WHITE,
                             (self.rect.x + (CARD_WIDTH - card_width) // 2, self.rect.y, card_width, CARD_HEIGHT),
                             border_radius=20)
            pygame.draw.rect(surface, BLACK,
                             (self.rect.x + (CARD_WIDTH - card_width) // 2, self.rect.y, card_width, CARD_HEIGHT), 2,
                             border_radius=20)
        else:
            pygame.draw.rect(surface, self.color,
                             (self.rect.x + (CARD_WIDTH - card_width) // 2, self.rect.y, card_width, CARD_HEIGHT),
                             border_radius=20)
            pygame.draw.rect(surface, BLACK,
                             (self.rect.x + (CARD_WIDTH - card_width) // 2, self.rect.y, card_width, CARD_HEIGHT), 2,
                             border_radius=20)

    def flip(self):
        self.flipping = True
        self.flip_progress = 0


# Set up grid of cards
grid = []
for i in range(GRID_SIZE):
    row = []
    for j in range(GRID_SIZE):
        card_color = cards.pop()
        x = MARGIN + j * (CARD_WIDTH + MARGIN)
        y = MARGIN + i * (CARD_HEIGHT + MARGIN) + 100
        row.append(Card(x, y, card_color))
    grid.append(row)

first_card = None
second_card = None
matched_cards = []
game_over = False
show_popup = False

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            if not first_card or not second_card:
                mouse_pos = event.pos
                for row in grid:
                    for card in row:
                        if card.rect.collidepoint(mouse_pos) and card.hidden and not card.flipping:
                            if not first_card:
                                first_card = card
                                first_card.flip()
                            elif not second_card and card != first_card:
                                second_card = card
                                second_card.flip()
                            break

    mouse_pos = pygame.mouse.get_pos()
    for row in grid:
        for card in row:
            if card.rect.collidepoint(mouse_pos) and card.hidden and not game_over:
                card.hovered = True
            else:
                card.hovered = False

    if first_card and second_card and not first_card.flipping and not second_card.flipping:
        if first_card.color == second_card.color:
            matched_cards.extend([first_card, second_card])
            first_card = None
            second_card = None
        else:
            pygame.time.delay(500)
            first_card.hidden = True
            second_card.hidden = True
            first_card = None
            second_card = None

    for row in grid:
        for card in row:
            if card not in matched_cards or not game_over:
                card.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
