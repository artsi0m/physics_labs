import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

l_one_u = [ 56, 80, 104, 136, 184, 264, 368, 488, 600, 672 ]
l_two_u = [ -696, -616, -504, - 376, -264, -200, -136, -104, -88, -72 ]
l_combined_u = [ -624, -552, -408, -232, -104, 88, 224, 392, 544, 632 ]
length_cm = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
length_meters = [ x * pow(10, -2) for x in length_cm ]

def main():
    b_one = [ calc(x) for x in l_one_u ]
    b_two = [ calc(x) for x in  l_two_u ]
    b_sum = [ x + y for x, y in zip(b_one, b_two)]
    b_third = [ calc(x) for x in l_combined_u ]

    for item in zip(l_one_u, b_one, l_two_u, b_two, b_sum, l_combined_u, b_third):
        print(item)

    fig_first, ax = plt.subplots()
    ax.plot(length_meters, b_one)
    ax.grid()
    ax.set_xlabel('Длина, Метры')
    ax.set_ylabel(r'Величина магнитной индукции, $Tл \times 10^{-5}$')
    ax.set_title('Первое измерение')

    fig_second, ay = plt.subplots()
    ay.plot(length_meters, b_two)
    ay.grid()
    ay.set_xlabel('Длина, Метры')
    ay.set_ylabel(r'Величина магнитной индукции, $Tл \times 10^{-5}$')
    ay.set_title('Второе измерение')

    fig_third, az = plt.subplots()
    az.plot(b_sum)
    az.plot(b_third)
    az.grid()
    az.set_ylabel(r'Величина магнитной индукции, $Tл \times 10^{-5}$')
    az.set_title('График алгебраической суммы проекций функций магнитных полей \n'
                 'и результирующего поля катушек \n', fontsize=10)
                 
    plt.show()

def calc(U):
    RES = 267 
    C = 3.8 * pow(10, -6)
    S = 7.1 * pow(10, -4)
    N = 1000
    ratio = pow(10, 2) 
    return ((RES * C * U) / (N * S)) * ratio


if __name__ == "__main__":
    main()
