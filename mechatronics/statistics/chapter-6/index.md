# Probability

## Introduction

Probability of an event is a number that indicates how likely an event is to occur. Therefore, it is a measure of uncertainty or a measure of disbelief in a particular statement.

Uncertainty is an inherent part of statistical inference as inferences are based n a sample, and a sample being a small part of the larger population, contains incomplete population.

## Sets

A set is a well-defined collection of distinct objects.

The objects that are in a set are called *members* or *elements* of that set. If $x$ belongs to the set $A$, it is denoted as $x \in A$. If $x$ does not belong to the set $A$, it is denoted as $x \notin A$.

Conventionally, sets are denoted by uppercase Latin letters (such as $A,B,C$), and the elements are denoted by lowercase Latin letters (such as $a,b,c$). The elements are enclosed in a pair of curly braces.

$$
\begin{equation}
\tag{Set}
A = \lbrace 1,2,3,4,5 \rbrace
\end{equation}
$$

The number of a set $A$, denoted as $n(A)$ is the number of elements in $A$. A set with no elements is called an *empty set* or a *null set*, and is denoted as $\phi$. If a set contains only one element, it is called a *singleton set* or a *unit set*. A set can have finitely many element, or an infinite number of elements.

!!! note

    The set $\lbrace 0 \rbrace$ is not an empty set, rather it is a singleton set containing the element $0$.

A set may be described in two ways:

Roster notation
: The set is described by enumerating all of its elements. If the pattern of the sequence is apparent from the listed elements, an ellipsis can be used for brevity.

- $A = \lbrace 1,3,5,7,11 \rbrace$
- $A = \lbrace 1,2,3,\dots,1000 \rbrace$
- $A = \lbrace \dots,-2,-1,0,1,2,\dots \rbrace$

Set builder notation
: The set is defined by a predicate that dictates whether an object is an element of the set or not. The separator between the variable and the predicate can be a colon or a vertical bar.

- $A = \lbrace x : x > 0 \rbrace$
- $A = \lbrace x \mid x > 0 \rbrace$
- $A = \lbrace x \in \R : x > 0 \rbrace$

Two sets $A$ and $B$ have a *one-to-one correspondence* if each element of $A$ is mapped to one and only one element of $B$, and vice versa.

A set is *countably infinite* or *denumerable* if its element can be form a one-to-one correspondence with the set of positive integers (such as the set of all even numbers). A set is *uncountably infinite* or *non-denumerable* if its elements can not be enumerated (such as the set of all real numbers).

### Subsets

A set $A$ is a subset of the set $B$, denoted as $A \subset B$, if every element of $A$ is also an element of $B$. A set is a subset of itself, and the empty set is a subset of every set.

Two sets $A$ and $B$ are equal, denoted as $A = B$, if $A$ is a subset of $B$ and $B$ is a subset of $A$.

A set $A$ is a proper subset of the set $B$, if $A$ is a subset of $B$, but is not equal to $B$.

The set representing the entire space under consideration is called the *universal set*, and is denoted as $S$ or $\Omega$. All sets, under consideration, are subsets of the universal set.

A set $S$ with $n$ elements have $2^n$ subsets, including $S$ and $\phi$.

### Venn Diagrams

A Venn diagram represents the space $S$ as a rectangular region, in which, its subsets $A,B,C$, represented as circles, exist. The Venn diagram is used to represent the sets pictorially, and to verify the relationships between them.

### Operators on sets

#### Union

The union of two sets $A$ and $B$, denoted as $A \cup B$, is a set that contains all the elements that belong to either $A$ or $B$.

$$
\begin{equation}
\tag{Union}
A \cup B = \lbrace x \mid x \in A \text{ or } x \in B \rbrace
\end{equation}
$$

#### Intersection

The intersection of two sets $A$ and $B$, denoted as $A \cap B$, is a set that contains only the elements that belong to both $A$ and $B$.

$$
\begin{equation}
\tag{Intersection}
A \cap B = \lbrace x \mid x \in A \text{ and } x \in B \rbrace
\end{equation}
$$

The sets $A$ and $B$ are *mutually exclusive* or *disjoint*, if their intersection is the empty set; $A \cap B = \phi$. Conversely, two sets are *conjoint*, if their intersection is not the empty set.

#### Difference

The difference of two sets $A$ and $B$, denoted as $A - B$, is a set that contains only those elements that belong to $A$ but not to $B$.

$$
\begin{equation}
\tag{Difference}
A - B = \lbrace x \mid x \in A \text{ and } x \notin B \rbrace
\end{equation}
$$

If $A$ and $B$ are disjoint, then $A - B$ coincides with the set $A$.

#### Complement

The complement of a set $A$, denoted as $\overline{A}$, is the set that contains only those elements that belong to the universal set $S$ but not to $A$.

$$
\begin{equation}
\tag{Difference}
\overline{A} = \lbrace x \mid x \in S \text{ and } x \notin A \rbrace
\end{equation}
$$

### Algebra on sets

If $A,B,C$ are subsets of the universal set $S$:

| Law | Union form | Intersection form |
| - | - | - |
| Commutative law | $A \cup B = B \cup A$ | $A \cap B = B \cap A$ |
| Associative law | $(A \cup B) \cup C = A \cup (B \cup C)$ | $(A \cap B) \cap C = A \cap (B \cap C)$ |
| Distributive law | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ | $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ |
| Idempotent law | $A \cup A = A$ | $A \cap A = A$ |
| Identity law | $A \cup S = S$, $A \cup \phi = A$ | $A \cap S = A$, $A \cap \phi = \phi$ |
| Complement law | $A \cup \overline{A} = S$ | $A \cap \overline{A} = \phi$ |
| De Morgan's law | $\overline{A \cup B} = \overline{A} \cap \overline{B}$ | $\overline{A \cap B} = \overline{A} \cup \overline{B}$ |

### Partition of sets

The partition of a set $S$ is the subdivision of the set into non-empty subsets, called *cells*, that are disjoint and exhaustive. If a set $A$ is partitioned into sets $A_1, A_2, \dots, A_n$, then:

- $A_i \cap A_j = \phi$ where $i \neq j$
- $A_1 \cup A_2 \cup \dots \cup A_n = S$

### Class of sets

A class is a collection of sets that can be unambiguously defined by a property that its member sets share.

The set of all subsets of a set $A$, denoted as $\mathcal{P}(A)$ is called the *power set* of $A$, which includes the empty set $\phi$ and $A$ itself. Therefore, the power set is a class of sets.

### Cartesian product sets

The Cartesian product of sets $A$ and $B$, denoted as $A \times B$, is a set that contains all ordered pairs $(x,y)$ such that $x$ belongs to $A$ and $y$ belongs to $B$.

$$
\begin{equation}
\tag{Cartesian product}
A \times B = \lbrace (x,y) \mid x \in A \text{ and } y \in B \rbrace
\end{equation}
$$

The product of a set $A$ with itself is denoted as $A^2$. This concept of product of sets can be extended to any finite number of sets.

!!! example

    If $A = \lbrace H,T \rbrace$ and $B = \lbrace 1,2,3,4,5,6 \rbrace$, then the Cartesian product set is the collection of twelve ordered pairs:

    $$
    \begin{aligned}
    A \times B = \lbrace &(H,1);(H,2);(H,3);(H,4);(H,5);(H,6); \\
                         &(T,1);(T,2);(T,3);(T,4);(T,5);(T,6)\rbrace
    \end{aligned}
    $$

### Relation and function

A relation between two sets $A$ and $B$ is a collection of ordered pairs containing one element from each set. A relation is a subset of the Cartesian product.

The set of the first elements of these ordered pairs is called the *domain*, whereas, the set of the second elements is called the *range*.

!!! example

    If a binary relation is $F = \lbrace (1,4), (2,7), (3,12) \rbrace$, then its domain is $D = \lbrace 1,2,3 \rbrace$ and its range is $R = \lbrace 4,7,12 \rbrace$.

A function is a mapping from a set $A$ to a set $B$, denoted as $f : A \mapsto B$, such that each element $x$ of $A$ is mapped to one and only one element of $B$.

Therefore, a function is a binary relation that maps each element of the domain to a unique element of the range. Hence, a function is a binary relation in which the first elements are not repeated.

The variable $x$ that represents an element of the domain is called the *independent variable*, and the variable $y = f(x)$, representing an element of the range, is called the *dependent variable*.

The one-to-one or many-to-one correspondence functions are also called *single-valued functions*. A *multi-valued function* is a function where each element of the domain can map to multiple values of the range, such as the square root function.

A function whose range consists of numbers is called a *numerical function*. A function whose domain and range are subsets of real numbers is called a *real-valued function* of a real variable.

A function is defined to be an *even function* if for every $x$ in a specific range $f(-x) = f(x)$. Whereas, a function is said to be an *odd function* if for every $x$ in a specific range $f(-x) = - f(x)$.

## Random experiment

An experiment is a process which yields a set of data as result, called the *outcome*. A single performance of an experiment is called a *trial*. An experiment which produces different results, even though it is repeated a large number of times, under similar conditions is called a *random experiment*.

A random experiment has the following properties:

- The experiment can be repeated any number of times.
- The experiment always has two or more possible outcomes.
- The outcome of each repetition is unpredictable; it has some uncertainty.

!!! note

    Drawing a card from a shuffled deck of 52 playing cards is a random experiment. A deck of playing cards has 4 suits of 13 cards each. The four suits are diamond (red), hearts (red), clubs (black), and spades (black). The face values, called *denominations*, of the 13 cards in each suit are ace, 2, 3, $\dots$, 10, jack, queen, and king. The term *honor card* refers to the denominations ace, 10, jack, queen, and king. The *face cards* are jack, queen, and king.

### Sample space

The sample space, denoted as $S$, is a set of all possible outcomes of a random experiment. Each possible outcome is a member of the sample space, and is called a *sample point*.

A sample space that contains a finite number of sample points is called a *finite sample space*. A sample space that is either finite or if its sample points can be placed in a one-to-one correspondence with the positive integer, is called a *discrete sample space*. If a sample space is neither *finite* nor *discrete*, it is called a *continuous sample space*.

### Events

An event is a set of outcomes, therefore, it is a subset of the sample space. An event that contains exactly one sample point is called a *simple event*, whereas, an event that contains more than one sample point is called a *compound event*. A compound event is produced by the union of simple events. An event $A$ occurs when the outcome of a random experiment corresponds to an element of $A$.

If $S$ is the sample space, then the subset $S$ is also an event, and is called a *certain event* or *sure event*, because it always occurs. The empty set $\phi$ is also an event, and is called an *impossible event*, because it can never occur.

Mutually exclusive event
: Two events $A$ and $B$ of a single experiment are *mutually exclusive* or *disjoint*, if and only if they can not both occur at the same time, that is, $A \cap B = \phi$. Three or more events are mutually exclusive if each pair of these events is mutually exclusive.

Exhaustive event
: A group of events is *collectively exhaustive* if the union of mutually exclusive events is the entire sample space $S$. A group of mutually exclusive and exhaustive events is called a *partition* of the sample space.

Equally likely events
: Two events $A$ and $B$ are equally likely if their probabilities to occur are the same.

### Events and symbolic representations

The verbal statements of some events and their corresponding symbolic representations in set are listed below:

| Statement | Set notation |
| - | - |
| Event $A$ | $A \subset S$ |
| Event $A$ is impossible | $A = \phi$ |
| Event $A$ is sure | $A = S$ |
| Event $A$ does not occur | $\overline{A} = S - A$ |
| Event $A$ or event $\overline{A}$ | $A \cup \overline{A} = S$ |
| Event $A$ or event $B$ | $A \cup B$ |
| Event $A$ and event $B$ | $A \cap B$ |
| Events $A$ and $B$ are mutually exclusive | $A \cap B = \phi$ |
| Events $A$ and $B$ are exhaustive | $A \cup B = S$ |
| Event $B$ occurs when $A$ occurs | $A \subseteq B$ |
| Event $A$ occurs but $B$ does not occur | $A \cap \overline{B}$ |
| Event $B$ occurs given that $A$ has occurred | $B \mid A$ |

### Counting sample points

TO BE CONTINUED

## Definitions of probability

### Subjective or personalistic probability

## Laws of probability

## Conditional probability

## Independent and dependent events
