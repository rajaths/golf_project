#matplotlib inline
import math
import matplotlib.pyplot as pyplot
import numpy as np

def camber_line( x, m, p, c ):
    return np.where((x>=0)&(x<=(c*p)),
                    m * (x / np.power(p,2)) * (2.0 * p - (x / c)),
                    m * ((c - x) / np.power(1-p,2)) * (1.0 + (x / c) - 2.0 * p ))
    
def dyc_over_dx( x, m, p, c ):
    return np.where((x>=0)&(x<=(c*p)),
                    ((2.0 * m) / np.power(p,2)) * (p - x / c),
                    ((2.0 * m ) / np.power(1-p,2)) * (p - x / c ))
    
def thickness( x, t, c ):
    term1 =  0.2969 * (np.sqrt(x/c))
    term2 = -0.1260 * (x/c)
    term3 = -0.3516 * np.power(x/c,2)
    term4 =  0.2843 * np.power(x/c,3)
    term5 = -0.1015 * np.power(x/c,4)
    return 5 * t * c * (term1 + term2 + term3 + term4 + term5)

def naca4(x, m, p, t, c=1):
    dyc_dx = dyc_over_dx(x, m, p, c)
    th = np.arctan(dyc_dx)
    yt = thickness(x, t, c)
    yc = camber_line(x, m, p, c)  
    return ((x - yt*np.sin(th), yc + yt*np.cos(th)), 
            (x + yt*np.sin(th), yc - yt*np.cos(th)))
    
#naca2412 
m = 0.02
p = 0.4
t = 0.12
c = 1.0

x = np.linspace(0,1,200)
for item in naca4(x, m, p, t, c):
    pyplot.plot(item[0], item[1], 'b')
pyplot.plot(x, camber_line(x, m, p, c), 'r')
pyplot.axis('equal')
pyplot.xlim((-0.05, 1.05))
# figure.set_size_inches(16,16,forward=True)

itemlist = list(item)
y_abovelist, y_belowlist = map(list, zip(itemlist))
y_abovearray = np.squeeze(np.asarray(y_abovelist))
y_belowarray = np.squeeze(np.asarray(y_belowlist))
x_list = list(x)

list_of_lists = list([x, y_abovearray, y_belowarray])

for a in zip(*list_of_lists):
    print(*a)
    
