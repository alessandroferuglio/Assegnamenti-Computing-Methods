### IMPORTO MODULI NECESSARI
import argparse
from timeit import default_timer as timer
import logging
from matplotlib import pyplot as plt


### DEFINIZIONE FUNZIONI
def conteggio(testo):
    for carattere in testo:
        if carattere in ('a', 'A'):
            dizionario['a'] += 1
        elif carattere in ('b', 'B'):
            dizionario['b'] += 1
        elif carattere in ('c', 'C'):
            dizionario['c'] += 1
        elif carattere in ('d', 'D'):
            dizionario['d'] += 1
        elif carattere in ('e', 'E'):
            dizionario['e'] += 1
        elif carattere in ('f', 'F'):
            dizionario['f'] += 1
        elif carattere in ('g', 'G'):
            dizionario['g'] += 1
        elif carattere in ('h', 'H'):
            dizionario['h'] += 1
        elif carattere in ('i', 'I'):
            dizionario['i'] += 1
        elif carattere in ('j', 'J'):
            dizionario['j'] += 1
        elif carattere in ('k', 'K'):
            dizionario['k'] += 1
        elif carattere in ('l', 'L'):
            dizionario['l'] += 1
        elif carattere in ('m', 'M'):
            dizionario['m'] += 1
        elif carattere in ('n', 'N'):
            dizionario['n'] += 1
        elif carattere in ('o', 'O'):
            dizionario['o'] += 1
        elif carattere in ('p', 'P'):
            dizionario['p'] += 1
        elif carattere in ('q', 'Q'):
            dizionario['q'] += 1
        elif carattere in ('r', 'R'):
            dizionario['r'] += 1
        elif carattere in ('s', 'S'):
            dizionario['s'] += 1
        elif carattere in ('t', 'T'):
            dizionario['t'] += 1
        elif carattere in ('u', 'U'):
            dizionario['u'] += 1
        elif carattere in ('v', 'V'):
            dizionario['v'] += 1
        elif carattere in ('w', 'W'):
            dizionario['w'] += 1
        elif carattere in ('y', 'Y'):
            dizionario['y'] += 1
        elif carattere in ('z', 'Z'):
            dizionario['z'] += 1

### LANCIO PROGRAMMA
start = timer()

parser = argparse.ArgumentParser(description = 'Il programma conta la frequenza relativa dei \
 caratteri alfabetici presenti nel testo')
parser.add_argument('titolo', type = str, help = 'Titolo del libro da inserire nel formato: \
 \'titololibro.txt\'')
parser.add_argument('--hist', action = 'store_true', default = False, help = \
'Stampa l\'istogramma delle frequenze relative')

args = parser.parse_args()

titolo = args.titolo

file1 = open(titolo, 'r', encoding="utf8")

TESTO = str(file1.readlines())

dizionario = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, \
'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, \
 'u' : 0, 'v': 0, 'w' : 0, 'y' : 0, 'z' : 0}

conteggio(TESTO)

TOTALE = 0
for elemento in dizionario:
    TOTALE += dizionario[elemento]
for elemento in dizionario:
    dizionario[elemento] /= TOTALE

lettere = list(dizionario.keys())
frequenze = list(dizionario.values())

for lettera in lettere:
    print(f'La frequenza relativa di {lettera} è {dizionario[lettera]  : .3f}')

end = timer()

logging.basicConfig(encoding='utf-8', level=logging.INFO)
logging.info(f'Il tempo di esecuzione del programma è di {end - start} secondi')

if args.hist is True:
    plt.bar(dizionario.keys(), dizionario.values(), color='g')
    plt.show()
