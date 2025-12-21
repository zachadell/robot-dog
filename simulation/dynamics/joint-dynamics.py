def update_joint_state(state, torque, inertia, dt):
  # get the rotational acceleration, update the rotational velocity, and then update the angle
  alpha = torque / inertia
  state.omega += alpha * dt
  state.theta += state.omega * dt
