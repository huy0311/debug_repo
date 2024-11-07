import pygame as pg
import sys

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0,0]
        self.collisions = {
                                'up': False,
                                'down': False,

                                'right': False,
                                'left': False,
                            }
        
    def rect(self):
        return pg.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap, movement=(0,0)):


        self.collisions = {
                                'up': False,
                                'down': False,

                                'right': False,
                                'left': False,
                            }
        frame_movement = (movement[0] + self.velocity[0],movement[1] + self.velocity[1])

        # Horizontal movement (x-axis)
        self.pos[0] += frame_movement[0]  # Apply horizontal movement first
        entity_rect = self.rect()

        # Check for collisions along the x-axis (left and right)
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:  # Moving right
                    # Push the player back to the left side of the tile
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                    self.pos[0] = entity_rect.x  # Update the player's position

                elif frame_movement[0] < 0:  # Moving left
                    # Push the player back to the right side of the tile
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                    self.pos[0] = entity_rect.x  # Update the player's position

        # Vertical movement (y-axis)
        self.pos[1] += frame_movement[1]  # Apply vertical movement
        entity_rect = self.rect()

        # Check for collisions along the y-axis (up and down)
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:  # Moving down (falling)
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                    self.pos[1] = entity_rect.y  # Update the player's position

                elif frame_movement[1] < 0:  # Moving up
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                    self.pos[1] = entity_rect.y  # Update the player's position

        # Apply gravity (if no downward collision)
        if not self.collisions['down']:
            self.velocity[1] = min(5, self.velocity[1] + 0.2)  # Simulating gravity


    
    def render(self, surf):
        # Draw the player sprite
        surf.blit(self.game.assets['player'], self.pos)

        # Debug: Draw the player's collision rectangle (in red)
        entity_rect = self.rect()
        pg.draw.rect(surf, (255, 0, 0), entity_rect, 2)  # Draw player rectangle (red)

        # Debug: Draw the tile collision rectangles (in green)
        for rect in self.game.tilemap.physics_rects_around(self.pos):
            pg.draw.rect(surf, (0, 255, 0), rect, 2)  # Draw tile rectangles (green)
