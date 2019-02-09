import pygame,os


def load_image(name, path, color_key=None):
    fullname = os.path.join(path, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()

    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y,group):
        super().__init__(group)
        self.x = x
        self.y = y
        self.image = load_image('RedRect.png','images')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)
