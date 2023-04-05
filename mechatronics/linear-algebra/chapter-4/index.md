# Vector space

<!-- omit in toc -->
## Table of contents

- [Field](#field)
- [Vector space](#vector-space-1)
- [Linear subspace](#linear-subspace)
- [Linear combination](#linear-combination)
- [Linear span](#linear-span)
- [TO BE CONTINUED !!!](#to-be-continued-)

## Field

A field is a set $F$ together with two binary operations called *addition* and *multiplication*, both of which behave similarly as they behave for real numbers, including the existence of an additive inverse and a multiplicative inverse.

## Vector space

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

## Linear subspace

A **linear subspace** of a vector space $V$ over a field $K$ is a subset $H$ of $V$ that is itself a vector space over $K$. It follows that a linear subspace $H$ of a vector space $V$ must satisfy the following properties:

- The zero vector of $V$ is in $H$.
- $H$ is closed under vector addition, that is, for each $\bold{u}$ and $\bold{v}$ in $H$, the sum $\bold{u} + \bold{v}$ is in $H$.
- $H$ is closed under scalar multiplication, that is, for each $\bold{v}$ in $H$ and each scalar $c$ in $K$, the vector $c \bold{v}$ is in $H$.

All vector spaces have two *trivial subspaces*:

- The *zero subspace* $\{\bold{0}\}$ consisting of the zero vector alone.
- The entire vector space itself.

## Linear combination

The **linear combination** of vectors $\bold{v}_1, \bold{v}_2, \dots, \bold{v}_n$ with scalars $a_1, a_2, \dots, a_n$ as coefficients is:

$$
\begin{equation}
\tag{Linear combination}
a_1 \bold{v}_1 + a_2 \bold{v}_2 + \dots + a_n \bold{v}_n
\end{equation}
$$

## Linear span

The **linear span** of a set $S$ of vectors, from a vector space $V$, is the set of all finite linear combinations of the vectors in $S$. It is characterized as the intersection of all linear subspaces of $V$ that contain $S$. Therefore, the linear span of a set of vectors is a linear subspace of $V$.

The linear span $H$ of a set $S$ is denoted as $\text{span}(S)$, and $H$ is called the *subspace spanned* by $S$, while $S$ is called the *spanning set* of $H$.

If $V$ is a vector space over the field $K$, and $S$ is the set $\{\bold{v}_1, \bold{v}_2, \dots, \bold{v}_n\}$ of vectors, it can be verified that the linear span $H$ of $S$ is a linear subspace of $V$.

- The zero vector of $V$ is in $W$.
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

## TO BE CONTINUED !!!