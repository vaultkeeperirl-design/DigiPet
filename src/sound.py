import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        # Sounds would be loaded here: self.sounds['beep'] = pygame.mixer.Sound('assets/sounds/beep.wav')

    def play(self, name):
        if name in self.sounds:
            self.sounds[name].play()
        else:
            # Fallback to a simple beep if possible, or just print
            print(f"Sound effect: {name}")
