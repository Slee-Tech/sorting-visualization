import pygame
from bar import *
import random

class Bars(object):
    def __init__(self, num_bars):
        self.bars = []
        self.start_x = 20
        self.start_y = 0
        self.num_bars = num_bars
        self.color = None
        self.create_bars()
        self.current = None
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.sorted = []
    
    def create_bars(self):
        for i in range(self.num_bars):
            self.bars.append(Bar(self.start_x, random.randrange(100,720,10), 2))
            self.start_x += 20
    
    def bubble_sort(self, window):
        for i in range(len(self.bars)):
           
            for j in range(len(self.bars)-i-1):
                if self.bars[j].height > self.bars[j+1].height:
                    # highlight the current bars 
                    self.bars[j].highlighted = True
                    self.bars[j+1].highlighted = True
                    # swap current height if greater
                    temp = self.bars[j].height
                    self.bars[j].height = self.bars[j+1].height
                    self.bars[j+1].height = temp
                self.clock.tick(self.fps)
                window.fill((0,0,0))
                for bar in self.bars:
                    bar.render(window)
                pygame.display.update()
                # reset current highlighted bars
                self.bars[j].highlighted = False
                self.bars[j+1].highlighted = False
        # pause after completed to see sorted list
        pygame.time.delay(3000)

def main():
    pygame.init()
    window = pygame.display.set_mode((1280, 720)) # changed from 1280 width
    pygame.display.set_caption("Bubble Sort Visualization")
    clock = pygame.time.Clock()
    test_bars = Bars(64)
    test_bars.bubble_sort(window)
    pygame.quit()

if __name__ == '__main__':
    main()