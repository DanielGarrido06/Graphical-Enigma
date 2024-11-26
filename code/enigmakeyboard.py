import pygame

class Keyboard:

    def forward(self, letter):
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        return signal

    def backward(self, signal):
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter
    
    def draw(self, screen, x, y, width, height, font):

        #Rectangle
        rectangle = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, (255, 255, 255), rectangle, width=2, border_radius=15)
       
        #Letters
        for i in range(26):
            letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
            letter = font.render(letter, True, ("grey"))
            text_box = letter.get_rect(center = (x + width / 2, y + (i+1)*height/27))
            screen.blit(letter, text_box)
