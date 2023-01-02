import pygame
import random


class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x, self.y = random.randint(60, 430), random.randint(60, 430)
        self.image = pygame.image.load('data/bomb.png')
        self.image_boom = pygame.image.load('data/boom.png')

        self.rect = self.image.get_rect(center=(self.x, self.y))

    def click(self, pos):
        if self.rect.collidepoint(pos):
            self.image = self.image_boom


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
    pygame.display.set_caption('GTA VI')
    clock = pygame.time.Clock()

    run = True

    bombs = pygame.sprite.Group()
    for i in range(20):
        bombs.add(Bomb())

    while run:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for bomb in bombs:
                    bomb.click(event.pos)

        bombs.draw(screen)
        bombs.update()

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
