import numpy as np
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

a = np.linspace(0., 1., 101)
b = 2. * a

test_triangular = ProbabilityDensityFunction(a, b)

plt.hist(test_triangular.random_in_pdf(100000), bins = 50)
plt.show()
