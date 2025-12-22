import numpy as np

def foot_pos(legState):
  x = legState.length1 * np.cos(legState.joint1.theta) + legState.length2 * np.cos(legState.joint1.theta + legState.joint2.theta)
  x = legState.length1 * np.sin(legState.joint1.theta) + legState.length2 * np.sin(legState.joint1.theta + legState.joint2.theta)
  return np.array([x, y])
