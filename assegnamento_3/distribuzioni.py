import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
import math
from matplotlib import pyplot as plt

class ProbabilityDensityFunction(InterpolatedUnivariateSpline):
    '''
    La classe definisce funzioni di distribuzione
    '''
    
    def __init__(self, x, y):
        '''
        Costruttore
        '''
        InterpolatedUnivariateSpline.__init__(self, x, y)
        ycdf = np.array([self.integral(x[0], xcdf) for xcdf in x])
        # ycdf è un array in cui ogni elemento è dato dall'integrale di self, quindi della
        # funzione densità di probabilità, tra il primo elemento di x e l'ennesimo
        # ho quindi un array di punti che seguono l'andamento della cumulative function
        self.cfd = InterpolatedUnivariateSpline(x, ycdf, k = 3)
        # Faccio la spline e ho la cumulative function continua
        xppf, ippf = np.unique(ycdf, return_index = True)
        # xppf sono gli elementi unici di ycdf, ippf è l'indice di tali elementi dell'array
        # è la percent point function perchè ho invertito gli elementi in x e in y
        yppf = x[ippf]
        # y della ppf sono gli argomenti di x indicizzati da ippf
        self.ppf = InterpolatedUnivariateSpline(xppf, yppf)

    def prob(self, x1, x2):
        '''
        Ritorna la peobabilità che una variabile random cada nell'intervallo [x1, x2]
        '''
        return self.cdf(x2) - self.cdf(x1)
        # La Cumulative Function dà la probabilità che la variabile cada a sx del suo argomento

    def rnd(self, size = 1000):
        '''
        Restituisce un array di valori randomici secondo la distribuzione di probabilità
        '''
        return self.ppf(np.random.uniform(size=size))

def test_triangular():
    x = np.linspace(0., 1., 101)
    y = 2. * x
    pdf = ProbabilityDensityFunction(x, y)
    a = np.array([0.2, 0.6])
    print(pdf(a))
    
    plt.figure('pdf')
    plt.plot(x, pdf(x))
    plt.show()

test_triangular()
    