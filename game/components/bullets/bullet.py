class Bullet:
    def __init__(self,image,center):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center= center
        
    def update(self, object):
        if self.rect.colliderect(object.rect):
            object.is_alive = False
            object.is_visible = False
            self.hit = True
    
    def draw (self,screen):
        screen.blit(self.image,self.rect)
    
  