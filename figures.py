"""Figures drawing logic"""

import pygame
from math import sqrt

class Figures:
    def __init__(self,start_pos_x, start_pos_y, end_pos_x, end_pos_y, line_thickness, color):
        self.start_pos_x = start_pos_x
        self.start_pos_y = start_pos_y
        self.end_pos_x = end_pos_x
        self.end_pos_y = end_pos_y
        self.line_thickness = line_thickness
        self.color = color
    
    def draw(self, screen):
        pass
    
class Rect(Figures):
    def __init__(self, start_pos_x, start_pos_y, end_pos_x, end_pos_y, line_thickness = 0, color = (0, 0, 0)):
        super().__init__(start_pos_x, start_pos_y, end_pos_x, end_pos_y, line_thickness, color)

    def draw(self, screen):
        # self.start_x = min(self.start_pos_x, self.end_pos_x)                   # negative coordinates drawing
        # self.start_y = min(self.start_pos_y, self. end_pos_y)                  # negative coordinates drawing
        # self.end_x = max(self.start_pos_x, self.end_pos_x)                     # negative coordinates drawing
        # self.end_y = max(self.start_pos_y, self.end_pos_y)                     # negative coordinates drawing
        width = self.end_pos_x - self.start_pos_x
        #print(f"w: {width}")
        height = self.end_pos_y - self.start_pos_y
        #print(f"h: {height}")
        pygame.draw.rect(screen, self.color, [self.start_pos_x, self.start_pos_y, width, height], self.line_thickness)
    

class Line(Figures):
    def __init__(self, start_pos_x, start_pos_y, end_pos_x, end_pos_y, line_thickness = 1, color = (0, 0, 0)):
        super().__init__(start_pos_x, start_pos_y, end_pos_x, end_pos_y, line_thickness, color)
    
    def draw(self, screen):
        #print(f"x: {end_pos_x}")
        #print(f"y: {end_pos_y}")
        pygame.draw.line(screen, self.color, [self.start_pos_x, self.start_pos_y], [self.end_pos_x, self.end_pos_y], self.line_thickness)   

class Circle(Figures):
    def __init__(self, start_pos_x, start_pos_y, end_pos_x, end_pos_y, line_thickness = 0, color = (0, 0, 0)):
        super().__init__(start_pos_x, start_pos_y, end_pos_x, end_pos_y, line_thickness, color)
    
    def draw(self, screen):
        radius = sqrt((self.end_pos_x - self.start_pos_x)**2 + (self.end_pos_y - self.start_pos_y)**2)
        pygame.draw.circle(screen, self.color, [self.start_pos_x, self.start_pos_y], radius, self.line_thickness) 


class Brush(Figures):
    def __init__(self, start_pos_x, start_pos_y, end_pos_x, end_pos_y, line_thickness = 1, color = (0, 0, 0)):
        super().__init__(start_pos_x, start_pos_y, end_pos_x, end_pos_y, line_thickness, color)
        
    def draw(self, screen):
        #print(f"start x: {start_pos_x}")
        #print(f"start y: {start_pos_y}")
        radius = self.line_thickness
        pygame.draw.circle(screen, self.color, [self.end_pos_x, self.end_pos_y], radius) 
