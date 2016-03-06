import pygame

class Projectile(Entity):
    List = pygame.sprite.Group() 
    active_projectiles = []
    main_weapon = True
    
    def __init__(self, x, y, image_string, dmg=10, speed_bonus=0):
        Entity.__init__(self, x, y, image_string)
        self.dmg = dmg
        self.speed_bonus = speed
        
        if len(Projectile.active_projectiles) > 0:
            last_element = Projectile.active_projectiles[-1]
            difference = abs((self.rect.x - last_element.rect.x))
            if difference < self.rect.width:
                return
        Projectile.active_projectiles.append(self)
        Projectile.List.add(self)
        
    
    @staticmethod    
    def movement(SCREENWIDTH, SCREENHEIGHT):
        for projectile in Projectile.List:
            projectile.rect.x += projectile.vel_x
    
    def destroy(self):
        Projectile.active_projectiles.remove(self)
        del self