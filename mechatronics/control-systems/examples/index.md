# Examples

## Example 1: Proving that an RC circuit is a linear system

!!! example

    **Show that an RC circuit obeying the given relationship is a linear system. For brevity, we assume $\tau = RC$.**

    $$
    \tau \frac{d}{dt} V_c + V_c = V_{in}
    $$ (1)

    Given inputs $V_{in1}$ and $V_{in2}$, we get responses $V_{c1}$ and $V_{c2}$ respectively, such that:

    $$
    \tau \frac{d}{dt} V_{c1} + V_{c1} = V_{in1}
    $$ (2)

    $$
    \tau \frac{d}{dt} V_{c2} + V_{c2} = V_{in2}
    $$ (3)

    Now, if we provide an input $V_{in3}$, which is a weighted sum of the prior two inputs, we get a response $V_{c3}$ according to the equation (1).

    $$
    \tau \frac{d}{dt} V_{c3} + V_{c3} = V_{in3}
    $$ (4)

    $$
    V_{in3} = k_1 V_{in1} + k_2 V_{in2}
    $$ (5)

    To prove that the RC circuit is a linear system, we need to show that:

    $$
    V_{c3} = k_1 V_{c1} + k_2 V_{c2}
    $$

    Substituting equations (2) and (3) into equation (5), we have:

    $$
    \begin{aligned}
    V_{in3} &= k_1 (\tau \frac{d}{dt} V_{c1} + V_{c1}) + k_2 (\tau \frac{d}{dt} V_{c2} + V_{c2}) \\
            &= \tau (k_1 \frac {d}{dt} V_{c1} + k_2 \frac {d}{dt} V_{c2}) + (k_1 V_{c1} + k_2 V_{c2}) \\
            &= \tau (\frac {d}{dt} k_1 V_{c1} + \frac {d}{dt} k_2 V_{c2}) + (k_1 V_{c1} + k_2 V_{c2}) \\
            &= \tau (\frac {d}{dt} (k_1 V_{c1} + k_2 V_{c2})) + (k_1 V_{c1} + k_2 V_{c2})
    \end{aligned}
    $$

    Matching with the equation (4), we observe that $V_{c3} = k_1 V_{c1} + k_2 V_{c2}$. Therefore, the RC circuit is indeed a linear system.

## Example 2: Proving that a second order differential equation is linear

!!! example

    **Show that the system described by the second order differential equation below is linear.**

    $$
    a_2 \frac {d^2}{dt^2} y(t) + a_1 \frac {d}{dt} y(t) + a_0 y(t) = b_1 \frac {d}{dt} x(t) + b_0 x(t)
    $$ (1)

    Given inputs $x_1$ and $x_2$, we get responses $y_1$ and $y_2$ respectively, such that:

    $$
    a_2 \frac {d^2}{dt^2} y_1(t) + a_1 \frac {d}{dt} y_1(t) + a_0 y_1(t) = b_1 \frac {d}{dt} x_1(t) + b_0 x_1(t)
    $$ (2)

    $$
    a_2 \frac {d^2}{dt^2} y_2(t) + a_1 \frac {d}{dt} y_2(t) + a_0 y_2(t) = b_1 \frac {d}{dt} x_2(t) + b_0 x_2(t)
    $$ (3)

    Now, if we provide an input $x_3$, which is a weighted sum of the prior two inputs, we get a response $y_3$ according to the equation (1).

    $$
    a_2 \frac {d^2}{dt^2} y_3(t) + a_1 \frac {d}{dt} y_3(t) + a_0 y_3(t) = b_1 \frac {d}{dt} x_3(t) + b_0 x_3(t)
    $$ (4)

    $$
    x_3(t) = k_1 x_1(t) + k_2 x_2(t)
    $$ (5)

    To prove that the system described by the equation (1) is linear, we need to show that:

    $$
    y_3(t) = k_1 y_1(t) + k_2 y_2(t)
    $$

    Substituting equation (5) into equation (4), we have:

    $$
    \begin{aligned}
    a_2 \frac {d^2}{dt^2} y_3(t) + a_1 \frac {d}{dt} y_3(t) + a_0 y_3(t) &= b_1 \frac {d}{dt} (k_1 x_1(t) + k_2 x_2(t)) + b_0 (k_1 x_1(t) + k_2 x_2(t)) \\
    &= k_1 b_1 \frac {d}{dt} x_1(t) + k_2 b_1 \frac {d}{dt} x_2(t) + k_1 b_0 x_1(t) + k_2 b_0 x_2(t) \\
    &= k_1 b_1 \frac {d}{dt} x_1(t) + k_1 b_0 x_1(t) + k_2 b_1 \frac {d}{dt} x_2(t) + k_2 b_0 x_2(t) \\
    &= k_1 (b_1 \frac {d}{dt} x_1(t) + b_0 x_1(t)) + k_2 (b_1 \frac {d}{dt} x_2(t) + b_0 x_2(t))
    \end{aligned}
    $$

    Using equations (2) and (3), we have:

    $$
    \begin{aligned}
    k_1 (b_1 \frac {d}{dt} x_1(t) + b_0 x_1(t)) + k_2 (b_1 \frac {d}{dt} x_2(t) + b_0 x_2(t)) &= k_1 (a_2 \frac {d^2}{dt^2} y_1(t) + a_1 \frac {d}{dt} y_1(t) + a_0 y_1(t)) + k_2 (a_2 \frac {d^2}{dt^2} y_2(t) + a_1 \frac {d}{dt} y_2(t) + a_0 y_2(t)) \\
    &= k_1 a_2 \frac {d^2}{dt^2} y_1(t) + k_1 a_1 \frac {d}{dt} y_1(t) + k_1 a_0 y_1(t) + k_2 a_2 \frac {d^2}{dt^2} y_2(t) + k_2 a_1 \frac {d}{dt} y_2(t) + k_2 a_0 y_2(t) \\
    &= k_1 a_2 \frac {d^2}{dt^2} y_1(t) + k_2 a_2 \frac {d^2}{dt^2} y_2(t) + k_1 a_1 \frac {d}{dt} y_1(t) + k_2 a_1 \frac {d}{dt} y_2(t) + k_1 a_0 y_1(t) + k_2 a_0 y_2(t) \\
    &= a_2 \frac {d^2}{dt^2} (k_1 y_1(t) + k_2 y_2(t)) + a_1 \frac {d}{dt} (k_1 y_1(t) + k_2 y_2(t)) + a_0 (k_1 y_1(t) + k_2 y_2(t))
    \end{aligned}
    $$

    Matching with the equation (4), we observe that $y_3 = k_1 y_1 + k_2 y_2$. Therefore, the second order differential equation is indeed a linear system.

## Example 3: Proving that a second order differential equation is non-linear

!!! example

    **Show that the system described by the second order differential equation below is non-linear.**
    
    $$
    a_1 \frac {d}{dt} y(t) + a_0 y(t) = b x(t) + 2
    $$ (1)
    
    Given inputs $x_1$ and $x_2$, we get responses $y_1$ and $y_2$ respectively, such that:
    
    $$
    a_1 \frac {d}{dt} y_1(t) + a_0 y_1(t) = b x_1(t) + 2
    $$ (2)
    
    $$
    a_1 \frac {d}{dt} y_2(t) + a_0 y_2(t) = b x_2(t) + 2
    $$ (3)
    
    Now, if we provide an input $x_3$, which is a weighted sum of the prior two inputs, we get a response $y_3$ according to the equation (1).
    
    $$
    a_1 \frac {d}{dt} y_3(t) + a_0 y_3(t) = b x_3(t) + 2
    $$ (4)
    
    $$
    x_3(t) = k_1 x_1(t) + k_2 x_2(t)
    $$ (5)
    
    To prove that the system described by the equation (1) is linear, we need to show that:
    
    $$
    y_3(t) = k_1 y_1(t) + k_2 y_2(t)
    $$
    
    Substituting equation (5) into equation (4), we have:

    $$
    \begin{aligned}
    a_1 \frac {d}{dt} y_3(t) + a_0 y_3(t) &= b x_3(t) + 2 \\
    &= b (k_1 x_1(t) + k_2 x_2(t)) + 2 \\
    &= b (k_1 x_1(t) + k_2 x_2(t)) + 2 + 2 k_1 - 2 k_1 + 2 k_2 - 2 k_2 \\
    &= k_1 b x_1(t) + 2 k_1 + k_2 b x_2(t) + 2 k_2 + 2 - 2 k_1 - 2 k_2 \\
    &= k_1 (b x_1(t) + 2) + k_2 (b x_2(t) + 2) + 2(1 - k_1 - k_2)
    \end{aligned}
    $$
    
    Using equations (2) and (3), we have:
    
    $$
    \begin{aligned}
    k_1 (b x_1(t) + 2) + k_2 (b x_2(t) + 2) + 2(1 - k_1 - k_2) &= k_1 (a_1 \frac {d}{dt} y_1(t) + a_0 y_1(t)) + k_2 (a_1 \frac {d}{dt} y_2(t) + a_0 y_2(t)) + 2(1 - k_1 - k_2) \\
    &= k_1 a_1 \frac {d}{dt} y_1(t) + k_1 a_0 y_1(t) + k_2 a_1 \frac {d}{dt} y_2(t) + k_2 a_0 y_2(t) + 2(1 - k_1 - k_2) \\
    &= k_1 a_1 \frac {d}{dt} y_1(t) + k_2 a_1 \frac {d}{dt} y_2(t) + k_1 a_0 y_1(t) + k_2 a_0 y_2(t) + 2(1 - k_1 - k_2) \\
    &= a_1 \frac {d}{dt} (k_1 y_1(t) + k_2 y_2(t)) + a_0 (k_1 y_1(t) + k_2 y_2(t)) + 2(1 - k_1 - k_2) \\
    \end{aligned}
    $$
    
    Now if $y_3(t) = k_1 y_1(t) + k_2 y_2(t)$, as required by the superposition principle, we have a contradiction.
    
    $$
    a_1 \frac {d}{dt} y_3(t) + a_0 y_3(t) = a_1 \frac {d}{dt} y_3(t) + a_0 y_3(t) + 2(1 - k_1 - k_2)
    $$
    
    Hence, the system described by the given differential equation is non-linear.

## Example 4: Derivation of output response of an LTI system

!!! example

    **Determine an expression for the output function $y(t)$ of a linear time invariant system, given an input function $u(t)$.**

    Write the input signal $u(t)$ as a sample of itself; this means that $u(t)$ can be written as a weighted integral of unit impulse functions.

    $$
    u(t) = \int^{\infty}_{-\infty} u(\tau) \delta(t - \tau) d\tau
    $$

    Applying the linear invariant system $F$ to the input $u(t)$.

    $$
    \begin{aligned}
    y(t) &= F(u(t)) \\
         &= F(\int^{\infty}_{-\infty} u(\tau) \delta(t - \tau) d\tau)
    \end{aligned}
    $$

    Since the system obeys linearity, we can interchange the order of the system operator and the integration.

    $$
    y(t) = \int^{\infty}_{-\infty} u(\tau) F(\delta(t - \tau)) d\tau
    $$

    Substituting for the impulse response gives:

    $$
    y(t) = \int^{\infty}_{-\infty} u(\tau) h(t - \tau) d\tau
    $$

    This can be written as the convolution of the impulse response with an input function.

    $$
    y(t) = h(t) \ast u(t)
    $$

## Example 5: List of common Laplace transforms

!!! example

    In the table below, the time domain column contains the functions $y(t) = \mathcal{L}^{-1} \lbrace Y(s) \rbrace$ and the frequency domain column contains the functions $Y(s) = \mathcal{L} \lbrace y(t) \rbrace$.

    | Function | Time domain | Frequency domain |
    | - | - | - |
    | Unit impulse | $\delta (t)$ | 1 |
    | Delayed unit impulse | $\delta (t - \tau)$ | $e^{-\tau s}$ |
    | Unit step | $u(t)$ | $\frac {1}{s}$ |
    | Delayed unit step | $u(t - \tau)$ | $\frac {1}{s} e^{-\tau s}$ |
    | Ramp | $t \cdot u(t)$ | $\frac {1}{s^2}$ |
    | Integer $n$th power | $t^n \cdot u(t)$ | $\frac {n!}{s^{n+1}}$ |
    | Complex $q$th power | $t^q \cdot u(t)$ | $\frac {\Gamma (q+1)}{s^{q+1}}$ |
    | $n$th root | $\sqrt[n]{t} \cdot u(t)$ | $\frac {1}{s^{\frac {1}{n} + 1}} \Gamma ( \frac {1}{n} + 1 )$ |
    | $n$th power with frequency shift | $t^n e^{-\alpha t} \cdot u(t)$ | $\frac {n!}{(s + \alpha)^{n + 1}}$ |
    | Delayed $n$th power with frequency shift | $(t- \tau)^n e^{-\alpha (t - \tau)} \cdot u(t - \tau)$ | $\frac {n! \cdot e^{-\tau s}}{(s + \alpha)^{n + 1}}$ |
    | Exponential decay | $e^{-\alpha t} \cdot u(t)$ | $\frac {1}{s + \alpha}$ |
    | Two-sided exponential decay | $e^{-\alpha \lvert t \rvert}$ | $\frac {2 \alpha}{\alpha^2 - s^{2}}$ |
    | Exponential approach | $(1 - e^{-\alpha t}) \cdot u(t)$ | $\frac {\alpha}{s(s + \alpha)}$ |
    | Sine | $\sin(\omega t) \cdot u(t)$ | $\frac {\omega}{s^2 + \omega^2}$ |
    | Cosine | $\cos(\omega t) \cdot u(t)$ | $\frac {s}{s^2 + \omega^2}$ |
    | Hyperbolic sine | $\sinh(\alpha t) \cdot u(t)$ | $\frac {\alpha}{s^2 - \alpha^2}$ |
    | Hyperbolic cosine | $\cosh(\alpha t) \cdot u(t)$ | $\frac {s}{s^2 - \alpha^2}$ |
    | Exponentially decaying sine wave | $e^{-\alpha t} \sin(\omega t) \cdot u(t)$ | $\frac {\omega}{(s + \alpha )^2 + \omega^2}$ |
    | Exponentially decaying cosine wave | $e^{-\alpha t} \cos(\omega t) \cdot u(t)$ | $\frac {s + \alpha}{(s + \alpha)^2 + \omega^2}$ |
    | Natural logarithm | $\ln(t) \cdot u(t)$ | $\frac {-\ln(s) - \gamma}{s}$ |
    | Bessel function of $n$th order | $J_n (\omega t) \cdot u(t)$ | $\frac {(\sqrt {s^2 + \omega^2} - s)^n}{\omega^n \sqrt {s^2 + \omega^2}}$ |
    | Error function | $\operatorname{erf} (t) \cdot u(t)$ | $\frac {e^{s^2 / 4}}{s} ( 1 - \operatorname{erf} (\frac {s}{2}))$ |

## Example 6: Continue
