import pygame
import sys
import os
from src.constants import *
from src.ui import UI
from src.game_logic import GameLogic

def main():
    # Set dummy driver for headless environments if needed,
    # but for a real desktop app we'd want the default.
    # In this sandbox, we'll keep it flexible.
    if os.environ.get('SDL_VIDEODRIVER') is None:
        # Default to dummy if not specified and no display
        try:
            pygame.display.init()
        except:
            os.environ['SDL_VIDEODRIVER'] = 'dummy'
            pygame.display.init()
    else:
        pygame.display.init()

    pygame.init()

    screen = pygame.display.set_mode((SHELL_WIDTH, SHELL_HEIGHT))
    pygame.display.set_caption("DigiPet - Original Desktop Companion")

    ui = UI(screen)
    game = GameLogic(ui)

    try:
        game.run()
    except KeyboardInterrupt:
        pass
    finally:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
