# Mechanics

<!-- omit in toc -->
## Table of contents

- [Newton's laws of motion](#newtons-laws-of-motion)
  - [Newton's first law](#newtons-first-law)
  - [Newton's second law](#newtons-second-law)
  - [Newton's third law](#newtons-third-law)
- [Miscellaneous](#miscellaneous)
  - [Newton's law of universal gravitation](#newtons-law-of-universal-gravitation)
  - [Weight](#weight)
  - [International system of units](#international-system-of-units)
  - [Equilibrium](#equilibrium)
  - [Hooke's law](#hookes-law)
  - [Damping](#damping)
  - [Moment](#moment)
- [Linear motion](#linear-motion)
  - [Position](#position)
  - [Velocity](#velocity)
  - [Acceleration](#acceleration)
  - [Mass](#mass)
  - [Momentum](#momentum)
- [Rotational motion](#rotational-motion)
  - [Angular velocity](#angular-velocity)
  - [Angular acceleration](#angular-acceleration)
  - [Moment of inertia](#moment-of-inertia)
  - [Angular momentum](#angular-momentum)
  - [Torque](#torque)

## Newton's laws of motion

### Newton's first law

Newton's first law states that *a body remains at rest, or in motion at a constant speed in a straight line, unless acted upon by a force*.

Newton's first law expresses the principle of inertia, which is the natural behavior of a body to move in a straight line at constant speed, unless subjected to an unbalanced force.

### Newton's second law

Newton's second law states that *the time derivative of the momentum is the force*.

$$
\begin{equation}
\tag{Newton's second law}
\overrightarrow{F} = \frac{d \overrightarrow{p}}{d t} = \frac{d m \overrightarrow{v}}{d t}
\end{equation}
$$

If the mass $m$ does not change with time, then the derivative acts only upon the velocity, and so the force equals the product of the mass and acceleration.

$$
\overrightarrow{F} = m \frac{d \overrightarrow{v}}{d t} = m \overrightarrow{a}
$$

### Newton's third law

Newton's third law states that *if two bodies exert forces on each other, these forces have equal magnitude but opposite direction*.

$$
\begin{equation}
\tag{Newton's third law}
\overrightarrow{F_1} = - \overrightarrow{F_2}
\end{equation}
$$

Newton's third law relates to the conservation of momentum, which states that in a closed system, the total momentum remains constant. If two bodies have momentum $\overrightarrow{p_1}$ and $\overrightarrow{p_2}$ respectively, then the total momentum of the pair is $\overrightarrow{p} = \overrightarrow{p_1} + \overrightarrow{p_2}$. Since the total momentum $\overrightarrow{p}$ is constant, its time derivative is zero, and therefore:

$$
\frac{d \overrightarrow{p_1}}{d t} + \frac{d \overrightarrow{p_2}}{d t} = \frac{d \overrightarrow{p}}{d t} = 0 \\[8 pt]
\frac{d \overrightarrow{p_1}}{d t} = - \frac{d \overrightarrow{p_2}}{d t}
$$

## Miscellaneous

### Newton's law of universal gravitation

Newton's law of universal gravitation states that every point mass attracts every other point mass by a force proportional to the product of the two masses, and inversely proportional to the square of the distance between them. The constant of proportionality is the gravitation constant, which is approximately $6.674 \times 10^{-11} \text{ m}^3 \text{kg}^{-1} \text{s}^{-2}$.

$$
\begin{equation}
\tag{Newton's law of universal gravitation}
F_g = \frac{G m_1 m_2}{r^2}
\end{equation}
$$

### Weight

The weight of an object is defined as the product of its masss and the local acceleration of free fall. This acceleration includes the effects of the gravitational force (due to the mass of the Earth) and the centrifugal force (due to the rotation of the Earth).

$$
\begin{equation}
\tag{Weight}
W = mg
\end{equation}
$$

The local acceleration of free fall varies slightly with altitude and latitude, therefore, the standard gravitational acceleration $g$ is often used when a more accurate value is not available. The standard gravitational acceleration is determined at sea level and $45 \degree$ latitude, which is approximately $9.80655 \text{ m} \text{s}^{-2}$.

### International system of units

The international system of units (SI) is an evolving metric system of units. The system includes seven **base units**, and allows to construct additional **derived units** as products of powers of the base units. The system uses metric prefixes to systematically construct decimal multiples of the units.

| Name     | Symbol  | Quantity                  |
| -------- | ------- | ------------------------- |
| second   | **s**   | time                      |
| metre    | **m**   | length                    |
| kilogram | **kg**  | mass                      |
| ampere   | **A**   | electric current          |
| kelvin   | **K**   | thermodynamic temperature |
| mole     | **mol** | amount of substance       |
| candela  | **cd**  | luminous intensity        |

### Equilibrium

An object is in equilibrium when it expresses translational equilibrium and rotational equilibrium. For an object to be in translational equilibrium, the net force must be zero. Similarly, for an object to be in rotational equilibrium, the net torque must be zero.

$$
\begin{equation}
\tag{Translational equilibrium}
\sum F = 0
\end{equation}
$$

$$
\begin{equation}
\tag{Rotational equilibrium}
\sum \tau = 0
\end{equation}
$$

### Hooke's law

Hooke's law states that the force needed to extend or compress a spring is proportional to the size of deformation measured from its unloaded position. The constant of proportionality is the spring constant $k$ that represents its stiffness.

$$
\begin{equation}
\tag{Hooke's law}
F_s = k x
\end{equation}
$$

Hooke's law is an accurate approximation for most solid bodies, as long as the forces and deformations are relatively small. However, many materials considerably deviate from the Hooke's law well before the elastic limit.

### Damping

Damping is an influence on an oscillatory system that reduces or prevents its oscillation. In physical systems, damping is produced by processes that dissipate the energy stored in the oscillation.

The damping ratio $\zeta$ is a parameter that characterizes the frequency response of a second order ordinary differential equation.

### Moment

A moment is a mathematical expression involving the product of distance and a physical quantity. Moments are usually defined with respect to a fixed reference point and refer to physical quantities located at some distance from the reference point.

The nth moment $\mu_n$ is the product of the nth power of the distance to a point and a physical quantity at that point. If $Q$ is the physical quantity, and $r$ is the distance between the reference point to the point where $Q$ is measured, the nth moment is defined as:

$$
\begin{equation}
\tag{Moment}
\mu_n = r^n Q
\end{equation}
$$

## Linear motion

### Position

### Velocity

### Acceleration

### Mass

### Momentum

## Rotational motion

### Angular velocity

The angular velocity is defined as the rate of change of angular position with respect to time. The angular velocity can be considered with respect to a fixed origin, in which case, it is called **orbital angular velocity**, or with respect to the center of rotation of a rigid body, in which case, it is called **spin angular velocity**.

$$
\begin{equation}
\tag{Angular velocity}
\omega = \frac{d \phi}{d t}
\end{equation}
$$

When a particle is moving in a two-dimensional plane, the arc length sweeped is $l = r \phi$, where $\phi$ is measured in radians. Since only the tangential component of the linear velocity contributes to the angular velocity, $\frac{dl}{dt} = v \sin{\theta}$, where $\theta$ is the angle between the velocity vector $\bold{v}$ and the position vector $\bold{r}$. This allows to relate the linear velocity with the angular velocity.

$$
\omega = \frac{v \sin{\theta}}{r}
$$

When a particle in moving in a three-dimensional space, the direction of the angular velocity $\bold{\omega}$ is normal to the instantaneous plane of rotation, following the right hand rule. This relation can be expressed in terms of the cross product:

$$
\bold{\omega} = \frac{\bold{r} \times \bold{v}}{r^2}
$$

### Angular acceleration

The angular acceleration is defined as the rate of change of orbital angular velocity with respect to time.

$$
\begin{equation}
\tag{Angular acceleration}
\alpha = \frac{d \omega}{d t}
\end{equation}
$$

When a particle is moving in a two-dimensional plane, the instantaneous angular acceleration is described as $a = \frac{d}{dt}(\frac{v_\bot}{r})$, where $v_\bot$ is the tangential component of the linear velocity. This equation can be expanded using the quotient rule. In a circular motion, the second term in the expansion vanishes since the distance from the origin remains constant.

$$
a = \frac{1}{r} \frac{d v_\bot}{d t} - \frac{v_\bot}{r^2} \frac{d r}{d t}
$$

### Moment of inertia

The **moment of inertia** or **rotational inertia** is a quantity that determines the torque needed for a desired angular acceleration. The moment of inertia of a particle with mass $m$ at a distance $r$ from the axis of rotation is defined as the second moment of mass. The moment of inertia of a complex object is defined as the sum of the moment of inertia of each particle inside that object.

$$
\begin{equation}
\tag{Moment of inertia}
I = \sum_{i} m_i r_i^2
\end{equation}
$$

The table below lists the moment of inertia of rigid bodies with common shapes about the z-axis of rotation for both hollow and solid structures.

| Shape | Moment of inertia (Hollow) | Moment of inertia (Solid) |
| - | - | - |
| Cylinder | $I = \frac{1}{2} m (r_{\text{inner}}^2 + r_{\text{outer}}^2)$ | $I = \frac{1}{2} m r^2$ |
| Sphere | $I = \frac{2}{3} m r^2$ | $I = \frac{2}{5} m r^2$ |
| Disk | $I = m r^2$ | $I = \frac{1}{2} m r^2$ |
| Cone | $I = \frac{1}{2} m r^2$ | $I = \frac{3}{10} m r^2$ |

### Angular momentum

The angular momentum is a measure of the momentum of an object around an axis of rotation. It is defined as the product of the moment of inertia $I$ and the angular velocity $\omega$.

$$
\begin{equation}
\tag{Angular momentum}
L = I \omega
\end{equation}
$$

For a particle in motion, with $I = m r^2$ and $\omega = (\bold{r} \times \bold{v}) / r^2$, the angular momentum is the cross product of the radius vector $r$ and the linear momentum $p$. If $\theta$ is the angle between the radius vector and the velocity vector, the magnitude of the angular momentum is the product $L = m v r \sin{\theta}$.

$$
\bold{L} = \bold{r} \times \bold{p} \\[8 pt]
$$

### Torque

Torque is the rotational tendency of a force. When a force $\overrightarrow{F}$ is applied to a point $P$ whose position relative to $O$ is $\overrightarrow{r}$, the torque around $O$ is defined as:

$$
\begin{equation}
\tag{Torque}
\overrightarrow{\tau} = \overrightarrow{r} \times \overrightarrow{F}
\end{equation}
$$

From the definition of cross product, the torque $\overrightarrow{\tau}$ is perpendicular to the plane containing $\overrightarrow{F}$ and $\overrightarrow{r}$, and has a magnitude

$$
| \overrightarrow{\tau} | = r F \sin{\theta}
$$
