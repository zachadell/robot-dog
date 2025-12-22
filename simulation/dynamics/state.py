class JointState: # just a single joint - angle & angular velocity
  def __init__(self, theta=0.0, omega=0.0):
    self.theta = theta
    self.omega = omega

class LegState: # 2 link leg - angle & angular velocity of both links
  def __init__(self, link1theta=0.0, link1omega=0.0, link1length=0.0, link2theta=0.0, link2omega=0.0, link2length=0.0):
    self.joint1 = JointState(link1theta, link1omega)
    self.length1 = link1length
    self.joint2 = JointState(link2theta, link2omega)
    self.length2 = link2length
