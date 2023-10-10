# Chapter 1: Signals and Systems

## Continuous-Time and Discrete-Time Signals

### Mathematical Representation

There are two basic types of signals: continuous-time signals and discrete-time signals. In the case of continuous-time signals, the independent variable is continuous, and thus these signals are defined for a continuum of values of the independent variable. On the other hand, discrete-time signals are defined only at discrete-times, and consequently, for these signals, the independent variable takes only a discrete set of values.

To distinguish between continuous-time and discrete-time signals, the symbol $t$ is used to denote the continuous-time independent variable and $n$ to denote the discrete-time independent variable. In addition, for continuous-time signals, the independent variable is enclosed in parenthesis, whereas for discrete-time signals, the independent variable is enclosed in brackets. The function $x[n]$ is sometimes also called discrete-time sequence.

A discrete-time signal $x[n]$ may represent a phenomenon for which the independent variable is inherently discrete. On the other hand, a very important class of discrete-time signals arises from the sampling of continuous-time signals. In this case, the discrete-time signal $x[n]$ represents successive samples of an underlying phenomenon for which the independent variable is continuous. Systems with digital processors require the use of discrete-time sequences representing sampled versions of continuous-time signals.

## Signal Energy and Power

The total energy over the time interval $t_1 \le t \le t_2$ in a continuous-time $x(t)$ is defined as:

$$
E = \int^{t_2}_{t_1} \left| x(t) \right|^2 dt
$$

where $|x|$ denotes the magnitude of the (possibly complex) number $x$. The time-averaged power is obtained by dividing the energy equation by the length, $t_2 - t_1$, of the time interval.

$$
P = \frac{1}{t_2 - t_1} \int^{t_2}_{t_1} \left| x(t) \right|^2 dt
$$

Similarly, the total energy in a discrete-time signal $x[n]$ over time interval $n_1 \le n \le n_2$ is defined as:

$$
E = \sum^{n_2}_{n = n_1} \left| x[n] \right|^2
$$

and dividing by the number of points in the interval, $n_2 - n_1 + 1$, yields the average power over the interval:

$$
P = \frac{1}{n_2 - n_1 + 1} \sum^{n_2}_{n = n_1} \left| x[n] \right|^2
$$

Furthermore, in many systems, it is desired to examine power and energy in signals over an infinite time interval, that is, for $-\infty \lt t +\infty$ or for $-\infty \lt n +\infty$. In these cases, the total energy is defined as limits of the above equations as the time interval increases without bound. That is, in continuous time:

$$
E_\infty \overset{\Delta}{=} \lim_{T \to \infty} \int^{T}_{-T} \left| x(t) \right|^2 dt = \int^{+\infty}_{-\infty} \left| x(t) \right|^2 dt
$$

and in discrete time:

$$
E_\infty \overset{\Delta}{=} \lim_{N \to \infty} \sum^{+N}_{n = -N} \left| x[n] \right|^2 = \sum^{+\infty}_{n = -\infty} \left| x[n] \right|^2
$$

Note that for some signals, the above integral or sum might not converge, that is, if $x(t)$ or $x[n]$ equals a nonzero constant value for all time. Such integrals have infinite energy, while signals with $E_\infty \lt \infty$ have finite energy.

In an analogous fashion, the time-averaged power over an infinite interval can be defined as:

$$
P_\infty \overset{\Delta}{=} \lim_{T \to \infty} \frac{1}{2T} \int^{T}_{-T} \left| x(t) \right|^2 dt
$$

and:

$$
P_\infty \overset{\Delta}{=} \lim_{N \to \infty} \frac{1}{2N + 1} \sum^{+N}_{n = -N} \left| x[n] \right|^2
$$

in continuous time and discrete time, respectively. With these definitions, three important classes of signals can be identified. The first of these is the class of signals with finite total energy, that is, those signals for which $E_\infty \lt \infty$. Such a signal must have zero average power, since, for example, in continuous time case:

$$
P_\infty = \lim_{T \to \infty} \frac{E_\infty}{2T} = 0
$$

An example of a finite-energy signal is a signal that takes on the value $1$ for $0 \le t \le 1$ and $0$ otherwise. In this case, $E_\infty = 1$ and $P_\infty = 0$.

A second class of signals are those with finite average power, $P_\infty$. If $P_\infty \gt 0$, then, of necessity, $E_\infty = \infty$. This makes sense since if there is a nonzero average energy per unit time, then integrating or summing this over an infinite time interval yields an infinite amount of energy. For example, the constant signal $x[n] = 4$ has infinite energy, but average power $P_\infty = 16$.

There are also signals for which neither $P_\infty$ nor $E_\infty$ are finite. A simple example is the signal $x(t) = t$.

# Reference 1: Discrete-Time Signals and Systems

## Discrete-Time Signals

Signals are broadly classified into analog and discrete signals. An analog signal can be denoted by $x_a(t)$, in which the variable $t$ can represent any physical quantity, but it can be assumed that it represents time in seconds. A discrete signal can be denoted by $x(n)$, in which the variable $n$ is integer-valued and represents discrete instances in time. Therefore, it is called also discrete-time signal, which is a number sequence and can be denoted by one of the following notations:

$$
x(n) = \lbrace x(n) \rbrace = \lbrace \dots, x(-1), \underset{\uarr}{x(0)}, x(1), \dots \rbrace
$$

where the $\uarr$ indicates the sample at $n = 0$.

In MATLAB, a finite-duration sequence can be represented by a row vector of appropriate values. However, such a vector does not have any information about sample position $n$. Therefore, a correct representation of $x(n)$ would require two vectors, one each for $x$ and $n$. For example, a sequence $x(n) = \lbrace 2, 1, -1, 0, 1, 4, 3, 7 \rbrace$ can be represented in MATLAB by:

```matlab
n = [-3,-2,-1,0,1,2,3,4];
x = [2,1,-1,0,1,4,3,7];
```

Generally, the $x$-vector representation is used alone when the sample position information is not required or when such information is trivial, such as when the sequence begins at $n = 0$. An arbitrary infinite-duration sequence can not be represented in MATLAB due to the finite memory limitations.

### Types of Sequences

Several elementary sequences are used in digital signal processing for analysis purposes. Their definitions and MATLAB representations follow.

#### Unit Sample Sequence

$$
\delta(n) =
\begin{cases}
1, n = 0 \\
0, n \ne 0
\end{cases}
= \lbrace \dots, 0,0,\underset{\uarr}{1},0,0, \dots \rbrace
$$

In MATLAB the function `zeros(1,N)` generates a row vector of $N$ zeros, which can be used to implement $\delta(n)$ over a finite interval. However, the logical expression `n == 0` is an elegant way of implementing $\delta(n)$.

# Reference 2: Discrete-Time Signals and Systems - An Operator Approach

