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



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y,idleImageLeft,idleImageRight,group):
        super().__init__(group)
        self.is_loaded = False
        # left(right) run
        self.LRFrames = []
        self.RRFrames = []
        # left (right) attack
        self.LSFrames = []
        self.RSFrames = []
        self.cur_frame = 0
        self.image = None
        self.rect = None
        self.x = x
        self.y = y
        self.speed = 12
        self.left = False
        self.right = True
        self.standing = True
        self.run = False
        self.walkCount = 0
        self.attackCount = 0
        self.attacking = False
        self.idleImageLeft =idleImageLeft
        self.idleImageRight = idleImageRight
        self.isJump = False
        self.jumpCountStart = 9
        self.jumpCount = 9
        self.enemyLeft = False
        self.enemyRight = False
        self.enemyBottom = False


    def load_images(self, name, path, type, count, whereL, whereR):
        for i in range(0, count):
            n = ''
            if i <= 9:
                n += '0' + str(i)
            else:
                n += str(i)
            img_temp = load_image(name + n + type, path)
            size = img_temp.get_rect()
            img_temp = pygame.transform.scale(img_temp, (size.width, size.height))
            whereL.append(img_temp)
            flipped_surface = pygame.transform.flip(img_temp, True, False)
            whereR.append(flipped_surface)
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
                self.image = self.idleImageLeft
                size = self.image.get_rect()
            else:
                self.image = self.idleImageRight
                size = self.image.get_rect()
        if self.attackCount + 1 >= 12 * 1:
            self.attackCount = 0
            self.attacking = False
        if self.attacking:
            if self.right:
                self.image = self.RSFrames[self.attackCount // 1]
            else:
                self.image = self.LSFrames[self.attackCount // 1]
            self.attackCount += 2
        self.mask = pygame.mask.from_surface(self.image)