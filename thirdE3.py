

def main():
    b_one = [ calc(x) for x in l_one_u ]
    b_two = [ calc(x) for x in  l_two_u ]
    b_sum = [ x + y for x, y in zip(b_one, b_two)]
    b_third = [ calc(x) for x in l_combined_u ]
    for item in zip(l_one_u, b_one, l_two_u, b_two, b_sum, l_combined_u, b_third):
        print(item)


def calc(U):
    RES = 267 
    C = 3.8 * pow(10, -6)
    S = 7.1 * pow(10, -4)
    N = 1000
    ratio = pow(10, 2)
    return ((RES * C * U) / (N * S)) * ratio

l_one_u = [ 56, 80, 104, 136, 184, 264, 368, 488, 600, 672 ]
l_two_u = [ -696, -616, -504, - 376, -264, -200, -136, -104, -88, -72 ]
l_combined_u = [ -624, -552, -408, -232, -104, 88, 224, 392, 544, 632 ]

if __name__ == "__main__":
    main()
