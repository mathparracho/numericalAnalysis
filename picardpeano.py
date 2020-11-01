
import math
from numpy import log as ln

def func(x):
    Xplus1 = math.cos(x)
    return Xplus1

def main(x,iteracoes):
    for k in range(iteracoes):
        Xplus1 = func(x)
        x = Xplus1

    print(Xplus1)
main(1,30)