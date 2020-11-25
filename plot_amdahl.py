import matplotlib.pyplot as plt
import numpy as np
import math


######################Symmetric Speedup#####################
def symmetric_speedup(n,f):
    r_bce_axis = []
    speedup_axis = []

    #n = 16
    # 16, 64, 256
    #f = 0.5
    # 0.999, 0.99, 0.975, 0.9, 0.5
    r = 0
    
    for i in range(0,200):
        r = r + .4
        r_bce_axis.append(r)
        performance = math.sqrt(r)
        speedup_symmatric = 1 / ((1-f)/performance + (f*r)/(performance*n))
        speedup_axis.append(speedup_symmatric)  
    
    print("Maximum Speedup is " + str(max(speedup_axis)))

    plt.axis([0, n, 0, n])
    plot_title = "Symmetric, n = "+ str(n)
    plt.title(plot_title)
    plt.xlabel("r BCEs")
    plt.ylabel("Speedup symmetric")
    f_label = "f = " + str(f)
    plt.plot(r_bce_axis,speedup_axis,label = f_label)
    
    plt.legend()
    plt.show()


######################Asymmetric Speedup#####################
def asymmetric_speedup(n,f):
    r_bce_axis = []
    speedup_axis = []
    r = 0
    for i in range(0,200):
        r = r + .4
        r_bce_axis.append(r)
        performance = math.sqrt(r)
        speedup_asymmatric = 1 / ((1-f)/performance + f/(performance+n-r))
        speedup_axis.append(speedup_asymmatric)  
    
    print("Maximum Speedup is " + str(max(speedup_axis)))
    plt.axis([0, n, 0, n])
    plot_title = "Asymmetric, n = "+ str(n)
    plt.title(plot_title)
    plt.xlabel("r BCEs")
    plt.ylabel("Speedup Asymmetric")
    f_label = "f = " + str(f)
    plt.plot(r_bce_axis,speedup_axis,label = f_label)

    plt.legend()
    plt.show()


######################Dynamic Speedup######################
def dynamic_speedup(n,f):
    r_bce_axis = []
    speedup_axis = []
    r = 0
    for i in range(0,1000):
        r = r + .4
        r_bce_axis.append(r)
        performance = math.sqrt(r)
        speedup_dynamic = 1 / ((1-f)/performance + f/n)
        speedup_axis.append(speedup_dynamic)  
    
    print("Maximum Speedup is " + str(max(speedup_axis)))
    plt.axis([0, n, 0, n])
    plot_title = "Dynamic, n = "+ str(n)
    plt.title(plot_title)
    plt.xlabel("r BCEs")
    plt.ylabel("Speedup Dynmaic")
    f_label = "f = " + str(f)
    axes = plt.plot(r_bce_axis,speedup_axis,label = f_label)
    plt.legend()
    plt.show()




symmetric_speedup(256,0.99)
#asymmetric_speedup(256,0.999)
#dynamic_speedup(256,0.5)

