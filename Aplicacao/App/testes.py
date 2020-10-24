import numpy as np
from scipy.optimize import linprog
from numpy.linalg import solve


# minimize
# -10x_1 - 20x_2
# s.a.
# 3x_1 + 4x_2   <= 10
# x_1 + 5x_2 <= 6
# x >= 0

def mostrar_resultado(c, A_ub, b_ub):
    solved = linprog(c, A_ub=A_ub, b_ub=b_ub,
                     bounds=(0, None))
    return solved


def resolver_questao():
    A_ub = np.array([[1, 5]])
    b_ub = np.array([6])
    c = np.array([-10, -20])
    return c, A_ub, b_ub


[c, A_ub, b_ub] = resolver_questao()

resultado = mostrar_resultado(c, A_ub, b_ub)

print('Valor ótimo:', resultado.fun)

print("Os valores de x serão:")

count = len(resultado.x)

for i in range(count):
    print("x[", i + 1, "]=", resultado.x[i])


