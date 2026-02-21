# Screen and UI constants

# The actual "game screen" size (pixelated)
SCREEN_WIDTH = 48
SCREEN_HEIGHT = 32
SCALE = 10  # Scale for display

# Handheld shell dimensions
SHELL_WIDTH = 800
SHELL_HEIGHT = 600

# Colors
COLOR_BLACK = (20, 20, 20)
COLOR_WHITE = (230, 230, 230)
COLOR_SHELL = (100, 100, 200)  # Blue-ish shell
COLOR_SCREEN_BG = (155, 188, 15)  # Classic GameBoy greenish tint
COLOR_PIXEL = (15, 56, 15)      # Classic GameBoy dark green

# Button positions (relative to shell)
BUTTON_A_POS = (SHELL_WIDTH // 2 - 100, 500)
BUTTON_B_POS = (SHELL_WIDTH // 2, 500)
BUTTON_C_POS = (SHELL_WIDTH // 2 + 100, 500)
BUTTON_RADIUS = 30
