import  numpy as np
import math
import convergence_test as CT
import matplotlib.pyplot as plt
from sympy import *

#*********limit of a sequence*************
def visualize_limit_seq(f,n):
#*********convergence test*************
    limit = (limit_seq(f(n),n).doit())
    print("The limit is : ",limit)

    if limit == math.inf:
        print("This is not a convergent sequence")
        return 0


#**********gets values for graph**********
    e = float(input("Give some number for e : "))
    values_graph = []
    s = 0.1
    A = [s]
    value = f(s)
    values_graph.append(value)
    while abs(limit-value) > e:
        A.append(s)
        values_graph.append(value)
        s+= 0.1
        value = f(s)
        
    print("Plotting the actual graph : ") #plots complete lists
    plt.plot(A,values_graph)
    limit_L = [limit for i in A]
    plt.plot(A,limit_L)
    plt.legend(["function", "limit"])
    plt.show()

#************To plot last n number of values**************#
    count = len(A)
    print("This is the number of iterations computed : ",count)
    small_A = []
    zoom_scale = int(input("zoom scale(Enter some lower value compared to computed one ) : "))
    small_values = []
    
    def zoom(zoom_scale):
        for i in range(count-zoom_scale,count):
            small_A.append(A[i])
            small_values.append(values_graph[i])
        print("Let's zoom in")
        plt.plot(small_A,small_values)
        limit_L = [limit for i in small_A]
        plt.plot(small_A,limit_L)
        plt.legend(["function", "limit"])
        plt.show()
    zoom(zoom_scale)
#***********Repeat zooming**********#
    while True:
        zoom_scale = int(input("Try other scales or else enter 0 : "))
        if zoom_scale == 0:
            break
        else:
            zoom(zoom_scale)
           
#***************LIMIT OF A SERIES*********************
def visualize_limit_ser(f,n):
    result = CT.Test(f,n)
    if result != True:
        return 0
    











def f(n):
    return 1/n

n = var('n')

visualize_limit_seq(f,n)
# visualize_limit_ser(f,n)