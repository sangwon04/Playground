# Class Test
class Vehicle():
    def __init__(self, color, make, gas):
        self.color = color
        self.make = make
        self.gas = gas

    def drive(self):
        if self.gas > 0:
            print "Vroom!"
            self.gas -= 1
        else:
            print "Gas tank empty"
