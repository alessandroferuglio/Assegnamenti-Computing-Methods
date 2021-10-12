import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline as IUSpline

class ProbabilityDensityFunction:
    '''
    Classe definisce una densità di probabilità
    '''
    def __init__(self, x, y, k = 3):
        '''
        Costruttore
        '''
        self.x = x
        self.y = y
        self.k = k
        self.pdf = IUSpline(x, y, k)
    
    # def prob(self, a, b):
    #     '''
    #     Probabilità che una variabile random generata secondo pdf cada nell'intervallo [a, b]
    #     '''
    #     return self.pdf.integral(a, b)
    # 
    # def random(self, n = 100):
    #     '''
    #     Genera n numeri random secondo la distribuzione di probabilità definita
    #     '''
    #     ycf = np.array([pdf.integral(x[0], xcf) for xcf in x])
    #     xppf, ippf = np.unique(ycf, return_intex = True)
    #     yppf = x[ippf]
    #     cf = IUSpline(xppf, yppf)
    #     return cf(np.random.uniform(n))
        
x = [0., 0.2, 0.5, 0.8, 1.]
y = [0., 0.2, 0.5, 0.8, 1.]

distribuzione_triangolare = ProbabilityDensityFunction(x, y, 3)

