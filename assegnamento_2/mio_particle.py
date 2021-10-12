import math
import logging

class Particella:
    
    def __init__(self, massa, carica, nome, impulso = 0):
        self.massa = massa
        self.carica = carica
        self.nome = nome
        self.impulso = impulso
       
        
    def print_info(self):
        print(f'La particella in esame ha le seguenti proprietà: \n "{self.nome}" di massa {self.massa} e carica {self.carica}')
      
    def print_energia(self):
        print(f'L\'energia della particella è: {self.energia}')
        
    def print_impulso(self):
        print(f'L\'impulso della particella è: {self.impulso}')
    
    def print_beta(self):
        print(f'La beta della particella è: {self.beta}')
    
    
    @property
    def impulso(self):
        return self._impulso
    
    @impulso.setter
    def impulso(self, valore):
        if valore < 0:
            logging.error('Il valore dell\'impulso non può essere negativo')
            print('Il valore dell\'impulso viene settato a 0')
            self._impulso = 0.
        else:
            self._impulso = valore
    
### per energia e beta non esiste variabile corrispondente; c'è solo per l'impulso; per ottenere questa energia cambio l'impulso tc l'energia sia quella richiesta; nel set di energy agisco sull'impulso; Non setto direttamente self._impulso, ma richiamo il setter dell'impulso, che mi fa l'ulteriore controllo. self._impulso: cambio valore; self.impulso: entro nel setter

    @property
    def energia(self):
        return math.sqrt(self.massa**2 + self.impulso**2)
    
    @energia.setter
    def energia(self, valore):
        if valore < self.massa:
            logging.error('Il valore dell\'energia non può essere minore di quello della massa')
        else:
            self.impulso = math.sqrt(valore**2 - self.massa**2)
    
    @property
    def beta(self):
        return self.impulso
    
    @beta.setter
    def beta(self, valore):
        if valore < 0 or valore > 1:
            logging.error('Il valore di beta non può essere negativo')
        else:
            self.impulso = valore
            
    
    # @property
    # def gamma(self):
    #     return 1/math.sqrt(1-self.impulso**2)
    # 
    # @gamma.setter
    # def gamma(self, gamma):
    #     if gamma < 1:
    #         logging.error('Il valore di gamma deve essere maggiore di 1')
    #     else:
    #         self.gamma = gamma
    #         self.impulso = math.sqrt(1 - 1/gamma**2)
            
class Protone(Particella):
    def __init__(self):
        Particella.__init__(self, 938, 1, 'p', impulso = 0)
        
class Elettrone(Particella):
    def __init__(self):
        Particella.__init__(self, 0.511, -1, 'e-', impulso = 0)

p = Protone()

p.print_info()