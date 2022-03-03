import pygame, time, random
from pygame import mixer
import numpy as np


class Gra(object):

  def __init__(self):

    pygame.init()
    self.screen = pygame.display.set_mode((597, 600))
    self.img = pygame.image.load("C:/Users/mjaro/Desktop/projektypython/pygame_images/chmurki.jpg")
    self.img0 = pygame.image.load("C:/Users/mjaro/Desktop/projektypython/pygame_images/k1.png")
    self.img1 = pygame.image.load("C:/Users/mjaro/Desktop/projektypython/pygame_images/k2.png")
    self.img2 = pygame.image.load("C:/Users/mjaro/Desktop/projektypython/pygame_images/k3.png")
    self.paczka = pygame.image.load("C:/Users/mjaro/Desktop/projektypython/pygame_images/tygryski.png")
    self.img3 = pygame.transform.smoothscale(self.paczka, (75,75))
    self.img4 = pygame.image.load("C:/Users/mjaro/Desktop/projektypython/pygame_images/angelek.png")
    self.x, self.y = 0, 0
    self.next_frame = time.time() + 0.08
    self.frame = 0
    self.yimg= 300
    self.ximg = 300
    self.y_tyg = 50
    self.x_tyg = 600
    self.x_dz = 900
    self.y_dz = 30
    self.szybkosc_dz = [-5,-4,-3,-2,-1,1,2,3,4,5]
    self.array = np.array([0.2, 0.1, 0.3, 0.4, 0.5, 0.7, 0.08, 0.1, 0.15, 1.35, 1.2, 1.5, 0.9, 0.8, 0.7, 1.5])
    self.speed_paczka = 7 * self.array
    self.szybkosc = 1
    self.sound1 = mixer.Sound('C:/Users/mjaro/Desktop/projektypython/pygame_images/1s.wav')
    self.sound2 = mixer.Sound('C:/Users/mjaro/Desktop/projektypython/pygame_images/2s.wav')
    self.sound = [1,2]
    self.clock = pygame.time.Clock()
    self.delta = 0.0
    self.max_tps = 60
    self.pkt = 0
    pygame.display.set_caption('Babuszka') 
    
    


    on = True
    while on:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          on = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
          on = False


      # Ticking 
      self.delta += self.clock.tick() / 1000.0
      while self.delta > 1/self.max_tps:
        self.delta -= 1/self.max_tps
        self.fizyka()
        self.fizyka_dz()
        self.spr()
        
      
      self.draw()


      
      
      
      

      pygame.display.flip()




  def draw(self):
    self.screen.blit(self.img3, (self.x_tyg, self.y_tyg))
    self.screen.blit(self.img4, (self.x_dz, self.y_dz))
    self.czcionka = pygame.font.SysFont("dejavusans", 40)
    self.punkty = str(self.pkt)
    self.text_render = self.czcionka.render(self.punkty, 1, (255, 255, 0))
    self.screen.blit(self.text_render, (10,0))



  def spr(self):
    self.rel_x = self.x % self.img.get_width()
    self.screen.blit(self.img, (self.rel_x - self.img.get_width(), self.y))
    self.x += -3 
    if self.rel_x < 597:
        self.screen.blit(self.img, (self.rel_x, self.y))
    

    while time.time() > self.next_frame:
      self.frame = (self.frame + 1) % 3
      self.next_frame = time.time() + 0.08
    
    if self.frame == 0:
      self.screen.blit(self.img0, (self.ximg, self.yimg))
    elif self.frame == 1:
      self.screen.blit(self.img1, (self.ximg, self.yimg))
    elif self.frame == 2:
      self.screen.blit(self.img2, (self.ximg, self.yimg))

    
  def fizyka(self):

    # ruszanie kaczuszka
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        self.yimg += -1*5
    if pressed[pygame.K_s]:
        self.yimg +=  1*5
    if pressed[pygame.K_a]:
        self.ximg += -1*5
    if pressed[pygame.K_d]:
        self.ximg += 1*5

    
    # resetowanie paczki po x -300
    self.x_tyg += - self.szybkosc
    if self.x_tyg < -300:
      
      self.y_tyg = random.randrange(0, 530, 1)
      self.x_tyg = random.randrange(600, 1000)
      self.szybkosc = random.choice(self.speed_paczka)
      
      
    # zjadanie paczki
    if (self.ximg + 125 > self.x_tyg > self.ximg - 50) and (self.yimg +75 > self.y_tyg > self.yimg - 50 ):
      self.y_tyg = random.randrange(0, 530, 1)
      self.x_tyg = random.randrange(600,1000)
      self.szybkosc = random.choice(self.speed_paczka)
      self.wybor = random.choice(self.sound)
      if self.wybor == 1: self.sound1.play()
      if self.wybor == 2: self.sound2.play()
      self.pkt += 1
    
   
    
      
      
      
    
  
  def fizyka_dz(self):
    if self.x_dz > 450:
      self.x_dz += -1 *5
    elif self.y_dz < 400:
      self.y_dz += 0.2 *5
    elif self.y_dz >= 400:
      self.x_dz = 900
      self.y_dz = random.randrange(1,300)

  
  

    

















    

Gra()