# Linear algebra

<!-- omit in toc -->
## Table of contents

- [Linear system](#linear-system)
  - [Linear equation](#linear-equation)
  - [System of linear equations](#system-of-linear-equations)
  - [Solution set](#solution-set)
  - [Vector equation](#vector-equation)
  - [Matrix equation](#matrix-equation)
  - [Homogeneous linear systems](#homogeneous-linear-systems)
- [Matrix notation](#matrix-notation)
  - [Matrix](#matrix)
  - [Matrix multiplication](#matrix-multiplication)
  - [Coefficient matrix](#coefficient-matrix)
  - [Augmented matrix](#augmented-matrix)
  - [Elementary row operations](#elementary-row-operations)
  - [Row equivalence](#row-equivalence)
  - [Row echelon form](#row-echelon-form)
  - [Reduced row echelon form](#reduced-row-echelon-form)
  - [Gaussian elimination](#gaussian-elimination)
  - [Parametric description](#parametric-description)
  - [Existence and uniqueness theorem](#existence-and-uniqueness-theorem)
  - [LU decomposition](#lu-decomposition)
- [Vector algebra](#vector-algebra)
  - [Euclidean vector](#euclidean-vector)
  - [Unit vector](#unit-vector)
  - [Real coordinate space](#real-coordinate-space)
  - [Field](#field)
  - [Vector space](#vector-space)
  - [Linear subspace](#linear-subspace)
  - [Linear combination](#linear-combination)
  - [Linear span](#linear-span)
  - [Null space](#null-space)
  - [Column space](#column-space)
  - [Linear transformation](#linear-transformation)
- [Eigenvectors and eigenvalues](#eigenvectors-and-eigenvalues)
  - [Eigenvector](#eigenvector)
  - [Eigenspace](#eigenspace)
  - [Eigenvalues of a triangular matrix](#eigenvalues-of-a-triangular-matrix)

## Linear system

### Linear equation

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

The following properties apply to a system of linear equations:

Independence
: The equations of a linear system are **independent** if none of the equations can be algebraically derived from the others.

Consistency
: A linear system is **consistent** if it has at least one solution. A linear system is **inconsistent** if it has no solution.

Equivalence
: Two linear systems are **equivalent** if and only if they have the same solution set.   

### Solution set

A **solution** of a linear system is an ordered tuple $(s_1, s_2, \dots, s_n)$ that makes each equation a true statement when the values $s_i$ are substituted for variables $x_i$. The set of all possible solutions of a linear system is called the **solution set**.

$$
\begin{equation}
\tag{Solution set}
\begin{aligned}
\lbrace (s_1, s_2, &\dots, s_n), \\
        (s_1, s_2, &\dots, s_n), \\
                   &\vdots       \\
        (s_1, s_2, &\dots, s_n) \rbrace
\end{aligned}
\end{equation}
$$

A linear system can behave in any one of three possible ways:

- The system has *infinitely many solutions*.
- The system has a *single unique solution*.
- The system has *no solution*.

### Vector equation

The general form of a system of linear equations can be equivalently represented as a vector equation, where each variable is a weight for a column vector in a linear combination.

$$
\begin{equation}
\tag{Vector equation}
x_1
\begin{bmatrix}
a_{11} \\
a_{21} \\
\vdots \\
a_{m1}
\end{bmatrix}
+
x_2
\begin{bmatrix}
a_{12} \\
a_{22} \\
\vdots \\
a_{m2}
\end{bmatrix}
+
\cdots
+
x_n
\begin{bmatrix}
a_{1n} \\
a_{2n} \\
\vdots \\
a_{mn}
\end{bmatrix}
=
\begin{bmatrix}
b_{1} \\
b_{2} \\
\vdots \\
b_{m}
\end{bmatrix}
\end{equation}
$$

### Matrix equation

The general form of a system of linear equations is equivalent to a matrix equation of the form: $A \bold{x} = \bold{b}$, where $A$ is the coefficient matrix, and $\bold{x}$ and $\bold{b}$ represents the $n$ variables and $m$ constant terms respectively.

$$
\begin{equation}
\tag{Matrix equation}
\begin{bmatrix}
a_{11} & a_{12} & \dots  & a_{1n} \\
a_{21} & a_{22} & \dots  & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots  & a_{mn}
\end{bmatrix}
\begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{bmatrix}
=
\begin{bmatrix}
b_{1} \\
b_{2} \\
\vdots \\
b_{m}
\end{bmatrix}
\end{equation}
$$

If $A$ is a $m \times n$ matrix, with columns $\bold{a_1}, \bold{a_2}, \dots, \bold{a_n}$ and if $\bold{b}$ is in $\R^m$, the matrix equation: $A \bold{x} = \bold{b}$ has the same solution set as the vector equation: $x_1 \bold{a_1} + x_2 \bold{a_2} + \dots + x_n \bold{a_n} = \bold{b}$ which, in turn, has the same solution set as the system of linear equations whose augmented matrix is: $\begin{bmatrix}\bold{a_1} & \bold{a_2} & \dots & \bold{a_n} & \bold{b}\end{bmatrix}$.

If $A$ is an $m \times n$ matrix, then the following statements are logically equivalent. That is, for a particular $A$, either they are all true statements or they are all false.

- For each $\bold{b}$ in $\R^m$, the equation $A \bold{x} = \bold{b}$ has a solution.
- Each $\bold{b}$ in $\R^m$ is a linear combination of the columns of $A$.
- The columns of $A$ span $\R^m$.
- The matrix $A$ has a pivot position in every row.

### Homogeneous linear systems

A system of linear equations is **homogeneous** if it can be written in the following form, where $A$ is an $m \times n$ matrix and $\bold{0}$ is the zero vector in $\R^m$.

$$
\begin{equation}
\tag{Homogeneous linear system}
A \bold{x} = \bold{0}
\end{equation}
$$

The homogeneous equation $A \bold{x} = \bold{0}$ always has the trivial solution $\bold{x} = \bold{0}$. However, it has a nontrivial solution if and only if the equation has at least one free variable.

## Matrix notation

### Matrix

A **matrix** is a rectangular array of numbers. The horizontal lines form *rows* and the vertical lines form *columns*.

- A matrix with $m$ rows and $n$ columns is called an $m \times n$ matrix.
- The symbol $a_{ij}$ represents the entry at $i^{th}$ row and $j^{th}$ column.
- A *nonzero row* refers to a row with at least one nonzero entry.
- A *nonzero column* refers to a column with at least one nonzero entry.
- The *leading entry* is the leftmost nonzero entry in a row.
- A *pivot position* is the location that corresponds to a leading 1 in the reduced echelon form.
- The *pivot column* is the column that contains a pivot position.
- The *pivot* is the nonzero number at the pivot position.

### Matrix multiplication

**Matrix multiplication** is a binary operation that produces an $m \times p$ matrix $C$ from an $m \times n$ matrix $A$ and and $n \times p$ matrix $B$.

$$
\begin{equation}
\tag{Matrix multiplication}
\begin{bmatrix}
a_{11} & a_{12} & \dots  & a_{1n} \\
a_{21} & a_{22} & \dots  & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots  & a_{mn}
\end{bmatrix}
\begin{bmatrix}
b_{11} & b_{12} & \dots  & b_{1p} \\
b_{21} & b_{22} & \dots  & b_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
b_{n1} & b_{n2} & \dots  & b_{np}
\end{bmatrix}
=
\begin{bmatrix}
c_{11} & c_{12} & \dots  & c_{1p} \\
c_{21} & c_{22} & \dots  & c_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
c_{m1} & c_{m2} & \dots  & c_{mp}
\end{bmatrix}
\end{equation}
$$

Each entry $c_{ij}$ in the matrix product $C$ is the dot product of the $i^{th}$ row of $A$ and $j^{th}$ column of $B$.

$$
c_{ij} = a_{i1} b_{1j} + a_{i2} b_{2j} + \cdots + a_{in} b_{nj} = \sum^{n}_{k=1} {a_{ik} b_{kj}}
$$

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

Uniqueness of the reduced row echelon form
: Each matrix $A$ is row equivalent to one and only one reduced echelon matrix. Since the reduced echelon form is unique, the leading entries are always in the same positions
in any echelon form obtained from a given matrix.

Basic and free variables
: In the reduced row echelon form of the augmented matrix of a linear system, a variable that corresponds to a leading 1 is called a *basic* variable, and a variable that does not correspond to a leading 1 is called a *free* variable.

### Gaussian elimination

**Gaussian elimination** (also called *row reduction*) is a technique for solving a system of linear equations by reducing its augmented matrix to the reduced echelon form. The process of row reduction can be divided into two phases: *forward elimination* and *backward substitution*.

Sometimes, the forward elimination is called the Gaussian elimination, while the forward elimination combined with the backward substitution is called the *Gauss-Jordan elimination*.

Forward elimination
: The **forward elimination** phase reduces a given matrix to row echelon form, from which the consistency of the linear system can be determined.

  1. Start with the leftmost nonzero column as a pivot column.
  2. Select a nonzero entry in the pivot column as a pivot. If necessary, swap rows to move this entry into the pivot position.
  3. Use elementary row operations to create zeroes in all positions below the pivot position.
  4. Cover (or ignore) the row containing the pivot position and the rows above it.
  5. Repeat the above steps on the sub-matrix that remains until there are no more nonzero rows to modify.

Backward substitution
: The **backward substitution** phase further reduces the echelon matrix to reduced row echelon form, from which the solution set of the linear system can be determined.

  1. Beginning with the rightmost pivot, create zeroes above each pivot, and work upwards and to the left.
  2. Multiply each row containing a pivot position by a scalar such that each pivot becomes a leading 1.

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

**Matrix decomposition** (or *matrix factorization*) is a factorization of a matrix as the product of two or more matrices.

### LU decomposition

Lower-upper decomposition (or *LU factorization*) is a factorization of a matrix $A$ as the product of a lower unit triangular matrix $L$ and an upper triangular matrix $U$.

$$
\begin{equation}
\tag{LU decomposition}
A = LU
\end{equation}
$$

The lower unit triangular matrix $L$ is a square matrix, where all elements above the diagonal are zero, and the diagonal consists of only 1's. The upper triangular matrix $U$ is the echelon form of the matrix $A$.

$$
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33} \\
\end{bmatrix}
=
\begin{bmatrix}
1 & 0      & 0      \\
l_{21} & 1 & 0      \\
l_{31} & l_{32} & 1 \\
\end{bmatrix}
\begin{bmatrix}
u_{11} & u_{12} & u_{13} \\
0      & u_{22} & u_{23} \\
0      & 0      & 0      \\
\end{bmatrix}
$$

The element $l_{ij}$ is the multiplier used to make $a_{ij}$ zero during the $j^{th}$ step of the forward elimination, according to the operation: $a_{ij} = a_{ij} - l_{ij} a_{jj}$. Since, $a_{ij}$ becomes zero after this operation:

$$
l_{ij} = \frac{a_{ij}}{a_{jj}}
$$

When a matrix $A$ can be decomposed as $A = L U$, the equation $A \bold{x} = \bold{b}$ can be written as $L (U \bold{x})$, and $\bold{x}$ can be found by solving the pair of equations:

$$
\begin{aligned}
L \bold{y} &= \bold{b} \\
U \bold{x} &= \bold{y}
\end{aligned}
$$

## Vector algebra

### Euclidean vector

A **Euclidean vector** is a geometric object in the Euclidean vector space. It is defined as a directed line segment with an initial point $A$ and a terminal point $B$, and denoted as $\overrightarrow{AB}$.

$$
\begin{equation}
\tag{Euclidean vector}
\overrightarrow{AB} =
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
\end{equation}
$$

### Unit vector

A **unit vector** is a vector of length $1$. The **normalized vector** $\hat{\bold{u}}$ of a nonzero vector $\bold{u}$ is the unit vector in the direction of $\bold{u}$.

$$
\begin{equation}
\tag{Normalized vector}
\hat{\bold{u}} = \frac{\bold{u}}{||\bold{u}||}
\end{equation}
$$

The term $||\bold{u}||$ is the **Euclidean norm** of the vector $\bold{u}$, which is the square root of the sum of squares of the coordinates of $\bold{u}$.

$$
\begin{equation}
\tag{Euclidean norm}
||u|| = \sqrt[2]{x_1^2 + x_2^2 + \dots + x_n^2}
\end{equation}
$$

### Real coordinate space

The **real coordinate space** of dimension $n$ is the set $\R^n$ that consists of all n-tuples of real numbers $\R$. An **n-tuple** is an ordered list of $n$ elements. Therefore, $\R^n$ is the set of all permutations of $n$ real numbers.

$$
\begin{equation}
\tag{Real coordinate space}
\R^n = (x_1, x_2, \dots , x_n)
\end{equation}
$$

### Field

A field is a set $F$ together with two binary operations called *addition* and *multiplication*, both of which behave similarly as they behave for real numbers, including the existence of an additive inverse and a multiplicative inverse.

### Vector space

A vector space over a field $F$ is a nonempty set $V$ together with two binary operations called *addition* and *scalar multiplication*, that satisfy the axioms listed below:

| Axiom | Meaning |
| - | - |
| Commutativity of vector addition | $\bold{u} + \bold{v} = \bold{v} + \bold{u}$ |
| Associativity of vector addition | $\bold{u} + (\bold{v} + \bold{w}) = (\bold{u} + \bold{v}) + \bold{w}$ |
| Compatibility of scalar multiplication with field multiplication | $c(d \bold{v}) = (c d) \bold{v}$ |
| Distributivity of scalar multiplication over vector addition | $c(\bold{u} + \bold{v}) = c \bold{u} + c \bold{v}$ |
| Distributivity of scalar multiplication over field addition | $(c + d) \bold{v} = c \bold{v} + d \bold{v}$ |
| Identity element of vector addition | There exists a *zero vector* $\bold{0} \in V$, such that $\bold{v} + 0 = \bold{v}$ for all $\bold{v} \in V$ |
| Identity element of scalar multiplication | $1 \bold{v} = \bold{v}$, where $1$ denotes the multiplicative identity in $F$ |
| Inverse element of vector addition | For all $\bold{v} \in V$, there exists an *additive inverse* $\bold{-v} \in V$, such that $\bold{v} + (\bold{-v}) = \bold{0}$ |
| Closure of vector addition | The sum $\bold{u} + \bold{v}$ is in $V$ |
| Closure of scalar multiplication | The scalar multiple $c \bold{v}$ is in $V$ |

For all scalars $c \in F$ and vectors $\bold{v} \in V$, direct consequences of these axioms include:

- $0 \bold{v} = \bold{0}$
- $c \bold{0} = \bold{0}$
- $-1(\bold{v}) = \bold{-v}$

When the scalar field is the real numbers, the vector space is called the *real vector space*, whereas, when the scalar field is the complex numbers, the vector space is called the *complex vector space*.

In the context of vector spaces, the elements of the vector space $V$ are called *vectors* and the elements of the field $K$ are called *scalars*.

### Linear subspace

A **linear subspace** of a vector space $V$ over a field $K$ is a subset $H$ of $V$ that is itself a vector space over $K$. It follows that a linear subspace $H$ of a vector space $V$ must satisfy the following properties:

- The zero vector of $V$ is in $H$.
- $H$ is closed under vector addition, that is, for each $\bold{u}$ and $\bold{v}$ in $H$, the sum $\bold{u} + \bold{v}$ is in $H$.
- $H$ is closed under scalar multiplication, that is, for each $\bold{v}$ in $H$ and each scalar $c$ in $K$, the vector $c \bold{v}$ is in $H$.

All vector spaces have two *trivial subspaces*:

- The *zero subspace* $\{\bold{0}\}$ consisting of the zero vector alone.
- The entire vector space itself.

### Linear combination

The **linear combination** of vectors $\bold{v}_1, \bold{v}_2, \dots, \bold{v}_n$ with scalars $a_1, a_2, \dots, a_n$ as weights is:

$$
\begin{equation}
\tag{Linear combination}
a_1 \bold{v}_1 + a_2 \bold{v}_2 + \dots + a_n \bold{v}_n
\end{equation}
$$

### Linear span

The **linear span** of a set $S$ of vectors, from a vector space $V$, is the set of all finite linear combinations of the vectors in $S$. It is characterized as the intersection of all linear subspaces of $V$ that contain $S$. Therefore, the linear span of a set of vectors is a linear subspace of $V$.

The linear span $H$ of a set $S$ is denoted as $\text{span}(S)$, and $H$ is called the *subspace spanned* by $S$, while $S$ is called the *spanning set* of $H$.

If $V$ is a vector space over the field $K$, and $S$ is the set $\{\bold{v}_1, \bold{v}_2, \dots, \bold{v}_n\}$ of vectors, it can be verified that the linear span $H$ of $S$ is a linear subspace of $V$.

- The zero vector of $V$ is in $H$.
    $$
    \bold{0} = 0 \bold{v}_1 + 0 \bold{v}_2 + \dots + 0 \bold{v}_n
    $$
- $H$ is closed under vector addition.
    $$
    \begin{aligned}
    \bold{u} + \bold{v} &= (a_1 \bold{v}_1 + a_2 \bold{v}_2 + \dots + a_n \bold{v}_n) + (b_1 \bold{v}_1 + b_2 \bold{v}_2 + \dots + b_n \bold{v}_n) \\
          &= (a_1 + b_1) \bold{v}_1 + (a_2 + b_2) \bold{v}_2 + \dots + (a_n + b_n) \bold{v}_n
    \end{aligned}
    $$
- $H$ is closed under scalar multiplication.
    $$
    \begin{aligned}
    c \bold{u} &= c (a_1 \bold{v}_1 + a_2 \bold{v}_2 + \dots + a_n \bold{v}_n) \\
        &= (c a_1) \bold{v}_1 + (c a_2) \bold{v}_2 + \dots + (c a_n) \bold{v}_n
    \end{aligned}
    $$

### Null space

The **null space** of an $m \times n$ matrix $A$, denoted as $\text{Nul}(A)$ is the solution set of the homogeneous equation $A \bold{x} = \bold{0}$.

$$
\begin{equation}
\tag{Null space}
\text{Nul}(A) = \lbrace \bold{x} \in \R^n : A \bold{x} = \bold{0} \rbrace
\end{equation}
$$

The null space can be visualized as the set of all $\bold{x}$ in $\R^n$ that are mapped into the zero vector of $\R^m$ through the linear transformation $\bold{x} \mapsto A \bold{x}$.

The null space of an $m \times n$ matrix $A$ is a subspace of $\R^n$. Equivalently, the solution set of the homogenous equation $A \bold{x} = \bold{0}$, with $m$ homogeneous linear equations in $n$ variables, is a subspace of $\R^n$.

The spanning set for the null space of a matrix $A$ is calculated by reducing the augmented matrix $\begin{bmatrix} A & \bold{0} \end{bmatrix}$ to reduced row echelon form in order to describe the basic variables in terms of the free variables.

$$
\begin{bmatrix}
-3 &  6 & -1 & 1 & -7 & 0 \\
 1 & -2 &  2 & 3 & -1 & 0 \\
 2 & -4 &  5 & 8 & -4 & 0
\end{bmatrix}
\rArr
\begin{bmatrix}
1 & -2 & 0 & -1 &  3 & 0 \\
0 &  0 & 1 &  2 & -2 & 0 \\
0 &  0 & 0 &  0 &  0 & 0
\end{bmatrix}
$$

Then the parametric description vector is decomposed into a linear combination of vectors where the weights are the free variables. The set of the resulting vectors $\lbrace \bold{u}, \bold{v}, \bold{w} \rbrace$ is a spanning set for $\text{Nul}(A)$.

$$
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
x_4 \\
x_5
\end{bmatrix}
=
\begin{bmatrix}
2 x_2 + x_4 - 3 x_5 \\
x_2 \\
-2 x_4 + 2 x_5 \\
x_4 \\
x_5
\end{bmatrix}
= x_2
\begin{bmatrix}
2 \\
1 \\
0 \\
0 \\
0
\end{bmatrix}
+ x_4
\begin{bmatrix}
1 \\
0 \\
-2 \\
1 \\
0
\end{bmatrix}
+ x_5
\begin{bmatrix}
-3 \\
0 \\
2 \\
0 \\
1
\end{bmatrix}
= x_2 \bold{u} + x_4 \bold{v} + x_5 \bold{w}
$$

### Column space

The **column space** of an $m \times n$ matrix $A$, denoted as $\text{Col}(A)$, is the set of all linear combinations of the columns of $A$. If $A = \begin{bmatrix} \bold{a_1} & \bold{a_2} & \dots & \bold{a_n} \end{bmatrix}$, then:

$$
\begin{equation}
\tag{Column space}
\text{Col}(A) = \text{Span} \lbrace \bold{a_1}, \bold{a_2}, \dots, \bold{a_n} \rbrace
\end{equation}
$$

The $\text{Span} \lbrace \bold{a_1}, \bold{a_2}, \dots, \bold{a_n} \rbrace$ is a subspace, and the columns of $A$ are in $\R^m$, therefore, the column space of an $m \times n$ matrix $A$ is a subspace of $\R^m$

The typical vector in $\text{Col}(A)$ can be written as $A \bold{x}$ for some $\bold{x}$ because the notation $A \bold{x}$ represents a linear combination of the columns of $A$. This notation shows that $\text{Col}(A)$ is the range of the linear transformation $\bold{x} \mapsto A \bold{x}$.

$$
\text{Col}(A) = \lbrace \bold{b} : \bold{b} = A \bold{x}, \bold{x} \in \R^n \rbrace
$$

The following table highlights the contrast between $\text{Nul}(A)$ and $\text{Col}(A)$.

| $\text{Nul}(A)$ | $\text{Col}(A)$ |
| - | - |
| $\text{Nul}(A)$ is a subspace of $\R^n$. | $\text{Col}(A)$ is a subspace of $\R^m$. |
| $\text{Nul}(A)$ is implicitly defined; there is only a condition ($A \bold{x} = \bold{0}$) that vectors in $\text{Nul}(A)$ must satisfy. | $\text{Col}(A)$ is explicitly defined; the description is alone sufficient to find vectors in $\text{Col}(A)$. |
| There is no obvious relation between $\text{Nul}(A)$ and the entries in $A$. | There is an obvious relation between $\text{Col}(A)$ and the entries in $A$, since each column in $A$ is in $\text{Col}(A)$. |
| A typical vector $\bold{v}$ in $\text{Nul}(A)$ has the property that $A \bold{v} = \bold{0}$. | A typical vector $\bold{v}$ in $\text{Col}(A)$ has the property that the equation $A \bold{x} = \bold{v}$ is consistent. |
| It is easy to test whether a vector $v$ belongs to $\text{Nul}(A)$, but it is hard to find vectors from the description of $\text{Nul}(A)$. | It is easy to find vectors from the description of $\text{Col}(A)$, but it is hard to test whether a vector $v$ belongs to $\text{Col}(A)$. |
| $\text{Nul}(A) = \lbrace \bold{0} \rbrace$ if and only if the equation $A \bold{x} = \bold{0}$ has only the trivial solution. | $\text{Col}(A) = \R^m$ if and only if the equation $A \bold{x} = \bold{b}$ has a solution for every $\bold{b}$ in $\R^m$. |
| $\text{Nul}(A) = \lbrace \bold{0} \rbrace$ if and only if the linear transformation $\bold{x} \mapsto A \bold{x}$ is one-to-one. | $\text{Col}(A) = \R^m$ if and only if the linear transformation $\bold{x} \mapsto A \bold{x}$ maps $\R^n$ onto $\R^m$. |

### Linear transformation

A **linear transformation** $T$ from a vector space $V$ into a vector space $W$ is a rule that assigns to each vector $\bold{x}$ in $V$ a unique vector $T(\bold{x})$ in $W$, such that:

- TO BE CONTINUED

## Eigenvectors and eigenvalues

### Eigenvector

An **eigenvector** of an $n \times n$ matrix $A$ is a nonzero vector $\bold{x}$ such that $A \bold{x} = \lambda \bold{x}$ for some scalar $\lambda$. A scalar $\lambda$, possibly zero, is called an **eigenvalue** of $A$ if there is a nontrivial solution $\bold{x}$ of $A \bold{x} = \lambda \bold{x}$; such an $\bold{x}$ is an eigenvector corresponding to $\lambda$.

If$ $\bold{x}$ is an eigenvector of $A$ such that $A \bold{x} = \lambda \bold{x}$ for some scalar $\lambda$:

$$
\begin{aligned}
A \bold{x} &= \lambda \bold{x} \\
A \bold{x} - \lambda \bold{x} &= \bold{0} \\
(A - \lambda I) \bold{x} &= \bold{0}
\end{aligned}
$$

Thus, $\lambda$ is an eigenvalue of $A$ if and only if the equation $(A - \lambda I) \bold{x} = \bold{0}$ has a nontrivial solution.

### Eigenspace

The **eigenspace** of an $n \times n$ matrix $A$ corresponding to a scalar $\lambda$ is the solution set of the homogeneous equation $(A - \lambda I) \bold{x} = \bold{0}$. Therefore, the eigenspace is the null space of the matrix $A - \lambda I$, and is a subspace of $\R^n$. The eigenspace consists of the zero vector and all the eigenvectors corresponding to $\lambda$.

### Eigenvalues of a triangular matrix

The eigenvalues of a triangular matrix are the entries on its main diagonal. This is can be shown by considering a $3 \times 3$ upper triangular matrix $A$.

$$
A - \lambda I =
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
0      & a_{22} & a_{23} \\
0      & 0      & a_{33}
\end{bmatrix} -
\begin{bmatrix}
\lambda & 0       & 0      \\
0       & \lambda & 0      \\
0       & 0       & \lambda
\end{bmatrix} =
\begin{bmatrix}
a_{11} - \lambda & a_{12}            & a_{13} \\
0                & a_{22}  - \lambda & a_{23} \\
0                & 0                 & a_{33} - \lambda
\end{bmatrix}
$$

The scalar $\lambda$ is an eigenvalue of $A$ if and only if the equation $(A - \lambda I) \bold{x} = \bold{0}$ has a nontrivial solution, that is, if and only if the equation has a free variable.

Because of the zero entries in $A - \lambda I$, the equation has a free variable if and only if at least one of the entries on the main diagonal of $A - \lambda I$ is zero. This happens if and only if $\lambda$ is equal to one of the entries $a_{11}, a_{22}, a_{33}$, which are the entries on the main diagonal of $A$.
