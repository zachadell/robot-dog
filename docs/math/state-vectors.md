A state vector is a vector that contains the minimum amount of data to predict future positions. In the example below, $\theta$ is the angle of a joint and $\dot{\theta}$ is the velocity of the joint.

$`
S =
\begin{bmatrix}
\theta \\
\dot{\theta}
\end{bmatrix}
`$

Velocity must be included in a state vector because it is the speed and direction an object is moving, which is important in predicting the movement of an object/joint.
