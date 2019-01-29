"""
Multiple Inheritance
"""

from ex3 import Car


class EuroCar(Car):
    def moveCar(self, direction):
        print 'Euro car is moving to {} direction'.format(direction)
        super(EuroCar, self).movecar(direction)  # It is used when we call base class function


audi = EuroCar()
audi.moveCar('Left')
