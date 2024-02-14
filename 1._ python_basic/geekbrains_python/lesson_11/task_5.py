class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        self.comp = complex(self.real, self.img)

    def __add__(self, other):
        return self.comp + other.comp

    def __mul__(self, other):
        return self.comp * other.comp


x = Complex(50.5, 4.3)
y = Complex(50, 4)
print(x + y)
