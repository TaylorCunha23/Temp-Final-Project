import pygame
import random
from pygame_menu import Menu
import pygame_textinput
import sys

# textinput = pygame_textinput.TextInputVisualizer()

pygame.init()
pygame.display.init()
FPS = 60

class Controller:
    def __init__(self, surface, font, set_difficulty):
        self.set_difficulty = set_difficulty
        self.score = 0
        self.round = 1
        self.surface = surface
        self.font = font
        # self.textinput = pygame_textinput.TextInput(font_family='Comic Sans MS', font_size=50)
        self.textinput = pygame_textinput.TextInputVisualizer()
        self.correct_guess = None
        self.menu = None

    def mainloop(self):
        self.start_game()

    
    #     menu = Menu('Pictionary Game', 800, 800, theme=pygame_menu.themes.THEME_GREEN)
    #     menu.add_selector('Difficulty :', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=self.set_difficulty)
    #     menu.add_button('Start', self.start_game)
    #     menu.add_button('Quit', pygame_menu.events.EXIT)

    #     menu.mainloop(pygame.display.set_mode((800, 800)))

    # def set_difficulty(self, difficulty):
    #     self.difficulty = difficulty


    # def generate_drawing(self):
    #     # function to generate a drawing
    #     pass

    def calculate_score(self, time_left):
        if time_left > 45000:
            return 10
        elif time_left > 30000:
            return 8
        elif time_left > 15000:
            return 5
        else:
            return 2

    def start_game(self):
    #     pygame.display.set_caption("Pictionary Game")
    #     screen = pygame.display.set_mode((800, 800))
        # clock = pygame.time.Clock()
        if self.set_difficulty == 0:
            self.set_difficulty = 1  # Set difficulty to easy if not changed in the menu
        self.score = 0
        self.round = 0
        self.play_round()

    def play_round(self):
        # while True:
            drawing = Drawing(self.set_difficulty, self.round, self.surface)
            self.round += 1
            self.surface.fill((255,255,255))
            pygame.display.update()
            self.correct_guess = drawing.correct_guess
            timer = 30
            wait_for_key = True
            while timer > 0 and wait_for_key:
                drawing.generate()
                events = pygame.event.get()
                textinput = pygame_textinput.TextInputVisualizer()
                textinput.update(events)
                self.surface.blit(textinput.surface, (10, 10))
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    else:
                        if textinput == self.correct_guess:
                        # wait_for_key = False
                        # if event.key == pygame.K_RETURN:
                            # if self.textinput.get_text() == correct_guess:
                            self.score += self.calculate_score(timer)
                            print("Correct! Next round...")
                            if self.round < 3:
                                self.surface.fill((255,255,255))
                                pygame.display.update()
                                break
                                    # self.play_round()
                            else:
                                print("Game Over!")
                                self.end_game()
                                return
                        else:
                            print("Wrong, try again.")
                            wait_for_input = False
                            break
                            # self.play_round()
                    # self.textinput.clear_text()
                self.surface.fill((255,255,255))
                drawing.generate()
                self.surface.blit(self.textinput.surface, (10, 10))
                pygame.display.update()
                timer -= 1
        # return self.correct_guess
       


class Drawing:
    def __init__(self, difficulty, round, surface):
        self.set_difficulty = difficulty
        self.round = round
        self.time_limit = 30
        self.timer = 0
        self.answer = ''
        self.surface = surface
        self.correct_guess = None
        # correct_guess = Drawing.correct_guess()
        # d = Drawing()
        # d.correct_guess()
        self.generate()
    
    def generate(self):
        if self.set_difficulty == 1:
            self.generate_easy()
        if self.set_difficulty == 2:
            self.generate_medium()
        if self.set_difficulty == 3:
            self.generate_hard()
            

    
    def generate_easy(self):
        #star
        if self.round == 1:
            self.correct_guess = 'star'
            star_points = [(100, 0), (120, 50), (170, 50), (130, 80), (150, 130), (100, 100), (50, 130), (70, 80), (30, 50), (80, 50)]
            star_color = (255, 255, 0)
            pygame.draw.polygon(self.surface, star_color, star_points)
            pygame.display.flip()
        #banana
        if self.round == 2:
            self.correct_guess = 'banana'
            banana_points = [(250, 400), (200, 500), (250, 600), (400, 650), (550, 650), (700, 600), (750, 500), (700, 400)]
            pygame.draw.polygon(self.surface, "YELLOW", banana_points)
            pygame.display.flip()
        #phone
        if self.round == 3:
            self.correct_guess = 'phone'
            pygame.draw.rect(self.surface, "BLACK", (550, 200, 400, 700))
            pygame.draw.rect(self.surface, "GRAY", (560, 210, 380, 680))
            pygame.draw.circle(self.surface, "GRAY", (750, 150), 100)
            pygame.draw.rect(self.surface, "GRAY", (730, 110, 40, 70))
            pygame.draw.rect(self.surface, "GRAY", (710, 40, 80, 70))
            pygame.draw.rect(self.surface, "GRAY", (720, 20, 60, 20))
            pygame.draw.rect(self.surface, "GRAY", (720, 700, 60, 20))
            pygame.draw.rect(self.surface, "WHITE", (580, 230, 360, 640))
            pygame.display.flip()

    def generate_medium(self):
        #house
        if self.round == 1:
            self.correct_guess = 'house'
            pygame.draw.polygon(self.surface, "red", [(500, 200), (800, 200), (650, 50)])
            pygame.draw.rect(self.surface, "blue", (500, 200, 300, 300))
            pygame.draw.rect(self.surface, "GREEN", (600, 400, 100, 100))
            pygame.draw.circle(self.surface, "GRAY", (680, 450), 5)
            pygame.draw.rect(self.surface, "WHITE", (520, 250, 75, 75))
            pygame.draw.rect(self.surface, "WHITE", (705, 250, 75, 75))
            pygame.display.flip()
        #laptop
        if self.round == 2:
            self.correct_guess = 'laptop'
            # Draw the laptop body
            laptop_width = 600 
            laptop_height = 400
            screen_width = 500 
            screen_height = 300
            button_width = 30
            button_height = 30
            laptop_x = (800 - laptop_width) // 2 
            laptop_y = (1500 - laptop_height) // 2
            pygame.draw.rect(self.surface, "GRAY", (laptop_x, laptop_y, laptop_width, laptop_height))
            screen_x = laptop_x + 50  
            screen_y = laptop_y + 50
            pygame.draw.rect(self.surface, "BLACK", (screen_x, screen_y, screen_width, screen_height))
            button_x = screen_x + screen_width - button_width - 10  
            button_y = screen_y + 10
            pygame.draw.rect(self.surface, "BLUE", (button_x, button_y, button_width, button_height))
            pygame.display.flip()
        #scissors
        if self.round == 3:
            self.correct_guess = 'scissors'
            handle_width = 100 
            handle_height = 300
            blade_width = 600 
            blade_height = 100
            edge_width = 60 
            edge_height = blade_height
            handle_x = (800 - handle_width) // 2 
            handle_y = (1500 - handle_height) // 2
            pygame.draw.rect(self.surface, "GRAY", (handle_x, handle_y, handle_width, handle_height))
            pygame.draw.rect(self.surface, "WHITE", (handle_x + 10, handle_y + 10, handle_width - 20, handle_height - 20))
            blade_x = (800 - blade_width) // 2 
            blade_y = (handle_y - blade_height) // 2
            pygame.draw.rect(self.surface, "BLACK", (blade_x, blade_y, blade_width, blade_height))
            edge_x = blade_x + blade_width - edge_width 
            edge_y = blade_y
            pygame.draw.rect(self.surface, "WHITE", (edge_x, edge_y, edge_width, edge_height))
            pygame.display.flip()
    def generate_hard(self):
        #peacock
        if self.round == 1:
            self.correct_guess = 'peacock'
            pygame.draw.circle(self.surface, (0, 0, 255), (800//2, 1500//2), 150)
            pygame.draw.circle(self.surface, (0, 128, 0), (800//2-150, 1500//2), 75)
            pygame.draw.circle(self.surface, (0, 0, 0), (800//2-100, 1500//2-50), 15)
            pygame.draw.polygon(self.surface, (255, 255, 0), [(800//2-25, 1500//2), (800//2-75, 1500//2-25), (800//2-75, 1500//2+25)])
            pygame.draw.circle(self.surface, (255, 255, 0), (800//2+150, 1500//2), 100)
            pygame.draw.circle(self.surface, (255, 255, 0), (800//2+175, 1500//2-100), 75)
            pygame.draw.circle(self.surface, (255, 255, 0), (800//2+200, 1500//2), 100)
            pygame.display.flip()
        #eiffel tower
        if self.round == 2:
            self.correct_guess = "eiffel tower"
            pygame.draw.rect(self.surface, "gray", (800//2-25, 1500//2, 50, 400))
            pygame.draw.rect(self.surface, "brown", (800//2-200, 1500//2+400, 400, 50))
            pygame.draw.rect(self.surface, "gray", (800//2-150, 1500//2-300, 300, 300))
            pygame.draw.rect(self.surface, "brown", (800//2-100, 1500//2-400, 200, 100))
            pygame.draw.rect(self.surface, "gray", (800//2-10, 1500//2-500, 20, 100))
            pygame.display.flip()
        #skull
        if self.round == 3: 
            self.correct_guess = "skull"
            pygame.draw.circle(self.surface, "white", (800//2, 1500//2), 200)
            pygame.draw.line(self.surface, "black", (800//2-150, 1500//2), (800//2+150, 1500//2), 10)
            pygame.draw.line(self.surface, "black", (800//2, 1500//2-150), (800//2, 1500//2+150), 10)
            pygame.draw.circle(self.surface, "black", (800//2-80, 1500//2-60), 40)
            pygame.draw.circle(self.surface, "black", (800//2+80, 1500//2-60), 40)
            pygame.draw.circle(self.surface, "black", (800//2, 1500//2+50), 80)
            pygame.display.flip()           