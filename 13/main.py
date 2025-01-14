import numpy as np
import scipy
import re


cost_of_A = 3
cost_of_B = 1
c = np.array([cost_of_A, cost_of_B])
bounds = (0, None)
# solution must be an integer
integrality = 1

expression = r"X\+(\d+), Y\+(\d+)"
expression_x = r"X\=(\d+), Y\=(\d+)"

fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()
    tokens = 0
    for i in range(0, len(lines), 4):
        line_A = lines[i].strip()
        A = np.array([[int(match)] for match in re.findall(expression, line_A)[0]])
        line_B = lines[i+1].strip()
        B = np.array([[int(match)] for match in re.findall(expression, line_B)[0]])
        line_X = lines[i+2].strip()
        X = np.array([int(match) for match in re.findall(expression_x, line_X)[0]]) + 10000000000000
        A_eq = np.hstack([A, B])
        sol = np.linalg.solve(A_eq, X)
        int_sol = np.round(sol, 0)
        if np.all(A_eq @ int_sol == X):
            print(int_sol)
            tokens += c.T @ int_sol


        A, B = sol
        if abs(int(np.round(A,0))-A) <1e-8 and abs(int(np.round(B,0))-B)<1e-8:
            print(sol)
            print(c.T @ sol)
            #tokens += c.T @ np.round(sol, 0)

        res = scipy.optimize.linprog(c=c, A_eq=A_eq, b_eq=X ,integrality = integrality, bounds = bounds)
        if res.success:
            #tokens += int(res.fun)
            print(i//4+1,res.x, res.fun)
        else:
            print(i//4+1, 'no solution')
    
print(tokens)
