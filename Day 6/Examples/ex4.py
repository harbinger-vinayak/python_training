"""
Constructor
"""

class Car(object):

    def __init__(self, name, steering_type='Manual'):
        self.name = name
        self.steering_type = steering_type

    def capitalize(self):
        return self.name[0].upper() + self.name[1:]


audi = Car('audi')
merc = Car(name='merc', steering_type='Automatic')  # Instance with mandatory and optional keyword

print audi.capitalize()
# print merc.capitalize()
print merc.steering_type
# print audi.steering_type
