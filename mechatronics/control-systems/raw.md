# Control system

<!-- omit in toc -->
## Table of contents

- [Chapter 2: Mathematical Models of Systems](#chapter-2-mathematical-models-of-systems)
  - [Preview](#preview)
  - [Introduction](#introduction)
  - [Linear approximations of physical systems](#linear-approximations-of-physical-systems)

## Chapter 2: Mathematical Models of Systems

### Preview

Mathematical models of physical systems are key elements in the design and analysis of control systems. The dynamic behavior is generally described by ordinary differential equations. Since most physical systems are nonlinear, linear approximations are used which allows to use Laplace transform methods. Then input-output relationship can be obtained in the form of transfer functions. The transfer functions can be organized into block diagrams or signal-flow graphs to graphically depict the interconnections. Block diagrams and signal-flow graphs are very convenient and natural tools for designing and analyzing complicated control systems.

### Introduction

The approach to dynamic system modelling can be listed as follows:

1. Define the system and its components.
2. Formulate the mathematical model and express necessary assumptions.
3. Obtain the differential equations representing the mathematical model.
4. Solve the equations for the desired output variables.
5. Examine the solutions and the assumptions.
6. If necessary, reanalyze or redesign the system.

<!-- Section 2.2: Differential equations of physical systems -->
<!-- Skipped due to being too lengthy and physics-intensive -->

### Linear approximations of physical systems

Most physical systems are linear withing some range of the variables, however, they ultimately become nonlinear as the variables are increased without limit. Therefore, the range of linearity must be considered for each system.

A system is defined as linear in terms of the system excitation and response. In general, a necessary condition for a linear system can be determined in terms of an excitation $x(t)$ and a response $y(t)$. When the system at rest is subjected to an excitation $x_1(t)$, it provides a response $y_1(t)$. Furthermore, when the system is subjected to an excitation $x_2(t)$, it provides a corresponding response $y_2(t)$. For a linear system, it is necessary that the excitation $x_1(t) + x_2(t)$ result in a response $y_1(t) + y_2(t)$. This is the principle of superposition.

Furthermore, the magnitude scale factor must be preserved in a linear system. Again, considering a system with an input $x(t)$ that results in an output $y(t)$. Then the response of a linear system to a constant multiple $\beta$ of an input $x$ must be equal to the response to the input multiplied by the same constant so that the output is equal to $\beta y(t)$. This is the property of homogeneity.

A linear system satisfies the properties of superposition and homogeneity.