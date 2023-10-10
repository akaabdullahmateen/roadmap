# Frequency response methods

<!-- omit in toc -->
## Table of contents

- [Preview](#preview)
- [Introduction](#introduction)
- [Frequency response plots](#frequency-response-plots)

## Preview

In this chapter, we consider the steady-state response of a system to a sinusoidal input test signal. We will see that the response of a linear constant coefficient system to a sinusoidal input signal is an output sinusoidal signal at the same frequency as the input. However, the magnitude and phase of the output signal differ from those of the input sinusoidal signal, and the amount of difference is a function of the input frequency. Thus, we will be investigating the steady-state response of the system to a sinusoidal input as the frequency varies.

We will examine the transfer function $G(s)$ when $s = j \omega$ and develop methods for graphically displaying the complex number $G(j \omega)$ as $\omega$ varies. The Bode plot is one of the most powerful graphical tools for analyzing and designing control systems, and we will cover that subject in this chapter. We will also consider polar plots and log-magnitude and phase diagrams. We will develop several time-domain performance measures in terms of the frequency response of the system, as well as introduce the concept of a system bandwidth.

## Introduction

A very practical and important approach to the analysis and design of a system is the frequency response method. The frequency response of a system is defined as the steady-state response of the system to a sinusoidal input signal. The sinusoidal is a unique input signal, and the resulting output signal for a linear system is sinusoidal in the steady-state; it differs from the input only in amplitude and phase angle.

For example, consider the system $Y(s) = T(s) R(s)$ with $r(t) = A \sin{\omega t}$. We have:

$$
R(s) = \frac{A \omega}{s^2 + \omega^2} \\ [8pt]
T(s) = \frac{m(s)}{q(s)} = \frac{m(s)}{\prod^n_{i = 1}(s + p_i)}
$$

where $-p_i$ are assumed to be distinct poles. Then in partial fractions form, we have:

$$
Y(s) = \frac{k_1}{s + p_1} + \cdots + \frac{k_n}{s + p_n} + \frac{\alpha s + \beta}{s^2 + \omega^2}
$$

Taking the inverse Laplace transform yields:

$$
y(t) = k_1 e^{-p_1 t} + \cdots + k_n e^{-p_n t} + \mathcal{L}^{-1} \left\{ \frac{\alpha s + \beta}{s^2 + \omega^2} \right\}
$$

where $\alpha$ and $\beta$ are constants which are problem dependent. If the system is stable, then all $p_i$ have positive real parts and

$$
\lim_{t \to \infty} y(t) = \lim_{t \to \infty} \mathcal{L}^{-1} \left\{ \frac{\alpha s + \beta}{s^2 + \omega^2} \right \}
$$

since each exponential term $k_i e^{-p_i t}$ decays to zero as $t \to \infty$. In the limit for $y(t)$, it can be shown, for $t \to \infty$ (the steady state),

$$
y(t) = \mathcal{L}^{-1} \left[ \frac{\alpha s + \beta}{s^2 + \omega^2} \right] = \frac{1}{\omega} \left| A \omega T(j \omega) \right| \sin(\omega t + \phi) \\ [8pt]
= A \left| T(j \omega) \right| \sin(\omega t + \phi)
$$

where $\phi = \angle{T(j \omega)}$. Thus, the steady-state output signals depends only on the magnitude and phase of $T(j \omega)$ at a special frequency $\omega$. The steady state response is true only for stable systems, $T(s)$.

One advantage of the frequency response method is the easy availability of sinusoid test signals for various range of frequencies and amplitudes. Thus, the experimental determination of the system frequency response is easily accomplished. The unknown transfer function of a system can often by deduced from the experimentally determined frequency response of the system. Furthermore, the design of a system in the frequency domain provides the designer with control of bandwidth of a system, as well as some measure of the response of the system to undesired noise and disturbances.

A second advantage of the frequency response method is that the transfer function describing the sinusoidal steady-state behavior of a system can be obtained by replacing $s$ with $j \omega$ in the system transfer function $T(s)$. The transfer function representing the sinusoidal steady-state behavior of a system is then a function of the complex variable $j \omega$ and is itself a complex function $T(j \omega)$ that possesses a magnitude and phase angle. The magnitude and phase angle of $T(j \omega)$ are readily represented by graphical plots that provide significant insight into the analysis and design of control systems.

The basic disadvantage of the frequency response method for analysis and design is the indirect link between the frequency and the time domain. Direct correlations between the frequency response and the corresponding transient response characteristics are mostly negligible, and in practice, the frequency response characteristic is adjusted by using various design criteria that will normally result in a satisfactory transient response.

The Laplace transform pair is:

$$
F(s) = \mathcal{L} \{ f(t) \} = \int^\infty_0 f(t) e^{-s t} dt \\ [8pt]
f(t) = \mathcal{L}^{-1} \{ F(s) \} = \frac{1}{2 \pi j} \int^{\sigma + j \infty}_{\sigma - j \infty} F(s) e^{s t} ds
$$

where the variable $s = \sigma + j \omega$. Similarly, the Fourier transform pair is:

$$
F(\omega) = \mathcal{F} \{ f(t) \} = \int^\infty_{- \infty} f(t) e^{-j \omega t} dt \\ [8pt]
f(t) = \mathcal{F}^{-1} \{ F(\omega) \} = \frac{1}{2 \pi} \int^\infty_{- \infty} F(\omega) e^{j \omega t} d \omega
$$

The Fourier transform exists for $f(t)$ when:

$$
\int^\infty_{-\infty} | f(t) | dt \lt \infty
$$

The Fourier and Laplace transforms are closely related, as can be seen by examining the equations above. When the function $f(t)$ is defined only for $t \ge 0$, as is often the case, the lower limits on the integral are the same. Thus we note that the two equations differ only in the complex variable. Thus, if the Laplace transform of a function $f_1(t)$ is known to be $F_1(s)$, we can obtain the Fourier transform of this same function by setting $s = j \omega$ in $F_1(s)$.

Again we might ask, since the Fourier and Laplace transform are so closely related, why not use the Laplace transform? Why use Fourier transform at all? The Laplace transform enables us to investigate the $s$-plane locations of the poles and zeroes of a transfer function $T(s)$. However, the frequency response method allows us to consider the transfer function $T(j \omega)$ and to concern ourselves with the amplitude and phase characteristics of the system. This ability to investigate and represent the character of a system by amplitude, phase equations, and curves is an advantage for the analysis and design of control systems.

If we consider the frequency response of the closed-loop system, we might have an input $r(t)$ that has a Fourier transform in the frequency domain as follows:

$$
R(j \omega) = \int^\infty_{-\infty} r(t) e^{- j \omega t} dt
$$

Then the output frequency response of a unity feedback control system can be obtained by substituting $s = j \omega$ in the closed-loop system relationship, $Y(s) = T(s) R(s)$, so that we have:

$$
Y(j \omega) = T(j \omega) R(j \omega) = \frac{G_c(j \omega) G(j \omega)}{1 + G_c(j \omega) G(j \omega)} R(j \omega)
$$

Using the inverse Fourier transform, the output transient response would be:

$$
y(t) = \mathcal{F}^{-1} \{ Y(j \omega) \} = \frac{1}{2 \pi} \int^\infty_{- \infty} Y(j \omega) e^{j \omega t} d \omega
$$

However, it is usually difficult to evaluate this inverse transform integral for all but the simplest systems, and a graphical integration may be used. Alternatively, as we will note in succeeding sections, several measures of the transient response can be related to the frequency characteristics and utilized for design purposes.

## Frequency response plots

The transfer function of a system $G(s)$ can be described in the frequency domain by the relation:

$$
G(j \omega) = G(s) |_{s = j \omega} = R(\omega) + j X(\omega)
$$

where:

$$
R(\omega) = \Re \{G(j \omega) \} \\
X(\omega) = \Im \{G(j \omega) \}
$$

<!-- Figure 8.1 -->

Alternatively the transfer function can be represented by a magnitude $| G(j \omega) |$ and a phase $\phi(j \omega)$ as:

$$
G(j \omega) = | G(j \omega) | e^{j \phi(\omega)} = | G(j \omega) | \angle{\phi(\omega)}
$$

where

$$
\phi(\omega) = \tan^{-1} \frac{X(\omega)}{R(\omega)} \\ [8pt]
| G(j \omega) | = \sqrt{[R(\omega)]^2 + [X(\omega)]^2}
$$

The graphical representation of the frequency response of the system $G(j \omega)$ can utilize either of these equations. The polar plot representation of the frequency response is obtained by using the former equation. The coordinates of the polar plot are the real and imaginary parts of $G(j \omega)$.

There are several possibilities for coordinates of a graph portraying the frequency response of a system. We may use a polar plot to represent the frequency response of a system. However, the limitations of polar plots are readily apparent. The addition of poles and zeroes to an existing system requires recalculation of the frequency response. Furthermore, calculating the frequency response in this manner is tedious and does not include the effect of the individual poles or zeroes.

The introduction of logarithmic plots, often called Bode plots, simplifies the determination of the graphical portrayal of the frequency response. The logarithmic plots are called Bode plots in honor of H. W. Bode, who used them extensively in his studies of feedback amplifiers. The transfer function in the frequency domain is:

$$
G(j \omega) = | G(j \omega) | e^{j \phi(\omega)}
$$

The logarithm of the magnitude is normally expressed in terms of the logarithm to the base 10, so we use:

$$
\text{Logarithmic gain} = 20 \log_10 | G(j \omega) |
$$

where the units are decibels (dB). The logarithmic gain in dB and the angle $\phi(\omega)$ can be plotted versus the frequency $\omega$ by utilizing several different arrangements. For a Bode diagram, the plot of logarithmic gain in dB versus $\omega$ is normally plotted on one set of axes, and the phase $\phi(\omega)$ versus $\omega$ on another set of axes. For example, the Bode plot of the transfer function can be readily obtained. The frequency $\omega = 1 / \tau$ is often called the break frequency or corner frequency.

A linear scale of frequency is not the most convenient or judicious choice, and we consider the use of logarithmic scale of frequency. An interval of two frequencies with a ratio equal to 10 is called a decade, so the range of frequencies from $\omega_1$ to $\omega_2$, where $\omega_2 = 10 \omega_1$, is called a decade. Instead of using a horizontal axis of $\log \omega$ and linear rectangular coordinates, it is easier to use semilog axes with a linear rectangular coordinate for dB and a logarithmic coordinate for $\omega$. Alternatively we could use a logarithmic coordinate for the magnitude as well as for frequency, and avoid the necessity of calculating the logarithm of the magnitude.

The frequency interval $\omega_2 = 2 \omega_1$ is often used and called an octave of frequencies. The primary advantage of the logarithmic plot is the conversion of multiplicative factors into additive factors by virtue of the definition of logarithmic gain. This can be readily asserted by considering the transfer function:

$$
G(j \omega) = \frac{K_b \prod^Q_{i = 1}(1 + j \omega \tau_i) \prod^P_{l = 1}(1 + (2 \zeta_l / \omega_{n_l})j \omega + (j \omega / \omega_{n_l})^2)}{(j \omega)^N \prod^M_{m = 1}(1 + j \omega \tau_m) \prod^R_{k = 1}(1 + (2 \zeta_k / \omega_{n_k})j \omega + (j \omega / \omega_{n_k})^2)}
$$

This transfer function includes $Q$ zeroes, $N$ poles at the origin, $M$ poles on the real axis, $P$ pairs of complex conjugate zeroes, and $R$ pairs of complex conjugate poles. The logarithmic magnitude of $G(j \omega)$ is:

$$
20 \log | G(j \omega) | = 20 \log K_b + 20 \sum^Q_{i = 1} \log | 1 + j \omega \tau_i | - 20 \log | (j \omega)^N | - 20 \sum^M_{m = 1} \log | 1 + j \omega \tau_m | \\
+ 20 \sum^P_{l = 1} \log \left| 1 + \frac{2 \zeta_l}{\omega_{n_l}} j \omega + \left(\frac{j \omega}{\omega_{n_l}}\right)^2 \right| - 20 \sum^R_{k = 1} \log \left| 1 + \frac{2 \zeta_k}{\omega_{n_k}} j \omega + \left(\frac{j \omega}{\omega_{n_k}}\right)^2 \right|
$$

and the Bode plot can be obtained by adding the contribution of each individual factor. Furthermore, the separate phase angle plot is obtained as:

$$
\phi(\omega) = \sum^Q_{i = 1} \tan^{-1}(\omega \tau_i) - N(90\degree) - \sum^M_{m = 1} \tan^{-1}(\omega \tau_m) - \sum^R_{k = 1} \tan^{-1} \frac{2 \zeta_k \omega_{n_k} \omega}{\omega_{n_k}^2 - \omega^2} + \sum^P_{l = 1} \tan^{-1} \frac{2 \zeta_l \omega_{n_l} \omega}{\omega_{n_l}^2 - \omega^2}
$$

which is the summation of the phase angles due to each individual factor of the transfer function. Therefore, the four different kinds of factors that may occur in a transfer function are as follows:

- Constant gain, $K_b$
- Poles (or zeroes) at the origin, $(j \omega)$
- Poles (or zeroes) on the real axis, $(j \omega \tau + 1)$
- Complex conjugate poles (or zeroes), $(1 + (2 \zeta / \omega_n)j \omega + (j \omega / \omega_n)^2)$

