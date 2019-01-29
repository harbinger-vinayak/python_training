
class Car(object):
    tyres = 5
    type = 'manual'

    # __var = 10  # it is private variable

    def movecar(self, direction):
        self.direction = direction
        print 'Car is moving to {} direction'.format(self.direction)

    def getdirection(self):
        return self.direction


if __name__ == '__main__':
    audi = Car()  # Instance of a class
    # print audi.type
    # print audi.__Car__var

    audi.movecar(direction='Left')
    print audi.direction  # Left
    print audi.getdirection()  # Left
