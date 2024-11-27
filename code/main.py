import pygame

from enigma import Enigma
from enigmakeyboard import Keyboard
from enigmaplugboard import Plugboard
from reflector import Reflector
from rotor import Rotor
from draw import draw

# Initialize pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma Machine")

# Fonts
FONT = pygame.font.SysFont("Courier", 25)
BOLD_FONT = pygame.font.SysFont("Courier", 25, bold=True)


# Variables for the GUI
WIDTH = 1600
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGINS = {"left": 100, "right": 100, "top": 200, "bottom": 200}
GAP = 100

INPUT = ""
OUTPUT = ""
PATH = []


# Historical rotor wirings and notches, taken from https://en.wikipedia.org/wiki/Enigma_rotor_details
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", "I")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E", "II")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V", "III")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J", "IV")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z", "V")

# Historical reflector wirings, taken from https://en.wikipedia.org/wiki/Enigma_rotor_details
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD", "A")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT", "B")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL", "C")

# Keyboard and plugboard
kb = Keyboard()
pb = Plugboard([("A", "V"), ("C", "X"), ("Q", "D"), ("M", "P"), ("T", "Z"), ("G", "S"), ("K", "N"), ("Y", "L"), ("R", "U"), ("H", "W")])

# Create the enigma machine
enigma = Enigma(B,IV,II,V,pb,kb)

# TODO: Set the rings
# Good luck getting this to work properly with everything else, I couldn't!
# enigma.set_rings((1,1,1))

# Set the key
enigma.set_key("XSP")

animating = True
while animating:   

    # Draw enigma machine
    draw(enigma, PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD_FONT)

    #Text Input
    text = BOLD_FONT.render(INPUT, True, ("white"))
    text_box = text.get_rect(center = (WIDTH/2, MARGINS["top"]/2))
    SCREEN.blit(text, text_box)

    #Text Output
    text = BOLD_FONT.render(OUTPUT, True, ("white"))
    text_box = text.get_rect(center = (WIDTH/2, MARGINS["top"]/2+25))
    SCREEN.blit(text, text_box)     
    
    # Update the screen
    pygame.display.flip()

        # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                animating = False
            elif event.key == pygame.K_SPACE:
                INPUT += " "
                OUTPUT += " "
            elif event.unicode.isalpha():
                key = event.unicode.upper()
                INPUT += key
                cipher, PATH = enigma.encipher(key)
                OUTPUT += cipher