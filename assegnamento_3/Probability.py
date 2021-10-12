import numpy as np
import unittest
from matplotlib import pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

class ProbabilityDensityFunction:
    '''La classe permette di definire densità di probabilità
    '''
    def __init__(self, x, y, k = 3):
        ''' Costruttore
        '''
        self.x = x
        self.y = y
        self.k = k
        self.pdf = InterpolatedUnivariateSpline(x, y, k = k)

    def prob_nel_punto(self, x):
        ''' Restituisce la probabilità nel punto indicato
        '''
        return self.pdf(x)

    def prob_in(self, x1, x2):
        ''' Restituisce la probabilità che un numero generato in modo randomico secondo la \
        distribuzione di probabilità definita, cada nell'intevallo [x1, x2]
        '''
        return self.pdf.integral(x1, x2)

    def random_in_pdf(self, numb):
        '''Genera n numeri casuali distribuiti secondo la distribuzioned di probabilità definita
        '''
        ycf = np.array([self.pdf.integral(self.x[0], xcf) for xcf in self.x])
        xppf, ippf = np.unique(ycf, return_index = True)
        yppf = self.x[ippf]
        inversecf = InterpolatedUnivariateSpline(xppf, yppf)
        return inversecf(np.random.uniform(0., 1., size = numb))
        
class TestTriangular(unittest.TestCase):
    '''Unit test con distribuzione triangolare
    '''

    def test_prob_nel_punto(self):
        '''Verifica calcolo della probabilità in diversi punti
        '''
        a = np.linspace(0., 1., 101)
        b = 2. * a
        pdf = ProbabilityDensityFunction(a, b)
        self.assertAlmostEqual(pdf.prob_nel_punto(0), 0)
        self.assertAlmostEqual(pdf.prob_nel_punto(0.5), 1)
        self.assertAlmostEqual(pdf.prob_nel_punto(1), 2)
        
    def test_prob_in(self):
        '''Verifica la probabilità calcolata in diversi intervalli
        '''
        a = np.linspace(0., 1., 101)
        b = 2. * a
        pdf = ProbabilityDensityFunction(a, b)
        self.assertAlmostEqual(pdf.prob_in(0, 1), 1)
        self.assertAlmostEqual(pdf.prob_in(0, 0.5), 0.25)
        self.assertAlmostEqual(pdf.prob_in(0.5, 1), 0.75)
        
    def test_random_in_pdf(self):
        '''Verifica che per un numero sufficientemente alto di numeri la distribuzione generata
        tenda a quella triangolare'''
        
        

### Fa sì che runno lo unit test solo quando lo chiamo come 'python modulo.py' in maniera esplicita
### e non quando faccio 'import modulo'
if __name__ == '__main__':
    unittest.main()
