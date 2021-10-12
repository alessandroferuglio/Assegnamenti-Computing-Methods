import math
import argparse

class Particle:
    
    def __init__(self, mass, charge, name, momentum = 0.):
        """Momentum è opzionale, lo inizializzo con un valore pari a 0"""
        """Definisco gli attributi della classe Particle"""  
        self.mass = mass
        self.charge = charge
        self.name = name 
        self.momentum = momentum
        ### scrivendo qui senza underscore, la riga self.momentum chiama il 
        ### property setter, che inizializza l'attributo underscoremomentum
          
    
    """Creo metodo print"""
    def info(self):
        msg = 'Particle "{name}" of mass {mass: .3f} Mev/c^2, charge: {charge}'
        return msg.format(name=self.name, mass=self.mass, charge=self.charge)
        
    @property
    def energy(self):
         return math.sqrt(self.mass**2 + self.momentum**2)
    
    @energy.setter
    def energy(self, energy):
        if energy < self.mass:
            print('Cannot set the energy to a value lower than the particle mass')
        else:
            self.momentum = math.sqrt(energy**2 - self.mass**2)
  
### PROBLEMA: scritta così la property non funziona, è circolare,  self.momentum
### chiama la property momentum, e così all'infinito
    @property
    def momentum(self):
        return self._momentum
 
### anche momentum.setter, quando scrivo self.momentum, mi richiama il setter stesso
### SOLUZIONE: torno agli attributi e trasformo momentum in una variabile privata
### ora agisco direttamente su attributo e non chiamo più il setter
    @momentum.setter
    def momentum(self, momentum):
        if momentum < 0:
            print('Cannot set the momentum to a negative value')
            print('Momentum will be set to 0.')
            self._momentum = 0.
        else:
            self._momentum = momentum
     
p = Particle(105.6, -1, 'Muon')
print(p.info())
print('Particle energy: ', p.energy)
p.energy = 200
print(p.energy)
print(p.momentum)
p.momentum = 20
print(p.momentum)

proton = Particle(939, charge = +1, name = 'Proton', momentum = -10)
print(proton.energy)