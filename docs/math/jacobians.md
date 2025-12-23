Jacobians tell you how something moves if you slighty move it. On a 2D plane, jacobians could be used to tell how much a small change in the original position will affect the position after a transformation.

<a href="https://www.desmos.com/geometry/edn6ee4hh2"><img src="https://github.com/zachadell/robot-dog/blob/main/docs/images/Jacobians/Jacobians%20Animation%201.gif" width="400" height="400">

The image above shows the transformation: $`f\left(\begin{bmatrix} x \\ y \end{bmatrix}\right) = \begin{bmatrix} x + sin(y) \\ y + sin(x) \end{bmatrix}`$. This is a non-linear transformation, meaning grid lines do not stay equally spaced and parallel. However, to find the jacobian matrix of a function at a certain point you need it to be linear. To get around this, we can zoom into the function until it is locally linear. Locally linear means the function has small enough variation from a linear function that it can be perceived as linear.

<a href="https://www.desmos.com/geometry/yarpqpgzpk"><img src="https://github.com/zachadell/robot-dog/blob/main/docs/images/Jacobians/Jacobians%20Animation%202.gif" width="400" height="400">

Now that the function can be used like a linear function, a jacobian matrix can be created. First, break the transformation function into a two scalar functions:

$`\begin{bmatrix} f_1(x,y) \\ f_2(x,y) \end{bmatrix} = \begin{bmatrix} x + sin(y) \\ y + sin(x) \end{bmatrix}`$

Next, create the jacobian matrix with this formula for 2D transformations:

$`J = \begin{bmatrix} \frac{\partial f_1}{\partial x} & \frac{\partial f_1}{\partial y} \\ \frac{\partial f_2}{\partial x} & \frac{\partial f_2}{\partial y} \end{bmatrix}`$

This matrix shows the partial derivatives for $f_1$ and $f_2$ with respect to $x$ and $y$. A partial derivate of a multi-variable function is its deritave with respect to one of its variables while the other variables are treated as constants.

Jacobians will be used in my robot dog to determine the movement of a legs foot in relation to joint positions. To do this, we need to change the functions to calculate for rotational movement. We can simply swap out $f_1$ and $f_2$ with the equations for the forward kinematics of a 2-link leg.

$`\begin{bmatrix} f_1(\theta_1,\theta_2,L_1,L_2) \\ f_2(\theta_1,\theta_2,L_1,L_2) \end{bmatrix} = \begin{bmatrix} L_1\cos(\theta_1) + L_2\cos(\theta_1 + \theta_2) \\ L_1\sin(\theta_1) + L_2\sin(\theta_1 + \theta_2) \end{bmatrix}`$

Then, a new matrix can be created for the new functions:

$`J = \begin{bmatrix} \frac{\partial f_1}{\partial \theta_1} & \frac{\partial f_1}{\partial \theta_2} \\ \frac{\partial f_2}{\partial \theta_1} & \frac{\partial f_2}{\partial \theta_2} \end{bmatrix}`$
