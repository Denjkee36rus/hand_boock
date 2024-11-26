class Car:
    pass

setattr(Car, 'model', 'Toyota')
setattr(Car, 'color', 'розовый')
setattr(Car, 'number', 'G1231')

print(Car.__dict__['color'])