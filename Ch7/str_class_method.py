class Phone:
    def __init__(self, brand, model, memory, price):
        self.brand = brand
        self.model = model
        self.memory = memory
        self.price = price

    def __str__(self):
        return ('My phone is a {} {} with {} GB of memory and costs ${:.2f}'.format(self.brand, self.model, self.memory, self.price))

samsungGalaxy = Phone("Samsung", "Galaxy", 16, 595.99)
pixel = Phone("Google", "Pixel", 32, 899.50)
print(samsungGalaxy)
print(pixel)
