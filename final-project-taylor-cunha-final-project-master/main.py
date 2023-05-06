import os
import pygame
import pygame_menu
from src.controller import Controller
import pygame_textinput
import pygame.time
os.environ['SDL_AUDIODRIVER'] = 'dummy'

class PictionaryGame:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.init()
        font = pygame.font.SysFont('Comic Sans MS', 50)
        surface = pygame.display.set_mode((1500, 800))
        pygame.display.set_caption("Pictionary Game")
        self.surface = surface
        self.font = pygame.font.Font(None, 30)
        self.controller = None
        self.set_difficulty = 0
        self.round = 1
        self.score = 0
        self.menu = pygame_menu.Menu(
            "Pictionary Game", 1500, 800, theme=pygame_menu.themes.THEME_GREEN
        )
        self.menu.add.selector(
            "Select Level: ",
            [("Easy", 1), ("Medium", 2), ("Hard", 3)],
            onchange=self.on_difficulty_change
        )
        self.menu.add.button("Play", self.start_game)
        self.menu.add.button("Quit", pygame_menu.events.EXIT)
        
    def on_difficulty_change(self, value, difficulty):
        self.set_difficulty = difficulty

    def set_difficulty(self, value, difficulty):
        self.set_difficulty = difficulty
        # self.start_game()

    def start_game(self):
        self.controller = Controller(self.surface, self.font, self.set_difficulty)
        self.controller.start_game()
        # self.controller.mainloop()
        # self.controller.start_game()

    def mainloop(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            self.surface.fill((255, 255, 255))
            self.menu.update(events)
            self.menu.draw(self.surface)
            pygame.display.flip()

if __name__ == '__main__':
    game = PictionaryGame()
    game.mainloop()


# game = PictionaryGame()
# # drawing = Drawing()
# game.mainloop()
# pygame.quit()
