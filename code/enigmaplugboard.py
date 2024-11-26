class Plugboard:
    
    def __init__(self, pairs):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            a, b = pair
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