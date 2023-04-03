"""Interface logic"""

import pygame

WIDTH = 1024
HEIGHT = 768

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SELECTED = (255,153,18)



class Interface:
    def __init__(self, color = WHITE, parameters = (WIDTH / 2, 5, 80, 40)):
        self.color = color
        self.parameters = parameters
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.parameters)

    def pressed(self, surface):
        pygame.draw.rect(surface, SELECTED, self.parameters, 5)

    # def draw_interface(self, surface):
        #     for k in figures_buttons:
        #         k.draw(surface)
    


brush_button = Interface(WHITE, (5, 5, 40, 40))

rect_button = Interface(WHITE, (50, 5, 40, 40))
line_button = Interface(WHITE, (95, 5, 40, 40))
circle_button = Interface(WHITE, (140, 5, 40, 40))

thickness_button_minus =Interface(WHITE, (185, 5, 40, 40))
thickness_button_value =Interface(WHITE, (230, 5, 40, 40))
thickness_button_plus =Interface(WHITE, (275, 5, 40, 40))

figures_buttons = [brush_button, rect_button, line_button, circle_button]

black_color_button = Interface(BLACK, (WIDTH - 225, 5, 40, 40))
white_color_button = Interface(WHITE, (WIDTH - 180, 5, 40, 40))
red_color_button = Interface(RED, (WIDTH - 135, 5, 40, 40))
green_color_button = Interface(GREEN, (WIDTH - 90, 5, 40, 40))
blue_color_button = Interface(BLUE, (WIDTH - 45, 5, 40, 40))

colors_buttons = [black_color_button, white_color_button, red_color_button, green_color_button, blue_color_button]

save_button = Interface(WHITE, (WIDTH / 2 - 40, 5, 80, 40))