#aula 02

def func(x):
    res = 2 * (x**2) - 3
    return res

def main(x1,x2,iteracoes):
    fx1 = func(x1)
    fx2 = func(x2)
    for k in range(iteracoes):
        #fixo 'b' pois 'a' esta mais proximo da raiz    
        #reta
        
        if (x2-x1 == 0):
            break

        a = (fx2-fx1) / (x2 - x1)
        b = fx2 - (a*x2)
        root = -b / a
        
        #print(root)

        if (fx1 * fx2 < 0):
            x1 = root
            fx2 = fx2 / 2
            fx1 = func(x1)

        else:
            x2 = root
            fx1 = fx1 / 2
            fx2 = func(x2)
    print(root)


main(1,2,100)