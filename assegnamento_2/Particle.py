import math
import logging

class Particle:
    '''
    Definisco la classe particella
    '''
    def __init__(self, name, mass, charge, momentum = 0):
        self.name = name
        self.mass = mass
        self.charge = charge
        self.momentum = momentum

    def print_info(self):
        print(f'La particella "{self.name}" ha massa {self.mass} e carica {self.charge}')

    def print_info_plus(self):
        print(f'La particella ha un impulso pari a {self.momentum: .2f} e un\'energia di \
{self.energy} Mev/c^2')

    @property
    def momentum(self):
        return self._momentum

    @momentum.setter
    def momentum(self, value):
        if value < 0:
            logging.error('Il valore dell\'impulso non può essere negativo')
            print('L\'impulso verrà inizializzato a 0')
            self._momentum = 0
        else:
            self._momentum = value

    @property
    def energy(self):
        return math.sqrt(self._momentum**2 + self.mass**2)

    @energy.setter
    def energy(self, value):
        if value < self.mass:
            logging.error('Il valore dell\'energia non può essere minore della massa')
            print('L\'energia della particella verrà inizializzata con la sua massa')
        else:
            self._momentum = math.sqrt(value**2 - self.mass**2)

protone = Particle('proton', 138, 1)

protone.energy = 200

protone.print_info()
protone.print_info_plus()
