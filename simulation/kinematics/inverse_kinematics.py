import numpy as np

def step(vars, target_pos, func):
  current_pos = func(vars)
  error = target_pos - current_pos
  J = jacobian.numerical(vars, func)
  dvars = np.linalg.pinv(J) @ error
  return vars + dvars
