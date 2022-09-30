import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


u_lst = [ 100, 95, 90, 85, 80, 75, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20 ]
l_x_lst = [ 4, 3.8, 3.6, 3.4, 3.2, 2.8, 2.6, 2.4, 2.4, 2.2, 2, 1.8, 1.8, 1.6, 1.4, 1.2, 1 ]
l_y_lst = [ 6.7, 6.2, 6, 5.6, 4.8, 4, 3.6, 2.8, 2.2, 1.6, 1.4, 1, 0.6, 0.4, 0.4, 0.4, 0.2 ]

def main():
    pass

def calc_E(l_x):
    r_first = 200 * pow(10, 3)
    r_second = 13 * pow(10, 3)
    b_x = 50
    dist = 2.2 * pow(10, -3) # distance in Si
    return ((r_first + r_second) * b_x * l_x) / ( 2 * r_second * dist)

def calc_P(l_y):
    S_area = 81.6 * pow(10, -3)
    reference_capacitance = 1 * pow(10, -6)
    b_y = 100 * pow(10, -3)
    return (reference_capacitance * b_y * l_y) / ( 2 * S_area)

if __name__ == "__main__":
    main()

