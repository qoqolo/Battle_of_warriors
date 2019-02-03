import pygame
import os

pygame.init()
#pygame.key.set_repeat(200, 70)

clock = pygame.time.Clock()
#screen_size = (1922 // 1.5, 1082 // 1.5)
screen_size = (1024, 762)
FPS = 40
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

'''
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.is_loaded = False
        self.LFrames = []
        self.RFrames = []
        self.cur_frame = 0
        self.image = None
        self.rect = None
        self.x = x
        self.y = y
        self.speed = 11
        self.left = False
        self.right = True
        self.standing = True
        self.run = False
        self.walkCount = 0


    def load_images(self, name, path, type, count):
        for i in range(0, count):
            n = ''
            if i <=9:
                n += '0' + str(i)
            else:
                n += str(i)
            img_temp = load_image(name + n + type, path)
            size = img_temp.get_rect()
            img_temp = pygame.transform.scale(img_temp, (size.width, size.height))
            self.RFrames.append(img_temp)
            flipped_surface = pygame.transform.flip(img_temp, True, False)
            self.LFrames.append(flipped_surface)
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
        self.rect = self.rect.move(self.x, self.y)
        self.update()

    def update(self):
        if self.walkCount + 1 >= 12*1:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                #win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.image = self.LFrames[self.walkCount // 1]
                self.walkCount += 1
            elif self.right:
                self.image = self.RFrames[self.walkCount // 1]
                self.walkCount += 1
        else:
            if self.right:
                self.image = load_image('0_Golem_Idle_000.png', 'images//PNG Sequences//Idle')
                size = self.image.get_rect()
                self.image = pygame.transform.scale(self.image, (size.width // 7, size.height // 7))
            else:
                self.image = load_image('0_Golem_Idle_000.png', 'images//PNG Sequences//Idle')
                size = self.image.get_rect()
                self.image = pygame.transform.scale(self.image, (size.width // 7, size.height // 7))
                self.image = pygame.transform.flip(self.image, True, False)
'''
def draw_background(surface):
    pygame.draw.rect(surface, pygame.Color('green'), (0, 762 // 2, 1024, 762 // 2))
    pygame.draw.rect(surface, pygame.Color(82, 239, 246, 255), (0, 0, 1024, 762 // 2))
    pygame.draw.rect(surface, pygame.Color(115, 74, 1, 255), (80, 752 // 2 - 200, 40, 230))
    pygame.draw.circle(surface, pygame.Color(2, 132, 32, 255), (100, 752 // 2 - 200), 90)




class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(player_group)
        self.is_loaded = False
        #left(right) run
        self.LRFrames = []
        self.RRFrames = []
        #left (right) attack
        self.LSFrames =[]
        self.RSFrames =[]
        self.cur_frame = 0
        self.image = None
        self.rect = None
        self.x = x
        self.y = y
        self.speed = 10
        self.left = False
        self.right = True
        self.standing = True
        self.run = False
        self.walkCount = 0

    def load_images(self, name, path, type, count):
        for i in range(0, count):
            n = ''
            if i <= 9:
                n += '0' + str(i)
            else:
                n += str(i)
            img_temp = load_image(name + n + type, path)
            size = img_temp.get_rect()
            img_temp = pygame.transform.scale(img_temp, (size.width, size.height))
            self.RRFrames.append(img_temp)
            flipped_surface = pygame.transform.flip(img_temp, True, False)
            self.LRFrames.append(flipped_surface)
            self.rect = img_temp.get_rect()
        self.is_loaded = True
        self.rect = self.rect.move(self.x, self.y)
        self.update()

    def update(self):
        if self.walkCount + 1 >= 12 * 1:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                # win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.image = self.LRFrames[self.walkCount // 1]
                self.walkCount += 1
            elif self.right:
                self.image = self.RRFrames[self.walkCount // 1]
                self.walkCount += 1
        else:
            if self.right:
                self.image = load_image('0_Golem_Idle_000.png', 'images//PNG Sequences//Idle')
                size = self.image.get_rect()
                self.image = pygame.transform.scale(self.image, (size.width // 7, size.height // 7))
            else:
                self.image = load_image('0_Golem_Idle_000.png', 'images//PNG Sequences//Idle')
                size = self.image.get_rect()
                self.image = pygame.transform.scale(self.image, (size.width // 7, size.height // 7))
                self.image = pygame.transform.flip(self.image, True, False)



run = True
man = Player(200, 530)
man.load_images('0_Golem_Running_0', 'images//PNG Sequences//Running_', '.png', 12)
print(man.image)
print(man.is_loaded)
print(man.rect)
while run:
    pygame.time.Clock().tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        man.standing = False
        if man.right is True:
            man.rect.left += man.rect.width//14
            man.right = False
            man.left = True
        man.rect.left -= man.speed
    elif keys[pygame.K_RIGHT]:
        man.standing = False
        if man.left is True:
            man.rect.left -= man.rect.width//14
            man.right = True
            man.left = False
        man.rect.left += man.speed
    else:
        man.standing = True
        man.walkCount = 0
    # bg = pygame.image.load('images/BG4.png')
    #bg = load_image('bg.jpg', 'images')
    #bg = pygame.transform.scale(bg, (screenWidth, screenHeight))
    #win.blit(bg, (0, 0))
    bg = pygame.Surface(screen_size)
    bg.fill(pygame.Color('white'))
    draw_background(bg)
    win.blit(bg, (0, 0))
    player_group.draw(win)
    player_group.update()
    pygame.display.flip()
    #clock.tick(FPS)

pygame.quit()
