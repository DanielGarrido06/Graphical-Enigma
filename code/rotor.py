class Rotor:

    def __init__(self, wiring, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notch = notch

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
        #Rotate the rotor back
        self.rotate_back()
        
        #Adjust the turnover notch in relation to the wiring of the rotor
        position_notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.notch)
        self.notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(position_notch - position) % 26]

