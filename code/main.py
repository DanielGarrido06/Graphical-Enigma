'''
Reflector: A
Rotors: I-II-III
Plugboard: A-R, G-K, O-X
Message: A => X
'''

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

# Historical reflector wirings and notches, taken from https://en.wikipedia.org/wiki/Enigma_rotor_details
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

letter = "A"
kb = Keyboard()
pb = Plugboard([("A", "R"), ("G", "K"), ("O", "X")])
signal = kb.forward(letter)
signal = pb.forward(signal)
signal = III.forward(signal)
signal = II.forward(signal)
signal = I.forward(signal)
signal = A.reflect(signal)
signal = I.backward(signal)
signal = II.backward(signal)
signal = III.backward(signal)
signal = pb.backward(signal)
letter = kb.backward(signal)
print(f"Letter: {letter}")