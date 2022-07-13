from sympy import *
def ratio(u,n):
    print("RATIO TEST")
    print("---------------")
    try:
        if limit(u(n),n,oo) != 0:
            return False
        L = simplify(u(n+1)/u(n))
        lim = limit(L,n,oo)
        if lim > 1: 
            return False
        elif lim < 1: 
            return True
        else: 
            return Raabe(u,n)
    except:
        return Raabe(u,n)
def Raabe(u,n):
    print("RAABE")
    print("---------------")
    try:
        L = simplify(n*((u(n)/u(n+1))-1))
        lim = limit(L,n,oo)
        if lim > 1:
            return False
        elif lim < 1:
            return True
        else: return cauchy(u,n)
    except:
        return cauchy(u,n)
def cauchy(u,n):
    print("CAUCHY")
    print("---------------")
    try:
        L = simplify(u(n)**(1/n))
        pprint(L)
        lim = limit_seq(L,n).doit()
        if lim == 1:
            print("Inconclusive ")
            return 1/2
        elif lim < 1:
            return True
        else:
            return False
    except:
        print("The sequence might be ossilatory")
        return None
# def u(n):
#     return 1/2**(n+(-1)**n)  
    
n = Symbol('n')
def Test(u,n):
    test = (ratio(u,n))
    if test == False:
        print("The series is divergent ")
    elif test == True:
        print("The series is convergent ")
    elif test == 1/2:
        print("Cannot find nature with these tests ")
    return test