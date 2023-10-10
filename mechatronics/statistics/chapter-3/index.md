# Measures of central tendency or averages

<!-- omit in toc -->
## Table of contents

- [Introduction](#introduction)
  - [Criteria of an average](#criteria-of-an-average)
  - [Types of averages](#types-of-averages)
- [Arithmetic mean](#arithmetic-mean)
  - [Weighted arithmetic mean](#weighted-arithmetic-mean)
  - [Properties of arithmetic mean](#properties-of-arithmetic-mean)
  - [Mean of grouped data](#mean-of-grouped-data)
  - [Change of origin and scale](#change-of-origin-and-scale)
- [Geometric mean](#geometric-mean)
- [Harmonic mean](#harmonic-mean)
- [Median](#median)

## Introduction

The visual presentation and condensation of data into a frequency distribution are insufficient when two or more different data sets are to be compared. A data set can be summarized in a single value, that lies somewhere in the center and represents the entire data set. This is the value at which the data in that data set have a tendency to concentrate.

*Central tendency* is the tendency of the observations to cluster in the central part of a data set. Therefore, the value that represents the central tendency is called *measure of central tendency* or *average*. The measure of central tendency should have the following characteristics:

- The measure of central tendency should be somewhere within the range of the data.
- The measure of central tendency should remain unchanged by a rearrangement of the observations in a different order.

### Criteria of an average

For an average to be considered a satisfactory average, it should be:

- rigorously defined,
- based on all the observations made,
- simple to understand and easy to interpret,
- quickly and easily calculated,
- amenable to mathematical treatment,
- relatively stable in repeated sampling experiments, and
- not excessively influenced by abnormally large or small observations

### Types of averages

The most common types of averages are:

- Arithmetic mean
- Geometric mean
- Harmonic mean
- Median
- Mode

The first three types indicates the magnitude of the observed values, the fourth type indicates the middle value, while the last type indicates the most frequent value in the distribution.

## Arithmetic mean

The *arithmetic mean* (or simply *mean*) is defined as the value obtained by dividing the sum of the values of all observations by the total number of observations.

Population mean
: The arithmetic mean corresponding to a population, denoted by $\mu$. The population mean of a set of $N$ observations $x_1, x_2, \dots, x_N$ is defined as:

    $$
    \begin{equation}
    \tag{Population mean}
    \mu = \frac{x_1 + x_2 + \dots + x_N}{N} = \frac{\sum x_i}{N}
    \end{equation}
    $$

Sample mean
: The arithmetic mean corresponding to a sample from a population, denoted by placing a bar over the symbol used to represent the observations. The sample mean of a set of $N$ observations $x_1, x_2, \dots, x_N$ is defined as:

    $$
    \begin{equation}
    \tag{Sample mean}
    \bar{x} = \frac{x_1 + x_2 + \dots + x_N}{N} = \frac{\sum x_i}{N}
    \end{equation}
    $$

The population mean $\mu$ is a fixed quantity, whereas, the sample mean $\bar{x}$ is a variable quantity, because different samples from the same population tend to have different means.

### Weighted arithmetic mean

*Weights* are numeric multipliers that express the relative importance of various observations in a data set. When the observations in a data set are not of equal importance, weights $w_1, w_2, \dots, w_N$ are assigned to their corresponding observations.

The *weighted arithmetic mean*, denoted by $\bar{x}_w$ of a set of $N$ observations $x_1, x_2, \dots, x_N$ with corresponding weights $w_1, w_2, \dots, w_N$, is defined  as:

$$
\begin{equation}
\tag{Weighted arithmetic mean}
\bar{x}_w = \frac{x_1 w_1 + x_2 w_2 + \dots + x_N w_N}{w_1 + w_2 + \dots + w_N}
          = \frac{\sum x_i w_i}{\sum w_i}
\end{equation}
$$

### Properties of arithmetic mean

The arithmetic mean has the following properties:

- For a set of data, the sum of the deviations of the observations $x_i$ from their mean $\bar{x}$ (taken with their signs) is equal to zero.

$$
\begin{equation}
\tag{Sum of deviations}
\begin{aligned}
\sum (x_i - \bar{x}) &= \sum x_i - n \bar{x} \\
                     &= \sum x_i - \sum x_i \\
                     &= 0
\end{aligned}
\end{equation}
$$

- The sum of squared deviations of the observations $x_i$ from their mean $\bar{x}$ is minimum. In mathematical terms, $\sum (x_i - x)^2 \leq \sum (x_i - \alpha)^2$, where $\alpha$ is an arbitrary value; the equality holds when $\alpha = \bar{x}$.

$$
\begin{equation}
\tag{Minimal property of mean}
\begin{aligned}
\sum (x_i - \alpha)^2 &= \sum (x_i - \bar{x} + \bar{x} - \alpha)^2 \\
                      &= \sum [(x_i - \bar{x})^2 + 2(x_i - \bar{x})(\bar{x} - \alpha) + (\bar{x} - \alpha)^2] \\
                      &= \sum (x_i - \bar{x})^2 + 2(\bar{x} - \alpha) \sum (x_i - \bar{x}) + N(\bar{x} - \alpha)^2 \\
                      &= \sum (x_i - \bar{x})^2 + N(\bar{x} - \alpha)^2 \\
                      &\geq \sum (x_i - x)^2
\end{aligned}
\end{equation}
$$

- If $k$ subgroups of data consisting of $n_1, n_2, \dots , n_k$ ($\sum n_i = n$) observations, have respective means $\bar{x}_1, \bar{x}_2, \dots, \bar{x}_k$, then the mean of all the data $\bar{x}$ is defined as:

$$
\begin{equation}
\tag{Weighted mean of subgroup means}
\bar{x} = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2 + \dots + n_k \bar{x}_k}{n_1 + n_2 + \dots + n_k} = \frac{\sum n_i \bar{x}_i}{n}
\end{equation}
$$

- If $y_i = a x_i + b$ ($i = 1, 2, \dots , n$), where $a$ and $b$ are real numbers, and $a \not= 0$, then $\bar{y} = a \bar{x} + b$.

$$
\begin{equation}
\tag{Invariance of mean under linear transformation}
\begin{aligned}
\sum y_i &= \sum (a x_i + b) \\
         &= a \sum x_i + n b \\

n \bar{y} &= a n \bar{x} + n b \\
\bar{y} &= a \bar{x} + b \\
\end{aligned}
\end{equation}
$$

### Mean of grouped data

When the number of observations is large, the data is organized into a frequency distribution, which is used to calculate the *approximate* values for descriptive measures as the identities of the observations are lost.

The approximate value of mean is calculated by assuming that the observations in each class are identical with the class midpoint, so that the product of the midpoint with the frequency of the class, would be approximately equal to the sum of the observations in that class.

Therefore, if a frequency distribution has $k$ classes with midpoints $x_1, x_2, \dots, x_k$, and corresponding frequencies $f_1, f_2, \dots, f_k$ ($\sum f_i = n$), the mean is defined as:

$$
\begin{equation}
\tag{Mean of grouped data}
\bar{x} = \frac{f_1 x_1 + f_2 x_2 + \dots + f_k x_k}{f_1 + f_2 + \dots + f_k} = \frac{\sum f_i x_i}{n}
\end{equation}
$$

### Change of origin and scale

<!-- TODO: -->

## Geometric mean

The *geometric mean*, denoted by $G$, of a set of $n$ positive values $x_1, x_2, \dots, x_n$ is defined as the positive $n^{th}$ root of their product.

$$
\begin{equation}
\tag{Geometric mean}
G = \sqrt[n]{x_1 x_2 \dots x_n}
\end{equation}
$$

When $n$ is large, the computation of the geometric mean becomes difficult. In such cases, the arithmetic can be simplified by using logarithms:

$$
\begin{aligned}
\log{G} &= \frac{1}{n}(\log{x_1} + \log{x_2} + \dots + \log{x_n}) \\
        &= \frac{1}{n} \sum \log{x_i} \\
G       &= \log^{-1}{(\frac{1}{n} \sum{\log{x_i}})}
\end{aligned}
$$

For grouped data organized into a frequency distribution, having $k$ classes with midpoints $x_1, x_2, \dots, x_k$ and corresponding frequencies $f_1, f_2, \dots, f_k$ ($\sum f_i = n$), the geometric mean is defined as:

$$
\begin{equation}
\tag{Geometric mean of grouped data}
G = \sqrt[n]{x_1^{f_1} \cdot x_2^{f_2} \dots x_k^{f_k}}
\end{equation}
$$

In terms of logarithms, the geometric mean of grouped data can be defined as:

$$
\begin{aligned}
\log{G} &= \frac{1}{n}(f_1 \log{x_1} + f_2 \log{x_2} + \dots + f_k \log{x_k}) \\
        &= \frac{1}{n} \sum{f_i \log{x_i}} \\
G       &= \log^{-1}{(\frac{1}{n} \sum{f_i \log{x_i}})}
\end{aligned}
$$

The weighted geometric mean of the values $x_1, x_2, \dots , x_k$ with corresponding weights $w_1, w_2, \dots , w_k$, is defined as:

$$
\begin{equation}
\tag{Weighted geometric mean}
G_w = \log^{-1}{(\frac{1}{\sum w_i} \sum{w_i \log{x_i}})}
\end{equation}
$$

The geometric mean is appropriate to average ratios and rates of change.

## Harmonic mean

The *harmonic mean*, denoted by $H$, of a set of $n$ values $x_1, x_2, \dots , x_n$ is defined as the reciprocal of the arithmetic mean of the reciprocals of the values; given $x_i \not= 0$.

$$
\begin{equation}
\tag{Harmonic mean}
\begin{aligned}
H &= \frac{n}{\frac{1}{x_1} + \frac{1}{x_2} + \dots + \frac{1}{x_n}} \\
  &= \frac{n}{\sum{\frac{1}{x_i}}}
\end{aligned}
\end{equation}
$$

The harmonic mean is appropriate to average certain ratios and rates of change. More precisely, when rates are expressed as $x$ per $y$, and $x$ is a constant, the harmonic mean is required, but if $y$ is constant, the arithmetic mean is required.

For grouped data organized into a frequency distribution, having $k$ classes with midpoints $x_1, x_2, \dots, x_k$ and corresponding frequencies $f_1, f_2, \dots, f_k$ ($\sum f_i = n$), the harmonic mean is defined as:

$$
\begin{equation}
\tag{Harmonic mean of grouped data}
H = \frac{f_1 + f_2 + \dots + f_n}{\frac{f_1}{x_1} + \frac{f_2}{x_2} + \dots + \frac{f_n}{x_n}} = \frac{n}{\sum {f_i \frac{1}{x_i}}}
\end{equation}
$$

The weighted harmonic mean of the values $x_1, x_2, \dots , x_k$ with corresponding weights $w_1, w_2, \dots , w_k$, is defined as:

$$
\begin{equation}
\tag{Weighted harmonic mean}
H = \frac{w_1 + w_2 + \dots + w_n}{\frac{w_1}{x_1} + \frac{w_2}{x_2} + \dots + \frac{w_n}{x_n}} = \frac{\sum w_i}{\sum {w_i \frac{1}{x_i}}}
\end{equation}
$$

## Median

The *median* is defined as the value which divides an ordered data set into two equal parts, with one part containing observations greater than this value, while the other part containing observations smaller than this value. In other words, median is the value at or below which $50 \%$ of the ordered data lie.

The sample median of $n$ observations $x_1, x_2, \dots , x_n$ when arranged in *order* from smallest to largest, is the middle value if $n$ is odd, and the average of the two middle values if $n$ is even. In other words, when $n$ is odd, the median is the value at position $\frac{n + 1}{2}$, and when $n$ is even, the median is the value

$$
\begin{equation}
\tag{Median}
\begin{aligned}
\text{median} = \begin{cases} x_{\frac{n + 1}{2}} & \text{if $n$ is odd} \\
\frac{x_{\frac{n}{2}} + x_{\frac{n}{2} + 1}}{2} & \text{if $n$ is even}
\end{cases}
\end{aligned}
\end{equation}
$$
