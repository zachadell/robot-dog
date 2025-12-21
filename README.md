# robot-dog

## Goal

My main goal for this project is learning useful algorithms, concepts, and processes that I can use in robotics. I want to be able to take the knowledge I have acquired and apply it to coding other robotics projects such as my school's VRC club.

## Scope

### Project Description

A quadrupedal robot that can do the following:
- Walk
- Strafe
- Turn
- Balance
- Position track
- Map environments
- Navigate autonomously
- Traverse rough terrain
- Interact with people autonomously
- Do something when idle (ie: sit)

### Task Priority

Task priority is rated on a scale of 1-4.
| Priority level | Description | Tasks |
| --- | --- | --- |
| High Priority | It is needed no matter what. | <ul><li>Walking<li>Turning |
| Medium Priority | It is important to have, but it is not necessary for prototypes. | <ul><li>Strafing<li>Balancing |
| Low Priority | It is nice to have, but it is not necassary for the first build. | <ul><li>Position tracking<li>Environment mapping<li>Autonomous navigation<li>Terrain traversing |
| Minimum Priority | It is not necessary at all, and will only be added once all higher priority tasks have been accomplished. | <ul><li>Interaction<li>Idle behaviours |

## What I created

-- small discription of each thing I have created

## Math/Physics Involved

Robot dogs utilize linear algebra, kinematics, tracking algorithms, and control algorithms to ensure reliability and accuracy. Linear algebra and kinematics are used in robot dogs to predict how it will act when it performs an action. These predictions can be used alongside instrument readings to find the most likely position of the robot using a tracking algorithm such as kalman filtering. Kalman filtering is [explanation of kalman filtering]. The position of the robot and position of motors can be used to calculate the amount motors have to move to reach their destination using a control algorithm such as PID. PID stands for Proportional-Integral-Derivative. It is used to gradually speed up and slow the motors as they reach their target to the reduce drift caused by rapid acceleration and decceleration.
