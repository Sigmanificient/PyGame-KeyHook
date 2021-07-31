import pygame
from app.transparancy import setup
from app import ALPHA, WHITE

from pynput.keyboard import Listener

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

        self.bubbles = ["App Started"]
        self.font = pygame.font.SysFont("Consolas", 32)

        self.refresh = pygame.USEREVENT + 1
        self.refresh_event = pygame.event.Event(self.refresh)

        self.is_running = False

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False
            return

        if event.type == self.refresh:
            self.draw()

    def draw(self):
        if not len(self.bubbles):
            return

        self.screen.fill(ALPHA)

        offset = 0
        for word in self.bubbles[-3:]:
            text = self.font.render(str(word), True, ALPHA)
            text_rect = text.get_rect()

            text_rect.right = self.screen.get_width() - 20 - offset
            text_rect.bottom = self.screen.get_height() - 60

            offset += (text_rect.width + 40)

            pygame.draw.rect(
                self.screen,
                WHITE,
                pygame.Rect(
                    *(
                        (x - 16) if c < 2 else (x + 32)
                        for c, x in enumerate(list(text_rect))
                    )
                ),
                border_radius=5
            )

            self.screen.blit(text, text_rect)

            pygame.display.update()

    def on_press(self, key_name):
        self.bubbles.append(key_name)
        pygame.event.post(self.refresh_event)

    def run(self):
        listener = Listener(on_press=self.on_press)
        listener.start()

        pygame.event.post(self.refresh_event)
        self.is_running = True

        while self.is_running:
            self.handle_event(pygame.event.wait())
