import pygame

import visual
from constants import *


class Button(visual.DrawableObject):
    """Класс для кнопок"""
    def __init__(self, x, y, image_off, image_on, scale):
        button_width = image_off.get_width()
        button_height = image_off.get_height()
        self.image_off = pygame.transform.scale(image_off, (int(button_width * scale), int(button_height * scale)))
        self.image_on = pygame.transform.scale(image_on, (int(button_width * scale), int(button_height * scale)))
        self.rect = self.image_off.get_rect()
        self.rect.topleft = (x, y)
        self.collided = False
        self.clicked = False

    def draw_on(self, surface):
        """Рисует кнопку"""
        if self.collided:
            surface.blit(self.image_on, (self.rect.x, self.rect.y))
        else:
            surface.blit(self.image_off, (self.rect.x, self.rect.y))

    def collide(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.collided = True
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True
        if not self.rect.collidepoint(pos):
            self.collided = False
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
        return action


def button_main():
    """Функция для тестирования"""
    start_button = Button(350, 150, start_img_off, start_img_on, 1)
    load_save_button = Button(350, 350, load_save_off, load_save_on, 1)
    exit_button = Button(350, 550, exit_img_off, exit_img_on, 1)
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Buttons')
    run = True
    while run:
        screen.fill((100, 255, 200))
        start_button.draw_on(screen)
        exit_button.draw_on(screen)
        load_save_button.draw_on(screen)
        if start_button.collide(screen):
            print("Hello")
        if exit_button.collide(screen):
            run = False
        if load_save_button.collide(screen):
            print("In progress...")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()


if __name__ == "__main__":
    button_main()





