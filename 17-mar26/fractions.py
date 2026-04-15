# overload all operators 
# Arithmetic: + (__add__), - (__sub__), * (__mul__), / (__truediv__)
# Comparison: == (__eq__), != (__ne__), < (__lt__), > (__gt__)

class Fraction:
    
    def __init__(self, num, den):
        self.num = num
        self.den = den 
        
        