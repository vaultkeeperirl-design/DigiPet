import pygame
from src.constants import *

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.game_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.scaled_surface = pygame.Surface((SCREEN_WIDTH * SCALE, SCREEN_HEIGHT * SCALE))

        # UI state
        self.selected_icon = 0 # 0 to 7
        self.icons_enabled = True
        self.font = pygame.font.SysFont(None, 12)
        self.large_font = pygame.font.SysFont(None, 24)
        self.button_states = {"A": False, "B": False, "C": False}

    def draw_shell(self):
        # Draw the physical device shell
        self.screen.fill((40, 40, 40)) # Background

        # Shell body (more egg-shaped)
        shell_rect = pygame.Rect(
            (SHELL_WIDTH - 450) // 2,
            (SHELL_HEIGHT - 550) // 2,
            450, 550
        )
        # Shell shadow
        shadow_rect = shell_rect.copy()
        shadow_rect.x += 10
        shadow_rect.y += 10
        pygame.draw.rect(self.screen, (20, 20, 20), shadow_rect, border_radius=180)

        pygame.draw.rect(self.screen, COLOR_SHELL, shell_rect, border_radius=180)
        # Add some "highlights" to shell
        pygame.draw.rect(self.screen, (120, 120, 220), shell_rect, width=15, border_radius=180)
        pygame.draw.rect(self.screen, (0, 0, 0), shell_rect, width=5, border_radius=180)

        # Screen frame
        frame_width = SCREEN_WIDTH * SCALE + 60
        frame_height = SCREEN_HEIGHT * SCALE + 60
        frame_rect = pygame.Rect(
            (SHELL_WIDTH - frame_width) // 2,
            (SHELL_HEIGHT - frame_height) // 2 - 60,
            frame_width,
            frame_height
        )
        pygame.draw.rect(self.screen, (40, 40, 40), frame_rect, border_radius=20)
        pygame.draw.rect(self.screen, (0, 0, 0), frame_rect, width=3, border_radius=20)

        # Buttons
        self.draw_button(BUTTON_A_POS, "A")
        self.draw_button(BUTTON_B_POS, "B")
        self.draw_button(BUTTON_C_POS, "C")

        # Title text on shell
        title = self.large_font.render("DIGI-PET", True, (255, 255, 255))
        self.screen.blit(title, (SHELL_WIDTH // 2 - title.get_width() // 2, 80))

    def draw_button(self, pos, label):
        color = (255, 100, 100) if self.button_states.get(label) else (200, 50, 50)
        pygame.draw.circle(self.screen, color, pos, BUTTON_RADIUS)
        pygame.draw.circle(self.screen, (0, 0, 0), pos, BUTTON_RADIUS, width=3)

        text = self.large_font.render(label, True, (0, 0, 0))
        text_rect = text.get_rect(center=pos)
        self.screen.blit(text, text_rect)

    def render_game_screen(self, pet, pet_sprite, mode="main", poop_sprite=None, food_sprite=None):
        # Fill game screen background
        bg_color = COLOR_SCREEN_BG if not pet.is_sleeping else (50, 60, 10)
        self.game_surface.fill(bg_color)

        if mode == "main":
            # Draw icons
            for i in range(8):
                is_selected = (i == self.selected_icon)
                color = COLOR_PIXEL if is_selected else (120, 150, 10)
                x = (i % 4) * (SCREEN_WIDTH // 4) + 4
                y = 2 if i < 4 else SCREEN_HEIGHT - 6
                if i == 7 and (pet.is_sick or pet.has_poop or pet.hunger < 20):
                    if pygame.time.get_ticks() % 1000 < 500: color = COLOR_PIXEL
                pygame.draw.rect(self.game_surface, color, (x, y, 5, 5), width=0 if is_selected else 1)

            # Draw poop
            if pet.has_poop and poop_sprite:
                self.game_surface.blit(poop_sprite, (SCREEN_WIDTH - 18, SCREEN_HEIGHT // 2))

            # Draw pet
            if pet_sprite:
                # Simple walk animation
                offset_x = (pygame.time.get_ticks() // 500 % 4) - 2
                pet_rect = pet_sprite.get_rect(center=(SCREEN_WIDTH // 2 + offset_x, SCREEN_HEIGHT // 2 + 2))
                self.game_surface.blit(pet_sprite, pet_rect)

        elif mode == "stats":
            stats = pet.get_status_summary()
            y_off = 2
            for key, val in stats.items():
                if key in ["Hunger", "Happiness", "Energy"]:
                    # Draw bars instead of text for main stats
                    text = self.font.render(f"{key[0]}:", False, COLOR_PIXEL)
                    self.game_surface.blit(text, (2, y_off))
                    pygame.draw.rect(self.game_surface, COLOR_PIXEL, (12, y_off + 2, 30, 4), 1)
                    pygame.draw.rect(self.game_surface, COLOR_PIXEL, (13, y_off + 3, int(28 * (val/100)), 2))
                    y_off += 6
                elif key == "Weight":
                    text = self.font.render(f"W:{val}g", False, COLOR_PIXEL)
                    self.game_surface.blit(text, (2, y_off))
                    y_off += 6
                if y_off > SCREEN_HEIGHT - 6: break

        elif mode == "feeding":
            if pet_sprite:
                self.game_surface.blit(pet_sprite, (5, SCREEN_HEIGHT // 2 - 4))
            if food_sprite:
                self.game_surface.blit(food_sprite, (SCREEN_WIDTH - 15, SCREEN_HEIGHT // 2 - 4))

        # Scale and blit to main screen
        pygame.transform.scale(self.game_surface, (SCREEN_WIDTH * SCALE, SCREEN_HEIGHT * SCALE), self.scaled_surface)

        screen_pos = (
            (SHELL_WIDTH - SCREEN_WIDTH * SCALE) // 2,
            (SHELL_HEIGHT - SCREEN_HEIGHT * SCALE) // 2 - 50
        )
        self.screen.blit(self.scaled_surface, screen_pos)
