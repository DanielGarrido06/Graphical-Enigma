import pygame

class Rotor:

    def __init__(self, wiring, notch, name):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notch = notch
        self.name = name
        self.ring = 1

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
    
    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal
    
    def show(self):
        print(self.left)
        print(self.right)
        print("")

    def rotate(self):
        self.left = self.left[1:] + self.left[0]
        self.right = self.right[1:] + self.right[0]

    def rotate_back(self):
        self.left = self.left[-1] + self.left[:-1]
        self.right = self.right[-1] + self.right[:-1]

    def rotate_to_letter(self, letter):
        while self.left[0] != letter:
            self.rotate()

    def set_ring(self, position):
        self.ring = position
        #Rotate the rotor back
        for _ in range(position - 1):
            self.rotate_back()
        
        #Adjust the turnover notch in relation to the wiring of the rotor
        position_notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.notch)
        self.notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(position_notch - position + 1) % 26]

    def draw(self, screen, x, y, width, height, font):

        #Rectangle
        rectangle = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, (255, 255, 255), rectangle, width=2, border_radius=15)
       
        #Left side letters
        for i in range(26):
            letter = self.left[i]
            letter = font.render(letter, True, ("grey"))
            text_box = letter.get_rect(center = (x + width / 4, y + (i+1)*height/27))
            #Highlight the top letter
            if i == 0:
                pygame.draw.rect(screen, "teal", text_box, border_radius=5)
            #Highlight the notch
            if self.left[i] == self.notch:
                letter = font.render(self.notch, True, (31, 31, 31))
                pygame.draw.rect(screen, "white", text_box, border_radius=5)
            
            screen.blit(letter, text_box)

        #Right side letters
        for i in range(26):
            letter = self.right[i]
            letter = font.render(letter, True, ("grey"))
            text_box = letter.get_rect(center = (x + width*3/4, y + (i+1)*height/27))
            screen.blit(letter, text_box)   