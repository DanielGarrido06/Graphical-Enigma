import pygame
import random
from enigma import Enigma
from enigmakeyboard import Keyboard
from enigmaplugboard import Plugboard
from reflector import Reflector
from rotor import Rotor
from draw import draw

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

# Keyboard
kb = Keyboard()

def get_user_input(prompt, choices):
    while True:
        user_input = input(f"{prompt}, ou deixe em branco para escolher aleatoriamente: ").strip().upper().replace(",", " ").replace("-", " ")
        if user_input == "":
            return random.choice(choices)
        elif user_input in choices:
            return user_input
        else:
            print("Escolha inválida. Tente novamente.")

# Get user input for rotor settings
rotor_choices = ["I", "II", "III", "IV", "V"]
rotors = get_user_input("Escolha a ordem dos Rotores (ex: II V IV)", [" ".join([r1, r2, r3]) for r1 in rotor_choices for r2 in rotor_choices if r2 != r1 for r3 in rotor_choices if r3 != r1 and r3 != r2])
rotor1, rotor2, rotor3 = rotors.split()

# Get user input for reflector settings
reflector_choices = ["A", "B", "C"]
reflector = get_user_input("Escolha o Refletor (A, B, ou C)", reflector_choices)

# Get user input for ring settings
ring_settings = get_user_input("Escolha as configurações dos anéis dos Rotores (ex: 1 21 5)", [" ".join([str(r1), str(r2), str(r3)]) for r1 in range(1, 27) for r2 in range(1, 27) for r3 in range(1, 27)])
ring1, ring2, ring3 = map(int, ring_settings.split())

# Get user input for initial key settings
key_choices = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
key_settings = get_user_input("Escolha a chave inicial dos Rotores (ex: ABC)", ["".join([k1, k2, k3]) for k1 in key_choices for k2 in key_choices for k3 in key_choices])
key1, key2, key3 = key_settings[0], key_settings[1], key_settings[2]

# Get user input for plugboard settings. The random funcionality is also available, but had to be implemented in a different way
plugboard_settings = input("Escolha as configurações do Plugboard (ex: AM FL TZ), ou deixe em branco para escolher aleatoriamente: ").strip().replace(",", " ").replace("-", " ").upper().split()
plugboard_pairs = [(pair[0], pair[1]) for pair in plugboard_settings]
# Option to use random selection of 10 pairs of letters for plugboard settings
if plugboard_pairs == []:
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(letters)
    plugboard_pairs = [(letters[i], letters[i + 1]) for i in range(0, 20, 2)]    
pb = Plugboard(plugboard_pairs)

# Set the rotors, reflector, rings, and key based on user input
enigma = Enigma(eval(reflector), eval(rotor1), eval(rotor2), eval(rotor3), pb, kb)
enigma.set_rings((ring1, ring2, ring3))
enigma.set_key(f"{key1}{key2}{key3}")


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
                # Quit the program
                animating = False
            elif event.key == pygame.K_SPACE:
                # Add a space to the input and output, without moving the rotors
                INPUT += " "
                OUTPUT += " "
            elif event.key == pygame.K_DELETE:
                # Reset the Enigma Machine
                INPUT = ""
                OUTPUT = ""
                PATH = []
                enigma = Enigma(eval(reflector), eval(rotor1), eval(rotor2), eval(rotor3), pb, kb)
                enigma.set_key(f"{key1}{key2}{key3}")
            elif event.unicode.isalpha():
                # Get the key pressed and encipher it
                key = event.unicode.upper()
                key = key.translate(str.maketrans("ÁÀÂÃÄÅÇÉÈÊËÍÌÎÏÑÓÒÔÕÖÚÙÛÜÝ", "AAAAAACEEEEIIIINOOOOOUUUUY"))
                INPUT += key
                cipher, PATH = enigma.encipher(key)
                OUTPUT += cipher