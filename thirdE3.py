import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

length_cm = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
length_meters = [ x * pow(10, -2) for x in length_cm ]



def main():

    l_one_u = input_data(10, "U₁, десять значений через пробел: ")
    l_two_u = input_data(10, "U₂, десять значений через пробел: ")
    l_combined_u = input_data(10, "U рез, десять значений через пробел: ")

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


def input_data(num, prompt):
    while True:
       numbers = list(map(int, input(prompt).split()))
       if len(numbers) == num:
           break
       else:
           print("Вы должны ввести {} целых чисел".format(num))
    return numbers

if __name__ == "__main__":
    main()
