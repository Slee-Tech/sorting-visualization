import pygame

class Bar(object):
    def __init__(self, x, height, width):
        self.x = x
        self.width = width
        self.height = height
        self.highlighted = False
        self.color = (100, 0, 205)
        self.highlight_color = (255,255,255)

    def render(self, window):
        if not self.highlighted:
            pygame.draw.line(window, self.color, (self.x, 720), (self.x, 720-self.height), self.width)
        else:
            pygame.draw.line(window, self.highlight_color, (self.x, 720), (self.x, 720-self.height), self.width)