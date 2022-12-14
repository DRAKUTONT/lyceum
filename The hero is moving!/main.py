import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 100

        self.image = pygame.image.load('data/creature.png').convert_alpha()

        self.rect = self.image.get_rect(midbottom=(self.x, self.y))

    def player_control(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.rect.x -= 10

        elif key[pygame.K_RIGHT]:
            self.rect.x += 10

        elif key[pygame.K_UP]:
            self.rect.y -= 10

        elif key[pygame.K_DOWN]:
            self.rect.y += 10

    def update(self):
        self.player_control()


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
    pygame.display.set_caption('GTA VI')
    clock = pygame.time.Clock()

    run = True

    player = pygame.sprite.GroupSingle()
    player.add(Player())

    while run:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.draw(screen)
        player.update()

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
