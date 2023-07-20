class Bullet:
    DAMAGE = 1
    def __init__(self,image,center):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center= center
        self.is_visible = True
        
    def update(self, object):
        if self.rect.colliderect(object.rect):  
            object.hit(self.DAMAGE)
            self.is_visible = False
            
    
    def draw (self,screen):
        screen.blit(self.image,self.rect)
    
  