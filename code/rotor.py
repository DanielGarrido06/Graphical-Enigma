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


    def shift_string(self, string):
        shifted = ""
        for char in string:
            if char.isalpha():
                shifted += chr((ord(char) - 65 + 1) % 26 + 65)
            else:
                shifted += char
        return shifted
    
    def rotate_left_back(self):
        self.left = self.shift_string(self.left)
        

    def rotate_to_letter(self, letter):
        while self.left[0] != letter:
            self.rotate()

    def set_ring(self, position):
        # Honestly, it's a miracle this works. I bashed my head against the wall for hours trying to figure this out, and then it just worked.
        self.ring = position
        for _ in range(position - 1):
            self.right = self.shift_string(self.right)
            self.rotate_left_back()

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