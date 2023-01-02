import pygame


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 100
        self.y = 100

        self.speed = 1

        self.image = pygame.image.load('data/car2.png').convert_alpha()

        self.rect = self.image.get_rect(midbottom=(self.x, self.y))

    def move(self):
        self.rect.x += self.speed

        if self.rect.right == 500:
            self.image = pygame.transform.flip(self.image, True, False)
            self.speed = -1

        elif self.rect.left == 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.speed = 1

    def update(self):
        self.move()


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
    pygame.display.set_caption('GTA VI')
    clock = pygame.time.Clock()

    run = True

    car = pygame.sprite.GroupSingle()
    car.add(Car())

    while run:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        car.draw(screen)
        car.update()

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
