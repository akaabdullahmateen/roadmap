# Python

## Table of contents

- [Table of contents](#table-of-contents)
- [Introduction](#introduction)
  - [Implementation](#implementation)
  - [Python enhancement proposals](#python-enhancement-proposals)
  - [Zen of Python](#zen-of-python)
  - [Style guide for Python code](#style-guide-for-python-code)
- [Lexical analysis](#lexical-analysis)
  - [Line structure](#line-structure)
    - [Logical lines](#logical-lines)
    - [Physical lines](#physical-lines)
    - [Comments](#comments)
    - [Encoding declaration](#encoding-declaration)
    - [Explicit line joining](#explicit-line-joining)
    - [Implicit line joining](#implicit-line-joining)
    - [Blank lines](#blank-lines)
    - [Indentation](#indentation)
    - [Whitespace between tokens](#whitespace-between-tokens)
  - [Identifiers and keywords](#identifiers-and-keywords)
    - [Rules for identifiers](#rules-for-identifiers)
    - [Naming conventions](#naming-conventions)
    - [Keywords](#keywords)
    - [Soft keywords](#soft-keywords)
    - [Reserved classes of identifiers](#reserved-classes-of-identifiers)
  - [Literals](#literals)
    - [String and byte literals](#string-and-byte-literals)
    - [Escape sequences](#escape-sequences)
    - [String literal concatenation](#string-literal-concatenation)
    - [Formatted string literals](#formatted-string-literals)
    - [Numeric literals](#numeric-literals)
    - [Integer literals](#integer-literals)
    - [Floating-point literals](#floating-point-literals)
    - [Imaginary literals](#imaginary-literals)
  - [Operators](#operators)
  - [Delimiters](#delimiters)
- [Data model](#data-model)
  - [Objects, values, and types](#objects-values-and-types)
  - [Standard type hierarchy](#standard-type-hierarchy)
    - [None](#none)
    - [NotImplemented](#notimplemented)
    - [Ellipsis](#ellipsis)
    - [`numbers.Number`](#numbersnumber)
      - [`numbers.Integral`](#numbersintegral)
      - [`numbers.Real` (`float`)](#numbersreal-float)
      - [`numbers.Complex` (`complex`)](#numberscomplex-complex)
    - [Sequences](#sequences)

## Introduction

Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented, and functional programming.

### Implementation

The most widely used implementation of Python is CPython. It is the reference implementation written in C. It compiles Python programs into an intermediate bytecode which is then executed by by its virtual machine.

### Python enhancement proposals

Python's development is conducted largely through the Python Enhancement Proposals (PEP) process, which is the primary mechanism for proposing major new features, collecting community input on issues, and documenting Python design decisions.

### Zen of Python

The Zen of Python, PEP 20, is a collection of 19 guiding principles for writing computer programs that influence the design of the Python programming language. It is included as an Easter egg in the Python interpreter, where it can be displayed by entering `import this`.

Beautiful is better than ugly.<br>
Explicit is better than implicit.<br>
Simple is better than complex.<br>
Complex is better than complicated.<br>
Flat is better than nested.<br>
Sparse is better than dense.<br>
Readability counts.<br>
Special cases aren't special enough to break the rules.<br>
Although practicality beats purity.<br>
Errors should never pass silently.<br>
Unless explicitly silenced.<br>
In the face of ambiguity, refuse the temptation to guess.<br>
There should be one - and preferably only one - obvious way to do it.<br>
Although that way may not be obvious at first unless you're Dutch.<br>
Now is better than never.<br>
Although never is often better than right now.<br>
If the implementation is hard to explain, it's a bad idea.<br>
If the implementation is easy to explain, it may be a good idea.<br>
Namespaces are one honking great idea - let's do more of those!<br>

### Style guide for Python code

TODO: PEP 8 - to be completed

## Lexical analysis

### Line structure

A Python program is divided into a number of logical lines.

#### Logical lines

A logical line is constructed from one or more physical lines by following the explicit or implicit line joining rules. Statements can not cross logical line boundaries except where allowed by syntax, such as between statements in compound statements.

#### Physical lines

A physical line is a sequence of characters terminated by an end-of-line sequence, such as Unix-form LF, Windows-form CR LF, and Macintosh-form CR. The end of input also serves as an implicit terminator for the final physical line.

#### Comments

A comment starts with a hash character `#` that is not part of a string literal, and ends at the end of the physical line. A comment signifies the end of the logical line unless the implicit line joining rules are invoked. Comments are ignored by the syntax. Python does not support multiline comments, however, they can be emulated by a pair of triple quotation marks.

#### Encoding declaration

If a comment in the first or second line of the Python script matches the regular expression `coding[=:]\s*([-\w.]+)`, this comment is processed as an encoding declaration. The recommended form of an encoding expression is:

```py
# -*- coding: <encoding-name> -*-
```

If no encoding declaration is found, the default encoding is UTF-8. The encoding is used for all lexical analysis, including string literals, comments, and identifiers.

#### Explicit line joining

Two or more physical lines may be joined into a single logical line using the backslash character `\`. When a physical line ends in a backslash that is not part of a string literal or comment, it is joined with the following line forming a single logical line, deleting the backslash and the following end-of-line character.

```py
if 1900 < year < 2100 and 1 <= month <= 12 \
    and 1 <= day <= 31 and 0 <= hour < 24 \
    and 0 <= minute < 60 and 0 <= second < 60: # Looks like a valid date
return 1
```

A line ending in a backslash cannot carry a comment. A backslash does not continue a comment. A backslash does not continue any token except for string literals. A backslash is illegal elsewhere on a line outside a string literal.

#### Implicit line joining

Triple-quoted strings or expressions in parenthesis, square brackets, or curly braces can be split over more than one physical line without using backslashes.

```py
month_names = ['January', 'February', 'March',     # These are the
               'April',   'May',      'June',      # English names
               'July',    'August',   'September', # for the months
               'October', 'November', 'December']  # of the year
```

Implicitly joined lines can carry comments, however, in the case of triple-quoted strings, they cannot carry comments. The indentation of the continued lines is not important. Black continuation lines are allowed.

#### Blank lines

A logical line that contains only spaces, tabs, formfeeds, and possibly comments, is ignored. During interactive input of statements, handling of a blank line may differ depending on the implementation of the read-eval-print loop. In the standard interactive interpreter, an entirely blank line, that is one containing not even whitespace or a comment, terminates a multiline statement.

#### Indentation

Leading whitespace (spaces and tabs) at the beginning of a logical line is used to compute the indentation level of the line, which in turn is used to determine the grouping of statements.

Tabs are replaced by spaces. The total number of spaces preceding the first non-blank character then determines the line's indentation. Indentation cannot be split over multiple lines using backslashes; the whitespace up to the first backslash determines the indentation.

Indentation is rejected as inconsistent if a source file mixes tabs and spaces in a way that makes the meaning dependent on the worth of a tab in spaces; a `TabError` is raised in that case.

#### Whitespace between tokens

Except at the beginning of a logical line or in string literals, the whitespace characters (space, tab, or formfeed) can be used interchangeably to separate tokens. Whitespace is needed between tokens only if their concatenation could otherwise be interpreted as a different token.

### Identifiers and keywords

An identifier is a user-defined name given to identities such as class, functions, variables, modules, or any other object in Python.

#### Rules for identifiers

An identifier can include lowercase letters (a-z), uppercase letters (A-Z), digits (0-9), and underscore (`_`). Identifiers cannot begin with a digit or contain only digits. Special characters are not allowed in identifiers. There is no restriction on the length of identifiers. Identifiers are case-sensitive.

#### Naming conventions

TODO: Google Python Style GUide

#### Keywords

Keywords are reserved words and cannot be used as an ordinary identifier. They must be spelled exactly as written below:

```py
False    await    else     import   pass
None     break    except   in       raise
True     class    finally  is       return
and      continue for      lambda   try
as       def      from     nonlocal while
assert   del      global   not      with
async    elif     if       or       yield
```

#### Soft keywords

Soft keywords are identifiers that are only reserved in specific contexts. These are `match`,` case`, `type`, and `_`. The identifiers `match`, `case`, and `_` are used in the `match` statement. The identifier `type` is used in the `type` statement.

#### Reserved classes of identifiers

Certain classes of identifiers (besides keywords) have special meaning. These classes are identified by the pattern of leading and trailing underscore characters.

| Pattern | Description |
| - | - |
| `_*` | Names not imported by `from module import *` |
| `_` | Denotes a wildcard in a `match` statement. Separately, the interactive interpreter makes the result of the last evaluation available in the variable `_`, and is stored in the `builtins` module. It is also commonly used for unused variables. |
| `__*__` | System-defined names, informally known as dunder names. These names are defined by the interpreter and its implementations, including the standard library. |
| `__*` | Class private names. Names in this category, when used within the context of a class definition, are rewritten to use a mangled form to help avoid name clashes between private attributes of base and derived classes. |

### Literals

Literals are notations for constant values of some builtin type.

#### String and byte literals

#### Escape sequences

#### String literal concatenation

#### Formatted string literals

#### Numeric literals

#### Integer literals

#### Floating-point literals

#### Imaginary literals

### Operators

Operators are special symbols, combinations of symbols, or keywords that designate some type of computation. The following is a list of operators:

```py
+        -        *        **       /        //       % 
<<       >>       &        |        ^        ~        :=
<        >        <=       >=       ==       !=       @
```
### Delimiters

A delimiter is a sequence of one or more characters that specifies the boundary between various sections in plain text or other data streams. The following tokens serve as delimiters in the grammar:

```py
(        )        [        ]        {        }        ->
,        :        .        ;        @        =        @=
+=       -=       *=       /=       //=      %=
&=       |=       ^=       >>=      <<=      **=
```

The period can also occur in floating-point and imaginary literals. A sequence of three periods has a special meaning as an ellipsis literal. The second half of the list, the augmented assignment operators, serve lexically as delimiters, but also perform an operation.

The following printing ASCII characters have special meaning as part of other tokens or are otherwise significant to the lexical analyzer:

```py
'        "        #        \
```

The following printing ASCII characters are not used in Python. Their occurrence outside string literals and comments is an unconditional error:

```py
$        ?        `
```

## Data model

### Objects, values, and types

Objects are Python's abstraction for data. All data in a Python program is represented by objects or by relations between objects. Every object has an identity, a type, and a value.

An object's identity never changes once it has been created. However, multiple names can reference the same underlying object, thereby sharing the same identity. This happens because Python caches immutable objects for increased performance and memory efficiency. The `is` operator compares the identity of two objects. The `id()` function returns an integer representing its identity; in CPython, this is the memory address.

An object's type determines the operations that the object supports, and also defines the possible values for objects of that type. The `type()` function returns an object's type, which is an object itself. Like an object's identity, an object's type is also immutable.

The value of some object can change. Objects whose value can change are said to be mutable; objects whose value is unchangeable once they are created are called immutable. The value of an immutable container object that contains a reference to a mutable object can change when the latter's value is changed, however, the container is still considered immutable, because the collection of objects it contains cannot be changed. An object's immutability is determined by its type.

Objects are never explicitly destroyed, however, when they become unreachable, they may be garbage-collected. An implementation is allowed to postpone garbage collection or omit it altogether. CPython currently uses a reference-counting scheme with optional delayed detection of cyclically linked garbage, which collects most objects as soon as they become unreachable, but is not guaranteed to collect garbage containing circular references. Note that catching an exception with a `try...except` statement may keep objects alive.

Some objects contain references to external resources such as open files or windows. But since garbage collection is not guaranteed to happen, such objects also provide an explicit way to release the external resource, usually with a `close()` method. Programs are strongly recommended to explicitly close such objects. The `try...finally` statement and the `with` statement provide convenient ways to do this.

Some objects contain references to other objects; these are called containers. Examples of containers are tuples, lists, and dictionaries. The references are part of a container's value.

### Standard type hierarchy

Below is a list of types that are built into Python. Extension modules and future versions of Python can define additional types.

#### None

This type has a single value. There is a single object with this value. This object is accessed through the builtin name `None`. It is used to signify the absence of a value in many situations, such as it is returned from functions that do not explicitly return anything. Its truth value is false.

#### NotImplemented

This type has a single value. There is a single object with this value. This object is accessed through the built-in name `NotImplemented`. Numeric methods and rich comparison methods should return this value if they do not implement the operation for the operands provided. The interpreter will then try the reflected operation, or some other fallback, depending on the operator.) It should not be evaluated in a boolean context.

#### Ellipsis

This type has a single value. There is a single object with this value. This object is accessed through the literal `...` or the built-in name `Ellipsis`. Its truth value is true.

#### `numbers.Number`

These are created by numeric literals and returned as results by arithmetic operators and arithmetic builtin functions. Numeric objects are immutable. The string representations of the numeric classes, computed by `__repr__()` and `__str__()`, have the following properties:

- They are valid numeric literals; when passed to their class constructor, produce an object having the value of the original number.
- The representation is in base 10, whenever possible.
- Leading zeroes are not shown, possibly except when there is a single zero before a decimal point.
- Trailing zeroes are not shown, possibly except when there is a single zero after a decimal point.
- A sign is shown only when the number is negative.

Python distinguishes between integers, floating-point numbers, and complex numbers:

##### `numbers.Integral`

These represent elements from the mathematical set of integers (positive and negative). There are two types of integers:

Integers (`int`)
: These represent numbers in an unlimited range, subject to available (virtual) memory only. For the purpose of shift and mask operations, a binary representation is assumed, and negative numbers are represented in a variant of 2's complement which gives the illusion of an infinite string of sign bits extended to the left.

Boolean (`bool`)
: These represent the truth values. The two objects representing the values `False` and `True` are the only Boolean objects. The Boolean type is a subtype of the integer type, and Boolean values behave like the values 0 and 1 respectively, in almost all contexts; the exception being that when converted to a string, the strings `"False"` and `"True"` are returned, respectively.

##### `numbers.Real` (`float`)

These represent machine-level double-precision floating-point numbers. The machine architecture and Python implementation decides the accept range and handling of overflow. Python does not support single-precision floating-point numbers; the savings in processor and memory usage that are usually the reason for using these are dwarfed by the overhead of using objects in Python, so there is no reason to complicate the language with two kinds of floating-point numbers.

##### `numbers.Complex` (`complex`)

These represent complex numbers as a pair of machine-level double-precision floating-point numbers. The real and imaginary parts of a complex number `z` can be retrieved through the read-only attributes `z.real` and `z.imag`.

#### Sequences

