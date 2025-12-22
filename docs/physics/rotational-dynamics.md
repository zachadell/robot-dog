I used the semi-implicit euler method for rotational dynamics because it is more stable than explicit euler, and is used in other physics engines.

Definitions:
- Torque is the rotational force acting on the object.
- Moment of Inetria is the object's resistance to rotation.

First, it finds the angular acceleration, $\alpha$, by dividing the torque, $\tau$, by the moment of inertia, $I$.

$\alpha = \frac{\tau}{I}$

Then, the angular velocity, $\omega$, is updated by adding the product of $\alpha$ and the change in time, $dt$.

$\omega = \omega + (\alpha * dt)$

Lastly, the rotation, $\theta$, is updated by adding the product of $\omega$ and $dt$
$\theta = \theta + (\omega * dt)$

This order is important to make sure it is adding the most recent data to $\theta$ and $\omega$. This prevents the energy loss seen in the explicit euler method. 
