import pygame
from src.pet import Pet
from src.constants import *
from src.render import SpriteManager

class GameLogic:
    def __init__(self, ui):
        self.ui = ui
        self.pet = Pet()
        self.pet.load()
        self.sprites = SpriteManager()
        self.running = True
        self.clock = pygame.time.Clock()
        self.mode = "main" # main, stats, feeding, training
        self.mode_timer = 0

    def handle_input(self):
        self.ui.button_states = {"A": False, "B": False, "C": False}

        # Check mouse buttons for visual feedback
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.is_button_clicked(mouse_pos, BUTTON_A_POS): self.ui.button_states["A"] = True
            elif self.is_button_clicked(mouse_pos, BUTTON_B_POS): self.ui.button_states["B"] = True
            elif self.is_button_clicked(mouse_pos, BUTTON_C_POS): self.ui.button_states["C"] = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if self.is_button_clicked(pos, BUTTON_A_POS):
                    self.on_button_a()
                elif self.is_button_clicked(pos, BUTTON_B_POS):
                    self.on_button_b()
                elif self.is_button_clicked(pos, BUTTON_C_POS):
                    self.on_button_c()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.on_button_a()
                elif event.key == pygame.K_RETURN or event.key == pygame.K_b:
                    self.on_button_b()
                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_c:
                    self.on_button_c()

    def is_button_clicked(self, mouse_pos, button_pos):
        dist = ((mouse_pos[0] - button_pos[0])**2 + (mouse_pos[1] - button_pos[1])**2)**0.5
        return dist <= BUTTON_RADIUS

    def on_button_a(self):
        if self.mode == "main":
            self.ui.selected_icon = (self.ui.selected_icon + 1) % 8
        elif self.mode == "stats":
            self.mode = "main"

    def on_button_b(self):
        if self.mode == "main":
            icon = self.ui.selected_icon
            if icon == 0: # Stats
                self.mode = "stats"
            elif icon == 1: # Food
                if self.pet.feed_meal():
                    self.mode = "feeding"
                    self.mode_timer = pygame.time.get_ticks() + 2000
            elif icon == 2: # Training
                if self.pet.train():
                    self.mode = "training"
                    self.mode_timer = pygame.time.get_ticks() + 2000
            elif icon == 3: # Clean
                self.pet.clean()
            elif icon == 4: # Lights
                self.pet.toggle_sleep()
            elif icon == 5: # Medical
                self.pet.heal()
            elif icon == 6: # Save
                self.pet.save()
        elif self.mode == "stats":
            self.mode = "main"

    def on_button_c(self):
        self.mode = "main"

    def run(self):
        while self.running:
            self.handle_input()
            self.pet.update()

            # Auto-return from timed modes
            if self.mode in ["feeding", "training"] and pygame.time.get_ticks() > self.mode_timer:
                self.mode = "main"

            # Draw everything
            self.ui.draw_shell()

            pet_sprite = self.sprites.get_pet_sprite(self.pet.species, self.pet.is_sleeping)
            poop_sprite = self.sprites.get_poop()
            food_sprite = self.sprites.get_food()

            self.ui.render_game_screen(
                self.pet,
                pet_sprite,
                mode=self.mode,
                poop_sprite=poop_sprite,
                food_sprite=food_sprite
            )

            pygame.display.flip()
            self.clock.tick(60)
