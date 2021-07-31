import pygame
from app.transparancy import setup
from app import ALPHA, WHITE

pygame.init()


class AppCore:

    def __init__(self):
        self.screen = pygame.display.set_mode(
            (0, 0), 1, pygame.FULLSCREEN | pygame.NOFRAME
        )

        setup(pygame.display.get_wm_info()["window"], ALPHA)

        with open("assets/translation_table.txt") as f:
            content = f.read()

        self.translation_table = {
            key: val for key, _, val in (
                line.partition(' ') for line in content.splitlines()
            )
        }

        self.is_running = False

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False

    def run(self):
        self.is_running = True

        while self.is_running:
            self.handle_event(pygame.event.wait())
            pygame.display.update()
