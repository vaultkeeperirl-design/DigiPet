import pygame
import time
from src.assets_gen import *

class SpriteManager:
    def __init__(self):
        self.sprites = {
            "Egg": get_egg_sprites(),
            "Bloop": get_baby_sprites(),
            "Sprout": get_child_sprites(),
            "Thorn": get_thorn_sprites(),
            "Arbor": get_adult_sprites(),
            "Wither": get_wither_sprites()
        }
        self.poop_sprite = get_poop_sprite()
        self.food_sprite = get_food_sprite()

    def get_pet_sprite(self, species, is_sleeping=False):
        if is_sleeping:
            return self.sprites.get(species, self.sprites["Egg"])[0]

        frames = self.sprites.get(species, self.sprites["Egg"])
        frame_idx = int(time.time() * 2) % len(frames)
        return frames[frame_idx]

    def get_poop(self):
        return self.poop_sprite

    def get_food(self):
        return self.food_sprite
