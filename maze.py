from pygame import * 
window_size = (700, 500)
window = display.set_mode(window_size)
clock = time.Clock()
FPS = 60
print('helo')

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, image, speed):
        super().__init__()
        self.image = image
        self.speed = speed
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def collide(self, other_sprite):
        return sprite.collide_rect(other_sprite, self)


class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_w] == True:
            self.rect.y -= self.speed
        if keys[K_s] == True:
            self.rect.y += self.speed
        if keys[K_a] == True:
            self.rect.x -= self.speed
        if keys[K_d] == True:
            self.rect.x += self.speed  

class Enemy(GameSprite):
    def __init__(self, x, y, image, speed, dir, min_distanc, max_distanc):
        super().__init__(x, y, image, speed)
        self.dir = dir
        self.min_distanc = min_distanc
        self.max_distanc = max_distanc
    def move(self):
        if self.dir == 'right':
            self.rect.x += self.speed
            if self.rect.x >= self.max_distanc:
                self.dir = "left"
        if self.dir == 'left':
            self.rect.x -= self.speed
            if self.rect.x <= self.min_distanc:
                self.dir = "right" 
        if self.dir == 'up':
            self.rect.y -= self.speed
            if self.rect.x <= self.min_distanc:
                self.dir = "down"
        if self.dir == 'down':
            self.rect.y += self.speed
            if self.rect.x >= self.max_distanc:
                self.dir = "up" 

display.set_caption('maze')
win_image = transform.scale(image.load('treasure.png'), (100, 100))
player_image = transform.scale(image.load('hero.png'), (65, 65))
enemy_image = transform.scale(image.load('cyborg.png'), (65, 65))
background = transform.scale(image.load('background.jpg'), window_size)
player = Player(100, 100, player_image, 10)
enemy = Enemy(400, 100, enemy_image, 5, 'left', 300, 500)
wall_1 = GameSprite(200, 100, Surface((100, 10)), 0)
wall_2 = GameSprite(300, 200, Surface((100, 10)), 0)
wall_3 = GameSprite(400, 100, Surface((100, 10)), 0)
wall_4 = GameSprite(300, 400, Surface((100, 10)), 0)
win = GameSprite(300, 300, win_image, 0)
font.init()
font1 = font.Font(font.get_default_font(), 70)
win_txt = font1.render('YOU WIN!', True, (255, 215, 0))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
game = True
while game == True:
    window.blit(background,(0, 0))
    player.draw()
    enemy.draw()
    wall_1.draw()
    wall_2.draw()
    wall_3.draw()
    wall_4.draw()
    player.move()
    win.draw()
    enemy.move()
    if player.collide(enemy) or player.collide(wall_1) or player.collide(wall_2) or player.collide(wall_3) or player.collide(wall_4):
        window.blit(lose, (300,400))
        display.update()
        time.delay(3000)
        game = False
    if player.collide(win):
        window.blit(win_txt, (300, 400))
        display.update()
        time.delay(3000)
        game = False
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
    


