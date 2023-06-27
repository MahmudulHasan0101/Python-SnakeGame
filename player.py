import pygame

class vec2d:
    def __init__(self, x, y) :
        self.x = x
        self.y = y

class Snake:
    def __init__(self, x, y, vel, radious, color):
        self.vel = vel
        self.color = color
        self.radious = radious
        self.body = []
        self.body.append(vec2d(x, y))
        self.velX = 0
        self.velY = 0
        self.shrinkdown = radious * 0.4

    def reset(self, x, y):
        self.body.clear()
        self.body.append(vec2d(x, y))
        self.velX = 0
        self.velY = 0

    def draw(self, screen):
        shrink = 0.0
        ds = self.shrinkdown / len(self.body)

        for pos in self.body:
            pygame.draw.circle(screen, self.color, (int(pos.x), int(pos.y)), int(self.radious - shrink))
            shrink += ds
       
    def update(self):
        self.body[-1].x = self.body[0].x + self.velX
        self.body[-1].y = self.body[0].y + self.velY
        self.body.insert(0, self.body[-1])
        self.body.pop()

    def collide(self, x, y, radious):
        if ((x-self.body[0].x)**2 + (y-self.body[0].y)**2 <= (self.radious + radious)**2):
            return True
        return False

    def grow(self):
        self.body.append(vec2d(-1,-1))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if (self.velY == 0):
                if (event.key == pygame.K_w):
                    self.velY = -self.vel
                    self.velX = 0

                elif (event.key == pygame.K_s):
                    self.velY = self.vel
                    self.velX = 0

            elif (self.velX == 0):
                if (event.key == pygame.K_a):
                    self.velX = -self.vel
                    self.velY = 0

                elif (event.key == pygame.K_d):
                    self.velX = self.vel
                    self.velY = 0