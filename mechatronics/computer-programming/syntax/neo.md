# Python language reference

<!-- omit in toc -->
## Table of contents

- [Lexical analysis](#lexical-analysis)
  - [Comments](#comments)
  - [Line structure](#line-structure)
  - [Indentation](#indentation)
  - [Grammar](#grammar)
    - [Identifiers](#identifiers)
    - [Keywords](#keywords)
    - [Operators](#operators)
    - [Delimiters](#delimiters)
  - [Literals](#literals)
- [Strings](#strings)
  - [String literals](#string-literals)
  - [Raw strings](#raw-strings)
  - [Byte literals](#byte-literals)
  - [Formatted strings](#formatted-strings)
    - [String conversion](#string-conversion)
    - [Debugging](#debugging)
    - [Formatting](#formatting)
  - [String literal concatenation](#string-literal-concatenation)
- [Format specification](#format-specification)
  - [Alignment](#alignment)
  - [Sign](#sign)
  - [Alternative form](#alternative-form)
- [Expressions](#expressions)
  - [Arithmetic conversions](#arithmetic-conversions)
- [Built-in functions](#built-in-functions)
  - [abs()](#abs)
  - [ascii()](#ascii)
  - [bin()](#bin)
  - [bool()](#bool)
  - [bytearray()](#bytearray)
  - [bytes()](#bytes)
  - [callable()](#callable)
  - [chr()](#chr)
  - [complex()](#complex)
  - [dict()](#dict)
  - [divmod()](#divmod)
  - [enumerate()](#enumerate)
  - [eval()](#eval)
  - [exec()](#exec)
  - [filter()](#filter)
  - [float()](#float)
  - [format()](#format)
  - [getattr()](#getattr)
  - [globals()](#globals)
  - [hasattr()](#hasattr)
  - [hash()](#hash)
  - [help()](#help)
  - [hex()](#hex)
  - [id()](#id)
  - [input()](#input)
  - [int()](#int)
  - [isinstance()](#isinstance)
  - [issubclass()](#issubclass)
  - [iter()](#iter)
  - [len()](#len)
  - [list()](#list)
  - [locals()](#locals)
  - [map()](#map)
- [MISCELLANEOUS](#miscellaneous)

## Lexical analysis

### Comments

A comment starts with a hash character `#` and continues till the end of the physical line. Python does not support multiline comments, but they can be emulated by wrapping the text inside a pair of triple quotes.

```py
# Single line comment

"""
Multiline
comment
"""
```

### Line structure

A **physical line** is a sequence of characters terminated by an end-of-line sequence (CR, LF, or CRLF). A **logical line** is constructed from one or more physical lines by following explicit or implicit line joining rules.

Physical lines can be explicitly joined with a backslash character, as long as the individual tokens are kept intact. Implicit line joining occurs when the statement syntax allows splitting over multiple physical lines, without the need for backslashes.

```py
# Explicit line joining
1 + 2 + \
3 + 4

# Implicit line joining
"""Long long long
   long long line"""
```

### Indentation

Leading whitespace characters (spaces and tabs) are used to compute the indentation level of the line, which determines the grouping of statements.

- Statements at the global indentation level must have zero leading spaces.
- Statements returning to a lower indentation level must have the same number of spaces as any other outer indentation level.
- If tabs are mixed with spaces in a way that requires knowing the worth of a tab in spaces, indentation is rejected as inconsistent, and `TabError` is raised.

### Grammar

#### Identifiers

An identifier is a name (possibly bound to an object). If an identifier is bound to an object, evaluation of the identifier yields the object. If an identifier is not bound to an object, an attempt to evaluate it raises a `NameError` exception.

An identifiers is case-sensitive and unlimited in length. It can include Latin letters, underscores, and (except for the first character) digits.

Certain forms of identifiers, besides keywords, have special meaning and are reserved:

| Form    | Description                                                             |
| ------- | ----------------------------------------------------------------------- |
| `_*`    | Names that are not imported by the `from module import *` statement.    |
| `_`     | In a `case` pattern within a `match` statement, `_` denotes a wildcard. |
| `__*__` | Names defined by the interpreter and implementation .                   |
| `__*`   | Private names of a class (private names are mangled).                   |

Private name mangling
: An identifier of the form `__*` inside a class definition, is a *private name* of that class. Private names are mangled to prevent name clashes between base and derived classes. For example, a private name `__spam` inside a class `__Ham` will be mangled to `_Ham__spam`.

#### Keywords

The following identifiers are reserved as keywords of the language, and can not be used as ordinary identifiers.

```py
and         continue    finally     is          raise
as          def         for         lambda      return
assert      del         from        None        True
async       elif        global      nonlocal    try
await       else        if          not         while
break       except      import      or          with
class       False       in          pass        yield
```

Some identifiers are only reserved under specific contexts, and can be used as identifier names in other contexts.

- `match`
- `case`
- `_`

#### Operators

The following tokens act as operators in the grammar.

```py
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=
```

#### Delimiters

The following tokens serve as delimiters in the grammar:

```py
(       )       [       ]       {       }
,       :       .       ;       @       =       ->
+=      -=      *=      /=      //=     %=      @=
&=      |=      ^=      >>=     <<=     **=
```

The following printed ASCII characters have special meaning as part of other tokens or are otherwise significant to the lexical parser:

```py
'       "       #       \
```

The following printed ASCII characters are not used in Python. Their occurrence outside string literals and comments is an error:

```py
$       ?       `
```

### Literals

A literal represents a constant value of a built-in type. The object underlying a literal is immutable. Python has three broad types of literals: string, byte, and numeric literals. The numeric literals are further composed of three types: integer, floating point, and imaginary literals.

## Strings

### String literals

String literals represent sequence of textual characters from human languages. Their internal representation is dependent on the encoding format. These strings of characters are enclosed in either a pair of single quotes, double quotes, triple single quotes, or triple double quotes.

```py
'String enclosed in single quotes'
"String enclosed in double quotes"
"""String enclosed in triple quotes"""
```

Triple quoted strings can include the newline character without escaping it. Therefore, multiline text can be created using triple quoted strings.

```py
"""This string includes the newline
   and the whitespaces at the start of this line"""
# This string includes the newline
#    and the whitespaces at the start of this line
```

### Raw strings

String literals can be prefixed with the character `r` or `R` to indicate a *raw string*. Raw strings treat backslashes are literal characters, therefore escape sequences are not treated specially.

```py
r"This backslash escape does not work in raw strings\\"
# This backslash escape does not work in raw strings\\
```

### Byte literals

String literals can be prefixed with the character `b` or `B` to indicate a *byte literal*. Byte literals represent sequence of raw bytes, which are 8 bit unsigned values. These bytes can be written as ASCII characters (if their value is less than 128), or as hexadecimal escapes (if their value is 128 or greater).

```py
b"Hello"
# Hello

b"\x48\x65\x6c\x6c\x6f"
# Hello
```

Bytes written as ASCII characters or hexadecimal escapes, are both represented internally the same. Both forms are printed as ASCII characters if the character's value is less than 128 and as hexadecimal escapes otherwise.

### Formatted strings

Strings literals can be prefixed with the character `f` or `F` to indicate a *formatted string*. Formatted string allows including Python expressions as `{expression}` inside the string.

```py
comedian = Monty Python

f"The Python language is named after {comedian}"
# The Python language is named after Monty Python
```

#### String conversion

The expression can be followed by an exclamation mark `!` and then a conversion field. The conversion field decides which function is called to convert the value to a string, if it is not already a string.

| Option | Description                                                   |
| ------ | ------------------------------------------------------------- |
| `s`    | Converts the value to a string by calling `str()` function.   |
| `r`    | Converts the value to a string by calling `repr()` function.  |
| `a`    | Converts the value to a string by calling `ascii()` function. |

```py
text = "The Greek letter ɑ is Monty's favorite"

f"{text!s}"
# The Greek letter ɑ is Monty's favorite

f"{text!r}"
# The Greek letter ɑ is Monty\'s favorite

f"{text!a}"
# The Greek letter \\u0251 is Monty\'s favorite
```

#### Debugging

The expression can be followed by an equal sign `=` to display both the expression text and its value after evaluation.

```py
comedian = Monty Python

f"The Python language is named after {comedian=}"
# The Python language is named after comedian=Monty Python
```

#### Formatting

The expression can be followed by a colon symbol `:` and then a format specifier. The format specifier defines how individual values are presented. The syntax of the format specifier is described in the Format Specification Mini-language.

```py
number = 12.3456

f"The number {number} is approximately {number:.2f}"
# The number 12.3456 is approximately 12.35"
```

### String literal concatenation

String concatenation refers to joining multiple strings into a single string. The individual strings are allowed to have different quoting conventions. There are various ways to concatenate strings:

- Adjacent string literals with only whitespaces in between are concatenated.
- The operator `+` can be used to concatenate the strings on its either sides.
- A backslash can be added at the end of a line to ignore the newline, and allow the string to continue over the next physical line.

```py
"This is a single "
"long string"
# This is a single long string

"This left side is concatenated" +
"to the right side"
# This left side is concatenated to the right side.

"This string will not include \
the backslash or newline characters"
# This string will not include the backslash or newline characters
```

## Format specification

```bnf
format_spec     ::= [[fill]align][sign]["z"]["#"]["0"][width][grouping_option]["." precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "^" | "="
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```

### Alignment

The *align* option forces the alignment of the field within the available space (controlled by the *width* option). If a valid *align* option is specified, it can preceded by a *fill* character, which is used as the character for padding; the default is space.

| Option | Description                                                        |
| ------ | ------------------------------------------------------------------ |
| `<`    | Forces the field to be left aligned within the available space.    |
| `>`    | Forces the field to be right aligned within the available space.   |
| `^`    | Forces the field to be center aligned within the available space.  |
| `=`    | Forces the padding to placed after the sign but before the digits. |

```py
f"This number is left aligned: {12.34:<010}"
# This number is left aligned: 12.3400000

f"This number is right aligned: {12.34:>010}"
# This number is right aligned: 0000012.34

f"This number is center aligned: {12.34:^010}"
# This number is center aligned: 0012.34000

f"This number is specially aligned: {12.34:=+010}"
# This number is specially aligned: +000012.34
```

### Sign

The *sign* option controls whether a sign should be used for a number.

| Option                      | Sign for positive numbers | Sign for negative numbers |
| --------------------------- | ------------------------- | ------------------------- |
| `+`                         | Plus sign `+`             | Minus sign `-`            |
| `-`                         | None                      | Minus sign `-`            |
| <code>&nbsp;</code> (space) | Leading space             | Minus sign `-`            |

### Alternative form

The hash *#* option causes the alternative form to be used for the conversion. For integers, when binary, octal, or hexadecimal output is used, this option adds the prefixes `0b`, `0o`, and `0x` respectively to the output value.

```py
number = 95

f"{number:#x}"
# 0x5f

f"{number:#o}"
# 0o137

f"{number:#b}"
# 0b1011111
```

For floating point and complex numbers, this options causes the value to always contain a decimal point character, even if no digits follow it. In addition, for `g` conversions, trailing zeroes are not removed from the result.

## Expressions

### Arithmetic conversions

Numeric operands of an arithmetic operator are converted to a common type according to the following rules:

- If either operand is a complex number, the other is converted to the complex type.
- Otherwise, if either operand is a floating point number, the other is converted to the floating point type.
- Otherwise, both must be integers and no conversion is necessary.

## Built-in functions

### abs()

```py
def abs(x)
```

Returns the absolute value of a number. If the argument is a complex number, its magnitude is returned.

### ascii()

```py
def ascii(object)
```

Returns a string representation of the object, but escapes the non-ASCII characters using `\x`, `\u`, or `\U` escapes.

### bin()

```py
def bin(x)
```

Returns the binary representation of an integer. The return value is a binary string prefixed with `0b`. If the argument is not an integer, it has to define an `__index()` method that returns an integer.

### bool()

```py
class bool(x=False)
```

Returns a Boolean value corresponding to the argument truthfulness. If the argument is false or omitted, it returns `False`, and `True` otherwise. The class `bool` is a subclass of class `int`, and can not be subclassed.

### bytearray()

```py
class bytearray(source=b"")
class bytearray(source=b"", encoding)
class bytearray(source=b"", encoding, errors)
```

Constructs a mutable array of bytes. Without any argument, an empty array is created. The array is initialized differently based on the given `source` argument:

- If `source` is a string, the `encoding` parameter must also be provided. The `bytearray()` then converts the string to bytes using `str.encode()`.
- If `source` is an integer, the `bytearray` will have that size and will be initialized with null bytes.
- If `source` is an iterable, it must be an iterable of integers in the range $0 \leq x < 256$, which are used as the initial contents of the array.

### bytes()

```py
class bytes(source=b"")
class bytes(source=b"", encoding)
class bytes(source=b"", encoding, errors)
```

Constructs an immutable array of bytes. The `bytes` class is an immutable version of the `bytearray` class. The array is initialized differently based on the given `source` argument:

- If `source` is a string, the `encoding` parameter must also be provided. The `bytearray()` then converts the string to bytes using `str.encode()`.
- If `source` is an integer, the `bytearray` will have that size and will be initialized with null bytes.
- If `source` is an iterable, it must be an iterable of integers in the range $0 \leq x < 256$, which are used as the initial contents of the array.

### callable()

```py
def callable(object)
```

Returns a Boolean value indicating whether the given object appears callable. If it returns `True`, it is still possible that a call fails, but if returns `False`, calling the object will never succeed.

### chr()

```py
def chr(i)
```

Returns a string representing the character whose Unicode code point is the integer `i`. The integer argument must be in range $0 \leq i \leq 1,114,111$.

### complex()

```py
class complex(real=0, imag=0)
class complex(string)
```

Creates a complex number from a real part and an optional imaginary part, with the value $\text{real} + \text{imag} \times j$. The complex number can also be created from a string representing the complex number. If a string argument is given, the string must not contain whitespace around the central `+` or `-` operator, and `j` must be used as the imaginary unit.

### dict()

```py
class dict(**kwargs)
class dict(mapping, **kwargs)
class dict(iterable, **kwargs)
```

Creates a new dictionary. TODO: SEE `dict` FOR MORE DETAILS.

### divmod()

```py
def divmod(a, b)
```

Takes two non-complex numbers as arguments, and returns the tuple `(a // b, a % b)`. The returned tuple contains the quotient and remainder product from the integer division of the arguments.

### enumerate()

```py
def enumerate(iterable, start=0)
```

Returns an enumerate object, which yields pairs containing a count (from `start`, which defaults to zero) and a values yielded by the iterable argument.

### eval()

```py
def eval(expression, globals=None, locals=None)
```

Evaluates the given source in the context of the given globals and locals. The source `expression` must be a string representing a Python expression, or a code object as returned by `compile()`. In either case, the value of the `expression` after a successful evaluation is returned.

If the `globals` and `locals` arguments are omitted, the code is executed in the current global and local namespaces. If only `globals` is given, `locals` defaults to it.

### exec()

```py
def exec(object, globals=None, locals=None)
```

Executes the given source in the context of the given globals and locals. The source `object` must be a string representing one or more Python statements, or a code object as returned by `compile()`. In either case, `None` is returned.

If the `globals` and `locals` arguments are omitted, the code is executed in the current global and local namespaces. If only `globals` is given, `locals` defaults to it.

### filter()

```py
def filter(function, iterable)
```

Returns an iterator yielding those items of the iterable for which the given function is true. If the `function` argument is `None`, returns the items that are true.

### float()

```py
class float(x=0.0)
```

Converts a string or a number to a floating point number. If the argument is a string, the string must represent a valid floating point number, or be either `"Infinity"`, `"inf"`, or `"nan"`.

### format()

```py
def format(value, format_spec="")
```

Converts the value to a formatted representation controlled by the `format_spec` argument. The `format_spec` argument is expressed in the Format Specification Mini-language. If omitted, `format()` simply converts the value to a string.

### getattr()

```py
def getattr(object, name)
def getattr(object, name, default)
```

Returns the value of the named attribute of the object, which is equivalent to `object.name` except that the `name` argument is a string. When the `default` argument is given, it is returned when the attribute does not exist; without it, an `AttributeError` exception is raised in that case.

### globals()

```py
def globals()
```

Returns the dictionary containing the global variables in the current scope. For code within functions, this is determined when the function is defined and remains the same regardless of where the function is called.

### hasattr()

```py
def hasattr(object, name)
```

Returns a Boolean value indicating whether the object has an attribute with the given name; the attribute `name` is given as a string. This is done by calling `getattr(object, name)` and catching `AttributeError`.

### hash()

```py
def hash(object)
```

Returns the hash value of the object, if it has one. Two values that compare equal have the same hash value, even if they are of different types.

### help()

```py
def help()
def help(request)
```

Invokes the built-in help system, intended for interactive use. If no argument is given, the interactive help system starts on the interpreter console. If the argument is a string, representing the name of a module, function, class, method, or keyword, a help page is printed for that topic.

### hex()

```py
def hex(x)
```

Converts an integer to a lowercase hexadecimal string prefixed with `0x`. If the argument is not an integer, it must define an `__index()__` method that returns an integer.

### id()

```py
def id(object)
```

Returns the identity of an object. The identity is an integer that is guaranteed to be unique for simultaneously existing objects. CPython uses the object's memory address as its identity.

### input()

```py
def input()
def input(prompt)
```

Reads a string from the standard input, strips its trailing newline, and returns the stripped string. If the prompt string is given, it is printed to the standard output without a trailing newline, before reading the input string. If EOF is read, `EOFERROR` is raised.

### int()

```py
class int(x=0)
class int(x, base=10)
```

Converts a number or a string to an integer, or return `0` if no arguments are given. If a floating point number is given, it is truncated towards zero, that is, positive numbers are floored and negative numbers are ceiled.

If `x` is not a number or if base is given, then `x` must be a string, bytes, or bytearray instance representing an integer literal in the given base. If `x` is a string:

- The string can be preceded by `+` or `-` sign with no space in between.
- The string can have leading zeroes.
- The string can have single underscores interspersed between digits.
- The string can be surrounded by leading and trailing whitespace characters.

The default base is 10, although the allowed bases are 0 and 2 through 36. If base is 0, the actual base is determined as 2, 8, 10, or 16 based on the prefix, and leading zeroes are disallowed. For other bases, the prefixes are optional.

### isinstance()

```py
def isinstance(object, classinfo)
```

Returns a Boolean value indicating whether the object is an instance of the given class or a subclass thereof. The `classinfo` can be a tuple of type objects, in which case, the function returns `True`, if the object is an instance of any entry in `classinfo`.

### issubclass()

```py
def issubclass(class, classinfo)
```

Returns a Boolean value indicating whether the class is a direct, indirect, or virtual subclass of `classinfo`; a class is considered a subclass of itself. The `classinfo` can be a tuple of class objects, in which case, the function returns `True`, if the class is a subclass of any entry in `classinfo`.

### iter()

```py
def iter(object)
def iter(object, sentinel)
```

Returns an iterator from the given object. In the first form, the given object must supply its own iterator, or be a sequence.

In the second form, the given object must be a callable object. The callable object is called until it returns the sentinel. Until then, it returns the value retrieved.

### len()

```py
def len(s)
```

Returns the number of items in the object. The argument can be a sequence (such as a string, bytes, tuple, list, or range), or a collection (such as a dictionary, set, or frozen set).

### list()

```py
class list
class list(iterable)
```

Creates an empty list, if no arguments are given, or a list initialized from values yielded from the iterator, if an argument is given.

### locals()

```py
def locals()
```

Returns a dictionary containing the local variables in the current scope. Free variables are returned by `locals()` when it is called in function blocks, but not in class blocks.

### map()

```py
def map(function, iterable, *iterables)
```

To be continued!

<!-- Left out due to being unnecessary for the moment -->
<!--
aiter()
all()
anext()
any()
breakpoint()
@classmethod
compile()
delattr()
dir()
frozenset()
-->

---

## MISCELLANEOUS

- print() built-in function
  - print function will advance to the next line by default
  - sep and end parameters of print()
- python is case sensitive
- whitespace is mostly irrelevant except for indentation
- "5+5" is a string, while 5+5 is a mathematical expression
- repeated strings using string * 10 method
- concatenation using + and , inside print()
- operator , automatically inserts a space between its operands
- escape sequences, table of escape sequences
- data types, strings + numbers
- variables, assignment operator =
    - variable types are inferred
    - lhs = variable name, constants are not allowed
    - rhs = expressions or literals
- rules for naming variables or identifiers:
    - digits are not allowed as first characters, only a-z, A-Z, and underscore _
    - rest of the characters can be a-z, A-Z, underscore, and 0-9
    - names are case sensitive
  - use descriptive names for variables
- reserved words known as keywords that can not be used as names for variables
- list of keywords can be shown in program using:
    ```py
    import keyword
    keyword.kwlist()
    ```
- variables can be reassigned to new values
- list of mathematical operators
  - addition +
  - subtraction -
  - multiplication *
  - division /
  - modulus %
  - exponent **
  - floor division //
- augmented assignment: x+=5 instead of x = x + 5
- input from user with input() function
- eval() function to taking numeric input
- precedence of mathematical operators
  - parenthesis () (highest)
  - exponent **
  - division /, floor division //, modulus %
  - multiplication *
  - addition +, subtraction - (lowest)
- data type casting
- comments in python
  - comments are ignored by the interpreter
  - single line comments start with #
  - multiline comments are enclosed in triple quotes """
- number type in python
  - int - integers both positive and negative
  - float - floating-point real values both positive and negative
  - complex - complex numbers such as 2 + 3i
  - python does not need explicit type specifier, it infers type based on value for the variable
- data type casting/conversion: float() and int()
- multiple assignment of a variable
  - a = b = c = 5
  - x, y = 100, 200
  - x, y, z = 100, 200, "Alphabet"
- swapping values of two variables
  - a, b = b, a
  - x,y,z = z,x,y
- multiple inputs from user
  - x,y = eval(input("Enter two numbers separated by commas: "))
- f-strings for formatted strings, where expressions are embedded in curly braces {}
- TypeError that occurs when operands are not of correct type
- Type casting from string to integer, float
- Type casting from integer, float to string
- Useful functions in math module
- constants in math module (pi, tau, e, inf, nan)
- multiline statement with backslash \
- number formatting in f-strings: Format Specification Mini-Language
- round(x,p) rounds the floating point number x to precision p
- complex numbers, j is used as the imaginary unit
  - y = 3+4j
  - y = complex(3,4)
  - y = complex("3+4j")
  - y = complex(input("Enter a complex number: "))
- mathematical functions are valid for complex numbers as well
  - complex1 * complex2
  - abs(complex1)
- methods from complex class
  - real_part = complex_number.real
  - imag_part = complex_number.imag
  - conjugate_part = complex_number.conjugate()
- 