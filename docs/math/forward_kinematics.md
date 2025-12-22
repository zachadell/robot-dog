Forward kinematics is the process of finding the location and orientation of the end point of a leg. My robot dog will mostly use 2-link legs like the one in the diagram below. 

<img src="https://raw.githubusercontent.com/zachadell/robot-dog/refs/heads/main/docs/images/Forward%20Kinematics.png" width="334" height="369.5">

Forward kinematics for 2-link legs uses four variables: 
- $\theta_1$ - The global rotation of the first link
- $L_1$ - The length of the first link
- $\theta_2$ - The local rotation of the second link compared to the first link
- $L_2$ - The length of the second link

The forward kinematics equation for 2-link legs is:

$x = L_1\cos(\theta_1) + L_2\cos(\theta_1 + \theta_2)$

$y = L_1\sin(\theta_1) + L_2\sin(\theta_1 + \theta_2)$

> Note: These equations output the **local** position. To find the global position of the end point, add it to the position of the first joint.

These equations can be broken down into two parts: first link and second link. The left half of each equation finds the endpoint of the first link relative to the first joint. The right half of each equation finds the endpoint of the second link relative to the second joint. $\theta_1$ and $\theta_2$ are added in the second half to convert the local rotation of the second link into global rotation.
