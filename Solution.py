A = int(input())
B = int(input())
x = []


def find_factors(nm, chk):
    fctrs = []
    for i in range(2, nm // 2 + 2):
        if (nm % i == 0 and i > chk):
            fctrs += [i]
    fctrs += [nm]
    return fctrs

if (A < B):
    print("A cannot be less than B")
else:
    C = A - B
    print(find_factors(C, B))