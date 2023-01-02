import pygame


class EndWindow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x, self.y = -600, 0

        self.speed = 3.33
        self.image = pygame.image.load('data/gameover.png')

        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self):
        self.rect.x += self.speed
        if self.rect.right == 600:
            self.speed = 0

    def update(self):
        self.move()


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 300), pygame.RESIZABLE)
    pygame.display.set_caption('GTA VI')
    clock = pygame.time.Clock()

    run = True

    end_window = pygame.sprite.GroupSingle(EndWindow())

    while run:
        screen.fill((0, 0, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        end_window.draw(screen)
        end_window.update()

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
