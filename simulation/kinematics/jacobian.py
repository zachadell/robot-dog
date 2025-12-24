import numpy as np

def numerical_jacobian(vars, func, d=1e-10):
  J = np.zeros((2, len(vars)))
  f0 = func(vars)
  for i in range(len(vars)):
    copy = vars.copy()
    copy[i] += d
    f1 = func(copy)
    J[:, i] = (f1 - f0) / d
  return J
