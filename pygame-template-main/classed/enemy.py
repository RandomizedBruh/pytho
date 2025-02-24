import pygame


class Enemy(pygame.sprite.Sprite):


    image=""
    surface=None
    rect=None
    width = 100
    height=100
    x=0
    y=0
    speed=8
    

    def __init__(self,image,width=100 ,height=100,x=0,y=0,speed=8):
        super().__init__()
        print("создаём приколы")
        self.x=x
        self.y=y
        self.image=image
        self.width = width
        self.height = height
        self.surface=pygame.image.load(image)
        self.surface=pygame.transform.scale(self.surface,(self.width, self.height))
        self.rect = self.surface.get_rect(center=(self.x,self.y))
        self.speed = speed


    def draw(self,screen: pygame.Surface):
        width=screen.get_width()
        height=screen.get_height()

        if(self.x<0):
            self.x=width
        elif(self.x > width):
            self.x=0
        if (self.y < 0):
            self.y=height
        elif(self.y>height):
            self.y=0


        self.rect.center=(self.x,self.y)
        screen.blit(self.surface,self.rect)

    def move(self):


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            self.speed=8
        else: self.speed = 3
        if keys[pygame.K_a]:
            self.x -= self.speed
        elif keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -=self.speed
        elif keys[pygame.K_s]:
            self.y +=self.speed   

    def follow(self, object):
        dx = object.x - self.x
        dy = object.y - self.y
        distance = (dx**2 + dy**2) ** 0.5
        if distance >0 :
            dx /= distance
            dy /=distance
        self.x += dx * self.speed
        self.y += dy *self.speed