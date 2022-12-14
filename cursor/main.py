import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
    pygame.display.set_caption('GTA VI')
    clock = pygame.time.Clock()

    run = True

    pygame.mouse.set_visible(False)
    new_image = pygame.image.load('data/arrow.png').convert_alpha()

    while run:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if pygame.mouse.get_focused():
            screen.blit(new_image, (pygame.mouse.get_pos()))
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
