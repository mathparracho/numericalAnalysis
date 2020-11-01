#aula 02

def func(x):
    res = 2 * (x**2) - 3
    return res

def main(x1,x2,iteracoes):
    for i in range(iteracoes):
        fx1 = func (x1)
        fx2 = func (x2)
    
        m = (x1 + x2) / 2
        fm = func (m)

        #print(m)
        
        if fm * fx1 < 0:
            x2 = m
        else:
            x1 = m
    print(m)


main(1,2,100)