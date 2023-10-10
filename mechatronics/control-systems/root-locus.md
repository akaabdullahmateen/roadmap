# The root locus method

<!-- omit in toc -->
## Table of contents

- [Preview](#preview)
- [Introduction](#introduction)
- [The root locus concept](#the-root-locus-concept)

## Preview

The performance of a feedback system can be described in terms of the location of the roots of the characteristic equation in the $s$-plane. A graph showing how the roots of the characteristic equation move around the $s$-plane as a single parameter varies is known as a root locus plot. The root locus is a powerful tool for designing and analyzing feedback control systems. We will discuss practical techniques for obtaining a sketch of a root locus plot. We will consider computer-generated root locus plots and illustrate their effectiveness in the design process. We show that it is possible to use root locus methods for controller design when more than one parameter varies. This is important because we know that the response of a closed-loop feedback system can be adjusted to achieve the desired performance by judicious selection of one or more control parameters. The popular PID controller is introduced as a practical controller structure. We also define a measure of sensitivity of a specified root to a a small incremental change in a system parameter.

## Introduction

The relative stability and the transient performance of a closed-loop control system are directly related to the location of the closed-loop roots of the characteristic equation in the $s$-plane. It is frequently necessary to adjust one or more system parameters in order to obtain suitable root locations. Therefore, it is worthwhile to determine how the roots of the characteristic equation of a given system migrate about the $s$-plane as the parameters are varied; that is, it is useful to determine the locus of roots in the $s$-plane as a parameter is varied. The root locus method was introduced by Evans in 1948 and has been developed and utilized extensively in control engineering practice. The root locus technique is a graphical method for sketching the locus of roots in the $s$-plane as a parameter is varied. The root locus method provides the engineer with a measure of the sensitivity of the roots of the system to a variation in the parameter being considered. The root locus technique may be used to great advantage in conjunction with the Routh-Hurwitz criterion.

The root locus method provides graphical information, and therefore an approximate sketch can be used to obtain qualitative information concerning the stability and performance of the system. Furthermore, the locus of roots of the characteristic equation of a multi-loop system may be investigated as readily as for a single-loop system. If the root locations are not satisfactory, the necessary parameter adjustments can often be readily ascertained from the root locus.

## The root locus concept

The dynamic performance of a closed-loop system is described by the closed-loop transfer function:

$$
T(s) = \frac{Y(s)}{R(s)} = \frac{p(s)}{q(s)}
$$

where $p(s)$ and $q(s)$ are polynomials in $s$. The roots of the characteristic equation $q(s)$ determine the modes of response of the system. In the case of the simple single-loop system, we have the characteristic equation:

$$
1 + K G(s) = 0
$$

where $K$ is a variable parameter and $0 \leq K \lt \infty$. The characteristic roots of the system lie in the $s$-plane. Because $s$ is a complex variable, the characteristic equation may be rewritten in polar form as:

$$
| K G(s) | \angle{K G(s)} = -1 + j0
$$

and therefore it is necessary that:

$$
| K G(s) | = 1
$$

and:

$$
\angle{K G(s)} = 180\degree + k 360\degree
$$

where:

$$
k = 0, \plusmn 1, \plusmn 2, \plusmn 3, \dots
$$

The root locus is the path of the roots of the characteristic equation traced out in the $s$-plane as a system parameter varies from zero to infinity.

Consider a second-order system with $G(s) = \frac{1}{s(s+2)}$. The characteristic equation is:

$$
\Delta(s) = 1 + K G(s) = 1 + \frac{K}{s(s+2)} = 0
$$

or alternatively:

$$
\Delta(s) = s^2 + 2s + K = s^2 + 2 \zeta \omega_n s + \omega_n^2 = 0
$$

The locus of the roots as the gain $K$ is varied is found by requiring that:

$$
| K G(s) | = \left| \frac{K}{s(s+2)} \right| = 1 \\
\angle{K G(s)} = \plusmn 180\degree, \plusmn 540\degree, \dots
$$

The gain $K$ is varied from zero to infinity. For a second-order system, the roots are:

$$
s_1, s_2 = -\zeta \omega_n \plusmn \omega_n \sqrt{\zeta^2 - 1}
$$

and for $\zeta \lt 1$, we know that $\theta = \cos^{-1}\zeta$. Graphically, for two open-loop poles, the locus of the roots is a vertical line for $\zeta \geq 1$ in order to satisfy the angle requirement.