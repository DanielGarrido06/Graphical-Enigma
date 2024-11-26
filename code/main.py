from enigma import Enigma
from enigmakeyboard import Keyboard
from enigmaplugboard import Plugboard
from reflector import Reflector
from rotor import Rotor



# Historical rotor wirings and notches, taken from https://en.wikipedia.org/wiki/Enigma_rotor_details
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

# Historical reflector wirings, taken from https://en.wikipedia.org/wiki/Enigma_rotor_details
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# Keyboard and plugboard
kb = Keyboard()
pb = Plugboard([("A", "B"), ("C", "D"), ("E", "F")])

# Create the enigma machine
enigma = Enigma(B,IV,II,I,pb,kb)

# TODO: Set the rings
# enigma.set_rings((1,1,1))

# Set the key
enigma.set_key("CAT")

message = "TESTINGTESTINGTESTINGTESTING"
cipher_text = ""
for letter in message:
    cipher_text += enigma.encipher(letter)

print(cipher_text)
print(enigma.rotor3.notch)