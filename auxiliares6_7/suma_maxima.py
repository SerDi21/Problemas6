import sys
from typing import TextIO

Solution = tuple[int, int, int]


def read_data(f: TextIO) -> list[int]:
    entrada = []
    for line in f.readlines():
        entrada.append(int(line))
    return entrada


def process(v: list[int]) -> Solution:
    def sm(i: int, j: int) -> Solution:
        if j - i == 1:
            return v[i], i, j
        c = (i + j)//2
        izq = sm(i, c)
        der = sm(c, j)

        in_der = c
        sum_der = 0
        ac = 0
        for k in range(c, j):
            ac += v[k]
            if ac > sum_der:
                sum_der = ac
                in_der = k + 1

        sum_izq = 0
        ac = 0
        in_izq = c
        for k in range(c-1, i-1, -1):
            ac += v[k]
            if ac > sum_izq:
                sum_izq = ac
                in_izq = k
        sol_centro: Solution = ((sum_izq + sum_der), in_izq, in_der)
        return max(izq, der, sol_centro)
    return sm(0, len(v))


def show_results(sol: Solution):
    print(sol[0])
    print(sol[1])
    print(sol[2])


if __name__ == "__main__":
    entrada = read_data(sys.stdin)
    sol = process(entrada)
    show_results(sol)
