# Measures of dispersion, moments, and skewness

<!-- omit in toc -->
## Table of contents

- [Introduction](#introduction)
- [Range](#range)
  - [Absolute measure](#absolute-measure)
  - [Relative measure](#relative-measure)
- [Semi-interquartile range or quartile deviation](#semi-interquartile-range-or-quartile-deviation)
  - [Absolute measure](#absolute-measure-1)
  - [Relative measure](#relative-measure-1)
- [Mean deviation](#mean-deviation)
  - [Absolute measure](#absolute-measure-2)
  - [Relative measure](#relative-measure-2)
- [Variance](#variance)
  - [Absolute measure](#absolute-measure-3)
  - [Frequency distribution](#frequency-distribution)
  - [Relative measure](#relative-measure-3)
- [Standard deviation](#standard-deviation)
  - [Frequency distribution](#frequency-distribution-1)
  - [Relative measure](#relative-measure-4)
- [Trimmed and winsorized measures](#trimmed-and-winsorized-measures)
- [Moments](#moments)
- [Skewness](#skewness)
- [Kurtosis](#kurtosis)
- [Describing a frequency distribution](#describing-a-frequency-distribution)

## Introduction

It is quite possible that two or more sets of data may have the same average but their individual observations may differ considerably from the average. Thus, a value of central tendency does not completely describe the data. Additional information is needed that describes how the data is dispersed about the average.

This is done by measuring the *dispersion*, which means the extent to which the observations in a sample or population vary about their mean. A quantity that describes this characteristic is called a measure of dispersion, scatter, or variability.

It is desirable to have a measure of dispersion:

- in the same units as the observations,
- zero when all observations are equal,
- independent of origin,
- multiplied or divided by a constant.

There are two types of measures of dispersion:

Absolute measure of dispersion
: It measures the dispersion in terms of the same units, or square or units, as the observations.

Relative measure of dispersion
: It is expressed in the form of a ratio, coefficient, or percentage, and is independent of the units of measurement. It is useful for comparison of data of different nature.

The measure of central tendency and measure of dispersion, together, give an adequate description of data.

## Range

The *range* $R$ is defined as the difference between the smallest and the largest observations in a set of data.

### Absolute measure

If $x_m$ is the largest observation and $x_0$ is the smallest observation, the range is defined as:

$$
\begin{equation}
\tag{Range}
R = x_m - x_0
\end{equation}
$$

When the data is grouped as a frequency distribution, the range is estimated by finding the difference between the upper boundary of the highest class and the lower boundary of the lowest class. The range can not be computed if there are open-ended classes in the distribution.

### Relative measure

The relative measure of range is called the *coefficient of dispersion*, and is defined as:

$$
\begin{equation}
\tag{Coefficient of dispersion}
\text{coefficient of dispersion} = \frac{x_m - x_0}{x_m + x_0}
\end{equation}
$$

## Semi-interquartile range or quartile deviation

The interquartile range is a measure of dispersion, defined by the difference between the first and third quartiles; and the half of this range is called the *semi-interquartile range* or the *quartile deviation*.

### Absolute measure

If $Q_1$ is the first quartile and $Q_3$ is the third quartile, the quartile deviation is defined as:

$$
\begin{equation}
\tag{Quartile deviation}
\text{quartile deviation} = \frac{Q_3 - Q_1}{2}
\end{equation}
$$

### Relative measure

The relative measure of quartile deviation is called the *coefficient of quartile deviation* or *coefficient of semi-interquartile range*, and is defined as:

$$
\begin{equation}
\tag{Coefficient of quartile deviation}
\text{coefficient of quartile deviation} = \frac{Q_3 - Q_1}{Q_3 + Q_1}
\end{equation}
$$

## Mean deviation

The mean deviation of a set of data is defined as the arithmetic mean of the deviations measured either from the mean or from the median, all deviations being counted as positive.

The reason to count the deviations as positive is to avoid the difficulty arising from the property that the sum of deviations of the observations from their mean is zero.

### Absolute measure

For a data set of $n$ observations $x_1, x_2, \dots, x_n$, with mean $\overline{x}$, the mean deviation is defined as:

$$
\begin{equation}
\tag{Mean deviation}
\text{mean deviation} = \frac{\sum | x_i - \overline{x} |}{n}
\end{equation}
$$

The term $| x_i - \overline{x} |$ is replaced with $| x_i - \mu |$ for population, and indicates the absolute deviations of the observations from their mean.

For data grouped as a frequency distribution, with $k$ classes and midpoints $x_1, x_2, \dots, x_k$ and corresponding frequencies $f_1, f_2, \dots, f_k$ ($\sum{f_i} = n$), the mean deviation is defined as:

$$
\begin{equation}
\tag{Mean deviation of frequency distribution}
\text{mean deviation} = \frac{\sum{f_i | x_i - \overline{x} |}}{n}
\end{equation}
$$

### Relative measure

The relative measure of mean deviation is called the *coefficient of mean deviation*, and is defined as:

$$
\begin{equation}
\tag{Coefficient of mean deviation}
\text{coefficient of mean deviation} = \frac{\text{mean deviation}}{\text{mean}}
\end{equation}
$$

## Variance

The variance of a set of observations is defined as the mean of the squares of deviations of all the observations from their mean. When it is calculated from the entire population, the variance is called the *population variance*, and is denoted by $\sigma^2$. If, instead, it is calculated from a sample, the variance is called the *sample variance*, and is denoted by $S^2$.

### Absolute measure

For a population with mean $\mu$ and $n$ observations, the variance $\sigma^2$ is defined as:

$$
\begin{equation}
\tag{Variance}
\sigma^2 = \frac{\sum (x_i - \mu)^2}{n}
\end{equation}
$$

For a sample, the symbol $\mu$ is replaced with $\overline{x}$, and the symbol $\sigma^2$ is replaced with $S^2$.

### Frequency distribution

When data is grouped as frequency distribution, with $k$ classes and midpoints $x_1, x_2, \dots, x_k$ and corresponding frequencies $f_1, f_2, \dots, f_k$ ($\sum{f_i} = n$), the sample variance is defined as:

$$
\begin{equation}
\tag{Variance of frequency distribution}
S^2 = \frac{\sum{f_i(x_i - \overline{x})}^2}{n}
\end{equation}
$$

### Relative measure

The relative measure of variance is called the *coefficient of variance*, and is defined as:

$$
\begin{equation}
\tag{Coefficient of variance}
\text{coefficient of variance} = \frac{\sigma}{\mu} \times 100\%
\end{equation}
$$

## Standard deviation

The positive square root of variance is called the *standard deviation*.

$$
\begin{equation}
\tag{Standard deviation}
\sigma = \sqrt{\frac{\sum (x_i - \mu)^2}{n}}
\end{equation}
$$

### Frequency distribution

When data is grouped as frequency distribution, with $k$ classes and midpoints $x_1, x_2, \dots, x_k$ and corresponding frequencies $f_1, f_2, \dots, f_k$ ($\sum{f_i} = n$), the sample standard deviation is defined as:

$$
\begin{equation}
\tag{Standard deviation of frequency distribution}
S = \sqrt{\frac{\sum{f_i(x_i - \overline{x})}^2}{n}}
\end{equation}
$$

### Relative measure

The relative measure of standard deviation is called the *coefficient of standard deviation*, and is defined as:

$$
\begin{equation}
\tag{Coefficient of standard deviation}
\text{coefficient of standard deviation} = \frac{\text{standard deviation}}{\text{mean}}
\end{equation}
$$

## Trimmed and winsorized measures

## Moments

## Skewness

## Kurtosis

## Describing a frequency distribution