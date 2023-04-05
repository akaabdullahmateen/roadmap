# R language

<!-- omit in toc -->
## Table of contents

- [Introduction](#introduction)
- [Objects](#objects)
  - [Vectors](#vectors)
  - [Lists](#lists)
  - [Arrays](#arrays)
  - [Matrices](#matrices)
  - [Factors](#factors)
  - [Data frames](#data-frames)
- [Attributes](#attributes)
- [Lexical analysis](#lexical-analysis)
  - [Comments](#comments)
  - [Literals](#literals)
    - [Logical literals](#logical-literals)
    - [Numeric literals](#numeric-literals)
    - [Integer literals](#integer-literals)
    - [Complex literals](#complex-literals)
    - [String literals](#string-literals)
    - [Special constants](#special-constants)
- [Expressions](#expressions)
  - [Arithmetic operators](#arithmetic-operators)
- [Keyboard shortcuts](#keyboard-shortcuts)
- [EXTRA](#extra)

## Introduction

R is a system for statistical computation and graphics. It provides, among other things, a programming language, high level graphics, interfaces to other languages, and debugging facilities.

## Objects

An **object** is a specialized data structures provided by the R language to store data. There are no elementary data types in R, so all values are stored as R objects.

The data type of an R object can be seen through the `typeof()` function, which returns the underlying type of an R object.

In R, the language constructs, expressions, symbols, and functions are themselves objects, and can be manipulated in the same way as any other object.

### Vectors

A vector consists of an ordered collection of values of the same type. Single entities, such as `4.2`, are also vectors of length 1. There are six types of atomic vectors: *logical*, *integer*, *double*, *complex*, *character*, and *raw*.

### Lists

A list consists of an ordered collection of values of any type; the elements can be a mix of objects, structures, or even lists.

### Arrays

### Matrices

### Factors

### Data frames

## Attributes

## Lexical analysis

### Comments

A **comment** is an annotation in the R code that is ignored by the parser. Any text from a `#` character to the end of the line is considered a comment, unless the `#` character is inside a quoted string. R does not support multiline comments.

```r
# This is a comment
x <- 5 # This is also a comment
s <- "# This is not a comment"
```

### Literals

#### Logical literals
Logical literals represent the two Boolean values: True and False.

| Boolean value | Logical literals               |
| ------------- | ------------------------------ |
| True          | `TRUE`, `True`, `true`, `t`    |
| False         | `FALSE,` `False`, `false`, `f` |

#### Numeric literals

Numeric literals represent real numbers. Decimal numbers can optionally contain a decimal exponent part, and hexadecimal numbers can optionally contain a binary exponent part.

| Format               | Example    | Interpretation                             |
| -------------------- | ---------- | ------------------------------------------ |
| Decimal number       | `12.34`    | $12.34$                                    |
| Scientific notation  | `1.1e-2`   | $1.1\times10^{-2}$                         |
| Hexadecimal number   | `0xFF`     | $15\times16^1+15\times16^0$                |
| Binary exponent form | `0x4.1p-2` | $(4\times16^0+1\times16^{-1})\times2^{-2}$ |

#### Integer literals

Integer literals are created by adding the qualifier `L` at the end of a number. However, if the number is not a valid integer, a numeric value is created instead.

| Format              | Example  | Interpretation             |
| ------------------- | -------- | -------------------------- |
| Decimal number      | `123L`   | $123$                      |
| Scientific notation | `1.1e6L` | $1.1\times10^6$            |
| Hexadecimal number  | `0x2FL`  | $2\times16^1+15\times16^0$ |

!!! note

    The leading plus or minus sign is a unary operator, and is not considered part of the numeric or integer literal.

#### Complex literals

Complex literals represent pure imaginary numbers. They are created by adding `i` at the end of a number. Complex numbers of the form $a + b\iota$ are expressions rather than complex literals.

| Format                  | Example     | Interpretation |
| ----------------------- | ----------- | -------------- |
| Decimal number          | `12.34i`    | $12.34\iota$   |
| Scientific notation     | `1.123e-2i` | $0.01123\iota$ |
| Hexadecimal number      | `0x1FFi`    | $511\iota$     |
| Binary exponential form | `0xf.1p-4i` | $0.9414062i$   |

#### String literals

String literals are delimited by a pair of either single or double quotes. A null character `\0` is not allowed in a string literal; therefore, it terminates the string, and further characters are ignored.

| Delimiter    | Example           |
| ------------ | ----------------- |
| Single quote | `'Hello, World!'` |
| Double quote | `"Hello, World!"` |

#### Special constants

There are some special constants in R, which are reserved keywords with special meaning.

| Name          | Constant | Type    | Description                      |
| ------------- | -------- | ------- | -------------------------------- |
| NULL object   | `NULL`   | NULL    | Indicates empty NULL object      |
| Not Available | `NA`     | Logical | Indicates missing data values    |
| Infinity      | `Inf`    | Numeric | Indicates real positive infinity |
| Not-a-Number  | `NaN`    | Numeric | Indicates IEEE NaN               |

## Expressions

### Arithmetic operators

The following table lists the arithmetic operators in order of precedence (from highest to lower):

| Name           | Usage     |
| -------------- | --------- |
| Power          | `x ^ y`   |
| Unary minus    | `- x`     |
| Unary plus     | `+ x`     |
| Modulus        | `x %% y`  |
| Integer divide | `x %/% y` |
| Multiply       | `x * y`   |
| Divide         | `x / y`   |
| Add            | `x + y`   |
| Subtract       | `x - y`   |

---

## Keyboard shortcuts

| Command | Shortcut |
| - | - |
| Clear console | `Ctrl` + `L` |
| Comment out selected lines | `Ctrl` + `Shift` + `C` |

## EXTRA

A **symbol** is the name of an R object. Objects are referred to through these symbols.

---

An **expression** is an object that contains parsed but unevaluated R statements; an R *statement* is a syntactically correct collection of tokens. An object of type `expression` is only evaluated when explicitly passed to the `eval()` function.

---

A **function** (or more precisely, *function closure*) is an object that contains interrelated statements, which are only executed when the function is called. In R, functions have three basic components: a formal argument list, a body, and an environment.

Argument list
: The argument list is a comma-separated list of arguments. An argument can be a symbol, the special argument `...`, or a `symbol = default` construct. The construct `symbol = default` is used to specify a default value for an argument.

Body
: The body is a group of parsed R statements. It is usually a collection of statements in braces, but it can be a single statement, or something even more elementary, such as a symbol.

Environment
: The function's environment is the environment that was active when the function was created. Any symbols bound in that environment are *captured* and available to the function. This combination of the function code and the bindings in its environment is called a *function closure*.

When a function is called, a new environment called the *evaluation environment* is created, whose enclosure is the environment from the function closure. This new environment is initially populated with the unevaluated arguments to the function; as evaluation proceeds, local variables are created within it.

---

NULL is a special R object, that is used to indicate that an object is absent. The NULL object has no type and no modifiable properties. There is only one NULL object in R, to which all instances refer.

---

Builtin objects, together with special functions, contain the builtin functions of R. Builtin functions evaluate and then pass the arguments to the internal function, whereas, special functions pass the unevaluated arguments to the internal function.

---

Promise objects are part of R's lazy evaluation mechanism. They contain three slots: a value, an expression, and an environment.

Promise objects are created when a function is called. The expression passed as a formal argument, and the environment from which the function was called, are stored in the promise; no value is associated with the promise until the argument is accessed.

When the argument is accessed, the stored expression is evaluated in the stored environment, and the result is returned; this result is also stored by the promise as the value.

---

The dots `...` object are a type of pairlist that contain an arbitrary number of arguments passed to a function. A function that has dots `...` as a formal argument matches any passed argument, that do not match a formal argument, with the dots `...` argument.

---

An environment is an object that contains a *frame* and an *enclosure*. A frame is a set of symbol-value pairs, and an enclosure is a pointer to enclosing environment.

The value of a symbol is retrieved by first searching in the frame of the current environment. If no matching symbol is found, the symbol is searched in the frame of the enclosing environment. This process is repeated until the empty root environment is reached.

---

**Pairlists** are objects with an underlying linked list data structure. Each node in a pairlist has three slots: a CAR value (head of the list), a CDR value (remainder of the list), and a TAG value (text string). Pairlists are handled in exactly the same way as lists.

---

An **attribute** is a name-value pair attached to an R object for storing additional information. All elements except `NULL` can have attributes attached to them. These attributes are stored as a pairlist, where all elements are named.

---
