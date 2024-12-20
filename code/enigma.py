class Enigma:

    def __init__(self, reflector, rotor1, rotor2, rotor3, plugboard, keyboard):
        self.reflector = reflector
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.plugboard = plugboard
        self.keyboard = keyboard

    def encipher(self, letter):

    
        # Rotate the rotors
        if self.rotor2.left[0] == self.rotor2.notch and self.rotor3.left[0] == self.rotor3.notch:
            self.rotor1.rotate()
            self.rotor2.rotate()
            self.rotor3.rotate()

        #Double step anomaly. IDE might complain about the elif statement, but it is historically correct.
        elif self.rotor2.left[0] == self.rotor2.notch:
            self.rotor1.rotate()
            self.rotor2.rotate()
            self.rotor3.rotate()

        elif self.rotor3.left[0] == self.rotor3.notch:
            self.rotor2.rotate()
            self.rotor3.rotate()

        else:
            self.rotor3.rotate()


        # Pass the letter through the plugboard, rotors, reflector, and back through the rotors and plugboard
        # This surely isn't the prettiest way to write this, but it's the most readable I could come up with
        signal = self.keyboard.forward(letter)
        path = [signal, signal]
        signal = self.plugboard.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.rotor3.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.rotor2.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.rotor1.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.reflector.reflect(signal)
        path.append(signal)
        path.append(signal)
        path.append(signal)
        signal = self.rotor1.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.rotor2.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.rotor3.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.plugboard.backward(signal)
        path.append(signal)
        path.append(signal)
        letter = self.keyboard.backward(signal)
        return letter, path

    def backspace(self):
        if self.rotor2.left[-1] == self.rotor2.notch and self.rotor3.left[-1] == self.rotor3.notch:
            self.rotor1.rotate_back()
            self.rotor2.rotate_back()
            self.rotor3.rotate_back()
        
        elif self.rotor2.left[-1] == self.rotor2.notch:
            self.rotor1.rotate_back()
            self.rotor2.rotate_back()
            self.rotor3.rotate_back()
        
        elif self.rotor3.left[-1] == self.rotor3.notch:
            self.rotor2.rotate_back()
            self.rotor3.rotate_back()

        else:
            self.rotor3.rotate_back()    

    def set_key(self, key):
        self.rotor1.rotate_to_letter(key[0])
        self.rotor2.rotate_to_letter(key[1])
        self.rotor3.rotate_to_letter(key[2])

    def set_rings(self, rings):
        self.rotor1.set_ring(rings[0])
        self.rotor2.set_ring(rings[1])
        self.rotor3.set_ring(rings[2])