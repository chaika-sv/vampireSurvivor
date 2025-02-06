from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2(0, 0)

    def draw(self, target_pos):
        self.offset.x = -(target_pos[0] - WINDOW_WIDTH / 2)
        self.offset.y = -(target_pos[1] - WINDOW_HEIGHT / 2)

        # only sprites that has ground attribute (tiles)
        ground_sprites = [sprite for sprite in self if hasattr(sprite, 'ground')]

        # sprites that doesn't have ground attribute (not tiles)
        object_sprites = [sprite for sprite in self if not hasattr(sprite, 'ground')]

        # it's important to keep the order. first ground_sprites, then object_sprites
        for layer in [ground_sprites, object_sprites]:
            # Y sorting to draw objects with bigger y position first (in front of objects with smaller y)
            for sprite in sorted(layer, key = lambda sprite: sprite.rect.centery):
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)