import pygame

class Plugboard:
    
    def __init__(self, pairs):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.list = []
        for pair in pairs:
            a, b = pair
            self.list.append((a, b))
            # Replace a with #, then replace b with a, then replace # with b
            # This effectively swaps the two letters
            self.left = self.left.replace(a, '#').replace(b, a).replace('#', b)
    
    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
    
    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
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