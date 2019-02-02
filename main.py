import pygame
import os

pygame.init()
pygame.key.set_repeat(200, 70)

clock = pygame.time.Clock()
screen_size = (1922 // 1.5, 1082 // 1.5)
FPS = 10
screenWidth = int(screen_size[0])
screenHeight = int(screen_size[1])
screen_size = (screenWidth, screenHeight)
win = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Battle of warriors')
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

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




class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.is_loaded = False
        self.frames = []
        self.cur_frame = 0
        self.image = None
        self.rect = None
        self.x = x
        self.y = y
        self.speed = 10
        self.left = False
        self.right = False
        self.standing = True
        self.run = False
        if self.is_loaded:
            self.image = self.frames[self.cur_frame]
            self.rect = self.rect.move(x, y)

    def load_images(self, name, path, type, count):
        for i in range(0, count):
            img_temp = load_image(name + str(i) + type, path)
            size = img_temp.get_rect()
            img_temp = pygame.transform.scale(img_temp, (size.width//10, size.height//10))
            self.frames.append(img_temp)
            self.rect = img_temp.get_rect()
        self.is_loaded = True
        self.rect = self.rect.move(self.x, self.y)
        self.update()


    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
        self.is_loaded = True
        self.rect = self.rect.move(self.x, self.y)
        self.update()

    def update(self):
        if self.run:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
        else:
            self.cur_frame = 0
            self.image = load_image('_WALK_005.png','images//1_KNIGHT//_WALK')
            size = self.image.get_rect()
            self.image = pygame.transform.scale(self.image, (size.width // 10, size.height // 10))





run = True
man = AnimatedSprite(200, 470)
man.load_images('_RUN_00', 'images//1_KNIGHT//_RUN', '.png', 7)
print(man.image)
print(man.is_loaded)
print(man.rect)
while run:

    #pygame.time.Clock().tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            man.run = True
            if event.key == pygame.K_LEFT:
                man.rect.left -= man.speed
            if event.key == pygame.K_RIGHT:
                man.rect.left += man.speed

        else:
            man.run = False
    # bg = pygame.image.load('images/BG4.png')
    bg = load_image('BG4.png', 'images')
    bg = pygame.transform.scale(bg, (screenWidth, screenHeight))
    win.blit(bg, (0, 0))
    all_sprites.draw(win)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
