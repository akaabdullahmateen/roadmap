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

The following tokens serve as delimiters in the grammar:

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