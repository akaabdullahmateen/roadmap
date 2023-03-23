# Linear algebra

<!-- omit in toc -->
## Table of contents

- [Introduction](#introduction)
  - [Linear equations](#linear-equations)
  - [System of linear equations](#system-of-linear-equations)
  - [Solution sets](#solution-sets)
  - [Properties](#properties)
    - [Independence](#independence)
    - [Consistency](#consistency)
    - [Equivalence](#equivalence)
  - [Basic and free variables](#basic-and-free-variables)
  - [Parametric description](#parametric-description)
  - [Existence and uniqueness theorem](#existence-and-uniqueness-theorem)
- [Matrix notation](#matrix-notation)
  - [Matrix](#matrix)
  - [Coefficient matrix](#coefficient-matrix)
  - [Augmented matrix](#augmented-matrix)
  - [Elementary row operations](#elementary-row-operations)
  - [Row equivalence](#row-equivalence)
- [Row reduction](#row-reduction)
  - [Row echelon form](#row-echelon-form)
  - [Reduced row echelon form](#reduced-row-echelon-form)
  - [Uniqueness of the reduced row echelon form](#uniqueness-of-the-reduced-row-echelon-form)
  - [Pivot positions](#pivot-positions)
  - [Gaussian elimination](#gaussian-elimination)
    - [Forward elimination](#forward-elimination)
    - [Backward substitution](#backward-substitution)
- [Vector equations](#vector-equations)
  - [Vectors in $\\R^2$](#vectors-in-r2)
- [Matrix decomposition](#matrix-decomposition)
  - [LU decomposition](#lu-decomposition)

## Introduction

### Linear equations

A **linear equation** is an equation that can be written in the form:

$$
\begin{equation}
\tag{Linear equation}
a_1 x_1 + a_2 x_2 + \dots + a_n x_n = b
\end{equation}
$$

where $x_i$ are variables, $a_i$ are coefficients, and $b$ is a constant.

### System of linear equations

A **system of linear equations** (or a *linear system*) is a set of linear equations that involve the same variables.

$$
\begin{equation}
\tag{System of linear equations}
\begin{aligned}
a_{11} x_1 + a_{12} x_2 + &\dots + a_{1n} x_n = b_1 \\
a_{21} x_1 + a_{22} x_2 + &\dots + a_{2n} x_n = b_2 \\
                          &\vdots \\
a_{m1} x_1 + a_{m2} x_2 + &\dots + a_{mn} x_n = b_m
\end{aligned}
\end{equation}
$$

### Solution sets

A **solution** of a linear system is an ordered tuple $(s_1, s_2, \dots, s_n)$ such that each equation in the system is satisfied, if the variables $x_i$ are replaced with values $s_i$.

The **solution set** of a linear system is the set of all possible solutions. A linear system may behave in any one of three possible ways:

- The system has *infinitely many solutions*.
- The system has a *single unique solution*.
- The system has *no solution*.

### Properties

#### Independence

The equations of a linear system are **independent** if none of the equations can be algebraically derived from the others.

#### Consistency

A linear system is **consistent** if it has at least one solution. A linear system is **inconsistent** if it has no solution.

#### Equivalence

Two linear systems are **equivalent** if and only if they have the same solution set.   

### Basic and free variables

In the reduced row echelon form of the augmented matrix of a linear system, a variable that corresponds to a leading 1 is called a *basic* variable, and a variable that does not correspond to a leading 1 is called a *free* variable.

### Parametric description

The solution set of a linear system that has free variables is given as a *parametric description*, where the free variables act as parameters. Each different choice of a free variable determines a different solution of the system, and every solution of the system is determined by a choice of the free variable.

$$
\begin{aligned}
\begin{cases}
x_1 = 1 + 5 x_3 \\
x_2 = 4 - x_3 \\
x_3 = \text{free variable}
\end{cases}
\end{aligned}
$$

### Existence and uniqueness theorem

A linear system is consistent if and only if the rightmost column of the augmented matrix is not a pivot column, that is, the reduced row echelon form of the augmented matrix does not have any rows of the form:

$$
\begin{aligned}
\begin{bmatrix}
0 & 0 & \dots & 0 & b
\end{bmatrix}
&&\text{where $b$ is nonzero}
\end{aligned}
$$

If a linear system is consistent, then the solution set contains either a single unique solution, if there are no free variables, or infinitely many solutions, if there is at least one free variable.

## Matrix notation

### Matrix

A **matrix** is a rectangular array of numbers. The horizontal lines form *rows* and the vertical lines form *columns*.

- A matrix with $m$ rows and $n$ columns is called an $m \times n$ matrix.
- The symbol $a_{ij}$ represents the entry at $i^{th}$ row and $j^{th}$ column.
- A *nonzero row* refers to a row with at least one nonzero entry.
- A *nonzero column* refers to a column with at least one nonzero entry.
- The *leading entry* is the leftmost nonzero entry in a row.

### Coefficient matrix

A **coefficient matrix** is a matrix consisting of the coefficients of the variables in a linear system.

$$
\begin{equation}
\tag{Coefficient matrix}
\begin{bmatrix}
a_{11} & a_{12} & \dots  & a_{1n} \\
a_{21} & a_{22} & \dots  & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots  & a_{mn}
\end{bmatrix}
\end{equation}
$$

### Augmented matrix

An **augmented matrix** is a matrix obtained by appending the coefficient matrix with the column vector of constant terms.

$$
\begin{equation}
\tag{Augmented matrix}
\begin{bmatrix}
a_{11} & a_{12} & \dots  & a_{1n} & b_1    \\
a_{21} & a_{22} & \dots  & a_{2n} & b_2    \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
a_{m1} & a_{m2} & \dots  & a_{mn} & b_m
\end{bmatrix}
\end{equation}
$$

### Elementary row operations

An elementary row operation is any one of the following operations:

| Operation | Description | Symbolic representation |
| - | - | - |
| Swap | Swap two rows of a matrix. | $R_i \lrArr R_j$ |
| Scale | Multiply a row by a nonzero constant. | $k R_i \rArr R_i$ |
| Sum | Add a multiple of one row to another row. | $R_i + k R_j \rArr R_i$ |

### Row equivalence

Two matrices $A$ and $B$ are **row equivalent** if it is possible to transform $A$ into $B$ by a sequence of elementary row operations.

If the augmented matrices of two linear systems are row equivalent, then the two linear systems have the same solution set.

## Row reduction

### Row echelon form

A matrix is in **row echelon form** (called an *echelon matrix*) if it satisfies the following conditions:

- All rows consisting of only zeroes are at the bottom.
- The leading entry of any nonzero row is to the right of the leading entry of the row above it.
- All entries below a leading entry in a column are zero.

$$
\begin{bmatrix}
2   & \ast & \ast & \ast \\
0   & 1    & \ast & \ast \\
0   & 0    & 0    & 5    \\
0   & 0    & 0    & 0    \\
\end{bmatrix}
$$

### Reduced row echelon form

A matrix is in **reduced row echelon form** (called a *reduced echelon matrix*) if it satisfies the following conditions:

- It is in row echelon form.
- The leading entry in each nonzero row is $1$ (called a *leading 1*).
- Each leading 1 is the only nonzero entry in its column.

$$
\begin{bmatrix}
1   & 0   & \ast & 0 \\
0   & 1   & \ast & 0 \\
0   & 0   & 0    & 1 \\
0   & 0   & 0    & 0 \\
\end{bmatrix}
$$

### Uniqueness of the reduced row echelon form

Each matrix $A$ is row equivalent to one and only one reduced echelon matrix. However, the matrix $A$ may be row equivalent to more than one echelon matrix, using different sequences of elementary row operations.

Since the reduced echelon form is unique, the leading entries are always in the same positions
in any echelon form obtained from a given matrix.

### Pivot positions

A **pivot position** in a matrix $A$ is the location that corresponds to a leading 1 in the reduced echelon form of $A$. The column that contains a pivot position is called the **pivot column**, and the nonzero number at the pivot position is called the **pivot**.

### Gaussian elimination

**Gaussian elimination** (also called *row reduction*) is a technique for solving a system of linear equations by reducing its augmented matrix to the reduced echelon form. The process of row reduction can be divided into two phases: *forward elimination* and *backward substitution*.

Sometimes, the forward elimination is called the Gaussian elimination, while the forward elimination combined with the backward substitution is called the *Gauss-Jordan elimination*.

#### Forward elimination

The **forward elimination** phase reduces a given matrix to row echelon form, from which the consistency of the linear system can be determined.

1. Start with the leftmost nonzero column as a pivot column.
2. Select a nonzero entry in the pivot column as a pivot. If necessary, swap rows to move this entry into the pivot position.
3. Use elementary row operations to create zeroes in all positions below the pivot position.
4. Cover (or ignore) the row containing the pivot position and the rows above it.
5. Repeat the above steps on the sub-matrix that remains until there are no more nonzero rows to modify.

#### Backward substitution

The **backward substitution** phase further reduces the echelon matrix to reduced row echelon form, from which the solution set of the linear system can be determined.

1. Beginning with the rightmost pivot, create zeroes above each pivot, and work upwards and to the left.
2. Multiply each row containing a pivot position by a scalar such that each pivot becomes a leading 1.

## Vector equations

### Vectors in $\R^2$

A matrix with only one column is called a **column vector** (or simply a *vector*). A vector with two entries $\omega_1$ and $\omega_2$ is represented as:

$$
\bold{v} =
\begin{bmatrix}
\omega_1 \\
\omega_2
\end{bmatrix}
$$

# TO BE CONTINUED !!!!

## Matrix decomposition

**Matrix decomposition** (or *matrix factorization*) is a factorization of a matrix as the product of two or more matrices.

### LU decomposition

Lower-upper decomposition (or *LU factorization*) is a factorization of a matrix $A$ as the product of a lower triangular matrix $L$ and an upper triangular matrix $U$.

$$
\begin{equation}
\tag{LU decomposition}
A = LU
\end{equation}
$$

The lower triangular matrix $L$ is a square matrix, where all elements above the diagonal are zero, and the diagonal consists of only 1's. The upper triangular matrix $U$ is the echelon form of the matrix $A$.

$$
\begin{bmatrix}
a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
a_{31} & a_{32} & a_{33} & a_{34} \\
\end{bmatrix}
=
\begin{bmatrix}
1 & 0      & 0      \\
l_{21} & 1 & 0      \\
l_{31} & l_{32} & 1 \\
\end{bmatrix}
\cdot
\begin{bmatrix}
u_{11} & u_{12} & u_{13} & u_{14} \\
0      & u_{22} & u_{23} & u_{24} \\
0      & 0      & 0      & u_{34} \\
\end{bmatrix}
$$

When a matrix $A$ can be decomposed as $A = LU$, the equation $A \bold{x} = \bold{b}$ can be written as $L(U \bold{x})$, and $\bold{x}$ can be found by solving the pair of equations:

$$
\begin{aligned}
L \bold{y} &= \bold{b} \\
U \bold{x} &= y
\end{aligned}
$$