import pygame
class Reflector:

    def __init__(self, wiring, name):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.name = name

    def reflect(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def draw(self, screen, x, y, width, height, font):

        #Rectangle
        rectangle = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, (255, 255, 255), rectangle, width=2, border_radius=15)
       
        #Left side letters
        for i in range(26):
            letter = self.left[i]
            letter = font.render(letter, True, ("grey"))
            text_box = letter.get_rect(center = (x + width / 4, y + (i+1)*height/27))            
            screen.blit(letter, text_box)

        #Right side letters
        for i in range(26):
            letter = self.right[i]
            letter = font.render(letter, True, ("grey"))
            text_box = letter.get_rect(center = (x + width*3/4, y + (i+1)*height/27))
            screen.blit(letter, text_box)       