import pygame
import os
from Person import Player
from Obstacle import Obstacle

pygame.init()
# pygame.key.set_repeat(200, 70)
JOY = True
joystick = None
if JOY:
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
clock = pygame.time.Clock()
# screen_size = (1922 // 1.5, 1082 // 1.5)
screen_size = (1600, 900)
FPS = 60
screenWidth = int(screen_size[0])
screenHeight = int(screen_size[1])
screen_size = (screenWidth, screenHeight)
win = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Battle of warriors')
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
obj_group = pygame.sprite.Group()


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


def draw_background(surface):
    pygame.draw.rect(surface, pygame.Color('green'), (0, 762 // 2, 1024, 762 // 2))
    pygame.draw.rect(surface, pygame.Color(82, 239, 246, 255), (0, 0, 1024, 762 // 2))
    pygame.draw.rect(surface, pygame.Color(115, 74, 1, 255), (80, 752 // 2 - 200, 40, 230))
    pygame.draw.circle(surface, pygame.Color(2, 132, 32, 255), (100, 752 // 2 - 200), 90)


run = True
idleLeft = load_image('0_Golem_Idle_000.png','images//PNG Sequences_golem1//Idle_//')
idleRight = pygame.transform.flip(idleLeft, True, False)
man1 = Player(200, 610,idleLeft,idleRight,player_group)
man1.load_images('0_Golem_Running_0', 'images//PNG Sequences_golem1//Running_', '.png', 12, man1.RRFrames, man1.LRFrames)
man1.load_images('0_Golem_Slashing_0', 'images//PNG Sequences_golem1//Slashing_', '.png', 12, man1.RSFrames, man1.LSFrames)
idleLeft = load_image('0_Golem_Idle_000.png','images//PNG Sequences_golem3//Idle_//')
idleRight = pygame.transform.flip(idleLeft, True, False)
man2 = Player(600, 610,idleLeft,idleRight,player_group)
man2.load_images('0_Golem_Running_0', 'images//PNG Sequences_golem3//Running_', '.png', 12, man2.RRFrames, man2.LRFrames)
man2.load_images('0_Golem_Slashing_0', 'images//PNG Sequences_golem3//Slashing_', '.png', 12, man2.RSFrames, man2.LSFrames)
bg = load_image('1600x900_backg.jpg', 'images')
obj = Obstacle(1200,690,obj_group)
win.blit(bg, (0, 0))
while run:
    pygame.time.Clock().tick(FPS)
    if pygame.sprite.collide_mask(man1,man2):
        print('now', man2.rect.midright[0] , man1.rect.midbottom[0] , man2.rect.midleft[0], man2.rect.midright[0] > man1.rect.midbottom[0] > man2.rect.midleft[0])
        if ( man2.rect.midright[0] > man1.rect.midbottom[0] > man2.rect.midleft[0] ) and man1.rect.top > man2.rect.top:
            man1.enemyBottom = True
            man2.enemyBottom = False
            man1.enemyLeft = False
            man1.enemyRight = False
            man2.enemyRight = False
            man2.enemyLeft = False
        elif ( man1.rect.midright[0] > man2.rect.midbottom[0] > man1.rect.midleft[0]) and man2.rect.top > man1.rect.top:
            man2.enemyBottom = True
            man1.enemyBottom = False
            man1.enemyLeft = False
            man1.enemyRight = False
            man2.enemyRight = False
            man2.enemyLeft = False
        elif (man1.rect.left > man2.rect.left) and man1.rect.top == man2.rect.top:
            man1.enemyLeft = True
            man1.enemyRight = False
            man2.enemyRight = True
            man2.enemyLeft = False
        elif (man1.rect.left < man2.rect.left) and man1.rect.top == man2.rect.top:
            man1.enemyLeft = False
            man1.enemyRight = True
            man2.enemyRight = False
            man2.enemyLeft = True
    else:
        man1.enemyLeft = False
        man1.enemyRight = False
        man2.enemyRight = False
        man2.enemyLeft = False

    #if pygame.sprite.collide_mask(man1, obj):
    if obj.rect.right > man1.rect.centerx > obj.rect.left and man1.rect.bottomleft[1] >= obj.rect.top:
        man1.isJump = False
        man1.jumpCount = 0





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #print(event)
    mouse = pygame.mouse.get_pressed()
    mouse_coord = pygame.mouse.get_pos()
    #print(mouse_coord)
    keys = pygame.key.get_pressed()
    hat = [None]
    BTN_B = False
    BTN_X = False
    BTN_Y = False
    BTN_A = False
    if JOY:
        hat = joystick.get_hat(0)
        # buttons = joystick.get_numbuttons()
        BTN_B = joystick.get_button(1)
        BTN_X = joystick.get_button(2)
        BTN_Y = joystick.get_button(3)
        BTN_A = joystick.get_button(0)
        #hero 1
        if hat[0] == -1 and not man1.enemyLeft and man1.rect.bottomleft[0] > -50:
            man1.standing = False
            if man1.right is True:
                man1.rect.left += man1.rect.width // 14
                man1.right = False
                man1.left = True
            man1.rect.left -= man1.speed
        elif hat[0] == 1 and not man1.enemyRight and man1.rect.right < screenWidth+50:
            man1.standing = False
            if man1.left is True :
                man1.rect.left -= man1.rect.width // 14
                man1.right = True
                man1.left = False
            man1.rect.left += man1.speed
        else:
            man1.standing = True
            man1.walkCount = 0
        if BTN_X:
            man1.attacking = True

        if not man1.isJump or man1.enemyBottom:
            if BTN_Y:
                man1.isJump = True
                #print('yes')
                man1.walkCount = 0
        if man1.isJump:
            if man1.jumpCount >= -1 * man1.jumpCountStart:
                neg = 1
                if man1.jumpCount < 0:
                    neg = -1
                man1.rect.top -= (man1.jumpCount ** 2) // 2 * neg
                man1.jumpCount -= 1
            else:
                man1.isJump = False
                man1.jumpCount = man1.jumpCountStart

        #hero 2
        if (keys[pygame.K_LEFT] or keys[pygame.K_a] ) and not man2.enemyLeft and man2.rect.bottomleft[0] > -50:
            man2.standing = False
            if man2.right is True :
                man2.rect.left += man2.rect.width // 14
                man2.right = False
                man2.left = True
            man2.rect.left -= man2.speed
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not man2.enemyRight and man2.rect.right < screenWidth+50:
            man2.standing = False
            if man2.left is True:
                man2.rect.left -= man2.rect.width // 14
                man2.right = True
                man2.left = False
            man2.rect.left += man2.speed
        else:
            man2.standing = True
            man2.walkCount = 0
        if keys[pygame.K_RETURN]:
            man2.attacking = True
        if mouse[0] == 1:
            if man2.right and mouse_coord[0] < man2.rect.left+50:
                man2.right = False
                man2.left = True
            elif man2.left and mouse_coord[0] > man2.rect.left+50:
                man2.right = True
                man2.left = False
            #print('left',man2.left,'right',man2.right,'/n')
            man2.attacking = True

        if not man2.isJump:
            if keys[pygame.K_SPACE]:
                man2.isJump = True
                #print('yes')
                man2.walkCount = 0
        if man2.isJump:
            if man2.jumpCount >= -1 * man2.jumpCountStart:
                neg = 1
                if man2.jumpCount < 0:
                    neg = -1
                man2.rect.top -= (man2.jumpCount ** 2) // 2 * neg
                man2.jumpCount -= 1
            else:
                man2.isJump = False
                man2.jumpCount = man2.jumpCountStart
    else:
        #hero 1
        if keys[pygame.K_a] :
            man1.standing = False
            if man1.right is True:
                man1.rect.left += man1.rect.width // 14
                man1.right = False
                man1.left = True
            man1.rect.left -= man1.speed
        elif keys[pygame.K_d] :
            man1.standing = False
            if man1.left is True:
                man1.rect.left -= man1.rect.width // 14
                man1.right = True
                man1.left = False
            man1.rect.left += man1.speed
        else:
            man1.standing = True
            man1.walkCount = 0
        if keys[pygame.K_SPACE] :
            man1.attacking = True

        if not man1.isJump:
            if keys[pygame.K_LSHIFT]:
                man1.isJump = True
                print('yes')
                man1.walkCount = 0
        if man1.isJump:
            if man1.jumpCount >= -1 * man1.jumpCountStart:
                neg = 1
                if man1.jumpCount < 0:
                    neg = -1
                man1.rect.top -= (man1.jumpCount ** 2) // 2 * neg
                man1.jumpCount -= 1
            else:
                man1.isJump = False
                man1.jumpCount = man1.jumpCountStart
        #hero 2
        if keys[pygame.K_LEFT]:
            man2.standing = False
            if man2.right is True:
                man2.rect.left += man2.rect.width // 14
                man2.right = False
                man2.left = True
            man2.rect.left -= man2.speed
        elif keys[pygame.K_RIGHT]:
            man2.standing = False
            if man2.left is True:
                man2.rect.left -= man2.rect.width // 14
                man2.right = True
                man2.left = False
            man2.rect.left += man2.speed
        else:
            man2.standing = True
            man2.walkCount = 0
        if keys[pygame.K_RETURN]:
            man2.attacking = True
        if mouse[0] == 1:
            if man2.right and mouse_coord[0] < man2.rect.left:
                man2.right = False
                man2.left = True
            elif man2.left and mouse_coord[0] > man2.rect.left:
                man2.right = True
                man2.left = False
            print('left',man2.left,'right',man2.right,'/n')
            man2.attacking = True


        if not man2.isJump:
            if keys[pygame.K_RSHIFT]:
                man2.isJump = True
                #print('yes')
                man2.walkCount = 0
        if man2.isJump:
            if man2.jumpCount >= -1 * man2.jumpCountStart:
                neg = 1
                if man2.jumpCount < 0:
                    neg = -1
                man2.rect.top -= (man2.jumpCount ** 2) // 2 * neg
                man2.jumpCount -= 1
            else:
                man2.isJump = False
                man2.jumpCount = man2.jumpCountStart

    # bg = pygame.image.load('images/BG4.png')
    # bg = load_image('bg.jpg', 'images')
    # bg = pygame.transform.scale(bg, (screenWidth, screenHeight))
    # win.blit(bg, (0, 0))
    #bg = pygame.Surface(screen_size)
    #bg.fill(pygame.Color('white'))
    #draw_background(bg)

    #pygame.draw.rect(win,pygame.Color('red'),pygame.Rect(1200,690,120,80),0)
    obj_group.draw(win)
    obj_group.update()
    player_group.draw(win)
    player_group.update()
    pygame.display.flip()
    # clock.tick(FPS)
    player_group.clear(win,bg)
pygame.quit()
