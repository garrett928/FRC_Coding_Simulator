import pygame

import field
import robot


class Button:
    """A class to handle displaying and using a button on scrren"""

    def __init__(self, screen, name, x, y, width, height):
        self.screen = screen
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.line_width = 0
        self.color = (0, 255, 0)
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.width, self.height], self.line_width)

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_btns = pygame.mouse.get_pressed()
        print(mouse_btns)
        print(self.rect)
        print(mouse_pos)
        if mouse_btns[0] == 1 and self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            print("mouse pressed true")
            robot.x = field.RED_2[0]
            robot.y = field.RED_2[1]
            robot.theta = 0
            return True