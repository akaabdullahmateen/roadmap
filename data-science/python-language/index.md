# Python

<!-- omit in toc -->
## Table of contents

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
      - [Immutable sequences](#immutable-sequences)
      - [Mutable sequences](#mutable-sequences)
    - [Set types](#set-types)
    - [Mappings](#mappings)
      - [Dictionaries](#dictionaries)
    - [Callable types](#callable-types)
      - [User-defined functions](#user-defined-functions)
      - [Instance methods](#instance-methods)
      - [Generator functions](#generator-functions)
      - [Coroutine functions](#coroutine-functions)
      - [Asynchronous generator functions](#asynchronous-generator-functions)
      - [Builtin functions](#builtin-functions)
      - [Builtin methods](#builtin-methods)
      - [Classes](#classes)
      - [Class instances](#class-instances)
    - [Modules](#modules)
    - [Custom classes](#custom-classes)
    - [Class instances](#class-instances-1)
    - [File objects](#file-objects)
    - [Internal types](#internal-types)
  - [Special method names](#special-method-names)
    - [Basic customization](#basic-customization)
      - [`object.__new__(cls[, ...])`](#object__new__cls-)
      - [`object.__init__(self[, ...])`](#object__init__self-)
      - [`object.__del__(self)`](#object__del__self)
      - [`object.__repr__(self)`](#object__repr__self)
      - [`object.__str__(self)`](#object__str__self)
      - [`object.__bytes__(self)`](#object__bytes__self)
      - [`object.__format__(self, format_spec)`](#object__format__self-format_spec)
      - [Rich comparison methods](#rich-comparison-methods)
      - [`object.__hash__(self)`](#object__hash__self)
      - [`object.__bool__(self)`](#object__bool__self)
    - [Customizing attribute access](#customizing-attribute-access)
      - [`object.__getattr__(self, name)`](#object__getattr__self-name)
      - [`object.__getattribute__(self, name)`](#object__getattribute__self-name)
      - [`object.__setattr__(self, name, value)`](#object__setattr__self-name-value)
      - [`object.__delattr__(self, name)`](#object__delattr__self-name)
      - [`object.__dir__(self)`](#object__dir__self)
    - [Customizing module attribute access](#customizing-module-attribute-access)
    - [Implementing Descriptors](#implementing-descriptors)
      - [`object.__get__(self, instance, owner=None)`](#object__get__self-instance-ownernone)
      - [`object.__set__(self, instance, value)`](#object__set__self-instance-value)
      - [`object.__delete__(self, instance)`](#object__delete__self-instance)
    - [Invoking Descriptors](#invoking-descriptors)
    - [Slots](#slots)
      - [`object.__slots__`](#object__slots__)
  - [Arithmetic conversions](#arithmetic-conversions)
- [Operators](#operators-1)
  - [Comparison operators](#comparison-operators)
- [Builtin functions](#builtin-functions-1)
- [Builtin constants](#builtin-constants)

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

A comment starts with a hash character `#` that is not part of a string literal, and ends at the end of the physical line. A comment signifies the end of the logical line unless the implicit line joining rules are invoked. Comments are ignored by the syntax. Python does not support multiline comments; however, they can be emulated by a pair of triple quotation marks.

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

Sequences represent finite ordered sets that are indexed by non-negative numbers. The builtin function `len()` returns the number of items in a sequence. When the length of a sequence is $n$, the index set contains the numbers $0,1,\dots,n-1$. Item at index `i` of a sequence `a` is selected by `a[i]`.

Sequences also support slicing; that is, `a[i:j]` selects all items with index $k$ such that $i \le k \lt j$. When used as an expression, a slice is itself a sequence of the same type. Therefore, `a[i:j]` will behave like some other sequence `b` with the same items. This implies that the index set is renumbered so that it starts from 0.

Some sequences also support extended slicing with a third step parameter; that is, `a[i:j:k]` selects all items with index $x$ such that $x = i + n \times k$, $n \ge 0$, and $i \le x \lt j$.

Sequences are distinguished according to their mutability.

##### Immutable sequences

An object of an immutable sequence type cannot change once it is created. If the object contains references to other objects, these other objects may be mutable and can change; however, the collection of object directly referenced by an immutable object cannot change. The following types are immutable sequences:

Strings
: A string is a sequence of values that represent Unicode code points. All the code points in the range `U+0000 - U+10FFFF` can be represented in a string. Python does not have a `char` type; instead, every code point in the string is represented as a string object with length $1$. The builtin function `ord()` converts a code point from its string representation to an integer in the range `0 - 10FFFF`, whereas, `chr()` converts an integer in the range `0 - 10FFFF` to the corresponding length $1$ string object. The function `str.encode()` can be used to convert a `str` to `bytes` using the given encoding, and `bytes.decode()` can be used to achieve the opposite.

Bytes
: A bytes is an immutable array. The items are 8-bit bytes, represented by integers in the range $0 \le x \lt 256$. Byte literals, such as `b'abc'`, and the builtin `bytes()` constructor can be used to create bytes objects. Also, bytes objects can be decoded to strings via the `decode` method.

Tuples
: The items of a tuple are arbitrary Python objects. Tuples of two or more items are formed by comma-separated lists of expressions. A tuple of one item (a singleton) can be formed by affixing a comma to an expression; an expression by itself does not create a tuple, since parenthesis must be usable for grouping of expressions. An empty tuple can be formed by an empty pair of parenthesis.

##### Mutable sequences

Mutable sequences can be changed after they are created. The subscription and slicing notations can be used as the target of assignment and `del` statements. There are currently two intrinsic mutable sequence types; the `collections` and `array` module provide additional examples of mutable sequence types:

Lists
: The items of a list are arbitrary Python objects. Lists are formed by placing a comma-separated list of expressions in square brackets. Note that there are no special cases needed to form lists of length 0 or 1.

Byte arrays
: A byte array object is a mutable array. They are created by the builtin `bytearray()` constructor. Aside from being mutable (and hence, unhashable), byte arrays otherwise provide the same interface and functionality as the immutable `bytes` objects.

#### Set types

These represented unordered, finite sets of unique, immutable objects. As such, they cannot be indexed by any subscript. However, they can be iterated over, and the builtin `len()` function returns the number of items in a set. Common uses for sets are fast membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetrical difference.

For set elements, the same immutability rules apply as for dictionary keys. Note that numeric types obey the normal rules for numeric comparison: if two numbers compare equal (such as `1` and `1.0`), only one of them can be contained in a set. There are currently two intrinsic set types:

Sets
: These represent a mutable set. They are created by the builtin `set()` constructor and can be modified afterwards by several methods, such as `add()`.

Frozen sets
: These represent an immutable set. They are created by the builtin `frozenset()` constructor. As a frozen set is immutable and hashable, it can be used again as an element of another set, or as a dictionary key.

#### Mappings

These represent finite sets of objects indexed by arbitrary index sets. The subscript notation `a[k]` selects the item indexed by `k` from the mapping `a`; this can be used in expressions and as a target of assignments or `del` statements. The builtin function `len()` returns the number of items in a mapping. There is currently a single intrinsic mapping type; the modules `dbm.mdbm`, `dbm.gnu`, and `collections` provide additional examples of mapping types.

##### Dictionaries

Dictionaries represent mutable, finite sets of objects indexed by nearly arbitrary values. The only types of values not acceptable as keys are values containing lists or dictionaries or other mutable types that are compared by value rather than by object identity; the reason being that the efficient implementation of dictionaries requires a key's hash value to remain constant. Numeric types used for keys obey the normal rules for numeric comparison: if two numbers compare equal (such as `1` and `1.0`) then they can be used interchangeably to index the same dictionary entry.

Dictionaries preserve insertion order, meaning that keys will be produced in the same order they were added sequentially over the dictionary. Replacing an existing key does not change the order; however, removing a key and reinserting it will add it to the end instead of keeping its old place.

#### Callable types

These are the types to which the function call operation can be applied:

##### User-defined functions

A user-defined function object is created by a function definition. It should be called with an argument list containing the same number of items as the function's formal parameter list. It has some special attributes:

| Attribute | Description | Access type |
| - | - | - |
| `__doc__` | The function's documentation string, or `None` if unavailable. It is not inherited by subclasses. | Writable |
| `__name__` | The function's name. | Writable |
| `__qualname__` | The function's qualified name. | Writable |
| `__module__` | The name of the module in which the function was defined, or `None` if unavailable. | Writable |
| `__defaults__` | A tuple containing default argument values for those arguments that have defaults, or `None` if no arguments have a default value. | Writable |
| `__code__` | The code object representing the compiled function body. | Writable |
| `__globals__` | A reference to the dictionary that holds the function's global variables, which is the global namespace of the module in which the function was defined. | Read-only |
| `__dict__` | The namespace supporting arbitrary function attributes. | Writable |
| `__closure__` | A tuple of cells that contain bindings for the function's free variables, or `None`. | Read-only |
| `__annotations__` | A dictionary containing annotations of parameters. The keys of the dictionary are the parameter names, and `return` for the return annotation, if provided. | Writable |
| `__kwdefaults__` | A dictionary containing defaults for keyword-only parameters. | Writable |
| `__type_params__` | A tuple containing the type parameters of a generic function. | Writable |

Most of the attributes, with writable access type, check the type of the assigned value. Function objects also support getting and setting arbitrary attributes, which can be used, for example, to attach metadata to functions. Regular attribute dot notation is used to get and set such attributes.

A cell object has the attribute `cell_contents`. This can be used to get the value of the cell, as well as set the value. Additional information about a function's definition can be retrieved from its code object. The `cell` type can be accessed in the `types` module.

##### Instance methods

An instance method object combines a class, a class instance, and any callable object (usually a user-defined function). Methods also support accessing (but not setting) the arbitrary function attributes on the underlying function object. Instance methods have some special attributes:

| Attribute | Description |
| - | - |
| `__self__` | The class instance object |
| `__func__` | The function object |
| `__doc__` | The method's documentation, same as `__func__.__doc__` |
| `__name__` | The method's name, same as `__func__.__name__` |
| `__module__` | The name of the module in which the method was defined, `None` if unavailable |

User-defined method objects may be created when getting an attribute of a class if that attribute is a user-defined function object or a class method object, perhaps through an instance of that class.

When an instance method object is created by retrieving a user-defined function object from a class through one of its instances, its `__self__` attribute is the instance, and the method object is said to be bound. The new method's `__func__` attribute is the original function object.

When an instance method is created by retrieving a class method object from a class or instance, its `__self__` attribute is the class itself, and its `__func__` attribute is the function object underlying the class method.

When an instance method object is called, the underlying function (`__func__`) is called, inserting the class instance (`__self__`) in front of the argument list. For example, when `C` is a class which contains a definition for a function `f()`, and `x` is an instance of `C`, calling `x.f(1)` is equivalent to calling `C.f(x,1)`.

When an instance method object is derived from a class method object, the class instance stored in `__self__` will actually be the class itself, so that calling either `x.f(1)` or `C.f(1)` is equivalent to calling `f(C,1)`, where `f()` is the underlying function.

##### Generator functions

A function or method which uses the `yield` statement is called a generator function. Such a function, when called, always return an iterator object which can be used to execute the body of the function. Calling the iterator's `iterator.__next__()` method will cause the function to execute until it provides a value using the `yield` statement. When the function executes the `return` statement or falls off the end, a `StopIteration` exception is raised and the iterator will have reached the end of the set of values to be returned.

##### Coroutine functions

A function or method which is defined using `async def` is called a coroutine function. Such a function, when called, returns a coroutine object. It may contain `await` expressions, as well as `async with` and `async for` statements.

##### Asynchronous generator functions

A function or method which is defined using `async def` and which uses the `yield` statement is called an asynchronous generator function. Such a function, when called, returns an asynchronous iterator object which can be used in an `async for` statement to execute the body of the function.

Calling the asynchronous iterator's `aiterator.__anext__` method will return an awaitable which when awaited will execute until it provides a value using the `yield` expression. When the function executes an empty `return` statements or falls off the end, a `StopAsyncIteration` exception is raised and the asynchronous iterator will have reached the end of the set of values to be yielded.

##### Builtin functions

A builtin function is a wrapper around a C function, such as `len()` and `sin()`. The number and type of the arguments are determined by the C function. These have some special read-only attributes:

| Attribute | Description |
| - | - |
| `__doc__` | The function's documentation string, or `None` if unavailable |
| `__name__` | The function's name |
| `__self__` | Set to `None` |
| `__module__` | The name of the module in which the function was defined, or `None` if unavailable |

##### Builtin methods

A builtin method is basically a disguise of a builtin function, but containing an object passed to the C function as an implicit extra argument. An example is `alist.append()`, assuming `alist` is a list object. In this case, the special read-only attribute `__self__` is set to the object denoted by `alist`.

##### Classes

Classes are callable. These objects normally act as factories for new instances of themselves, but variations are possible for class types that override `__new__()`. The arguments of the call are passed to `__new__()` and, then usually, to `__init__()` to initialize the new instance.

##### Class instances

Instances of an arbitrary class can be made callable by defining a `__call__()` method in the class.

#### Modules

Modules are a basic organizational unit of Python code, and are created by the import system as invoked either by the `import` statement, or by calling functions such as `importlib.import_module()` and builtin `__import__()`. A module object has a namespace implemented by a dictionary object; this is the dictionary referenced by the `__globals__` attribute of functions defined in the module. Attribute references are translated to lookups in this dictionary; that is, `m.x` is equivalent to `m.__dict__["x"]`. Attribute assignment updates the module's namespace dictionary; that is, `m.x = 1` is equivalent to `m.__dict__["x"] = 1`. Module objects have some predefined writable attributes:

| Attribute | Description |
| - | - |
| `__name__` | The module's name |
| `__doc__` | The module's documentation string, or `None` if unavailable |
| `__file__` | The pathname of the file from which the module was loaded, if it was loaded from a file. The `__file__` attribute may be missing for certain types of modules, such as C modules that are statically linked into the interpreter. For extension modules loaded dynamically from a shared library, it is the pathname of the shared library file. |
| `__annotations__` | A dictionary containing variable annotations collected during module body execution |
| `__dict__` | The module's namespace as a dictionary object |

Because of the way CPython clears module dictionaries, the module dictionary will be cleared when the module falls out of scope even if the dictionary still has live references. To avoid this, copy the dictionary or keep the module around while using its dictionary directly.

#### Custom classes

Custom classes are typically created by class definitions. A class has a namespace implemented by a dictionary object. Class attribute references are translated to lookups in this dictionary; that is, `C.x` is translated to `C.__dict__["x]`, although there are a number of hooks which allow for other means of locating attributes. When the attribute name is not found there, the attribute search continues in the base classes. This search of the base classes uses the C3 method resolution order which behaves correctly even in the presence of diamond inheritance structures where there are multiple inheritance paths leading to a common ancestor.

When a class attribute reference, of class `C`, would yield a class method object, it is transformed into an instance method object whose `__self__` attribute is `C`. When it would yield a static method object, it is transformed into the object wrapped by the static method object.

Class attribute assignments update the class's dictionary, and never the dictionary of a base class. A class object can be called to yield a class instance. A class object has some special attributes:

| Attribute | Description |
| - | - |
| `__name__` | The class name |
| `__module__` | The name of the module in which the class was defined |
| `__dict__` | The dictionary containing the class's namespace |
| `__bases__` | A tuple containing the base classes, in the order of their occurrence in the base class list |
| `__doc__` | The class's documentation string, or `None` if unavailable |
| `__annotations__` | A dictionary containing variable annotations collected during class body execution |
| `__type_params__` | A tuple containing the type parameters of a generic class |

#### Class instances

A class instance is created by calling a class object. A class instance has a namespace implemented as a dictionary which is the first place in which attribute references are searched. When an attribute is not found there, and the instance's class has an attribute by that name, the search continues with the class attributes. If a class attribute is found that is a user-defined function object, it is transformed into an instance method object whose `__self__` attribute is the instance. Static method and class method objects are also transformed. If no class attribute is found, and the object's class has a `__getattr__()` method, then it is called to satisfy the lookup.

Attribute assignment and deletions update the instance's dictionary, and never a class's dictionary. If the class has a `__setattr__()` or `__delattr__()` method, then it is called instead of updating the instance dictionary directly.

Class instances can pretend to be numbers, sequences, or mappings if they have methods with certain special names. Class instances have some special attributes:

| Attribute | Description |
| - | - |
| `__dict__` | The attribute dictionary |
| `__class__` | The instance's class |

#### File objects

A file object represents an open file. Various shortcuts are available to create file objects; such as the builtin `open()` function, `os.popen()` method, `os.fdopen()` method, and the `makefile()` method of socket objects.

The objects `sys.stdin`, `sys.stdout`, and `sys.stderr` are initialized to file objects corresponding to the interpreter's standard input, output, and error streams. They are all open in text mode and therefore follow the interface defined by the `io.TextIOBase` abstract class.

#### Internal types

A few types used internally by the interpreter are exposed to the user. Their definitions may change with future versions of the interpreter. These are the code objects, frame objects, traceback objects, slice objects, static method objects, and class method objects.

### Special method names

A class can implement certain operations that are invoked by special syntax (such as arithmetic operations, subscripting, or slicing) by defining methods with special names. This is Python's approach to operator overloading, allowing classes to define their own behavior with respect to language operators. For example, if a class defines a method named `__getitem__()`, and `x` is an instance of this class, then `x[i]` is roughly equivalent to `type(x).__getitem__(x,i)`. Except where mentioned, attempts to execute an operation raise an exception when no appropriate method is defined, typically `AttributeError` or `TypeError`.

Setting a special method to `None` indicates that the corresponding operation is not available. For example, if a class sets `__iter__()` to `None`, the class is not iterable, so calling `iter()` on its instances will raise `TypeError`, without falling back to `__getitem__()`.

When implementing a class that emulates any builtin type, it is important that the emulation only be implemented to the degree that it makes sense for the object being modelled. For example, some sequences may work well with retrieval of individual elements, but extracting a slice may not make sense.

#### Basic customization

##### `object.__new__(cls[, ...])`

The `__new__()` method is called to create a new instance of the class. It is special-cased so it does not need to be declared. The `__new__()` method is a static method that takes the class (of which an instance was requested) as its first argument. The remaining arguments are those passed to the object constructor expression (the call to the class). The return value of `__new__()` should be the new object instance, which is usually an instance of `cls`.

Typical implementations create a new instance of the class by invoking the superclass's `__new__()` method using `super.__new__(cls[, ...])` with appropriate arguments and then modifying the newly created instance as necessary before returning it.

If `__new__()` is invoked during object construction and it returns an instance of `cls`, then the new instance's `__init__()` method will be invoked like `__init__(self[, ...])`, where `self` is the new instance and the remaining arguments are the same as were passed to the object's constructor. If `__new__()` does not return an instance of `cls`, then the new instance's `__init__()` method will not be invoked.

The `__new__()` method is intended mainly to allow subclasses, of immutable types, to customize instance creation. It is also commonly overridden in custom metaclasses in order to customize class creation.

##### `object.__init__(self[, ...])`

The `__init__()` method is called after the instance has been created by `__new__()`, but before it is returned to the caller. The arguments are those passed to the class constructor expression. If a base class has an `__init__()` method, the derived class's `__init__()` method must explicitly call it to ensure proper initialization of the base class part of the instance; for example, `super.__init__([args...])`.

Because `__new__()` and `__init__()` work together in constructing objects, `__init__()` must not return anything other than `None`; doing otherwise would cause a `TypeError` to be raised at runtime.

##### `object.__del__(self)`

The `__del__()` method is called when the instance is about to be destroyed. This is also called a finalizer or (improperly) a destructor. If a base class has a `__del__()` method, the derived class's `__del__()` method must explicitly call it to ensure proper deletion of the base class part of the instance.

It is possible, but not recommended, for the `__del__()` to postpone destruction of the instance by creating a new reference to it. This is called object resurrection. It is implementation-dependent whether `__del__()` is called a second time when a resurrected object is about to be destroyed; the current CPython implementation only calls it once. It is not guaranteed that the `__del__()` method is called for an object that still exists when the interpreter exits.

Note that `del x` does not directly call `x.__del__()`; the statement `del x` decrements the reference count for `x` by one, while the method `x.__del__()` is only called when `x` reference count reaches zero.

In CPython, it is possible for a reference cycle to prevent the reference count of an object from going to zero. In this case, the cycle will be later detected and deleted by the cyclic garbage collector. A common cause of reference cycles is when an exception has been caught in a local variable. The frame’s locals then reference the exception, which references its own traceback, which references the locals of all frames caught in the traceback.

Due to the precarious circumstances under which `__del__()` methods are invoked, exceptions that occur during their execution are ignored, and a warning is printed to `sys.stderr` instead.

##### `object.__repr__(self)`

The `__repr__()` method is called by the `repr()` function to compute the official string representation of an object. If at all possible, this should look like a valid Python expression that could be used to recreate an object with the same value, given an appropriate environment. If this is not possible, a string of the form `<...some useful description...>` should be returned. The return value must be a string object.

If a class defined `__repr__()` but not `__str__()`, then `__repr__()` is also used when an informal string representation of instances of that class is required. This is typically used for debugging, so it is important that the representation is informative and unambiguous.

##### `object.__str__(self)`

The `__str__()` method is called by the `str()`, `print()`, and `format()` functions to compute the informal or nicely printable string representation of an object. The return value must be a string object.

This method differs from `__repr__()` in that there is no expectation that `__str__()` return a valid Python expression; instead, a more convenient or concise representation can be used. The default implementation defined by the builtin type `object` calls `object.__repr__()`.

##### `object.__bytes__(self)`

The `__bytes__()` method is called by `bytes()` to compute a byte-string representation of an object. This should return a `bytes` object.

##### `object.__format__(self, format_spec)`

The `__format__()` method is called by the `format()` builtin function, evaluation of formatted string literals, and the `str.format()` method, to produce a formatted string representation of an object. The `format_spec` argument is a string that contains a description of the formatting options desired. The interpretation of the `format_spec` argument is dependent on the type implementing `__format__()`, however most classes will either delegate formatting to one of the builtin types, or use a similar formatting option syntax. The return value must be a string object.

##### Rich comparison methods

The rich comparison methods implement operator overloading for mathematical comparison operators; for example, `x < y` calls `x.__lt__(y)`. These methods are listed in the table below:

| Method | Comparison operator |
| - | - |
| `object.__lt__(self,other)` | `x <  y` |
| `object.__le__(self,other)` | `x <= y` |
| `object.__eq__(self,other)` | `x == y` |
| `object.__ne__(self,other)` | `x != y` |
| `object.__gt__(self,other)` | `x >  y` |
| `object.__ge__(self,other)` | `x >= y` |

A rich comparison method may return the singleton `NotImplemented` if it does not implement the operation for a given pair of arguments. By convention, `False` and `True` are returned for a successful comparison. However, these methods can return any value, so if the comparison operator is used in a Boolean context, Python will call `bool()` on the value to determine if the result is true or false.

By default, `object` implements `__eq__()` by using `is`, returning `NotImplemented` in the case of false comparison; that is, `True if x is y else NotImplemented`. For `__ne__()`, by default it delegates to `__eq__()` and inverts the result unless it is `NotImplemented`. There are no other implied relationships among the comparison operators or default implementations; for example, the truth of `x < y or x == y` does not imply `x <= y`. To automatically generate ordering operations from a single root operation, use `functools.total_ordering()`.

There are no swapped-argument versions of these methods, to be used when the left argument does not support the operation but the right argument does. Rather, `__lt__()` and `__gt__()`, `__le__()` and `__ge__()` are reflection of each other, and `__eq__()` and `__ne__()` are their own reflection. If the operands are of different types, and right operand’s type is a direct or indirect subclass of the left operand’s type, the reflected method of the right operand has priority, otherwise the left operand’s method has priority. Virtual subclassing is not considered.

##### `object.__hash__(self)`

The `__hash__()` method is called by the builtin `hash()` function, and for operations on members of hashed collections, including `set`, `frozenset`, and `dict`. The `__hash__()` method should return an integer. The only required property is that objects which compare equal have the same hash value. It is advised to mix together the hash values of the components of the object that also play a part in comparison of objects by packing them into a tuple and hashing the tuple.

```py
def __hash__(self):
    return hash((self.name, self.nick, self.color))
```

Note that the `hash()` method truncates the value returned from an object's custom `__hash__()` method to the size of a `Py_ssize_t`. This is typically 8 bytes on 64-bit builds and 4 bytes on 32-bit builds.

If a class does not define and `__eq__()` method, it should not define a `__hash__()` method either. If it defines `__eq__()` but not `__hash__()`, its instances will not be usable as items in hashable collections. If a class defines mutable objects and implements an `__eq__()` method, it should not implement `__hash__()`, since the implementation of hashable collections requires that a key's hash value is immutable.

User-defined classes have `__eq__()` and `__hash__()` methods by default; with them, all objects compare unequal (except with themselves) and `x.__hash__()` returns an appropriate value such that `x == y` implies both that `x is y` and `hash(x) == hash(y)`.

A class that overrides `__eq__()` and does not define `__hash__()` will have its `__hash__()` implicitly set to `None`. When the `__hash__()` method of a class is `None`, instances of the class will raise an appropriate `TypeError` when a program attempts to retrieve their hash value, and will also be correctly identified as unhashable when checking `isinstance(obj, collections.abc.Hashable)`.

If a class that overrides `__eq__()` needs to retain the implementation of `__hash__()` from a parent class, the interpreter must be told this explicitly by setting `__hash__ = <ParentClass>.__hash__`. If a class that does not override `__eq__()` wishes to suppress hash support, it should include `__hash__ = None` in the class definition. A class which defines its own `__hash__()` that explicitly raises a `TypeError` would be incorrectly identified as hashable by an `isinstance(obj, collections.abc.Hashable)` call.

By default, the `__hash__()` values of `str` and `bytes` objects are modified with an unpredictable random value. Although they remain constant within an individual Python process, they are not predictable between repeated invocations of Python.

##### `object.__bool__(self)`

The `__bool__()` method is called to implement truth value testing and the builtin function `bool()`. It should return `True` or `False`. When this method is not defined, `__len__()`, if defined, is called, and the object is considered true if its returned value is nonzero. If a class has neither `__len__()` nor `__bool__()`, all its instances are considered true.

#### Customizing attribute access

The following methods can be defined to customize the meaning of attribute access (use of, assignment to, or deletion of `x.name``) for class instances.

##### `object.__getattr__(self, name)`

The `__getattr__()` method is called when the default attribute access fails with an `AttributeError`. This happens when either `__getattribute__()` raises an `AttributeError` because name could not be resolved; or `__get__()` of a name property raises `AttributeError`. This method should either return the (computed) attribute value or raise an `AttributeError` exception.

Note that if the attribute is found through the normal mechanism, `__getattr__()` is not called. This is an intentional asymmetry between `__getattr__()` and `__setattr__()`. This is done both for efficiency reasons and because otherwise `__getattr__()` would have no way to access other attributes of the instance.

Note that at least for instance variables, you can fake total control by not inserting any values in the instance attribute dictionary (but instead inserting them in another object).

##### `object.__getattribute__(self, name)`

The `__getattribute__()` method is called unconditionally to implement attribute accesses for instances of the class. If the class also defines `__getattr__()`, the latter will not be called unless `__getattribute__()` either calls it explicitly or raises an `AttributeError`. This method should return the (computed) attribute value or raise an `AttributeError` exception.

In order to avoid infinite recursion, if `__getattribute__()` is overridden, it should always call the base class method `object.__getattribute(self, name)` to access any attribute.

##### `object.__setattr__(self, name, value)`

The `__setattr__()` method is called when an attribute assignment is attempted. This is called instead of the normal mechanism (store the value in the instance dictionary). The argument `name` is the attribute name and `value` is the value to be assigned to it.

If `__setattr__()` is overridden but wants to set the instance attribute through the normal mechanism, it should call the base class method `object.__setattr__(self, name, value)`.

##### `object.__delattr__(self, name)`

The `__delattr__()` method is called when an attribute deletion is attempted. This should only be implemented if `del obj.name` is meaningful for the object.

If `__delattr__()` is overridden but wants to delete the instance attribute through the normal mechanism, it should call the base class method `object.__delattr__(self, name)`.

##### `object.__dir__(self)`

The `__dir__()` method is Called when `dir()` is called on the object. A sequence must be returned. The `dir()` function converts the returned sequence to a list and sorts it.

#### Customizing module attribute access

Special functions `__getattr__()` and `__dir__()` can be also used to customize access to module attributes. The `__getattr__()` function at the module level should accept one argument which is the name of an attribute and return the computed value or raise an `AttributeError`. If an attribute is not found on a module object through the normal lookup, which is `object.__getattribute__()`, then `__getattr__()` is searched in the module `__dict__` before raising an `AttributeError`. If found, it is called with the attribute name and the result is returned.

The `__dir__()` function should accept no arguments, and return a sequence of strings that represents the names accessible on module. If present, this function overrides the standard `dir()` search on a module.

For a more fine grained customization of the module behavior (such as setting attributes and properties), the `__class__` attribute of a module object can be set to a subclass of `types.ModuleType`.

```py
import sys
from types import ModuleType

class VerboseModule(ModuleType):
    def __repr__(self):
        return f'Verbose {self.__name__}'

    def __setattr__(self, attr, value):
        print(f'Setting {attr}...')
        super().__setattr__(attr, value)

sys.modules[__name__].__class__ = VerboseModule
```

Note that defining module `__getattr__()` and setting module `__class__` only affect lookups made using the attribute access syntax. If the module globals are accessed directly, whether by code within the module or through a reference to the module’s globals dictionary, they have no effect.

#### Implementing Descriptors

The following methods only apply when an instance of a descriptor class appears in an owner class. 

##### `object.__get__(self, instance, owner=None)`
The `__get__()` method is called to get the attribute of the owner class (class attribute access) or of an instance of that class (instance attribute access). The optional owner argument is the owner class, while instance is the instance that the attribute was accessed through, or `None` when the attribute is accessed through the owner.

This method should return the computed attribute value or raise an `AttributeError` exception.
The `__get__()` method is callable with one or two arguments. Python’s own `__getattribute__()` implementation always passes in both arguments whether they are required or not.

##### `object.__set__(self, instance, value)`
The `__set__()` method is Called to set the attribute on an instance of the owner class to a new value. Note, adding `__set__()` or `__delete__()` changes the kind of descriptor to a data descriptor.

##### `object.__delete__(self, instance)`

The `__delete__()` method is Called to delete the attribute on an instance of the owner class.

#### Invoking Descriptors

In general, a descriptor is an object attribute with binding behavior; that is, one whose attribute access has been overridden by methods in the descriptor protocol: `__get__()`, `__set__()`, and `__delete__()`. If any of those methods are defined for an object, it is said to be a descriptor.

The default behavior for attribute access is to get, set, or delete the attribute from an object’s dictionary. For instance, `a.x` has a lookup chain starting with `a.__dict__['x']`, then `type(a).__dict__['x']`, and continuing through the base classes of `type(a)` excluding metaclasses.

However, if the looked-up value is an object defining one of the descriptor methods, then Python may override the default behavior and invoke the descriptor method instead. Where this occurs in the precedence chain depends on which descriptor methods were defined and how they were called.

The starting point for descriptor invocation is a binding, `a.x`. How the arguments are assembled depends on `a`:

Direct Call
: The simplest and least common call is when user code directly invokes a descriptor method: `x.
__get__(a)`.

Instance Binding
: If binding to an object instance, `a.x` is transformed into the call: `type(a).__dict__['x'].__get__(a, type(a))`.

Class Binding
: If binding to a class, `A.x` is transformed into the call: `A.__dict__['x'].__get__(None,
A)`.

Super Binding
: A dotted lookup such as `super(A, a).x` searches `a.__class__.__mro__` for a base class
`B` following `A` and then returns `B.__dict__['x'].__get__(a, A)`. If not a descriptor, `x` is returned unchanged.

For instance bindings, the precedence of descriptor invocation depends on which descriptor methods are defined. A descriptor can define any combination of `__get__()`, `__set__()`, and `__delete__()`. If it does not define `__get__()`, then accessing the attribute will return the descriptor object itself unless there is a value in the object’s instance dictionary. If the descriptor defines `__set__()` and/or `__delete__()`, it is a data descriptor; if it defines neither, it is a non-data descriptor. Normally, data descriptors define both `__get__()` and `__set__()`, while non-data descriptors have just the `__get__()` method. Data descriptors with `__get__()`
and `__set__()` (and/or `__delete__()`) defined always override a redefinition in an instance dictionary. In contrast, non-data descriptors can be overridden by instances.

Python methods (including those decorated with `@staticmethod` and `@classmethod`) are implemented as non-data descriptors. Accordingly, instances can redefine and override methods. This allows individual instances to acquire behaviors that differ from other instances of the same class.
The `property()` function is implemented as a data descriptor. Accordingly, instances cannot override the behavior of a property.

#### Slots

The attribute `__slots__` allow us to explicitly declare data members (like properties) and deny the creation of `__dict__` and `__weakref__`, unless explicitly declared in __`slots__` or available in a parent. The space saved over using `__dict__` can be significant. Attribute lookup speed can be significantly improved as well.

##### `object.__slots__`

This class variable can be assigned a string, iterable, or sequence of strings with variable names used by instances. The attribute `__slots__` reserves space for the declared variables and prevents the automatic creation of `__dict__` and `__weakref__` for each instance.


### Arithmetic conversions

For some arithmetic operators, numeric arguments are converted to a common type as follows:

- If either argument is a complex number, the other is converted to a complex number;
- otherwise, if either argument is a floating-point number, the other is converted to a floating-point number;
- otherwise, both must be integers, and no conversion is necessary.

## Operators



### Comparison operators

Comparisons yield boolean values: `True` or `False`. Custom rich comparison methods may return non-boolean values; in which case, Python calls `bool()` on such values in boolean contexts.

| Operation | Symbol | Special method |
| - | - | - |
| Less than | `<` | `__lt__()` |
| Less than or equal to | `<=` | `__le__()` |
| Greater than | `>` | `__gt__()` |
| Greater than or equal to | `>=` | `__ge__()` |
| Equal to | `==` | `__eq__()` |
| Not equal to | `!=` | `__ne__()` |

All comparison operators in Python have the same priority, which is lower than that of any arithmetic, shifting, or bitwise operation.

Comparisons can be chained arbitrarily; that is, `a < b < c < ... < y < z` is equivalent to `a < b and b < c and ... y < z` except that each expression is evaluated only once.



| Operator | Symbol | Special method |
| - | - | - | - |
| Power | `**` | `__pow__()` |
| Unary minus | `-` | `__neg__()` |
| Unary plus | `+` | `__pos__()` |
| Unary invert | `~` | `__invert__()` |
| Multiplication | `*` | `__mul__()` and `__rmul__()` |
| Division | `/` | `__truediv__()` |
| Floor division | `//` | `__floordiv__()` |
| Matrix multiplication | `@` | `__matmul__()` |
| Modulo | `%` | `__mod__()` |
| Addition | `+` | `__add__()` and `__radd__()` |
| Subtraction | `-` | `__sub__()` |
| Left shift | `<<` | `__lshift__()` |
| Right shift | `>>` | `__rshift__()` |
| Bitwise AND | `&` | `__and__()` and `__rand__()` |
| Bitwise XOR | `^` | `__xor__()` and `__rxor__()` |
| Bitwise OR | `|` | `__or__()` and `__ror__()` |

Notes on using __slots__:
• When inheriting from a class without __slots__, the __dict__ and __weakref__ attribute of the instances
will always be accessible.
• Without a __dict__ variable, instances cannot be assigned new variables not listed in the __slots__ definition.
Attempts to assign to an unlisted variable name raises AttributeError. If dynamic assignment of new
variables is desired, then add '__dict__' to the sequence of strings in the __slots__ declaration.
• Without a __weakref__ variable for each instance, classes defining __slots__ do not support weak refer-
ences to its instances. If weak reference support is needed, then add '__weakref__' to the sequence of
strings in the __slots__ declaration.
• __slots__ are implemented at the class level by creating descriptors for each variable name. As a result, class
attributes cannot be used to set default values for instance variables defined by __slots__; otherwise, the class
attribute would overwrite the descriptor assignment.
• The action of a __slots__ declaration is not limited to the class where it is defined. __slots__ declared in parents
are available in child classes. However, child subclasses will get a __dict__ and __weakref__ unless they
also define __slots__ (which should only contain names of any additional slots).
• If a class defines a slot also defined in a base class, the instance variable defined by the base class slot is
inaccessible (except by retrieving its descriptor directly from the base class). This renders the meaning of the
program undefined. In the future, a check may be added to prevent this.
• TypeError will be raised if nonempty __slots__ are defined for a class derived from a
"variable-length" built-in type such as int, bytes, and tuple.
• Any non-string iterable may be assigned to __slots__.
• If a dictionary is used to assign __slots__, the dictionary keys will be used as the slot names. The val-
ues of the dictionary can be used to provide per-attribute docstrings that will be recognised by inspect.
getdoc() and displayed in the output of help().
• __class__ assignment works only if both classes have the same __slots__.
• Multiple inheritance with multiple slotted parent classes can be used, but only one parent is allowed to have
attributes created by slots (the other bases must have empty slot layouts) - violations raise TypeError.
3.3. Special method names 35
The Python Language Reference, Release 3.12.0
• If an iterator is used for __slots__ then a descriptor is created for each of the iterator’s values. However, the
__slots__ attribute will be an empty iterator.
3.3.3 Customizing class creation
Whenever a class inherits from another class, __init_subclass__() is called on the parent class. This way,
it is possible to write classes which change the behavior of subclasses. This is closely related to class decorators,
but where class decorators only affect the specific class they’re applied to, __init_subclass__ solely applies to
future subclasses of the class defining the method.
classmethod object.__init_subclass__(cls)
This method is called whenever the containing class is subclassed. cls is then the new subclass. If defined as a
normal instance method, this method is implicitly converted to a class method.
Keyword arguments which are given to a new class are passed to the parent’s class __init_subclass__.
For compatibility with other classes using __init_subclass__, one should take out the needed keyword
arguments and pass the others over to the base class, as in:
class Philosopher:
def __init_subclass__(cls, /, default_name, **kwargs):
super().__init_subclass__(**kwargs)
cls.default_name = default_name
class AustralianPhilosopher(Philosopher, default_name="Bruce"):
pass
The default implementation object.__init_subclass__ does nothing, but raises an error if it is called
with any arguments.
Note: The metaclass hint metaclass is consumed by the rest of the type machinery, and is never passed to
__init_subclass__ implementations. The actual metaclass (rather than the explicit hint) can be accessed
as type(cls).
New in version 3.6.
When a class is created, type.__new__() scans the class variables and makes callbacks to those with a
__set_name__() hook.
object.__set_name__(self, owner, name)
Automatically called at the time the owning class owner is created. The object has been assigned to name in
that class:
class A:
x = C() # Automatically calls: x.__set_name__(A, 'x')
If the class variable is assigned after the class is created, __set_name__() will not be called automatically.
If needed, __set_name__() can be called directly:
class A:
pass
c = C()
A.x = c # The hook is not called
c.__set_name__(A, 'x') # Manually invoke the hook
See Creating the class object for more details.
New in version 3.6.
36 Chapter 3. Data model
The Python Language Reference, Release 3.12.0
Metaclasses
By default, classes are constructed using type(). The class body is executed in a new namespace and the class
name is bound locally to the result of type(name, bases, namespace).
The class creation process can be customized by passing the metaclass keyword argument in the class definition
line, or by inheriting from an existing class that included such an argument. In the following example, both MyClass
and MySubclass are instances of Meta:
class Meta(type):
pass
class MyClass(metaclass=Meta):
pass
class MySubclass(MyClass):
pass
Any other keyword arguments that are specified in the class definition are passed through to all metaclass operations
described below.
When a class definition is executed, the following steps occur:
• MRO entries are resolved;
• the appropriate metaclass is determined;
• the class namespace is prepared;
• the class body is executed;
• the class object is created.
Resolving MRO entries
object.__mro_entries__(self, bases)
If a base that appears in a class definition is not an instance of type, then an __mro_entries__() method
is searched on the base. If an __mro_entries__() method is found, the base is substituted with the result
of a call to __mro_entries__() when creating the class. The method is called with the original bases
tuple passed to the bases parameter, and must return a tuple of classes that will be used instead of the base.
The returned tuple may be empty: in these cases, the original base is ignored.
See also:
types.resolve_bases() Dynamically resolve bases that are not instances of type.
types.get_original_bases() Retrieve a class’s “original bases” prior to modifications by
__mro_entries__().
PEP 560 Core support for typing module and generic types.
Determining the appropriate metaclass
The appropriate metaclass for a class definition is determined as follows:
• if no bases and no explicit metaclass are given, then type() is used;
• if an explicit metaclass is given and it is not an instance of type(), then it is used directly as the metaclass;
• if an instance of type() is given as the explicit metaclass, or bases are defined, then the most derived metaclass
is used.
3.3. Special method names 37
The Python Language Reference, Release 3.12.0
The most derived metaclass is selected from the explicitly specified metaclass (if any) and the metaclasses (i.e.
type(cls)) of all specified base classes. The most derived metaclass is one which is a subtype of all of these
candidate metaclasses. If none of the candidate metaclasses meets that criterion, then the class definition will fail
with TypeError.
Preparing the class namespace
Once the appropriate metaclass has been identified, then the class namespace is prepared. If the metaclass has
a __prepare__ attribute, it is called as namespace = metaclass.__prepare__(name, bases,
**kwds) (where the additional keyword arguments, if any, come from the class definition). The __prepare__
method should be implemented as a classmethod. The namespace returned by __prepare__ is passed in to
__new__, but when the final class object is created the namespace is copied into a new dict.
If the metaclass has no __prepare__ attribute, then the class namespace is initialised as an empty ordered map-
ping.
See also:
PEP 3115 - Metaclasses in Python 3000 Introduced the __prepare__ namespace hook
Executing the class body
The class body is executed (approximately) as exec(body, globals(), namespace). The key difference
from a normal call to exec() is that lexical scoping allows the class body (including any methods) to reference
names from the current and outer scopes when the class definition occurs inside a function.
However, even when the class definition occurs inside the function, methods defined inside the class still cannot see
names defined at the class scope. Class variables must be accessed through the first parameter of instance or class
methods, or through the implicit lexically scoped __class__ reference described in the next section.
Creating the class object
Once the class namespace has been populated by executing the class body, the class object is created by calling
metaclass(name, bases, namespace, **kwds) (the additional keywords passed here are the same as
those passed to __prepare__).
This class object is the one that will be referenced by the zero-argument form of super(). __class__ is an
implicit closure reference created by the compiler if any methods in a class body refer to either __class__ or
super. This allows the zero argument form of super() to correctly identify the class being defined based on
lexical scoping, while the class or instance that was used to make the current call is identified based on the first
argument passed to the method.
CPython implementation detail: In CPython 3.6 and later, the __class__ cell is passed to the metaclass as a
__classcell__ entry in the class namespace. If present, this must be propagated up to the type.__new__
call in order for the class to be initialised correctly. Failing to do so will result in a RuntimeError in Python 3.8.
When using the default metaclass type, or any metaclass that ultimately calls type.__new__, the following
additional customization steps are invoked after creating the class object:
1) The type.__new__ method collects all of the attributes in the class namespace that define a
__set_name__() method;
1) Those __set_name__ methods are called with the class being defined and the assigned name of that par-
ticular attribute;
1) The __init_subclass__() hook is called on the immediate parent of the new class in its method reso-
lution order.
After the class object is created, it is passed to the class decorators included in the class definition (if any) and the
resulting object is bound in the local namespace as the defined class.
38 Chapter 3. Data model
The Python Language Reference, Release 3.12.0
When a new class is created by type.__new__, the object provided as the namespace parameter is copied to a
new ordered mapping and the original object is discarded. The new copy is wrapped in a read-only proxy, which
becomes the __dict__ attribute of the class object.
See also:
PEP 3135 - New super Describes the implicit __class__ closure reference
Uses for metaclasses
The potential uses for metaclasses are boundless. Some ideas that have been explored include enum, logging, in-
terface checking, automatic delegation, automatic property creation, proxies, frameworks, and automatic resource
locking/synchronization.
3.3.4 Customizing instance and subclass checks
The following methods are used to override the default behavior of the isinstance() and issubclass()
built-in functions.
In particular, the metaclass abc.ABCMeta implements these methods in order to allow the addition of Abstract
Base Classes (ABCs) as “virtual base classes” to any class or type (including built-in types), including other ABCs.
class.__instancecheck__(self, instance)
Return true if instance should be considered a (direct or indirect) instance of class. If defined, called to imple-
ment isinstance(instance, class).
class.__subclasscheck__(self, subclass)
Return true if subclass should be considered a (direct or indirect) subclass of class. If defined, called to imple-
ment issubclass(subclass, class).
Note that these methods are looked up on the type (metaclass) of a class. They cannot be defined as class methods in
the actual class. This is consistent with the lookup of special methods that are called on instances, only in this case
the instance is itself a class.
See also:
PEP 3119 - Introducing Abstract Base Classes Includes the specification for customizing isinstance() and
issubclass() behavior through __instancecheck__() and __subclasscheck__(), with mo-
tivation for this functionality in the context of adding Abstract Base Classes (see the abc module) to the
language.
3.3.5 Emulating generic types
When using type annotations, it is often useful to parameterize a generic type using Python’s square-brackets notation.
For example, the annotation list[int] might be used to signify a list in which all the elements are of type
int.
See also:
PEP 484 - Type Hints Introducing Python’s framework for type annotations
Generic Alias Types Documentation for objects representing parameterized generic classes
Generics, user-defined generics and typing.Generic Documentation on how to implement generic classes
that can be parameterized at runtime and understood by static type-checkers.
A class can generally only be parameterized if it defines the special class method __class_getitem__().
classmethod object.__class_getitem__(cls, key)
Return an object representing the specialization of a generic class by type arguments found in key.
When defined on a class, __class_getitem__() is automatically a class method. As such, there is no
need for it to be decorated with @classmethod when it is defined.
3.3. Special method names 39
The Python Language Reference, Release 3.12.0
The purpose of __class_getitem__
The purpose of __class_getitem__() is to allow runtime parameterization of standard-library generic classes
in order to more easily apply type hints to these classes.
To implement custom generic classes that can be parameterized at runtime and understood by static type-checkers,
users should either inherit from a standard library class that already implements __class_getitem__(), or
inherit from typing.Generic, which has its own implementation of __class_getitem__().
Custom implementations of __class_getitem__() on classes defined outside of the standard library may not be
understood by third-party type-checkers such as mypy. Using __class_getitem__() on any class for purposes
other than type hinting is discouraged.
__class_getitem__ versus __getitem__
Usually, the subscription of an object using square brackets will call the __getitem__() instance method
defined on the object’s class. However, if the object being subscribed is itself a class, the class method
__class_getitem__() may be called instead. __class_getitem__() should return a GenericAlias ob-
ject if it is properly defined.
Presented with the expression obj[x], the Python interpreter follows something like the following process to decide
whether __getitem__() or __class_getitem__() should be called:
from inspect import isclass
def subscribe(obj, x):
"""Return the result of the expression 'obj[x]'"""
class_of_obj = type(obj)
# If the class of obj defines __getitem__,
# call class_of_obj.__getitem__(obj, x)
if hasattr(class_of_obj, '__getitem__'):
return class_of_obj.__getitem__(obj, x)
# Else, if obj is a class and defines __class_getitem__,
# call obj.__class_getitem__(x)
elif isclass(obj) and hasattr(obj, '__class_getitem__'):
return obj.__class_getitem__(x)
# Else, raise an exception
else:
raise TypeError(
f"'{class_of_obj.__name__}' object is not subscriptable"
)
In Python, all classes are themselves instances of other classes. The class of a class is known as that class’s meta-
class, and most classes have the type class as their metaclass. type does not define __getitem__(), mean-
ing that expressions such as list[int], dict[str, float] and tuple[str, bytes] all result in
__class_getitem__() being called:
>>> # list has class "type" as its metaclass, like most classes:
>>> type(list)
<class 'type'>
>>> type(dict) == type(list) == type(tuple) == type(str) == type(bytes)
True
>>> # "list[int]" calls "list.__class_getitem__(int)"
>>> list[int]
list[int]
>>> # list.__class_getitem__ returns a GenericAlias object:
>>> type(list[int])
<class 'types.GenericAlias'>
40 Chapter 3. Data model
The Python Language Reference, Release 3.12.0
However, if a class has a custom metaclass that defines __getitem__(), subscribing the class may result in
different behaviour. An example of this can be found in the enum module:
>>> from enum import Enum
>>> class Menu(Enum):
... """A breakfast menu"""
... SPAM = 'spam'
... BACON = 'bacon'
...
>>> # Enum classes have a custom metaclass:
>>> type(Menu)
<class 'enum.EnumMeta'>
>>> # EnumMeta defines __getitem__,
>>> # so __class_getitem__ is not called,
>>> # and the result is not a GenericAlias object:
>>> Menu['SPAM']
<Menu.SPAM: 'spam'>
>>> type(Menu['SPAM'])
<enum 'Menu'>
See also:
PEP 560 - Core Support for typing module and generic types Introducing __class_getitem__(),
and outlining when a subscription results in __class_getitem__() being called instead of
__getitem__()
3.3.6 Emulating callable objects
object.__call__(self[, args... ])
Called when the instance is “called” as a function; if this method is defined, x(arg1, arg2, ...) roughly
translates to type(x).__call__(x, arg1, ...).
3.3.7 Emulating container types
The following methods can be defined to implement container objects. Containers usually are sequences (such as
lists or tuples) or mappings (like dictionaries), but can represent other containers as well. The first set
of methods is used either to emulate a sequence or to emulate a mapping; the difference is that for a sequence, the
allowable keys should be the integers k for which 0 <= k < N where N is the length of the sequence, or slice
objects, which define a range of items. It is also recommended that mappings provide the methods keys(), val-
ues(), items(), get(), clear(), setdefault(), pop(), popitem(), copy(), and update()
behaving similar to those for Python’s standard dictionary objects. The collections.abc module pro-
vides a MutableMapping abstract base class to help create those methods from a base set of __getitem__(),
__setitem__(), __delitem__(), and keys(). Mutable sequences should provide methods append(),
count(), index(), extend(), insert(), pop(), remove(), reverse() and sort(), like Python
standard list objects. Finally, sequence types should implement addition (meaning concatenation) and multipli-
cation (meaning repetition) by defining the methods __add__(), __radd__(), __iadd__(), __mul__(),
__rmul__() and __imul__() described below; they should not define other numerical operators. It is recom-
mended that both mappings and sequences implement the __contains__() method to allow efficient use of the
in operator; for mappings, in should search the mapping’s keys; for sequences, it should search through the values.
It is further recommended that both mappings and sequences implement the __iter__() method to allow efficient
iteration through the container; for mappings, __iter__() should iterate through the object’s keys; for sequences,
it should iterate through the values.
object.__len__(self)
Called to implement the built-in function len(). Should return the length of the object, an integer >= 0.
Also, an object that doesn’t define a __bool__() method and whose __len__() method returns zero is
considered to be false in a Boolean context.
3.3. Special method names 41
The Python Language Reference, Release 3.12.0
CPython implementation detail: In CPython, the length is required to be at most sys.maxsize. If
the length is larger than sys.maxsize some features (such as len()) may raise OverflowError. To
prevent raising OverflowError by truth value testing, an object must define a __bool__() method.
object.__length_hint__(self)
Called to implement operator.length_hint(). Should return an estimated length for the object (which
may be greater or less than the actual length). The length must be an integer >= 0. The return value may also
be NotImplemented, which is treated the same as if the __length_hint__ method didn’t exist at all.
This method is purely an optimization and is never required for correctness.
New in version 3.4.
Note: Slicing is done exclusively with the following three methods. A call like
a[1:2] = b
is translated to
a[slice(1, 2, None)] = b
and so forth. Missing slice items are always filled in with None.
object.__getitem__(self, key)
Called to implement evaluation of self[key]. For sequence types, the accepted keys should be integers and
slice objects. Note that the special interpretation of negative indexes (if the class wishes to emulate a sequence
type) is up to the __getitem__() method. If key is of an inappropriate type, TypeError may be raised;
if of a value outside the set of indexes for the sequence (after any special interpretation of negative values),
IndexError should be raised. For mapping types, if key is missing (not in the container), KeyError
should be raised.
Note: for loops expect that an IndexError will be raised for illegal indexes to allow proper detection of
the end of the sequence.
Note: When subscripting a class, the special class method __class_getitem__() may be called instead
of __getitem__(). See __class_getitem__ versus __getitem__ for more details.
object.__setitem__(self, key, value)
Called to implement assignment to self[key]. Same note as for __getitem__(). This should only be
implemented for mappings if the objects support changes to the values for keys, or if new keys can be added,
or for sequences if elements can be replaced. The same exceptions should be raised for improper key values as
for the __getitem__() method.
object.__delitem__(self, key)
Called to implement deletion of self[key]. Same note as for __getitem__(). This should only be
implemented for mappings if the objects support removal of keys, or for sequences if elements can be removed
from the sequence. The same exceptions should be raised for improper key values as for the __getitem__()
method.
object.__missing__(self, key)
Called by dict.__getitem__() to implement self[key] for dict subclasses when key is not in the
dictionary.
object.__iter__(self)
This method is called when an iterator is required for a container. This method should return a new iterator
object that can iterate over all the objects in the container. For mappings, it should iterate over the keys of the
container.
42 Chapter 3. Data model
The Python Language Reference, Release 3.12.0
object.__reversed__(self)
Called (if present) by the reversed() built-in to implement reverse iteration. It should return a new iterator
object that iterates over all the objects in the container in reverse order.
If the __reversed__() method is not provided, the reversed() built-in will fall back to using the
sequence protocol (__len__() and __getitem__()). Objects that support the sequence protocol should
only provide __reversed__() if they can provide an implementation that is more efficient than the one
provided by reversed().
The membership test operators (in and not in) are normally implemented as an iteration through a container.
However, container objects can supply the following special method with a more efficient implementation, which also
does not require the object be iterable.
object.__contains__(self, item)
Called to implement membership test operators. Should return true if item is in self, false otherwise. For
mapping objects, this should consider the keys of the mapping rather than the values or the key-item pairs.
For objects that don’t define __contains__(), the membership test first tries iteration via __iter__(),
then the old sequence iteration protocol via __getitem__(), see this section in the language reference.
3.3.8 Emulating numeric types
The following methods can be defined to emulate numeric objects. Methods corresponding to operations that are not
supported by the particular kind of number implemented (e.g., bitwise operations for non-integral numbers) should
be left undefined.
object.__add__(self, other)
object.__sub__(self, other)
object.__mul__(self, other)
object.__matmul__(self, other)
object.__truediv__(self, other)
object.__floordiv__(self, other)
object.__mod__(self, other)
object.__divmod__(self, other)
object.__pow__(self, other[, modulo ])
object.__lshift__(self, other)
object.__rshift__(self, other)
object.__and__(self, other)
object.__xor__(self, other)
object.__or__(self, other)
These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(),
pow(), **, <<, >>, &, ^, |). For instance, to evaluate the expression x + y, where x is an instance of
a class that has an __add__() method, type(x).__add__(x, y) is called. The __divmod__()
method should be the equivalent to using __floordiv__() and __mod__(); it should not be related to
__truediv__(). Note that __pow__() should be defined to accept an optional third argument if the
ternary version of the built-in pow() function is to be supported.
If one of those methods does not support the operation with the supplied arguments, it should return NotIm-
plemented.
object.__radd__(self, other)
object.__rsub__(self, other)
object.__rmul__(self, other)
object.__rmatmul__(self, other)
object.__rtruediv__(self, other)
object.__rfloordiv__(self, other)
3.3. Special method names 43
The Python Language Reference, Release 3.12.0
object.__rmod__(self, other)
object.__rdivmod__(self, other)
object.__rpow__(self, other[, modulo ])
object.__rlshift__(self, other)
object.__rrshift__(self, other)
object.__rand__(self, other)
object.__rxor__(self, other)
object.__ror__(self, other)
These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(),
pow(), **, <<, >>, &, ^, |) with reflected (swapped) operands. These functions are only called if the left
operand does not support the corresponding operation3 and the operands are of different types.4 For instance,
to evaluate the expression x - y, where y is an instance of a class that has an __rsub__() method,
type(y).__rsub__(y, x) is called if type(x).__sub__(x, y) returns NotImplemented.
Note that ternary pow() will not try calling __rpow__() (the coercion rules would become too compli-
cated).
Note: If the right operand’s type is a subclass of the left operand’s type and that subclass provides a different
implementation of the reflected method for the operation, this method will be called before the left operand’s
non-reflected method. This behavior allows subclasses to override their ancestors’ operations.
object.__iadd__(self, other)
object.__isub__(self, other)
object.__imul__(self, other)
object.__imatmul__(self, other)
object.__itruediv__(self, other)
object.__ifloordiv__(self, other)
object.__imod__(self, other)
object.__ipow__(self, other[, modulo ])
object.__ilshift__(self, other)
object.__irshift__(self, other)
object.__iand__(self, other)
object.__ixor__(self, other)
object.__ior__(self, other)
These methods are called to implement the augmented arithmetic assignments (+=, -=, *=, @=, /=, //=, %=,
**=, <<=, >>=, &=, ^=, |=). These methods should attempt to do the operation in-place (modifying self)
and return the result (which could be, but does not have to be, self). If a specific method is not defined, the
augmented assignment falls back to the normal methods. For instance, if x is an instance of a class with an
__iadd__() method, x += y is equivalent to x = x.__iadd__(y) . Otherwise, x.__add__(y)
and y.__radd__(x) are considered, as with the evaluation of x + y. In certain situations, augmented
assignment can result in unexpected errors (see faq-augmented-assignment-tuple-error), but this behavior is in
fact part of the data model.
object.__neg__(self)
object.__pos__(self)
object.__abs__(self)
3 “Does not support” here means that the class has no such method, or the method returns NotImplemented. Do not set the method to
None if you want to force fallback to the right operand’s reflected method—that will instead have the opposite effect of explicitly blocking such
fallback.
4 For operands of the same type, it is assumed that if the non-reflected method – such as __add__() – fails then the overall operation is not
supported, which is why the reflected method is not called.
44 Chapter 3. Data model
The Python Language Reference, Release 3.12.0
object.__invert__(self)
Called to implement the unary arithmetic operations (-, +, abs() and ~).
object.__complex__(self)
object.__int__(self)
object.__float__(self)
Called to implement the built-in functions complex(), int() and float(). Should return a value of the
appropriate type.
object.__index__(self)
Called to implement operator.index(), and whenever Python needs to losslessly convert the numeric
object to an integer object (such as in slicing, or in the built-in bin(), hex() and oct() functions). Presence
of this method indicates that the numeric object is an integer type. Must return an integer.
If __int__(), __float__() and __complex__() are not defined then corresponding built-in func-
tions int(), float() and complex() fall back to __index__().
object.__round__(self[, ndigits ])
object.__trunc__(self)
object.__floor__(self)
object.__ceil__(self)
Called to implement the built-in function round() and math functions trunc(), floor() and ceil().
Unless ndigits is passed to __round__() all these methods should return the value of the object truncated
to an Integral (typically an int).
The built-in function int() falls back to __trunc__() if neither __int__() nor __index__() is
defined.
Changed in version 3.11: The delegation of int() to __trunc__() is deprecated.
3.3.9 With Statement Context Managers
A context manager is an object that defines the runtime context to be established when executing a with statement.
The context manager handles the entry into, and the exit from, the desired runtime context for the execution of the
block of code. Context managers are normally invoked using the with statement (described in section The with
statement), but can also be used by directly invoking their methods.
Typical uses of context managers include saving and restoring various kinds of global state, locking and unlocking
resources, closing opened files, etc.
For more information on context managers, see typecontextmanager.
object.__enter__(self)
Enter the runtime context related to this object. The with statement will bind this method’s return value to
the target(s) specified in the as clause of the statement, if any.
object.__exit__(self, exc_type, exc_value, traceback)
Exit the runtime context related to this object. The parameters describe the exception that caused the context
to be exited. If the context was exited without an exception, all three arguments will be None.
If an exception is supplied, and the method wishes to suppress the exception (i.e., prevent it from being prop-
agated), it should return a true value. Otherwise, the exception will be processed normally upon exit from this
method.
Note that __exit__() methods should not reraise the passed-in exception; this is the caller’s responsibility.
See also:
PEP 343 - The “with” statement The specification, background, and examples for the Python with statement.
3.3. Special method names 45
The Python Language Reference, Release 3.12.0
3.3.10 Customizing positional arguments in class pattern matching
When using a class name in a pattern, positional arguments in the pattern are not allowed by default, i.e. case
MyClass(x, y) is typically invalid without special support in MyClass. To be able to use that kind of pattern,
the class needs to define a __match_args__ attribute.
object.__match_args__
This class variable can be assigned a tuple of strings. When this class is used in a class pattern with positional
arguments, each positional argument will be converted into a keyword argument, using the corresponding value
in __match_args__ as the keyword. The absence of this attribute is equivalent to setting it to ().
For example, if MyClass.__match_args__ is ("left", "center", "right") that means that case
MyClass(x, y) is equivalent to case MyClass(left=x, center=y). Note that the number of arguments
in the pattern must be smaller than or equal to the number of elements in __match_args__; if it is larger, the pattern
match attempt will raise a TypeError.
New in version 3.10.
See also:
PEP 634 - Structural Pattern Matching The specification for the Python match statement.
3.3.11 Emulating buffer types
The buffer protocol provides a way for Python objects to expose efficient access to a low-level memory array. This
protocol is implemented by builtin types such as bytes and memoryview, and third-party libraries may define
additional buffer types.
While buffer types are usually implemented in C, it is also possible to implement the protocol in Python.
object.__buffer__(self, flags)
Called when a buffer is requested from self (for example, by the memoryview constructor). The flags argu-
ment is an integer representing the kind of buffer requested, affecting for example whether the returned buffer
is read-only or writable. inspect.BufferFlags provides a convenient way to interpret the flags. The
method must return a memoryview object.
object.__release_buffer__(self, buffer)
Called when a buffer is no longer needed. The buffer argument is a memoryview object that was previously
returned by __buffer__(). The method must release any resources associated with the buffer. This method
should return None. Buffer objects that do not need to perform any cleanup are not required to implement this
method.
New in version 3.12.
See also:
PEP 688 - Making the buffer protocol accessible in Python Introduces the Python __buffer__ and __re-
lease_buffer__ methods.
collections.abc.Buffer ABC for buffer types.
3.3.12 Special method lookup
For custom classes, implicit invocations of special methods are only guaranteed to work correctly if defined on an
object’s type, not in the object’s instance dictionary. That behaviour is the reason why the following code raises an
exception:
>>> class C:
... pass
...
>>> c = C()
(continues on next page)
46 Chapter 3. Data model
The Python Language Reference, Release 3.12.0
(continued from previous page)
>>> c.__len__ = lambda: 5
>>> len(c)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: object of type 'C' has no len()
The rationale behind this behaviour lies with a number of special methods such as __hash__() and __repr__()
that are implemented by all objects, including type objects. If the implicit lookup of these methods used the conven-
tional lookup process, they would fail when invoked on the type object itself:
>>> 1 .__hash__() == hash(1)
True
>>> int.__hash__() == hash(int)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: descriptor '__hash__' of 'int' object needs an argument
Incorrectly attempting to invoke an unbound method of a class in this way is sometimes referred to as ‘metaclass
confusion’, and is avoided by bypassing the instance when looking up special methods:
>>> type(1).__hash__(1) == hash(1)
True
>>> type(int).__hash__(int) == hash(int)
True
In addition to bypassing any instance attributes in the interest of correctness, implicit special method lookup generally
also bypasses the __getattribute__() method even of the object’s metaclass:
>>> class Meta(type):
... def __getattribute__(*args):
... print("Metaclass getattribute invoked")
... return type.__getattribute__(*args)
...
>>> class C(object, metaclass=Meta):
... def __len__(self):
... return 10
... def __getattribute__(*args):
... print("Class getattribute invoked")
... return object.__getattribute__(*args)
...
>>> c = C()
>>> c.__len__() # Explicit lookup via instance
Class getattribute invoked
10
>>> type(c).__len__(c) # Explicit lookup via type
Metaclass getattribute invoked
10
>>> len(c) # Implicit lookup
10
Bypassing the __getattribute__() machinery in this fashion provides significant scope for speed optimisations
within the interpreter, at the cost of some flexibility in the handling of special methods (the special method must be
set on the class object itself in order to be consistently invoked by the interpreter).
3.3. Special method names 47
The Python Language Reference, Release 3.12.0
3.4 Coroutines
3.4.1 Awaitable Objects
An awaitable object generally implements an __await__() method. Coroutine objects returned from async def
functions are awaitable.
Note: The generator iterator objects returned from generators decorated with types.coroutine() are also
awaitable, but they do not implement __await__().
object.__await__(self)
Must return an iterator. Should be used to implement awaitable objects. For instance, asyncio.Future
implements this method to be compatible with the await expression.
Note: The language doesn’t place any restriction on the type or value of the objects yielded by the iterator
returned by __await__, as this is specific to the implementation of the asynchronous execution framework
(e.g. asyncio) that will be managing the awaitable object.
New in version 3.5.
See also:
PEP 492 for additional information about awaitable objects.
3.4.2 Coroutine Objects
Coroutine objects are awaitable objects. A coroutine’s execution can be controlled by calling __await__() and
iterating over the result. When the coroutine has finished executing and returns, the iterator raises StopIteration,
and the exception’s value attribute holds the return value. If the coroutine raises an exception, it is propagated by
the iterator. Coroutines should not directly raise unhandled StopIteration exceptions.
Coroutines also have the methods listed below, which are analogous to those of generators (see Generator-iterator
methods). However, unlike generators, coroutines do not directly support iteration.
Changed in version 3.5.2: It is a RuntimeError to await on a coroutine more than once.
coroutine.send(value)
Starts or resumes execution of the coroutine. If value is None, this is equivalent to advancing the iterator
returned by __await__(). If value is not None, this method delegates to the send() method of the
iterator that caused the coroutine to suspend. The result (return value, StopIteration, or other exception)
is the same as when iterating over the __await__() return value, described above.
coroutine.throw(value)
coroutine.throw(type[, value[, traceback ]])
Raises the specified exception in the coroutine. This method delegates to the throw() method of the iterator
that caused the coroutine to suspend, if it has such a method. Otherwise, the exception is raised at the suspension
point. The result (return value, StopIteration, or other exception) is the same as when iterating over the
__await__() return value, described above. If the exception is not caught in the coroutine, it propagates
back to the caller.
Changed in version 3.12: The second signature (type[, value[, traceback]]) is deprecated and may be removed
in a future version of Python.
coroutine.close()
Causes the coroutine to clean itself up and exit. If the coroutine is suspended, this method first delegates to the
close() method of the iterator that caused the coroutine to suspend, if it has such a method. Then it raises
48 Chapter 3. Data model
The Python Language Reference, Release 3.12.0
GeneratorExit at the suspension point, causing the coroutine to immediately clean itself up. Finally, the
coroutine is marked as having finished executing, even if it was never started.
Coroutine objects are automatically closed using the above process when they are about to be destroyed.
3.4.3 Asynchronous Iterators
An asynchronous iterator can call asynchronous code in its __anext__ method.
Asynchronous iterators can be used in an async for statement.
object.__aiter__(self)
Must return an asynchronous iterator object.
object.__anext__(self)
Must return an awaitable resulting in a next value of the iterator. Should raise a StopAsyncIteration
error when the iteration is over.
An example of an asynchronous iterable object:
class Reader:
async def readline(self):
...
def __aiter__(self):
return self
async def __anext__(self):
val = await self.readline()
if val == b'':
raise StopAsyncIteration
return val
New in version 3.5.
Changed in version 3.7: Prior to Python 3.7, __aiter__() could return an awaitable that would resolve to an
asynchronous iterator.
Starting with Python 3.7, __aiter__() must return an asynchronous iterator object. Returning anything else will
result in a TypeError error.
3.4.4 Asynchronous Context Managers
An asynchronous context manager is a context manager that is able to suspend execution in its __aenter__ and
__aexit__ methods.
Asynchronous context managers can be used in an async with statement.
object.__aenter__(self)
Semantically similar to __enter__(), the only difference being that it must return an awaitable.
object.__aexit__(self, exc_type, exc_value, traceback)
Semantically similar to __exit__(), the only difference being that it must return an awaitable.
An example of an asynchronous context manager class:
class AsyncContextManager:
async def __aenter__(self):
await log('entering context')
async def __aexit__(self, exc_type, exc, tb):
await log('exiting context')
3.4. Coroutines 49
The Python Language Reference, Release 3.12.0
New in version 3.5.
50 Chapter 3. Data model
CHAPTER
FOUR
EXECUTION MODEL
4.1 Structure of a program
A Python program is constructed from code blocks. A block is a piece of Python program text that is executed as a
unit. The following are blocks: a module, a function body, and a class definition. Each command typed interactively
is a block. A script file (a file given as standard input to the interpreter or specified as a command line argument to
the interpreter) is a code block. A script command (a command specified on the interpreter command line with the
-c option) is a code block. A module run as a top level script (as module __main__) from the command line using
a -m argument is also a code block. The string argument passed to the built-in functions eval() and exec() is a
code block.
A code block is executed in an execution frame. A frame contains some administrative information (used for debug-
ging) and determines where and how execution continues after the code block’s execution has completed.
4.2 Naming and binding
4.2.1 Binding of names
Names refer to objects. Names are introduced by name binding operations.
The following constructs bind names:
• formal parameters to functions,
• class definitions,
• function definitions,
• assignment expressions,
• targets that are identifiers if occurring in an assignment:
– for loop header,
– after as in a with statement, except clause, except* clause, or in the as-pattern in structural pattern
matching,
– in a capture pattern in structural pattern matching
• import statements.
• type statements.
• type parameter lists.
The import statement of the form from ... import * binds all names defined in the imported module,
except those beginning with an underscore. This form may only be used at the module level.
A target occurring in a del statement is also considered bound for this purpose (though the actual semantics are to
unbind the name).
51
The Python Language Reference, Release 3.12.0
Each assignment or import statement occurs within a block defined by a class or function definition or at the module
level (the top-level code block).
If a name is bound in a block, it is a local variable of that block, unless declared as nonlocal or global. If
a name is bound at the module level, it is a global variable. (The variables of the module code block are local and
global.) If a variable is used in a code block but not defined there, it is a free variable.
Each occurrence of a name in the program text refers to the binding of that name established by the following name
resolution rules.
4.2.2 Resolution of names
A scope defines the visibility of a name within a block. If a local variable is defined in a block, its scope includes that
block. If the definition occurs in a function block, the scope extends to any blocks contained within the defining one,
unless a contained block introduces a different binding for the name.
When a name is used in a code block, it is resolved using the nearest enclosing scope. The set of all such scopes
visible to a code block is called the block’s environment.
When a name is not found at all, a NameError exception is raised. If the current scope is a function scope, and
the name refers to a local variable that has not yet been bound to a value at the point where the name is used, an
UnboundLocalError exception is raised. UnboundLocalError is a subclass of NameError.
If a name binding operation occurs anywhere within a code block, all uses of the name within the block are treated
as references to the current block. This can lead to errors when a name is used within a block before it is bound. This
rule is subtle. Python lacks declarations and allows name binding operations to occur anywhere within a code block.
The local variables of a code block can be determined by scanning the entire text of the block for name binding
operations. See the FAQ entry on UnboundLocalError for examples.
If the global statement occurs within a block, all uses of the names specified in the statement refer to the bindings
of those names in the top-level namespace. Names are resolved in the top-level namespace by searching the global
namespace, i.e. the namespace of the module containing the code block, and the builtins namespace, the namespace
of the module builtins. The global namespace is searched first. If the names are not found there, the builtins
namespace is searched. The global statement must precede all uses of the listed names.
The global statement has the same scope as a name binding operation in the same block. If the nearest enclosing
scope for a free variable contains a global statement, the free variable is treated as a global.
The nonlocal statement causes corresponding names to refer to previously bound variables in the nearest enclosing
function scope. SyntaxError is raised at compile time if the given name does not exist in any enclosing function
scope. Type parameters cannot be rebound with the nonlocal statement.
The namespace for a module is automatically created the first time a module is imported. The main module for a
script is always called __main__.
Class definition blocks and arguments to exec() and eval() are special in the context of name resolution. A
class definition is an executable statement that may use and define names. These references follow the normal rules
for name resolution with an exception that unbound local variables are looked up in the global namespace. The
namespace of the class definition becomes the attribute dictionary of the class. The scope of names defined in a class
block is limited to the class block; it does not extend to the code blocks of methods. This includes comprehensions
and generator expressions, but it does not include annotation scopes, which have access to their enclosing class scopes.
This means that the following will fail:
class A:
a = 42
b = list(a + i for i in range(10))
However, the following will succeed:
class A:
type Alias = Nested
class Nested: pass
(continues on next page)
52 Chapter 4. Execution model
The Python Language Reference, Release 3.12.0
(continued from previous page)
print(A.Alias.__value__) # <type 'A.Nested'>
4.2.3 Annotation scopes
Type parameter lists and type statements introduce annotation scopes, which behave mostly like function scopes,
but with some exceptions discussed below. Annotations currently do not use annotation scopes, but they are expected
to use annotation scopes in Python 3.13 when PEP 649 is implemented.
Annotation scopes are used in the following contexts:
• Type parameter lists for generic type aliases.
• Type parameter lists for generic functions. A generic function’s annotations are executed within the annotation
scope, but its defaults and decorators are not.
• Type parameter lists for generic classes. A generic class’s base classes and keyword arguments are executed
within the annotation scope, but its decorators are not.
• The bounds and constraints for type variables (lazily evaluated).
• The value of type aliases (lazily evaluated).
Annotation scopes differ from function scopes in the following ways:
• Annotation scopes have access to their enclosing class namespace. If an annotation scope is immediately
within a class scope, or within another annotation scope that is immediately within a class scope, the code in
the annotation scope can use names defined in the class scope as if it were executed directly within the class
body. This contrasts with regular functions defined within classes, which cannot access names defined in the
class scope.
• Expressions in annotation scopes cannot contain yield, yield from, await, or := expressions. (These
expressions are allowed in other scopes contained within the annotation scope.)
• Names defined in annotation scopes cannot be rebound with nonlocal statements in inner scopes. This
includes only type parameters, as no other syntactic elements that can appear within annotation scopes can
introduce new names.
• While annotation scopes have an internal name, that name is not reflected in the __qualname__ of objects
defined within the scope. Instead, the __qualname__ of such objects is as if the object were defined in the
enclosing scope.
New in version 3.12: Annotation scopes were introduced in Python 3.12 as part of PEP 695.
4.2.4 Lazy evaluation
The values of type aliases created through the type statement are lazily evaluated. The same applies to the bounds
and constraints of type variables created through the type parameter syntax. This means that they are not evaluated
when the type alias or type variable is created. Instead, they are only evaluated when doing so is necessary to resolve
an attribute access.
Example:
>>> type Alias = 1/0
>>> Alias.__value__
Traceback (most recent call last):
...
ZeroDivisionError: division by zero
>>> def func[T: 1/0](): pass
>>> T = func.__type_params__[0]
>>> T.__bound__
(continues on next page)
4.2. Naming and binding 53
The Python Language Reference, Release 3.12.0
(continued from previous page)
Traceback (most recent call last):
...
ZeroDivisionError: division by zero
Here the exception is raised only when the __value__ attribute of the type alias or the __bound__ attribute of
the type variable is accessed.
This behavior is primarily useful for references to types that have not yet been defined when the type alias or type
variable is created. For example, lazy evaluation enables creation of mutually recursive type aliases:
from typing import Literal
type SimpleExpr = int | Parenthesized
type Parenthesized = tuple[Literal["("], Expr, Literal[")"]]
type Expr = SimpleExpr | tuple[SimpleExpr, Literal["+", "-"], Expr]
Lazily evaluated values are evaluated in annotation scope, which means that names that appear inside the lazily eval-
uated value are looked up as if they were used in the immediately enclosing scope.
New in version 3.12.
4.2.5 Builtins and restricted execution
CPython implementation detail: Users should not touch __builtins__; it is strictly an implementation detail.
Users wanting to override values in the builtins namespace should import the builtins module and modify its
attributes appropriately.
The builtins namespace associated with the execution of a code block is actually found by looking up the name
__builtins__ in its global namespace; this should be a dictionary or a module (in the latter case the module’s dic-
tionary is used). By default, when in the __main__ module, __builtins__ is the built-in module builtins;
when in any other module, __builtins__ is an alias for the dictionary of the builtins module itself.
4.2.6 Interaction with dynamic features
Name resolution of free variables occurs at runtime, not at compile time. This means that the following code will
print 42:
i = 10
def f():
print(i)
i = 42
f()
The eval() and exec() functions do not have access to the full environment for resolving names. Names may
be resolved in the local and global namespaces of the caller. Free variables are not resolved in the nearest enclosing
namespace, but in the global namespace.1 The exec() and eval() functions have optional arguments to override
the global and local namespace. If only one namespace is specified, it is used for both.
1 This limitation occurs because the code that is executed by these operations is not available at the time the module is compiled.
54 Chapter 4. Execution model
The Python Language Reference, Release 3.12.0
4.3 Exceptions
Exceptions are a means of breaking out of the normal flow of control of a code block in order to handle errors or
other exceptional conditions. An exception is raised at the point where the error is detected; it may be handled by
the surrounding code block or by any code block that directly or indirectly invoked the code block where the error
occurred.
The Python interpreter raises an exception when it detects a run-time error (such as division by zero). A Python
program can also explicitly raise an exception with the raise statement. Exception handlers are specified with the
try … except statement. The finally clause of such a statement can be used to specify cleanup code which
does not handle the exception, but is executed whether an exception occurred or not in the preceding code.
Python uses the “termination” model of error handling: an exception handler can find out what happened and continue
execution at an outer level, but it cannot repair the cause of the error and retry the failing operation (except by re-
entering the offending piece of code from the top).
When an exception is not handled at all, the interpreter terminates execution of the program, or returns to its interactive
main loop. In either case, it prints a stack traceback, except when the exception is SystemExit.
Exceptions are identified by class instances. The except clause is selected depending on the class of the instance:
it must reference the class of the instance or a non-virtual base class thereof. The instance can be received by the
handler and can carry additional information about the exceptional condition.
Note: Exception messages are not part of the Python API. Their contents may change from one version of Python to
the next without warning and should not be relied on by code which will run under multiple versions of the interpreter.
See also the description of the try statement in section The try statement and raise statement in section The raise
statement.
4.3. Exceptions 55
The Python Language Reference, Release 3.12.0
56 Chapter 4. Execution model
CHAPTER
FIVE
THE IMPORT SYSTEM
Python code in one module gains access to the code in another module by the process of importing it. The im-
port statement is the most common way of invoking the import machinery, but it is not the only way. Functions
such as importlib.import_module() and built-in __import__() can also be used to invoke the import
machinery.
The import statement combines two operations; it searches for the named module, then it binds the results of
that search to a name in the local scope. The search operation of the import statement is defined as a call to
the __import__() function, with the appropriate arguments. The return value of __import__() is used to
perform the name binding operation of the import statement. See the import statement for the exact details of
that name binding operation.
A direct call to __import__() performs only the module search and, if found, the module creation operation.
While certain side-effects may occur, such as the importing of parent packages, and the updating of various caches
(including sys.modules), only the import statement performs a name binding operation.
When an import statement is executed, the standard builtin __import__() function is called. Other mecha-
nisms for invoking the import system (such as importlib.import_module()) may choose to bypass __im-
port__() and use their own solutions to implement import semantics.
When a module is first imported, Python searches for the module and if found, it creates a module object1, initializing
it. If the named module cannot be found, a ModuleNotFoundError is raised. Python implements various
strategies to search for the named module when the import machinery is invoked. These strategies can be modified
and extended by using various hooks described in the sections below.
Changed in version 3.3: The import system has been updated to fully implement the second phase of PEP 302.
There is no longer any implicit import machinery - the full import system is exposed through sys.meta_path. In
addition, native namespace package support has been implemented (see PEP 420).
5.1 importlib
The importlib module provides a rich API for interacting with the import system. For example importlib.
import_module() provides a recommended, simpler API than built-in __import__() for invoking the im-
port machinery. Refer to the importlib library documentation for additional detail.
1 See types.ModuleType.
57
The Python Language Reference, Release 3.12.0
5.2 Packages
Python has only one type of module object, and all modules are of this type, regardless of whether the module is
implemented in Python, C, or something else. To help organize modules and provide a naming hierarchy, Python has
a concept of packages.
You can think of packages as the directories on a file system and modules as files within directories, but don’t take
this analogy too literally since packages and modules need not originate from the file system. For the purposes of this
documentation, we’ll use this convenient analogy of directories and files. Like file system directories, packages are
organized hierarchically, and packages may themselves contain subpackages, as well as regular modules.
It’s important to keep in mind that all packages are modules, but not all modules are packages. Or put another
way, packages are just a special kind of module. Specifically, any module that contains a __path__ attribute is
considered a package.
All modules have a name. Subpackage names are separated from their parent package name by a dot, akin to Python’s
standard attribute access syntax. Thus you might have a package called email, which in turn has a subpackage called
email.mime and a module within that subpackage called email.mime.text.
5.2.1 Regular packages
Python defines two types of packages, regular packages and namespace packages. Regular packages are traditional
packages as they existed in Python 3.2 and earlier. A regular package is typically implemented as a directory contain-
ing an __init__.py file. When a regular package is imported, this __init__.py file is implicitly executed,
and the objects it defines are bound to names in the package’s namespace. The __init__.py file can contain the
same Python code that any other module can contain, and Python will add some additional attributes to the module
when it is imported.
For example, the following file system layout defines a top level parent package with three subpackages:
parent/
__init__.py
one/
__init__.py
two/
__init__.py
three/
__init__.py
Importing parent.one will implicitly execute parent/__init__.py and parent/one/__init__.
py. Subsequent imports of parent.two or parent.three will execute parent/two/__init__.py and
parent/three/__init__.py respectively.
5.2.2 Namespace packages
A namespace package is a composite of various portions, where each portion contributes a subpackage to the parent
package. Portions may reside in different locations on the file system. Portions may also be found in zip files, on
the network, or anywhere else that Python searches during import. Namespace packages may or may not correspond
directly to objects on the file system; they may be virtual modules that have no concrete representation.
Namespace packages do not use an ordinary list for their __path__ attribute. They instead use a custom iterable
type which will automatically perform a new search for package portions on the next import attempt within that
package if the path of their parent package (or sys.path for a top level package) changes.
With namespace packages, there is no parent/__init__.py file. In fact, there may be multiple parent
directories found during import search, where each one is provided by a different portion. Thus parent/one
may not be physically located next to parent/two. In this case, Python will create a namespace package for the
top-level parent package whenever it or one of its subpackages is imported.
See also PEP 420 for the namespace package specification.
58 Chapter 5. The import system
The Python Language Reference, Release 3.12.0
5.3 Searching
To begin the search, Python needs the fully qualified name of the module (or package, but for the purposes of this dis-
cussion, the difference is immaterial) being imported. This name may come from various arguments to the import
statement, or from the parameters to the importlib.import_module() or __import__() functions.
This name will be used in various phases of the import search, and it may be the dotted path to a submodule, e.g.
foo.bar.baz. In this case, Python first tries to import foo, then foo.bar, and finally foo.bar.baz. If any
of the intermediate imports fail, a ModuleNotFoundError is raised.
5.3.1 The module cache
The first place checked during import search is sys.modules. This mapping serves as a cache of all modules that
have been previously imported, including the intermediate paths. So if foo.bar.baz was previously imported,
sys.modules will contain entries for foo, foo.bar, and foo.bar.baz. Each key will have as its value the
corresponding module object.
During import, the module name is looked up in sys.modules and if present, the associated value is the module
satisfying the import, and the process completes. However, if the value is None, then a ModuleNotFoundError
is raised. If the module name is missing, Python will continue searching for the module.
sys.modules is writable. Deleting a key may not destroy the associated module (as other modules may hold
references to it), but it will invalidate the cache entry for the named module, causing Python to search anew for the
named module upon its next import. The key can also be assigned to None, forcing the next import of the module
to result in a ModuleNotFoundError.
Beware though, as if you keep a reference to the module object, invalidate its cache entry in sys.modules, and then
re-import the named module, the two module objects will not be the same. By contrast, importlib.reload()
will reuse the same module object, and simply reinitialise the module contents by rerunning the module’s code.
5.3.2 Finders and loaders
If the named module is not found in sys.modules, then Python’s import protocol is invoked to find and load the
module. This protocol consists of two conceptual objects, finders and loaders. A finder’s job is to determine whether
it can find the named module using whatever strategy it knows about. Objects that implement both of these interfaces
are referred to as importers - they return themselves when they find that they can load the requested module.
Python includes a number of default finders and importers. The first one knows how to locate built-in modules, and
the second knows how to locate frozen modules. A third default finder searches an import path for modules. The
import path is a list of locations that may name file system paths or zip files. It can also be extended to search for any
locatable resource, such as those identified by URLs.
The import machinery is extensible, so new finders can be added to extend the range and scope of module searching.
Finders do not actually load modules. If they can find the named module, they return a module spec, an encapsulation
of the module’s import-related information, which the import machinery then uses when loading the module.
The following sections describe the protocol for finders and loaders in more detail, including how you can create and
register new ones to extend the import machinery.
Changed in version 3.4: In previous versions of Python, finders returned loaders directly, whereas now they return
module specs which contain loaders. Loaders are still used during import but have fewer responsibilities.
5.3. Searching 59
The Python Language Reference, Release 3.12.0
5.3.3 Import hooks
The import machinery is designed to be extensible; the primary mechanism for this are the import hooks. There are
two types of import hooks: meta hooks and import path hooks.
Meta hooks are called at the start of import processing, before any other import processing has occurred, other than
sys.modules cache look up. This allows meta hooks to override sys.path processing, frozen modules, or even
built-in modules. Meta hooks are registered by adding new finder objects to sys.meta_path, as described below.
Import path hooks are called as part of sys.path (or package.__path__) processing, at the point where their
associated path item is encountered. Import path hooks are registered by adding new callables to sys.path_hooks
as described below.
5.3.4 The meta path
When the named module is not found in sys.modules, Python next searches sys.meta_path, which contains
a list of meta path finder objects. These finders are queried in order to see if they know how to handle the named
module. Meta path finders must implement a method called find_spec() which takes three arguments: a name,
an import path, and (optionally) a target module. The meta path finder can use any strategy it wants to determine
whether it can handle the named module or not.
If the meta path finder knows how to handle the named module, it returns a spec object. If it cannot handle the named
module, it returns None. If sys.meta_path processing reaches the end of its list without returning a spec, then
a ModuleNotFoundError is raised. Any other exceptions raised are simply propagated up, aborting the import
process.
The find_spec() method of meta path finders is called with two or three arguments. The first is the fully qualified
name of the module being imported, for example foo.bar.baz. The second argument is the path entries to use
for the module search. For top-level modules, the second argument is None, but for submodules or subpackages, the
second argument is the value of the parent package’s __path__ attribute. If the appropriate __path__ attribute
cannot be accessed, a ModuleNotFoundError is raised. The third argument is an existing module object that
will be the target of loading later. The import system passes in a target module only during reload.
The meta path may be traversed multiple times for a single import request. For example, assuming none of the mod-
ules involved has already been cached, importing foo.bar.baz will first perform a top level import, calling mpf.
find_spec("foo", None, None) on each meta path finder (mpf). After foo has been imported, foo.
bar will be imported by traversing the meta path a second time, calling mpf.find_spec("foo.bar", foo.
__path__, None). Once foo.bar has been imported, the final traversal will call mpf.find_spec("foo.
bar.baz", foo.bar.__path__, None).
Some meta path finders only support top level imports. These importers will always return None when anything
other than None is passed as the second argument.
Python’s default sys.meta_path has three meta path finders, one that knows how to import built-in modules, one
that knows how to import frozen modules, and one that knows how to import modules from an import path (i.e. the
path based finder).
Changed in version 3.4: The find_spec() method of meta path finders replaced find_module(), which is
now deprecated. While it will continue to work without change, the import machinery will try it only if the finder
does not implement find_spec().
Changed in version 3.10: Use of find_module() by the import system now raises ImportWarning.
Changed in version 3.12: find_module() has been removed. Use find_spec() instead.
60 Chapter 5. The import system
The Python Language Reference, Release 3.12.0
5.4 Loading
If and when a module spec is found, the import machinery will use it (and the loader it contains) when loading the
module. Here is an approximation of what happens during the loading portion of import:
module = None
if spec.loader is not None and hasattr(spec.loader, 'create_module'):
# It is assumed 'exec_module' will also be defined on the loader.
module = spec.loader.create_module(spec)
if module is None:
module = ModuleType(spec.name)
# The import-related module attributes get set here:
_init_module_attrs(spec, module)
if spec.loader is None:
# unsupported
raise ImportError
if spec.origin is None and spec.submodule_search_locations is not None:
# namespace package
sys.modules[spec.name] = module
elif not hasattr(spec.loader, 'exec_module'):
module = spec.loader.load_module(spec.name)
else:
sys.modules[spec.name] = module
try:
spec.loader.exec_module(module)
except BaseException:
try:
del sys.modules[spec.name]
except KeyError:
pass
raise
return sys.modules[spec.name]
Note the following details:
• If there is an existing module object with the given name in sys.modules, import will have already returned
it.
• The module will exist in sys.modules before the loader executes the module code. This is crucial because
the module code may (directly or indirectly) import itself; adding it to sys.modules beforehand prevents
unbounded recursion in the worst case and multiple loading in the best.
• If loading fails, the failing module – and only the failing module – gets removed from sys.modules. Any
module already in the sys.modules cache, and any module that was successfully loaded as a side-effect, must
remain in the cache. This contrasts with reloading where even the failing module is left in sys.modules.
• After the module is created but before execution, the import machinery sets the import-related module at-
tributes (“_init_module_attrs” in the pseudo-code example above), as summarized in a later section.
• Module execution is the key moment of loading in which the module’s namespace gets populated. Execution
is entirely delegated to the loader, which gets to decide what gets populated and how.
• The module created during loading and passed to exec_module() may not be the one returned at the end of
import2.
Changed in version 3.4: The import system has taken over the boilerplate responsibilities of loaders. These were
previously performed by the importlib.abc.Loader.load_module() method.
2 The importlib implementation avoids using the return value directly. Instead, it gets the module object by looking the module name up in
sys.modules. The indirect effect of this is that an imported module may replace itself in sys.modules. This is implementation-specific
behavior that is not guaranteed to work in other Python implementations.
5.4. Loading 61
The Python Language Reference, Release 3.12.0
5.4.1 Loaders
Module loaders provide the critical function of loading: module execution. The import machinery calls the
importlib.abc.Loader.exec_module() method with a single argument, the module object to execute.
Any value returned from exec_module() is ignored.
Loaders must satisfy the following requirements:
• If the module is a Python module (as opposed to a built-in module or a dynamically loaded extension), the
loader should execute the module’s code in the module’s global name space (module.__dict__).
• If the loader cannot execute the module, it should raise an ImportError, although any other exception
raised during exec_module() will be propagated.
In many cases, the finder and loader can be the same object; in such cases the find_spec() method would just
return a spec with the loader set to self.
Module loaders may opt in to creating the module object during loading by implementing a create_module()
method. It takes one argument, the module spec, and returns the new module object to use during loading. cre-
ate_module() does not need to set any attributes on the module object. If the method returns None, the import
machinery will create the new module itself.
New in version 3.4: The create_module() method of loaders.
Changed in version 3.4: The load_module() method was replaced by exec_module() and the import ma-
chinery assumed all the boilerplate responsibilities of loading.
For compatibility with existing loaders, the import machinery will use the load_module() method of loaders
if it exists and the loader does not also implement exec_module(). However, load_module() has been
deprecated and loaders should implement exec_module() instead.
The load_module() method must implement all the boilerplate loading functionality described above in addition
to executing the module. All the same constraints apply, with some additional clarification:
• If there is an existing module object with the given name in sys.modules, the loader must use that existing
module. (Otherwise, importlib.reload() will not work correctly.) If the named module does not exist
in sys.modules, the loader must create a new module object and add it to sys.modules.
• The module must exist in sys.modules before the loader executes the module code, to prevent unbounded
recursion or multiple loading.
• If loading fails, the loader must remove any modules it has inserted into sys.modules, but it must remove
only the failing module(s), and only if the loader itself has loaded the module(s) explicitly.
Changed in version 3.5: A DeprecationWarning is raised when exec_module() is defined but cre-
ate_module() is not.
Changed in version 3.6: An ImportError is raised when exec_module() is defined but create_module()
is not.
Changed in version 3.10: Use of load_module() will raise ImportWarning.
5.4.2 Submodules
When a submodule is loaded using any mechanism (e.g. importlib APIs, the import or import-from
statements, or built-in __import__()) a binding is placed in the parent module’s namespace to the submodule
object. For example, if package spam has a submodule foo, after importing spam.foo, spam will have an
attribute foo which is bound to the submodule. Let’s say you have the following directory structure:
spam/
__init__.py
foo.py
and spam/__init__.py has the following line in it:
62 Chapter 5. The import system
The Python Language Reference, Release 3.12.0
from .foo import Foo
then executing the following puts name bindings for foo and Foo in the spam module:
>>> import spam
>>> spam.foo
<module 'spam.foo' from '/tmp/imports/spam/foo.py'>
>>> spam.Foo
<class 'spam.foo.Foo'>
Given Python’s familiar name binding rules this might seem surprising, but it’s actually a fundamental feature of the
import system. The invariant holding is that if you have sys.modules['spam'] and sys.modules['spam.
foo'] (as you would after the above import), the latter must appear as the foo attribute of the former.
5.4.3 Module spec
The import machinery uses a variety of information about each module during import, especially before loading. Most
of the information is common to all modules. The purpose of a module’s spec is to encapsulate this import-related
information on a per-module basis.
Using a spec during import allows state to be transferred between import system components, e.g. between the finder
that creates the module spec and the loader that executes it. Most importantly, it allows the import machinery to
perform the boilerplate operations of loading, whereas without a module spec the loader had that responsibility.
The module’s spec is exposed as the __spec__ attribute on a module object. See ModuleSpec for details on the
contents of the module spec.
New in version 3.4.
5.4.4 Import-related module attributes
The import machinery fills in these attributes on each module object during loading, based on the module’s spec,
before the loader executes the module.
It is strongly recommended that you rely on __spec__ and its attributes instead of any of the other individual
attributes listed below.
__name__
The __name__ attribute must be set to the fully qualified name of the module. This name is used to uniquely
identify the module in the import system.
__loader__
The __loader__ attribute must be set to the loader object that the import machinery used when loading
the module. This is mostly for introspection, but can be used for additional loader-specific functionality, for
example getting data associated with a loader.
It is strongly recommended that you rely on __spec__ instead instead of this attribute.
Changed in version 3.12: The value of __loader__ is expected to be the same as __spec__.loader.
The use of __loader__ is deprecated and slated for removal in Python 3.14.
__package__
The module’s __package__ attribute may be set. Its value must be a string, but it can be the same value
as its __name__. When the module is a package, its __package__ value should be set to its __name__.
When the module is not a package, __package__ should be set to the empty string for top-level modules,
or for submodules, to the parent package’s name. See PEP 366 for further details.
This attribute is used instead of __name__ to calculate explicit relative imports for main modules, as defined
in PEP 366.
It is strongly recommended that you rely on __spec__ instead instead of this attribute.
5.4. Loading 63
The Python Language Reference, Release 3.12.0
Changed in version 3.6: The value of __package__ is expected to be the same as __spec__.parent.
Changed in version 3.10: ImportWarning is raised if import falls back to __package__ instead of
parent.
Changed in version 3.12: Raise DeprecationWarning instead of ImportWarning when falling back
to __package__.
__spec__
The __spec__ attribute must be set to the module spec that was used when importing the module. Setting
__spec__ appropriately applies equally to modules initialized during interpreter startup. The one exception
is __main__, where __spec__ is set to None in some cases.
When __spec__.parent is not set, __package__ is used as a fallback.
New in version 3.4.
Changed in version 3.6: __spec__.parent is used as a fallback when __package__ is not defined.
__path__
If the module is a package (either regular or namespace), the module object’s __path__ attribute must be
set. The value must be iterable, but may be empty if __path__ has no further significance. If __path__ is
not empty, it must produce strings when iterated over. More details on the semantics of __path__ are given
below.
Non-package modules should not have a __path__ attribute.
__file__
__cached__
__file__ is optional (if set, value must be a string). It indicates the pathname of the file from which the
module was loaded (if loaded from a file), or the pathname of the shared library file for extension modules
loaded dynamically from a shared library. It might be missing for certain types of modules, such as C modules
that are statically linked into the interpreter, and the import system may opt to leave it unset if it has no semantic
meaning (e.g. a module loaded from a database).
If __file__ is set then the __cached__ attribute might also be set, which is the path to any compiled
version of the code (e.g. byte-compiled file). The file does not need to exist to set this attribute; the path can
simply point to where the compiled file would exist (see PEP 3147).
Note that __cached__ may be set even if __file__ is not set. However, that scenario is quite atypical.
Ultimately, the loader is what makes use of the module spec provided by the finder (from which __file__
and __cached__ are derived). So if a loader can load from a cached module but otherwise does not load
from a file, that atypical scenario may be appropriate.
It is strongly recommended that you rely on __spec__ instead instead of __cached__.
5.4.5 module.__path__
By definition, if a module has a __path__ attribute, it is a package.
A package’s __path__ attribute is used during imports of its subpackages. Within the import machinery, it func-
tions much the same as sys.path, i.e. providing a list of locations to search for modules during import. However,
__path__ is typically much more constrained than sys.path.
__path__ must be an iterable of strings, but it may be empty. The same rules used for sys.path also apply
to a package’s __path__, and sys.path_hooks (described below) are consulted when traversing a package’s
__path__.
A package’s __init__.py file may set or alter the package’s __path__ attribute, and this was typically the way
namespace packages were implemented prior to PEP 420. With the adoption of PEP 420, namespace packages no
longer need to supply __init__.py files containing only __path__ manipulation code; the import machinery
automatically sets __path__ correctly for the namespace package.
64 Chapter 5. The import system
The Python Language Reference, Release 3.12.0
5.4.6 Module reprs
By default, all modules have a usable repr, however depending on the attributes set above, and in the module’s spec,
you can more explicitly control the repr of module objects.
If the module has a spec (__spec__), the import machinery will try to generate a repr from it. If that fails or there
is no spec, the import system will craft a default repr using whatever information is available on the module. It will
try to use the module.__name__, module.__file__, and module.__loader__ as input into the repr,
with defaults for whatever information is missing.
Here are the exact rules used:
• If the module has a __spec__ attribute, the information in the spec is used to generate the repr. The “name”,
“loader”, “origin”, and “has_location” attributes are consulted.
• If the module has a __file__ attribute, this is used as part of the module’s repr.
• If the module has no __file__ but does have a __loader__ that is not None, then the loader’s repr is
used as part of the module’s repr.
• Otherwise, just use the module’s __name__ in the repr.
Changed in version 3.12: Use of module_repr(), having been deprecated since Python 3.4, was removed in
Python 3.12 and is no longer called during the resolution of a module’s repr.
5.4.7 Cached bytecode invalidation
Before Python loads cached bytecode from a .pyc file, it checks whether the cache is up-to-date with the source
.py file. By default, Python does this by storing the source’s last-modified timestamp and size in the cache file when
writing it. At runtime, the import system then validates the cache file by checking the stored metadata in the cache
file against the source’s metadata.
Python also supports “hash-based” cache files, which store a hash of the source file’s contents rather than its metadata.
There are two variants of hash-based .pyc files: checked and unchecked. For checked hash-based .pyc files,
Python validates the cache file by hashing the source file and comparing the resulting hash with the hash in the cache
file. If a checked hash-based cache file is found to be invalid, Python regenerates it and writes a new checked hash-
based cache file. For unchecked hash-based .pyc files, Python simply assumes the cache file is valid if it exists.
Hash-based .pyc files validation behavior may be overridden with the --check-hash-based-pycs flag.
Changed in version 3.7: Added hash-based .pyc files. Previously, Python only supported timestamp-based invali-
dation of bytecode caches.
5.5 The Path Based Finder
As mentioned previously, Python comes with several default meta path finders. One of these, called the path based
finder (PathFinder), searches an import path, which contains a list of path entries. Each path entry names a
location to search for modules.
The path based finder itself doesn’t know how to import anything. Instead, it traverses the individual path entries,
associating each of them with a path entry finder that knows how to handle that particular kind of path.
The default set of path entry finders implement all the semantics for finding modules on the file system, handling
special file types such as Python source code (.py files), Python byte code (.pyc files) and shared libraries (e.g.
.so files). When supported by the zipimport module in the standard library, the default path entry finders also
handle loading all of these file types (other than shared libraries) from zipfiles.
Path entries need not be limited to file system locations. They can refer to URLs, database queries, or any other
location that can be specified as a string.
The path based finder provides additional hooks and protocols so that you can extend and customize the types of
searchable path entries. For example, if you wanted to support path entries as network URLs, you could write a hook
5.5. The Path Based Finder 65
The Python Language Reference, Release 3.12.0
that implements HTTP semantics to find modules on the web. This hook (a callable) would return a path entry finder
supporting the protocol described below, which was then used to get a loader for the module from the web.
A word of warning: this section and the previous both use the term finder, distinguishing between them by using the
terms meta path finder and path entry finder. These two types of finders are very similar, support similar protocols,
and function in similar ways during the import process, but it’s important to keep in mind that they are subtly different.
In particular, meta path finders operate at the beginning of the import process, as keyed off the sys.meta_path
traversal.
By contrast, path entry finders are in a sense an implementation detail of the path based finder, and in fact, if the
path based finder were to be removed from sys.meta_path, none of the path entry finder semantics would be
invoked.
5.5.1 Path entry finders
The path based finder is responsible for finding and loading Python modules and packages whose location is specified
with a string path entry. Most path entries name locations in the file system, but they need not be limited to this.
As a meta path finder, the path based finder implements the find_spec() protocol previously described, however
it exposes additional hooks that can be used to customize how modules are found and loaded from the import path.
Three variables are used by the path based finder, sys.path, sys.path_hooks and sys.
path_importer_cache. The __path__ attributes on package objects are also used. These provide
additional ways that the import machinery can be customized.
sys.path contains a list of strings providing search locations for modules and packages. It is initialized from the
PYTHONPATH environment variable and various other installation- and implementation-specific defaults. Entries
in sys.path can name directories on the file system, zip files, and potentially other “locations” (see the site
module) that should be searched for modules, such as URLs, or database queries. Only strings should be present on
sys.path; all other data types are ignored.
The path based finder is a meta path finder, so the import machinery begins the import path search by calling the
path based finder’s find_spec() method as described previously. When the path argument to find_spec()
is given, it will be a list of string paths to traverse - typically a package’s __path__ attribute for an import within
that package. If the path argument is None, this indicates a top level import and sys.path is used.
The path based finder iterates over every entry in the search path, and for each of these, looks for an appropriate
path entry finder (PathEntryFinder) for the path entry. Because this can be an expensive operation (e.g. there
may be stat() call overheads for this search), the path based finder maintains a cache mapping path entries to
path entry finders. This cache is maintained in sys.path_importer_cache (despite the name, this cache
actually stores finder objects rather than being limited to importer objects). In this way, the expensive search for a
particular path entry location’s path entry finder need only be done once. User code is free to remove cache entries
from sys.path_importer_cache forcing the path based finder to perform the path entry search again.
If the path entry is not present in the cache, the path based finder iterates over every callable in sys.path_hooks.
Each of the path entry hooks in this list is called with a single argument, the path entry to be searched. This callable may
either return a path entry finder that can handle the path entry, or it may raise ImportError. An ImportError
is used by the path based finder to signal that the hook cannot find a path entry finder for that path entry. The exception
is ignored and import path iteration continues. The hook should expect either a string or bytes object; the encoding
of bytes objects is up to the hook (e.g. it may be a file system encoding, UTF-8, or something else), and if the hook
cannot decode the argument, it should raise ImportError.
If sys.path_hooks iteration ends with no path entry finder being returned, then the path based finder’s
find_spec() method will store None in sys.path_importer_cache (to indicate that there is no finder
for this path entry) and return None, indicating that this meta path finder could not find the module.
If a path entry finder is returned by one of the path entry hook callables on sys.path_hooks, then the following
protocol is used to ask the finder for a module spec, which is then used when loading the module.
The current working directory – denoted by an empty string – is handled slightly differently from other en-
tries on sys.path. First, if the current working directory is found to not exist, no value is stored in sys.
path_importer_cache. Second, the value for the current working directory is looked up fresh for each module
66 Chapter 5. The import system
The Python Language Reference, Release 3.12.0
lookup. Third, the path used for sys.path_importer_cache and returned by importlib.machinery.
PathFinder.find_spec() will be the actual current working directory and not the empty string.
5.5.2 Path entry finder protocol
In order to support imports of modules and initialized packages and also to contribute portions to namespace packages,
path entry finders must implement the find_spec() method.
find_spec() takes two arguments: the fully qualified name of the module being imported, and the (optional)
target module. find_spec() returns a fully populated spec for the module. This spec will always have “loader”
set (with one exception).
To indicate to the import machinery that the spec represents a namespace portion, the path entry finder sets sub-
module_search_locations to a list containing the portion.
Changed in version 3.4: find_spec() replaced find_loader() and find_module(), both of which are
now deprecated, but will be used if find_spec() is not defined.
Older path entry finders may implement one of these two deprecated methods instead of find_spec(). The
methods are still respected for the sake of backward compatibility. However, if find_spec() is implemented on
the path entry finder, the legacy methods are ignored.
find_loader() takes one argument, the fully qualified name of the module being imported. find_loader()
returns a 2-tuple where the first item is the loader and the second item is a namespace portion.
For backwards compatibility with other implementations of the import protocol, many path entry finders also sup-
port the same, traditional find_module() method that meta path finders support. However path entry finder
find_module() methods are never called with a path argument (they are expected to record the appropriate
path information from the initial call to the path hook).
The find_module() method on path entry finders is deprecated, as it does not allow the path entry finder to
contribute portions to namespace packages. If both find_loader() and find_module() exist on a path
entry finder, the import system will always call find_loader() in preference to find_module().
Changed in version 3.10: Calls to find_module() and find_loader() by the import system will raise Im-
portWarning.
Changed in version 3.12: find_module() and find_loader() have been removed.
5.6 Replacing the standard import system
The most reliable mechanism for replacing the entire import system is to delete the default contents of sys.
meta_path, replacing them entirely with a custom meta path hook.
If it is acceptable to only alter the behaviour of import statements without affecting other APIs that access the import
system, then replacing the builtin __import__() function may be sufficient. This technique may also be employed
at the module level to only alter the behaviour of import statements within that module.
To selectively prevent the import of some modules from a hook early on the meta path (rather than disabling the
standard import system entirely), it is sufficient to raise ModuleNotFoundError directly from find_spec()
instead of returning None. The latter indicates that the meta path search should continue, while raising an exception
terminates it immediately.
5.6. Replacing the standard import system 67
The Python Language Reference, Release 3.12.0
5.7 Package Relative Imports
Relative imports use leading dots. A single leading dot indicates a relative import, starting with the current package.
Two or more leading dots indicate a relative import to the parent(s) of the current package, one level per dot after
the first. For example, given the following package layout:
package/
__init__.py
subpackage1/
__init__.py
moduleX.py
moduleY.py
subpackage2/
__init__.py
moduleZ.py
moduleA.py
In either subpackage1/moduleX.py or subpackage1/__init__.py, the following are valid relative
imports:
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
Absolute imports may use either the import <> or from <> import <> syntax, but relative imports may only
use the second form; the reason for this is that:
import XXX.YYY.ZZZ
should expose XXX.YYY.ZZZ as a usable expression, but .moduleY is not a valid expression.
5.8 Special considerations for __main__
The __main__ module is a special case relative to Python’s import system. As noted elsewhere, the __main__
module is directly initialized at interpreter startup, much like sys and builtins. However, unlike those two, it
doesn’t strictly qualify as a built-in module. This is because the manner in which __main__ is initialized depends
on the flags and other options with which the interpreter is invoked.
5.8.1 __main__.__spec__
Depending on how __main__ is initialized, __main__.__spec__ gets set appropriately or to None.
When Python is started with the -m option, __spec__ is set to the module spec of the corresponding module or
package. __spec__ is also populated when the __main__ module is loaded as part of executing a directory,
zipfile or other sys.path entry.
In the remaining cases __main__.__spec__ is set to None, as the code used to populate the __main__ does
not correspond directly with an importable module:
• interactive prompt
• -c option
• running from stdin
• running directly from a source or bytecode file
68 Chapter 5. The import system
The Python Language Reference, Release 3.12.0
Note that __main__.__spec__ is always None in the last case, even if the file could technically be imported
directly as a module instead. Use the -m switch if valid module metadata is desired in __main__.
Note also that even when __main__ corresponds with an importable module and __main__.__spec__ is set
accordingly, they’re still considered distinct modules. This is due to the fact that blocks guarded by if __name__
== "__main__": checks only execute when the module is used to populate the __main__ namespace, and not
during normal import.
5.9 References
The import machinery has evolved considerably since Python’s early days. The original specification for packages is
still available to read, although some details have changed since the writing of that document.
The original specification for sys.meta_path was PEP 302, with subsequent extension in PEP 420.
PEP 420 introduced namespace packages for Python 3.3. PEP 420 also introduced the find_loader() protocol
as an alternative to find_module().
PEP 366 describes the addition of the __package__ attribute for explicit relative imports in main modules.
PEP 328 introduced absolute and explicit relative imports and initially proposed __name__ for semantics PEP 366
would eventually specify for __package__.
PEP 338 defines executing modules as scripts.
PEP 451 adds the encapsulation of per-module import state in spec objects. It also off-loads most of the boilerplate
responsibilities of loaders back onto the import machinery. These changes allow the deprecation of several APIs in
the import system and also addition of new methods to finders and loaders.
5.9. References 69
The Python Language Reference, Release 3.12.0
70 Chapter 5. The import system
CHAPTER
SIX
EXPRESSIONS
This chapter explains the meaning of the elements of expressions in Python.
Syntax Notes: In this and the following chapters, extended BNF notation will be used to describe syntax, not lexical
analysis. When (one alternative of) a syntax rule has the form
name ::= othername
and no semantics are given, the semantics of this form of name are the same as for othername.
6.1 Arithmetic conversions
When a description of an arithmetic operator below uses the phrase “the numeric arguments are converted to a
common type”, this means that the operator implementation for built-in types works as follows:
• If either argument is a complex number, the other is converted to complex;
• otherwise, if either argument is a floating point number, the other is converted to floating point;
• otherwise, both must be integers and no conversion is necessary.
Some additional rules apply for certain operators (e.g., a string as a left argument to the ‘%’ operator). Extensions
must define their own conversion behavior.
6.2 Atoms
Atoms are the most basic elements of expressions. The simplest atoms are identifiers or literals. Forms enclosed in
parentheses, brackets or braces are also categorized syntactically as atoms. The syntax for atoms is:
atom ::= identifier | literal | enclosure
enclosure ::= parenth_form | list_display | dict_display | set_display
| generator_expression | yield_atom
71
The Python Language Reference, Release 3.12.0
6.2.1 Identifiers (Names)
An identifier occurring as an atom is a name. See section Identifiers and keywords for lexical definition and section
Naming and binding for documentation of naming and binding.
When the name is bound to an object, evaluation of the atom yields that object. When a name is not bound, an attempt
to evaluate it raises a NameError exception.
Private name mangling: When an identifier that textually occurs in a class definition begins with two or more
underscore characters and does not end in two or more underscores, it is considered a private name of that class.
Private names are transformed to a longer form before code is generated for them. The transformation inserts the
class name, with leading underscores removed and a single underscore inserted, in front of the name. For example,
the identifier __spam occurring in a class named Ham will be transformed to _Ham__spam. This transformation
is independent of the syntactical context in which the identifier is used. If the transformed name is extremely long
(longer than 255 characters), implementation defined truncation may happen. If the class name consists only of
underscores, no transformation is done.
6.2.2 Literals
Python supports string and bytes literals and various numeric literals:
literal ::= stringliteral | bytesliteral
| integer | floatnumber | imagnumber
Evaluation of a literal yields an object of the given type (string, bytes, integer, floating point number, complex number)
with the given value. The value may be approximated in the case of floating point and imaginary (complex) literals.
See section Literals for details.
All literals correspond to immutable data types, and hence the object’s identity is less important than its value. Multiple
evaluations of literals with the same value (either the same occurrence in the program text or a different occurrence)
may obtain the same object or a different object with the same value.
6.2.3 Parenthesized forms
A parenthesized form is an optional expression list enclosed in parentheses:
parenth_form ::= "(" [starred_expression] ")"
A parenthesized expression list yields whatever that expression list yields: if the list contains at least one comma, it
yields a tuple; otherwise, it yields the single expression that makes up the expression list.
An empty pair of parentheses yields an empty tuple object. Since tuples are immutable, the same rules as for literals
apply (i.e., two occurrences of the empty tuple may or may not yield the same object).
Note that tuples are not formed by the parentheses, but rather by use of the comma. The exception is the empty tuple,
for which parentheses are required — allowing unparenthesized “nothing” in expressions would cause ambiguities
and allow common typos to pass uncaught.
72 Chapter 6. Expressions
The Python Language Reference, Release 3.12.0
6.2.4 Displays for lists, sets and dictionaries
For constructing a list, a set or a dictionary Python provides special syntax called “displays”, each of them in two
flavors:
• either the container contents are listed explicitly, or
• they are computed via a set of looping and filtering instructions, called a comprehension.
Common syntax elements for comprehensions are:
comprehension ::= assignment_expression comp_for
comp_for ::= ["async"] "for" target_list "in" or_test [comp_iter]
comp_iter ::= comp_for | comp_if
comp_if ::= "if" or_test [comp_iter]
The comprehension consists of a single expression followed by at least one for clause and zero or more for or if
clauses. In this case, the elements of the new container are those that would be produced by considering each of the
for or if clauses a block, nesting from left to right, and evaluating the expression to produce an element each time
the innermost block is reached.
However, aside from the iterable expression in the leftmost for clause, the comprehension is executed in a separate
implicitly nested scope. This ensures that names assigned to in the target list don’t “leak” into the enclosing scope.
The iterable expression in the leftmost for clause is evaluated directly in the enclosing scope and then passed as an
argument to the implicitly nested scope. Subsequent for clauses and any filter condition in the leftmost for clause
cannot be evaluated in the enclosing scope as they may depend on the values obtained from the leftmost iterable. For
example: [x*y for x in range(10) for y in range(x, x+10)].
To ensure the comprehension always results in a container of the appropriate type, yield and yield from
expressions are prohibited in the implicitly nested scope.
Since Python 3.6, in an async def function, an async for clause may be used to iterate over a asynchronous
iterator. A comprehension in an async def function may consist of either a for or async for clause following
the leading expression, may contain additional for or async for clauses, and may also use await expressions. If
a comprehension contains either async for clauses or await expressions or other asynchronous comprehensions
it is called an asynchronous comprehension. An asynchronous comprehension may suspend the execution of the
coroutine function in which it appears. See also PEP 530.
New in version 3.6: Asynchronous comprehensions were introduced.
Changed in version 3.8: yield and yield from prohibited in the implicitly nested scope.
Changed in version 3.11: Asynchronous comprehensions are now allowed inside comprehensions in asynchronous
functions. Outer comprehensions implicitly become asynchronous.
6.2.5 List displays
A list display is a possibly empty series of expressions enclosed in square brackets:
list_display ::= "[" [starred_list | comprehension] "]"
A list display yields a new list object, the contents being specified by either a list of expressions or a comprehension.
When a comma-separated list of expressions is supplied, its elements are evaluated from left to right and placed into
the list object in that order. When a comprehension is supplied, the list is constructed from the elements resulting
from the comprehension.
6.2. Atoms 73
The Python Language Reference, Release 3.12.0
6.2.6 Set displays
A set display is denoted by curly braces and distinguishable from dictionary displays by the lack of colons separating
keys and values:
set_display ::= "{" (starred_list | comprehension) "}"
A set display yields a new mutable set object, the contents being specified by either a sequence of expressions or a
comprehension. When a comma-separated list of expressions is supplied, its elements are evaluated from left to right
and added to the set object. When a comprehension is supplied, the set is constructed from the elements resulting
from the comprehension.
An empty set cannot be constructed with {}; this literal constructs an empty dictionary.
6.2.7 Dictionary displays
A dictionary display is a possibly empty series of dict items (key/value pairs) enclosed in curly braces:
dict_display ::= "{" [dict_item_list | dict_comprehension] "}"
dict_item_list ::= dict_item ("," dict_item)* [","]
dict_item ::= expression ":" expression | "**" or_expr
dict_comprehension ::= expression ":" expression comp_for
A dictionary display yields a new dictionary object.
If a comma-separated sequence of dict items is given, they are evaluated from left to right to define the entries of the
dictionary: each key object is used as a key into the dictionary to store the corresponding value. This means that you
can specify the same key multiple times in the dict item list, and the final dictionary’s value for that key will be the
last one given.
A double asterisk ** denotes dictionary unpacking. Its operand must be a mapping. Each mapping item is added to
the new dictionary. Later values replace values already set by earlier dict items and earlier dictionary unpackings.
New in version 3.5: Unpacking into dictionary displays, originally proposed by PEP 448.
A dict comprehension, in contrast to list and set comprehensions, needs two expressions separated with a colon
followed by the usual “for” and “if” clauses. When the comprehension is run, the resulting key and value elements
are inserted in the new dictionary in the order they are produced.
Restrictions on the types of the key values are listed earlier in section The standard type hierarchy. (To summarize, the
key type should be hashable, which excludes all mutable objects.) Clashes between duplicate keys are not detected;
the last value (textually rightmost in the display) stored for a given key value prevails.
Changed in version 3.8: Prior to Python 3.8, in dict comprehensions, the evaluation order of key and value was not
well-defined. In CPython, the value was evaluated before the key. Starting with 3.8, the key is evaluated before the
value, as proposed by PEP 572.
6.2.8 Generator expressions
A generator expression is a compact generator notation in parentheses:
generator_expression ::= "(" expression comp_for ")"
A generator expression yields a new generator object. Its syntax is the same as for comprehensions, except that it is
enclosed in parentheses instead of brackets or curly braces.
74 Chapter 6. Expressions
The Python Language Reference, Release 3.12.0
Variables used in the generator expression are evaluated lazily when the __next__() method is called for the
generator object (in the same fashion as normal generators). However, the iterable expression in the leftmost for
clause is immediately evaluated, so that an error produced by it will be emitted at the point where the generator
expression is defined, rather than at the point where the first value is retrieved. Subsequent for clauses and any filter
condition in the leftmost for clause cannot be evaluated in the enclosing scope as they may depend on the values
obtained from the leftmost iterable. For example: (x*y for x in range(10) for y in range(x,
x+10)).
The parentheses can be omitted on calls with only one argument. See section Calls for details.
To avoid interfering with the expected operation of the generator expression itself, yield and yield from
expressions are prohibited in the implicitly defined generator.
If a generator expression contains either async for clauses or await expressions it is called an asynchronous
generator expression. An asynchronous generator expression returns a new asynchronous generator object, which is
an asynchronous iterator (see Asynchronous Iterators).
New in version 3.6: Asynchronous generator expressions were introduced.
Changed in version 3.7: Prior to Python 3.7, asynchronous generator expressions could only appear in async def
coroutines. Starting with 3.7, any function can use asynchronous generator expressions.
Changed in version 3.8: yield and yield from prohibited in the implicitly nested scope.
6.2.9 Yield expressions
yield_atom ::= "(" yield_expression ")"
yield_expression ::= "yield" [expression_list | "from" expression]
The yield expression is used when defining a generator function or an asynchronous generator function and thus can
only be used in the body of a function definition. Using a yield expression in a function’s body causes that function
to be a generator function, and using it in an async def function’s body causes that coroutine function to be an
asynchronous generator function. For example:
def gen(): # defines a generator function
yield 123
async def agen(): # defines an asynchronous generator function
yield 123
Due to their side effects on the containing scope, yield expressions are not permitted as part of the implicitly
defined scopes used to implement comprehensions and generator expressions.
Changed in version 3.8: Yield expressions prohibited in the implicitly nested scopes used to implement comprehen-
sions and generator expressions.
Generator functions are described below, while asynchronous generator functions are described separately in section
Asynchronous generator functions.
When a generator function is called, it returns an iterator known as a generator. That generator then controls the
execution of the generator function. The execution starts when one of the generator’s methods is called. At that time,
the execution proceeds to the first yield expression, where it is suspended again, returning the value of expres-
sion_list to the generator’s caller, or None if expression_list is omitted. By suspended, we mean that
all local state is retained, including the current bindings of local variables, the instruction pointer, the internal evalu-
ation stack, and the state of any exception handling. When the execution is resumed by calling one of the generator’s
methods, the function can proceed exactly as if the yield expression were just another external call. The value of
the yield expression after resuming depends on the method which resumed the execution. If __next__() is used
(typically via either a for or the next() builtin) then the result is None. Otherwise, if send() is used, then the
result will be the value passed in to that method.
All of this makes generator functions quite similar to coroutines; they yield multiple times, they have more than one
entry point and their execution can be suspended. The only difference is that a generator function cannot control
6.2. Atoms 75
The Python Language Reference, Release 3.12.0
where the execution should continue after it yields; the control is always transferred to the generator’s caller.
Yield expressions are allowed anywhere in a try construct. If the generator is not resumed before it is finalized (by
reaching a zero reference count or by being garbage collected), the generator-iterator’s close() method will be
called, allowing any pending finally clauses to execute.
When yield from <expr> is used, the supplied expression must be an iterable. The values produced by iterating
that iterable are passed directly to the caller of the current generator’s methods. Any values passed in with send()
and any exceptions passed in with throw() are passed to the underlying iterator if it has the appropriate methods.
If this is not the case, then send() will raise AttributeError or TypeError, while throw() will just raise
the passed in exception immediately.
When the underlying iterator is complete, the value attribute of the raised StopIteration instance becomes
the value of the yield expression. It can be either set explicitly when raising StopIteration, or automatically
when the subiterator is a generator (by returning a value from the subgenerator).
Changed in version 3.3: Added yield from <expr> to delegate control flow to a subiterator.
The parentheses may be omitted when the yield expression is the sole expression on the right hand side of an assign-
ment statement.
See also:
PEP 255 - Simple Generators The proposal for adding generators and the yield statement to Python.
PEP 342 - Coroutines via Enhanced Generators The proposal to enhance the API and syntax of generators, mak-
ing them usable as simple coroutines.
PEP 380 - Syntax for Delegating to a Subgenerator The proposal to introduce the yield_from syntax, mak-
ing delegation to subgenerators easy.
PEP 525 - Asynchronous Generators The proposal that expanded on PEP 492 by adding generator capabilities
to coroutine functions.
Generator-iterator methods
This subsection describes the methods of a generator iterator. They can be used to control the execution of a generator
function.
Note that calling any of the generator methods below when the generator is already executing raises a ValueError
exception.
generator.__next__()
Starts the execution of a generator function or resumes it at the last executed yield expression. When a generator
function is resumed with a __next__() method, the current yield expression always evaluates to None. The
execution then continues to the next yield expression, where the generator is suspended again, and the value
of the expression_list is returned to __next__()’s caller. If the generator exits without yielding
another value, a StopIteration exception is raised.
This method is normally called implicitly, e.g. by a for loop, or by the built-in next() function.
generator.send(value)
Resumes the execution and “sends” a value into the generator function. The value argument becomes the result
of the current yield expression. The send() method returns the next value yielded by the generator, or raises
StopIteration if the generator exits without yielding another value. When send() is called to start the
generator, it must be called with None as the argument, because there is no yield expression that could receive
the value.
generator.throw(value)
generator.throw(type[, value[, traceback ]])
Raises an exception at the point where the generator was paused, and returns the next value yielded by the
generator function. If the generator exits without yielding another value, a StopIteration exception is
raised. If the generator function does not catch the passed-in exception, or raises a different exception, then
that exception propagates to the caller.
76 Chapter 6. Expressions
The Python Language Reference, Release 3.12.0
In typical use, this is called with a single exception instance similar to the way the raise keyword is used.
For backwards compatibility, however, the second signature is supported, following a convention from older
versions of Python. The type argument should be an exception class, and value should be an exception instance.
If the value is not provided, the type constructor is called to get an instance. If traceback is provided, it is set
on the exception, otherwise any existing __traceback__ attribute stored in value may be cleared.
Changed in version 3.12: The second signature (type[, value[, traceback]]) is deprecated and may be removed
in a future version of Python.
generator.close()
Raises a GeneratorExit at the point where the generator function was paused. If the generator function
then exits gracefully, is already closed, or raises GeneratorExit (by not catching the exception), close
returns to its caller. If the generator yields a value, a RuntimeError is raised. If the generator raises any
other exception, it is propagated to the caller. close() does nothing if the generator has already exited due
to an exception or normal exit.
Examples
Here is a simple example that demonstrates the behavior of generators and generator functions:
>>> def echo(value=None):
... print("Execution starts when 'next()' is called for the first time.")
... try:
... while True:
... try:
... value = (yield value)
... except Exception as e:
... value = e
... finally:
... print("Don't forget to clean up when 'close()' is called.")
...
>>> generator = echo(1)
>>> print(next(generator))
Execution starts when 'next()' is called for the first time.
1
>>> print(next(generator))
None
>>> print(generator.send(2))
2
>>> generator.throw(TypeError, "spam")
TypeError('spam',)
>>> generator.close()
Don't forget to clean up when 'close()' is called.
For examples using yield from, see pep-380 in “What’s New in Python.”
Asynchronous generator functions
The presence of a yield expression in a function or method defined using async def further defines the function
as an asynchronous generator function.
When an asynchronous generator function is called, it returns an asynchronous iterator known as an asynchronous
generator object. That object then controls the execution of the generator function. An asynchronous generator object
is typically used in an async for statement in a coroutine function analogously to how a generator object would
be used in a for statement.
Calling one of the asynchronous generator’s methods returns an awaitable object, and the execution starts when this
object is awaited on. At that time, the execution proceeds to the first yield expression, where it is suspended again,
returning the value of expression_list to the awaiting coroutine. As with a generator, suspension means that all
local state is retained, including the current bindings of local variables, the instruction pointer, the internal evaluation
6.2. Atoms 77
The Python Language Reference, Release 3.12.0
stack, and the state of any exception handling. When the execution is resumed by awaiting on the next object returned
by the asynchronous generator’s methods, the function can proceed exactly as if the yield expression were just another
external call. The value of the yield expression after resuming depends on the method which resumed the execution.
If __anext__() is used then the result is None. Otherwise, if asend() is used, then the result will be the value
passed in to that method.
If an asynchronous generator happens to exit early by break, the caller task being cancelled, or other exceptions,
the generator’s async cleanup code will run and possibly raise exceptions or access context variables in an unexpected
context–perhaps after the lifetime of tasks it depends, or during the event loop shutdown when the async-generator
garbage collection hook is called. To prevent this, the caller must explicitly close the async generator by calling
aclose() method to finalize the generator and ultimately detach it from the event loop.
In an asynchronous generator function, yield expressions are allowed anywhere in a try construct. However, if an
asynchronous generator is not resumed before it is finalized (by reaching a zero reference count or by being garbage
collected), then a yield expression within a try construct could result in a failure to execute pending finally
clauses. In this case, it is the responsibility of the event loop or scheduler running the asynchronous generator to call
the asynchronous generator-iterator’s aclose() method and run the resulting coroutine object, thus allowing any
pending finally clauses to execute.
To take care of finalization upon event loop termination, an event loop should define a finalizer function which takes
an asynchronous generator-iterator and presumably calls aclose() and executes the coroutine. This finalizer may
be registered by calling sys.set_asyncgen_hooks(). When first iterated over, an asynchronous generator-
iterator will store the registered finalizer to be called upon finalization. For a reference example of a finalizer method
see the implementation of asyncio.Loop.shutdown_asyncgens in Lib/asyncio/base_events.py.
The expression yield from <expr> is a syntax error when used in an asynchronous generator function.
Asynchronous generator-iterator methods
This subsection describes the methods of an asynchronous generator iterator, which are used to control the execution
of a generator function.
coroutine agen.__anext__()
Returns an awaitable which when run starts to execute the asynchronous generator or resumes it at the last
executed yield expression. When an asynchronous generator function is resumed with an __anext__()
method, the current yield expression always evaluates to None in the returned awaitable, which when run will
continue to the next yield expression. The value of the expression_list of the yield expression is the
value of the StopIteration exception raised by the completing coroutine. If the asynchronous genera-
tor exits without yielding another value, the awaitable instead raises a StopAsyncIteration exception,
signalling that the asynchronous iteration has completed.
This method is normally called implicitly by a async for loop.
coroutine agen.asend(value)
Returns an awaitable which when run resumes the execution of the asynchronous generator. As with the
send() method for a generator, this “sends” a value into the asynchronous generator function, and the
value argument becomes the result of the current yield expression. The awaitable returned by the asend()
method will return the next value yielded by the generator as the value of the raised StopIteration, or
raises StopAsyncIteration if the asynchronous generator exits without yielding another value. When
asend() is called to start the asynchronous generator, it must be called with None as the argument, because
there is no yield expression that could receive the value.
coroutine agen.athrow(value)
coroutine agen.athrow(type[, value[, traceback ]])
Returns an awaitable that raises an exception of type type at the point where the asynchronous generator was
paused, and returns the next value yielded by the generator function as the value of the raised StopItera-
tion exception. If the asynchronous generator exits without yielding another value, a StopAsyncIter-
ation exception is raised by the awaitable. If the generator function does not catch the passed-in exception,
or raises a different exception, then when the awaitable is run that exception propagates to the caller of the
awaitable.
78 Chapter 6. Expressions
The Python Language Reference, Release 3.12.0
Changed in version 3.12: The second signature (type[, value[, traceback]]) is deprecated and may be removed
in a future version of Python.
coroutine agen.aclose()
Returns an awaitable that when run will throw a GeneratorExit into the asynchronous generator function
at the point where it was paused. If the asynchronous generator function then exits gracefully, is already
closed, or raises GeneratorExit (by not catching the exception), then the returned awaitable will raise
a StopIteration exception. Any further awaitables returned by subsequent calls to the asynchronous
generator will raise a StopAsyncIteration exception. If the asynchronous generator yields a value, a
RuntimeError is raised by the awaitable. If the asynchronous generator raises any other exception, it is
propagated to the caller of the awaitable. If the asynchronous generator has already exited due to an exception
or normal exit, then further calls to aclose() will return an awaitable that does nothing.
6.3 Primaries
Primaries represent the most tightly bound operations of the language. Their syntax is:
primary ::= atom | attributeref | subscription | slicing | call
6.3.1 Attribute references
An attribute reference is a primary followed by a period and a name:
attributeref ::= primary "." identifier
The primary must evaluate to an object of a type that supports attribute references, which most objects do. This
object is then asked to produce the attribute whose name is the identifier. This production can be customized by
overriding the __getattr__() method. If this attribute is not available, the exception AttributeError is
raised. Otherwise, the type and value of the object produced is determined by the object. Multiple evaluations of the
same attribute reference may yield different objects.
6.3.2 Subscriptions
The subscription of an instance of a container class will generally select an element from the container. The subscrip-
tion of a generic class will generally return a GenericAlias object.
subscription ::= primary "[" expression_list "]"
When an object is subscripted, the interpreter will evaluate the primary and the expression list.
The primary must evaluate to an object that supports subscription. An object may support subscription through
defining one or both of __getitem__() and __class_getitem__(). When the primary is subscripted,
the evaluated result of the expression list will be passed to one of these methods. For more details on when
__class_getitem__ is called instead of __getitem__, see __class_getitem__ versus __getitem__.
If the expression list contains at least one comma, it will evaluate to a tuple containing the items of the expression
list. Otherwise, the expression list will evaluate to the value of the list’s sole member.
For built-in objects, there are two types of objects that support subscription via __getitem__():
1. Mappings. If the primary is a mapping, the expression list must evaluate to an object whose value is one of the
keys of the mapping, and the subscription selects the value in the mapping that corresponds to that key. An
example of a builtin mapping class is the dict class.
6.3. Primaries 79
The Python Language Reference, Release 3.12.0
1. Sequences. If the primary is a sequence, the expression list must evaluate to an int or a slice (as discussed
in the following section). Examples of builtin sequence classes include the str, list and tuple classes.
The formal syntax makes no special provision for negative indices in sequences. However, built-in sequences all
provide a __getitem__() method that interprets negative indices by adding the length of the sequence to the
index so that, for example, x[-1] selects the last item of x. The resulting value must be a nonnegative integer less
than the number of items in the sequence, and the subscription selects the item whose index is that value (counting
from zero). Since the support for negative indices and slicing occurs in the object’s __getitem__() method,
subclasses overriding this method will need to explicitly add that support.
A string is a special kind of sequence whose items are characters. A character is not a separate data type but a
string of exactly one character.
6.3.3 Slicings
A slicing selects a range of items in a sequence object (e.g., a string, tuple or list). Slicings may be used as expressions
or as targets in assignment or del statements. The syntax for a slicing:
slicing ::= primary "[" slice_list "]"
slice_list ::= slice_item ("," slice_item)* [","]
slice_item ::= expression | proper_slice
proper_slice ::= [lower_bound] ":" [upper_bound] [ ":" [stride] ]
lower_bound ::= expression
upper_bound ::= expression
stride ::= expression
There is ambiguity in the formal syntax here: anything that looks like an expression list also looks like a slice list, so
any subscription can be interpreted as a slicing. Rather than further complicating the syntax, this is disambiguated
by defining that in this case the interpretation as a subscription takes priority over the interpretation as a slicing (this
is the case if the slice list contains no proper slice).
The semantics for a slicing are as follows. The primary is indexed (using the same __getitem__() method as
normal subscription) with a key that is constructed from the slice list, as follows. If the slice list contains at least one
comma, the key is a tuple containing the conversion of the slice items; otherwise, the conversion of the lone slice item
is the key. The conversion of a slice item that is an expression is that expression. The conversion of a proper slice is a
slice object (see section The standard type hierarchy) whose start, stop and step attributes are the values of the
expressions given as lower bound, upper bound and stride, respectively, substituting None for missing expressions.
6.3.4 Calls
A call calls a callable object (e.g., a function) with a possibly empty series of arguments:
call ::= primary "(" [argument_list [","] | comprehension] ")"
argument_list ::= positional_arguments ["," starred_and_keywords]
["," keywords_arguments]
| starred_and_keywords ["," keywords_arguments]
| keywords_arguments
positional_arguments ::= positional_item ("," positional_item)*
positional_item ::= assignment_expression | "*" expression
starred_and_keywords ::= ("*" expression | keyword_item)
("," "*" expression | "," keyword_item)*
keywords_arguments ::= (keyword_item | "**" expression)
("," keyword_item | "," "**" expression)*
keyword_item ::= identifier "=" expression
80 Chapter 6. Expressions
The Python Language Reference, Release 3.12.0
An optional trailing comma may be present after the positional and keyword arguments but does not affect the se-
mantics.
The primary must evaluate to a callable object (user-defined functions, built-in functions, methods of built-in objects,
class objects, methods of class instances, and all objects having a __call__() method are callable). All argument
expressions are evaluated before the call is attempted. Please refer to section Function definitions for the syntax of
formal parameter lists.
If keyword arguments are present, they are first converted to positional arguments, as follows. First, a list of unfilled
slots is created for the formal parameters. If there are N positional arguments, they are placed in the first N slots.
Next, for each keyword argument, the identifier is used to determine the corresponding slot (if the identifier is the
same as the first formal parameter name, the first slot is used, and so on). If the slot is already filled, a TypeError
exception is raised. Otherwise, the argument is placed in the slot, filling it (even if the expression is None, it fills the
slot). When all arguments have been processed, the slots that are still unfilled are filled with the corresponding default
value from the function definition. (Default values are calculated, once, when the function is defined; thus, a mutable
object such as a list or dictionary used as default value will be shared by all calls that don’t specify an argument value
for the corresponding slot; this should usually be avoided.) If there are any unfilled slots for which no default value
is specified, a TypeError exception is raised. Otherwise, the list of filled slots is used as the argument list for the
call.
CPython implementation detail: An implementation may provide built-in functions whose positional parameters
do not have names, even if they are ‘named’ for the purpose of documentation, and which therefore cannot be supplied
by keyword. In CPython, this is the case for functions implemented in C that use PyArg_ParseTuple() to parse
their arguments.
If there are more positional arguments than there are formal parameter slots, a TypeError exception is raised,
unless a formal parameter using the syntax *identifier is present; in this case, that formal parameter receives a
tuple containing the excess positional arguments (or an empty tuple if there were no excess positional arguments).
If any keyword argument does not correspond to a formal parameter name, a TypeError exception is raised, unless
a formal parameter using the syntax **identifier is present; in this case, that formal parameter receives a dictio-
nary containing the excess keyword arguments (using the keywords as keys and the argument values as corresponding
values), or a (new) empty dictionary if there were no excess keyword arguments.
If the syntax *expression appears in the function call, expression must evaluate to an iterable. Elements
from these iterables are treated as if they were additional positional arguments. For the call f(x1, x2, *y, x3,
x4), if y evaluates to a sequence y1, …, yM, this is equivalent to a call with M+4 positional arguments x1, x2, y1,
…, yM, x3, x4.
A consequence of this is that although the *expression syntax may appear after explicit keyword arguments, it
is processed before the keyword arguments (and any **expression arguments – see below). So:
>>> def f(a, b):
... print(a, b)
...
>>> f(b=1, *(2,))
2 1
>>> f(a=1, *(2,))
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: f() got multiple values for keyword argument 'a'
>>> f(1, *(2,))
1 2
It is unusual for both keyword arguments and the *expression syntax to be used in the same call, so in practice
this confusion does not often arise.
If the syntax **expression appears in the function call, expression must evaluate to a mapping, the contents
of which are treated as additional keyword arguments. If a parameter matching a key has already been given a value
(by an explicit keyword argument, or from another unpacking), a TypeError exception is raised.
When **expression is used, each key in this mapping must be a string. Each value from the mapping is assigned
to the first formal parameter eligible for keyword assignment whose name is equal to the key. A key need not be a
Python identifier (e.g. "max-temp °F" is acceptable, although it will not match any formal parameter that could
6.3. Primaries 81
The Python Language Reference, Release 3.12.0
be declared). If there is no match to a formal parameter the key-value pair is collected by the ** parameter, if there
is one, or if there is not, a TypeError exception is raised.
Formal parameters using the syntax *identifier or **identifier cannot be used as positional argument
slots or as keyword argument names.
Changed in version 3.5: Function calls accept any number of * and ** unpackings, positional arguments may follow
iterable unpackings (*), and keyword arguments may follow dictionary unpackings (**). Originally proposed by
PEP 448.
A call always returns some value, possibly None, unless it raises an exception. How this value is computed depends
on the type of the callable object.
If it is—
a user-defined function: The code block for the function is executed, passing it the argument list. The first thing
the code block will do is bind the formal parameters to the arguments; this is described in section Function
definitions. When the code block executes a return statement, this specifies the return value of the function
call.
a built-in function or method: The result is up to the interpreter; see built-in-funcs for the descriptions of built-in
functions and methods.
a class object: A new instance of that class is returned.
a class instance method: The corresponding user-defined function is called, with an argument list that is one longer
than the argument list of the call: the instance becomes the first argument.
a class instance: The class must define a __call__() method; the effect is then the same as if that method was
called.
6.4 Await expression
Suspend the execution of coroutine on an awaitable object. Can only be used inside a coroutine function.
await_expr ::= "await" primary
New in version 3.5.
6.5 The power operator
The power operator binds more tightly than unary operators on its left; it binds less tightly than unary operators on
its right. The syntax is:
power ::= (await_expr | primary) ["**" u_expr]
Thus, in an unparenthesized sequence of power and unary operators, the operators are evaluated from right to left
(this does not constrain the evaluation order for the operands): -1**2 results in -1.
The power operator has the same semantics as the built-in pow() function, when called with two arguments: it yields
its left argument raised to the power of its right argument. The numeric arguments are first converted to a common
type, and the result is of that type.
For int operands, the result has the same type as the operands unless the second argument is negative; in that case,
all arguments are converted to float and a float result is delivered. For example, 10**2 returns 100, but 10**-2
returns 0.01.
Raising 0.0 to a negative power results in a ZeroDivisionError. Raising a negative number to a fractional
power results in a complex number. (In earlier versions it raised a ValueError.)
82 Chapter 6. Expressions
The Python Language Reference, Release 3.12.0
This operation can be customized using the special __pow__() method.
6.6 Unary arithmetic and bitwise operations
All unary arithmetic and bitwise operations have the same priority:
u_expr ::= power | "-" u_expr | "+" u_expr | "~" u_expr
The unary - (minus) operator yields the negation of its numeric argument; the operation can be overridden with the
__neg__() special method.
The unary + (plus) operator yields its numeric argument unchanged; the operation can be overridden with the
__pos__() special method.
The unary ~ (invert) operator yields the bitwise inversion of its integer argument. The bitwise inversion of x is
defined as -(x+1). It only applies to integral numbers or to custom objects that override the __invert__()
special method.
In all three cases, if the argument does not have the proper type, a TypeError exception is raised.
6.7 Binary arithmetic operations
The binary arithmetic operations have the conventional priority levels. Note that some of these operations also apply to
certain non-numeric types. Apart from the power operator, there are only two levels, one for multiplicative operators
and one for additive operators:
m_expr ::= u_expr | m_expr "*" u_expr | m_expr "@" m_expr |
m_expr "//" u_expr | m_expr "/" u_expr |
m_expr "%" u_expr
a_expr ::= m_expr | a_expr "+" m_expr | a_expr "-" m_expr
The * (multiplication) operator yields the product of its arguments. The arguments must either both be numbers, or
one argument must be an integer and the other must be a sequence. In the former case, the numbers are converted to a
common type and then multiplied together. In the latter case, sequence repetition is performed; a negative repetition
factor yields an empty sequence.
This operation can be customized using the special __mul__() and __rmul__() methods.
The @ (at) operator is intended to be used for matrix multiplication. No builtin Python types implement this operator.
New in version 3.5.
The / (division) and // (floor division) operators yield the quotient of their arguments. The numeric arguments
are first converted to a common type. Division of integers yields a float, while floor division of integers results in
an integer; the result is that of mathematical division with the ‘floor’ function applied to the result. Division by zero
raises the ZeroDivisionError exception.
This operation can be customized using the special __truediv__() and __floordiv__() methods.
The % (modulo) operator yields the remainder from the division of the first argument by the second. The numeric
arguments are first converted to a common type. A zero right argument raises the ZeroDivisionError excep-
tion. The arguments may be floating point numbers, e.g., 3.14%0.7 equals 0.34 (since 3.14 equals 4*0.7 +
0.34.) The modulo operator always yields a result with the same sign as its second operand (or zero); the absolute
value of the result is strictly smaller than the absolute value of the second operand1.
1 While abs(x%y) < abs(y) is true mathematically, for floats it may not be true numerically due to roundoff. For example, and assuming
a platform on which a Python float is an IEEE 754 double-precision number, in order that -1e-100 % 1e100 have the same sign as 1e100,
the computed result is -1e-100 + 1e100, which is numerically exactly equal to 1e100. The function math.fmod() returns a result whose
6.6. Unary arithmetic and bitwise operations 83
The Python Language Reference, Release 3.12.0
The floor division and modulo operators are connected by the following identity: x == (x//y)*y + (x%y).
Floor division and modulo are also connected with the built-in function divmod(): divmod(x, y) == (x//y,
x%y).2.
In addition to performing the modulo operation on numbers, the % operator is also overloaded by string objects to
perform old-style string formatting (also known as interpolation). The syntax for string formatting is described in the
Python Library Reference, section old-string-formatting.
The modulo operation can be customized using the special __mod__() method.
The floor division operator, the modulo operator, and the divmod() function are not defined for complex numbers.
Instead, convert to a floating point number using the abs() function if appropriate.
The + (addition) operator yields the sum of its arguments. The arguments must either both be numbers or both
be sequences of the same type. In the former case, the numbers are converted to a common type and then added
together. In the latter case, the sequences are concatenated.
This operation can be customized using the special __add__() and __radd__() methods.
The - (subtraction) operator yields the difference of its arguments. The numeric arguments are first converted to a
common type.
This operation can be customized using the special __sub__() method.
6.8 Shifting operations
The shifting operations have lower priority than the arithmetic operations:
shift_expr ::= a_expr | shift_expr ("<<" | ">>") a_expr
These operators accept integers as arguments. They shift the first argument to the left or right by the number of bits
given by the second argument.
This operation can be customized using the special __lshift__() and __rshift__() methods.
A right shift by n bits is defined as floor division by pow(2,n). A left shift by n bits is defined as multiplication
with pow(2,n).
6.9 Binary bitwise operations
Each of the three bitwise operations has a different priority level:
and_expr ::= shift_expr | and_expr "&" shift_expr
xor_expr ::= and_expr | xor_expr "^" and_expr
or_expr ::= xor_expr | or_expr "|" xor_expr
The & operator yields the bitwise AND of its arguments, which must be integers or one of them must be a custom
object overriding __and__() or __rand__() special methods.
The ^ operator yields the bitwise XOR (exclusive OR) of its arguments, which must be integers or one of them must
be a custom object overriding __xor__() or __rxor__() special methods.
The | operator yields the bitwise (inclusive) OR of its arguments, which must be integers or one of them must be a
custom object overriding __or__() or __ror__() special methods.
sign matches the sign of the first argument instead, and so returns -1e-100 in this case. Which approach is more appropriate depends on the
application.
2 If x is very close to an exact integer multiple of y, it’s possible for x//y to be one larger than (x-x%y)//y due to rounding. In such cases,
Python returns the latter result, in order to preserve that divmod(x,y)[0] * y + x % y be very close to x.
84 Chapter 6. Expressions
The Python Language Reference, Release 3.12.0
6.10 Comparisons
Unlike C, all comparison operations in Python have the same priority, which is lower than that of any arithmetic,
shifting or bitwise operation. Also unlike C, expressions like a < b < c have the interpretation that is conventional
in mathematics:
comparison ::= or_expr (comp_operator or_expr)*
comp_operator ::= "<" | ">" | "==" | ">=" | "<=" | "!="
| "is" ["not"] | ["not"] "in"
Comparisons yield boolean values: True or False. Custom rich comparison methods may return non-boolean
values. In this case Python will call bool() on such value in boolean contexts.
Comparisons can be chained arbitrarily, e.g., x < y <= z is equivalent to x < y and y <= z, except that y
is evaluated only once (but in both cases z is not evaluated at all when x < y is found to be false).
Formally, if a, b, c, …, y, z are expressions and op1, op2, …, opN are comparison operators, then a op1 b op2
c ... y opN z is equivalent to a op1 b and b op2 c and ... y opN z, except that each expression
is evaluated at most once.
Note that a op1 b op2 c doesn’t imply any kind of comparison between a and c, so that, e.g., x < y > z is
perfectly legal (though perhaps not pretty).
6.10.1 Value comparisons
The operators <, >, ==, >=, <=, and != compare the values of two objects. The objects do not need to have the
same type.
Chapter Objects, values and types states that objects have a value (in addition to type and identity). The value of an
object is a rather abstract notion in Python: For example, there is no canonical access method for an object’s value.
Also, there is no requirement that the value of an object should be constructed in a particular way, e.g. comprised of
all its data attributes. Comparison operators implement a particular notion of what the value of an object is. One can
think of them as defining the value of an object indirectly, by means of their comparison implementation.
Because all types are (direct or indirect) subtypes of object, they inherit the default comparison behavior from ob-
ject. Types can customize their comparison behavior by implementing rich comparison methods like __lt__(),
described in Basic customization.
The default behavior for equality comparison (== and !=) is based on the identity of the objects. Hence, equality
comparison of instances with the same identity results in equality, and equality comparison of instances with different
identities results in inequality. A motivation for this default behavior is the desire that all objects should be reflexive
(i.e. x is y implies x == y).
A default order comparison (<, >, <=, and >=) is not provided; an attempt raises TypeError. A motivation for
this default behavior is the lack of a similar invariant as for equality.
The behavior of the default equality comparison, that instances with different identities are always unequal, may be
in contrast to what types will need that have a sensible definition of object value and value-based equality. Such types
will need to customize their comparison behavior, and in fact, a number of built-in types have done that.
The following list describes the comparison behavior of the most important built-in types.
• Numbers of built-in numeric types (typesnumeric) and of the standard library types fractions.
Fraction and decimal.Decimal can be compared within and across their types, with the restriction
that complex numbers do not support order comparison. Within the limits of the types involved, they compare
mathematically (algorithmically) correct without loss of precision.
The not-a-number values float('NaN') and decimal.Decimal('NaN') are special. Any ordered
comparison of a number to a not-a-number value is false. A counter-intuitive implication is that not-a-number
values are not equal to themselves. For example, if x = float('NaN'), 3 < x, x < 3 and x == x
are all false, while x != x is true. This behavior is compliant with IEEE 754.
6.10. Comparisons 85
The Python Language Reference, Release 3.12.0
• None and NotImplemented are singletons. PEP 8 advises that comparisons for singletons should always
be done with is or is not, never the equality operators.
• Binary sequences (instances of bytes or bytearray) can be compared within and across their types. They
compare lexicographically using the numeric values of their elements.
• Strings (instances of str) compare lexicographically using the numerical Unicode code points (the result of
the built-in function ord()) of their characters.3
Strings and binary sequences cannot be directly compared.
• Sequences (instances of tuple, list, or range) can be compared only within each of their types, with
the restriction that ranges do not support order comparison. Equality comparison across these types results in
inequality, and ordering comparison across these types raises TypeError.
Sequences compare lexicographically using comparison of corresponding elements. The built-in containers
typically assume identical objects are equal to themselves. That lets them bypass equality tests for identical
objects to improve performance and to maintain their internal invariants.
Lexicographical comparison between built-in collections works as follows:
– For two collections to compare equal, they must be of the same type, have the same length, and each pair
of corresponding elements must compare equal (for example, [1,2] == (1,2) is false because the
type is not the same).
– Collections that support order comparison are ordered the same as their first unequal elements (for ex-
ample, [1,2,x] <= [1,2,y] has the same value as x <= y). If a corresponding element does not
exist, the shorter collection is ordered first (for example, [1,2] < [1,2,3] is true).
• Mappings (instances of dict) compare equal if and only if they have equal (key, value) pairs. Equality
comparison of the keys and values enforces reflexivity.
Order comparisons (<, >, <=, and >=) raise TypeError.
• Sets (instances of set or frozenset) can be compared within and across their types.
They define order comparison operators to mean subset and superset tests. Those relations do not define total
orderings (for example, the two sets {1,2} and {2,3} are not equal, nor subsets of one another, nor supersets
of one another). Accordingly, sets are not appropriate arguments for functions which depend on total ordering
(for example, min(), max(), and sorted() produce undefined results given a list of sets as inputs).
Comparison of sets enforces reflexivity of its elements.
• Most other built-in types have no comparison methods implemented, so they inherit the default comparison
behavior.
User-defined classes that customize their comparison behavior should follow some consistency rules, if possible:
• Equality comparison should be reflexive. In other words, identical objects should compare equal:
x is y implies x == y
• Comparison should be symmetric. In other words, the following expressions should have the same result:
x == y and y == x
x != y and y != x
x < y and y > x
x <= y and y >= x
3 The Unicode standard distinguishes between code points (e.g. U+0041) and abstract characters (e.g. “LATIN CAPITAL LETTER A”).
While most abstract characters in Unicode are only represented using one code point, there is a number of abstract characters that can in addition
be represented using a sequence of more than one code point. For example, the abstract character “LATIN CAPITAL LETTER C WITH
CEDILLA” can be represented as a single precomposed character at code position U+00C7, or as a sequence of a base character at code position
U+0043 (LATIN CAPITAL LETTER C), followed by a combining character at code position U+0327 (COMBINING CEDILLA).
The comparison operators on strings compare at the level of Unicode code points. This may be counter-intuitive to humans. For example,
"\u00C7" == "\u0043\u0327" is False, even though both strings represent the same abstract character “LATIN CAPITAL LETTER
C WITH CEDILLA”.
To compare strings at the level of abstract characters (that is, in a way intuitive to humans), use unicodedata.normalize().
86 Chapter 6. Expressions
The Python Language Reference, Release 3.12.0
• Comparison should be transitive. The following (non-exhaustive) examples illustrate that:
x > y and y > z implies x > z
x < y and y <= z implies x < z
• Inverse comparison should result in the boolean negation. In other words, the following expressions should
have the same result:
x == y and not x != y
x < y and not x >= y (for total ordering)
x > y and not x <= y (for total ordering)
The last two expressions apply to totally ordered collections (e.g. to sequences, but not to sets or mappings).
See also the total_ordering() decorator.
• The hash() result should be consistent with equality. Objects that are equal should either have the same hash
value, or be marked as unhashable.
Python does not enforce these consistency rules. In fact, the not-a-number values are an example for not following
these rules.
6.10.2 Membership test operations
The operators in and not in test for membership. x in s evaluates to True if x is a member of s, and False
otherwise. x not in s returns the negation of x in s. All built-in sequences and set types support this as well
as dictionary, for which in tests whether the dictionary has a given key. For container types such as list, tuple, set,
frozenset, dict, or collections.deque, the expression x in y is equivalent to any(x is e or x == e for e
in y).
For the string and bytes types, x in y is True if and only if x is a substring of y. An equivalent test is y.find(x)
!= -1. Empty strings are always considered to be a substring of any other string, so "" in "abc" will return
True.
For user-defined classes which define the __contains__() method, x in y returns True if y.
__contains__(x) returns a true value, and False otherwise.
For user-defined classes which do not define __contains__() but do define __iter__(), x in y is True
if some value z, for which the expression x is z or x == z is true, is produced while iterating over y. If an
exception is raised during the iteration, it is as if in raised that exception.
Lastly, the old-style iteration protocol is tried: if a class defines __getitem__(), x in y is True if and only if
there is a non-negative integer index i such that x is y[i] or x == y[i], and no lower integer index raises
the IndexError exception. (If any other exception is raised, it is as if in raised that exception).
The operator not in is defined to have the inverse truth value of in.
6.10.3 Identity comparisons
The operators is and is not test for an object’s identity: x is y is true if and only if x and y are the same object.
An Object’s identity is determined using the id() function. x is not y yields the inverse truth value.4
4 Due to automatic garbage-collection, free lists, and the dynamic nature of descriptors, you may notice seemingly unusual behaviour in certain
uses of the is operator, like those involving comparisons between instance methods, or constants. Check their documentation for more info.
6.10. Comparisons 87
The Python Language Reference, Release 3.12.0
6.11 Boolean operations
or_test ::= and_test | or_test "or" and_test
and_test ::= not_test | and_test "and" not_test
not_test ::= comparison | "not" not_test
In the context of Boolean operations, and also when expressions are used by control flow statements, the following
values are interpreted as false: False, None, numeric zero of all types, and empty strings and containers (including
strings, tuples, lists, dictionaries, sets and frozensets). All other values are interpreted as true. User-defined objects
can customize their truth value by providing a __bool__() method.
The operator not yields True if its argument is false, False otherwise.
The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting
value is returned.
The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting
value is returned.
Note that neither and nor or restrict the value and type they return to False and True, but rather return the last
evaluated argument. This is sometimes useful, e.g., if s is a string that should be replaced by a default value if it is
empty, the expression s or 'foo' yields the desired value. Because not has to create a new value, it returns a
boolean value regardless of the type of its argument (for example, not 'foo' produces False rather than ''.)
6.12 Assignment expressions
assignment_expression ::= [identifier ":="] expression
An assignment expression (sometimes also called a “named expression” or “walrus”) assigns an expression to an
identifier, while also returning the value of the expression.
One common use case is when handling matched regular expressions:
if matching := pattern.search(data):
do_something(matching)
Or, when processing a file stream in chunks:
while chunk := file.read(9000):
process(chunk)
Assignment expressions must be surrounded by parentheses when used as sub-expressions in slicing, conditional,
lambda, keyword-argument, and comprehension-if expressions and in assert and with statements. In all other
places where they can be used, parentheses are not required, including in if and while statements.
New in version 3.8: See PEP 572 for more details about assignment expressions.
88 Chapter 6. Expressions
The Python Language Reference, Release 3.12.0
6.13 Conditional expressions
conditional_expression ::= or_test ["if" or_test "else" expression]
expression ::= conditional_expression | lambda_expr
Conditional expressions (sometimes called a “ternary operator”) have the lowest priority of all Python operations.
The expression x if C else y first evaluates the condition, C rather than x. If C is true, x is evaluated and its
value is returned; otherwise, y is evaluated and its value is returned.
See PEP 308 for more details about conditional expressions.
6.14 Lambdas
lambda_expr ::= "lambda" [parameter_list] ":" expression
Lambda expressions (sometimes called lambda forms) are used to create anonymous functions. The expression
lambda parameters: expression yields a function object. The unnamed object behaves like a function
object defined with:
def <lambda>(parameters):
return expression
See section Function definitions for the syntax of parameter lists. Note that functions created with lambda expressions
cannot contain statements or annotations.
6.15 Expression lists
expression_list ::= expression ("," expression)* [","]
starred_list ::= starred_item ("," starred_item)* [","]
starred_expression ::= expression | (starred_item ",")* [starred_item]
starred_item ::= assignment_expression | "*" or_expr
Except when part of a list or set display, an expression list containing at least one comma yields a tuple. The length
of the tuple is the number of expressions in the list. The expressions are evaluated from left to right.
An asterisk * denotes iterable unpacking. Its operand must be an iterable. The iterable is expanded into a sequence
of items, which are included in the new tuple, list, or set, at the site of the unpacking.
New in version 3.5: Iterable unpacking in expression lists, originally proposed by PEP 448.
The trailing comma is required only to create a single tuple (a.k.a. a singleton); it is optional in all other cases. A
single expression without a trailing comma doesn’t create a tuple, but rather yields the value of that expression. (To
create an empty tuple, use an empty pair of parentheses: ().)
6.13. Conditional expressions 89
The Python Language Reference, Release 3.12.0
6.16 Evaluation order
Python evaluates expressions from left to right. Notice that while evaluating an assignment, the right-hand side is
evaluated before the left-hand side.
In the following lines, expressions will be evaluated in the arithmetic order of their suffixes:
expr1, expr2, expr3, expr4
(expr1, expr2, expr3, expr4)
{expr1: expr2, expr3: expr4}
expr1 + expr2 * (expr3 - expr4)
expr1(expr2, expr3, *expr4, **expr5)
expr3, expr4 = expr1, expr2
6.17 Operator precedence
The following table summarizes the operator precedence in Python, from highest precedence (most binding) to lowest
precedence (least binding). Operators in the same box have the same precedence. Unless the syntax is explicitly
given, operators are binary. Operators in the same box group left to right (except for exponentiation and conditional
expressions, which group from right to left).
Note that comparisons, membership tests, and identity tests, all have the same precedence and have a left-to-right
chaining feature as described in the Comparisons section.
Operator Description
(expressions...),
[expressions...], {key: value...},
{expressions...}
Binding or parenthesized expression, list display,
dictionary display, set display
x[index], x[index:index], x(arguments...),
x.attribute
Subscription, slicing, call, attribute reference
await x Await expression
** Exponentiation5
+x, -x, ~x Positive, negative, bitwise NOT
*, @, /, //, % Multiplication, matrix multiplication, division,
floor division, remainder6
+, - Addition and subtraction
<<, >> Shifts
& Bitwise AND
^ Bitwise XOR
| Bitwise OR
in, not in, is, is not, <, <=, >, >=, !=, == Comparisons, including membership tests and
identity tests
not x Boolean NOT
and Boolean AND
or Boolean OR
if – else Conditional expression
lambda Lambda expression
:= Assignment expression
5 The power operator ** binds less tightly than an arithmetic or bitwise unary operator on its right, that is, 2**-1 is 0.5.
6 The % operator is also used for string formatting; the same precedence applies.
90 Chapter 6. Expressions
CHAPTER
SEVEN
SIMPLE STATEMENTS
A simple statement is comprised within a single logical line. Several simple statements may occur on a single line
separated by semicolons. The syntax for simple statements is:
simple_stmt ::= expression_stmt
| assert_stmt
| assignment_stmt
| augmented_assignment_stmt
| annotated_assignment_stmt
| pass_stmt
| del_stmt
| return_stmt
| yield_stmt
| raise_stmt
| break_stmt
| continue_stmt
| import_stmt
| future_stmt
| global_stmt
| nonlocal_stmt
| type_stmt
7.1 Expression statements
Expression statements are used (mostly interactively) to compute and write a value, or (usually) to call a procedure (a
function that returns no meaningful result; in Python, procedures return the value None). Other uses of expression
statements are allowed and occasionally useful. The syntax for an expression statement is:
expression_stmt ::= starred_expression
An expression statement evaluates the expression list (which may be a single expression).
In interactive mode, if the value is not None, it is converted to a string using the built-in repr() function and the
resulting string is written to standard output on a line by itself (except if the result is None, so that procedure calls
do not cause any output.)
91
The Python Language Reference, Release 3.12.0
7.2 Assignment statements
Assignment statements are used to (re)bind names to values and to modify attributes or items of mutable objects:
assignment_stmt ::= (target_list "=")+ (starred_expression | yield_expression)
target_list ::= target ("," target)* [","]
target ::= identifier
| "(" [target_list] ")"
| "[" [target_list] "]"
| attributeref
| subscription
| slicing
| "*" target
(See section Primaries for the syntax definitions for attributeref, subscription, and slicing.)
An assignment statement evaluates the expression list (remember that this can be a single expression or a comma-
separated list, the latter yielding a tuple) and assigns the single resulting object to each of the target lists, from left to
right.
Assignment is defined recursively depending on the form of the target (list). When a target is part of a mutable object
(an attribute reference, subscription or slicing), the mutable object must ultimately perform the assignment and decide
about its validity, and may raise an exception if the assignment is unacceptable. The rules observed by various types
and the exceptions raised are given with the definition of the object types (see section The standard type hierarchy).
Assignment of an object to a target list, optionally enclosed in parentheses or square brackets, is recursively defined
as follows.
• If the target list is a single target with no trailing comma, optionally in parentheses, the object is assigned to
that target.
• Else:
– If the target list contains one target prefixed with an asterisk, called a “starred” target: The object must
be an iterable with at least as many items as there are targets in the target list, minus one. The first items
of the iterable are assigned, from left to right, to the targets before the starred target. The final items of
the iterable are assigned to the targets after the starred target. A list of the remaining items in the iterable
is then assigned to the starred target (the list can be empty).
– Else: The object must be an iterable with the same number of items as there are targets in the target list,
and the items are assigned, from left to right, to the corresponding targets.
Assignment of an object to a single target is recursively defined as follows.
• If the target is an identifier (name):
– If the name does not occur in a global or nonlocal statement in the current code block: the name
is bound to the object in the current local namespace.
– Otherwise: the name is bound to the object in the global namespace or the outer namespace determined
by nonlocal, respectively.
The name is rebound if it was already bound. This may cause the reference count for the object previously
bound to the name to reach zero, causing the object to be deallocated and its destructor (if it has one) to be
called.
• If the target is an attribute reference: The primary expression in the reference is evaluated. It should yield
an object with assignable attributes; if this is not the case, TypeError is raised. That object is then asked
to assign the assigned object to the given attribute; if it cannot perform the assignment, it raises an exception
(usually but not necessarily AttributeError).
Note: If the object is a class instance and the attribute reference occurs on both sides of the assignment operator,
the right-hand side expression, a.x can access either an instance attribute or (if no instance attribute exists) a
92 Chapter 7. Simple statements
The Python Language Reference, Release 3.12.0
class attribute. The left-hand side target a.x is always set as an instance attribute, creating it if necessary. Thus,
the two occurrences of a.x do not necessarily refer to the same attribute: if the right-hand side expression
refers to a class attribute, the left-hand side creates a new instance attribute as the target of the assignment:
class Cls:
x = 3 # class variable
inst = Cls()
inst.x = inst.x + 1 # writes inst.x as 4 leaving Cls.x as 3
This description does not necessarily apply to descriptor attributes, such as properties created with prop-
erty().
• If the target is a subscription: The primary expression in the reference is evaluated. It should yield either
a mutable sequence object (such as a list) or a mapping object (such as a dictionary). Next, the subscript
expression is evaluated.
If the primary is a mutable sequence object (such as a list), the subscript must yield an integer. If it is negative,
the sequence’s length is added to it. The resulting value must be a nonnegative integer less than the sequence’s
length, and the sequence is asked to assign the assigned object to its item with that index. If the index is out of
range, IndexError is raised (assignment to a subscripted sequence cannot add new items to a list).
If the primary is a mapping object (such as a dictionary), the subscript must have a type compatible with the
mapping’s key type, and the mapping is then asked to create a key/value pair which maps the subscript to the
assigned object. This can either replace an existing key/value pair with the same key value, or insert a new
key/value pair (if no key with the same value existed).
For user-defined objects, the __setitem__() method is called with appropriate arguments.
• If the target is a slicing: The primary expression in the reference is evaluated. It should yield a mutable sequence
object (such as a list). The assigned object should be a sequence object of the same type. Next, the lower and
upper bound expressions are evaluated, insofar they are present; defaults are zero and the sequence’s length.
The bounds should evaluate to integers. If either bound is negative, the sequence’s length is added to it. The
resulting bounds are clipped to lie between zero and the sequence’s length, inclusive. Finally, the sequence
object is asked to replace the slice with the items of the assigned sequence. The length of the slice may be
different from the length of the assigned sequence, thus changing the length of the target sequence, if the target
sequence allows it.
CPython implementation detail: In the current implementation, the syntax for targets is taken to be the same as
for expressions, and invalid syntax is rejected during the code generation phase, causing less detailed error messages.
Although the definition of assignment implies that overlaps between the left-hand side and the right-hand side are
‘simultaneous’ (for example a, b = b, a swaps two variables), overlaps within the collection of assigned-to
variables occur left-to-right, sometimes resulting in confusion. For instance, the following program prints [0, 2]:
x = [0, 1]
i = 0
i, x[i] = 1, 2 # i is updated, then x[i] is updated
print(x)
See also:
PEP 3132 - Extended Iterable Unpacking The specification for the *target feature.
7.2. Assignment statements 93
The Python Language Reference, Release 3.12.0
7.2.1 Augmented assignment statements
Augmented assignment is the combination, in a single statement, of a binary operation and an assignment statement:
augmented_assignment_stmt ::= augtarget augop (expression_list | yield_expression)
augtarget ::= identifier | attributeref | subscription | slicing
augop ::= "+=" | "-=" | "*=" | "@=" | "/=" | "//=" | "%=" | "**="
| ">>=" | "<<=" | "&=" | "^=" | "|="
(See section Primaries for the syntax definitions of the last three symbols.)
An augmented assignment evaluates the target (which, unlike normal assignment statements, cannot be an unpacking)
and the expression list, performs the binary operation specific to the type of assignment on the two operands, and
assigns the result to the original target. The target is only evaluated once.
An augmented assignment expression like x += 1 can be rewritten as x = x + 1 to achieve a similar, but not
exactly equal effect. In the augmented version, x is only evaluated once. Also, when possible, the actual operation is
performed in-place, meaning that rather than creating a new object and assigning that to the target, the old object is
modified instead.
Unlike normal assignments, augmented assignments evaluate the left-hand side before evaluating the right-hand side.
For example, a[i] += f(x) first looks-up a[i], then it evaluates f(x) and performs the addition, and lastly,
it writes the result back to a[i].
With the exception of assigning to tuples and multiple targets in a single statement, the assignment done by augmented
assignment statements is handled the same way as normal assignments. Similarly, with the exception of the possible in-
place behavior, the binary operation performed by augmented assignment is the same as the normal binary operations.
For targets which are attribute references, the same caveat about class and instance attributes applies as for regular
assignments.
7.2.2 Annotated assignment statements
Annotation assignment is the combination, in a single statement, of a variable or attribute annotation and an optional
assignment statement:
annotated_assignment_stmt ::= augtarget ":" expression
["=" (starred_expression | yield_expression)]
The difference from normal Assignment statements is that only a single target is allowed.
For simple names as assignment targets, if in class or module scope, the annotations are evaluated and stored in a
special class or module attribute __annotations__ that is a dictionary mapping from variable names (mangled if
private) to evaluated annotations. This attribute is writable and is automatically created at the start of class or module
body execution, if annotations are found statically.
For expressions as assignment targets, the annotations are evaluated if in class or module scope, but not stored.
If a name is annotated in a function scope, then this name is local for that scope. Annotations are never evaluated
and stored in function scopes.
If the right hand side is present, an annotated assignment performs the actual assignment before evaluating annotations
(where applicable). If the right hand side is not present for an expression target, then the interpreter evaluates the
target except for the last __setitem__() or __setattr__() call.
See also:
PEP 526 - Syntax for Variable Annotations The proposal that added syntax for annotating the types of variables
(including class variables and instance variables), instead of expressing them through comments.
94 Chapter 7. Simple statements
The Python Language Reference, Release 3.12.0
PEP 484 - Type hints The proposal that added the typing module to provide a standard syntax for type annota-
tions that can be used in static analysis tools and IDEs.
Changed in version 3.8: Now annotated assignments allow the same expressions in the right hand side as regular
assignments. Previously, some expressions (like un-parenthesized tuple expressions) caused a syntax error.
7.3 The assert statement
Assert statements are a convenient way to insert debugging assertions into a program:
assert_stmt ::= "assert" expression ["," expression]
The simple form, assert expression, is equivalent to
if __debug__:
if not expression: raise AssertionError
The extended form, assert expression1, expression2, is equivalent to
if __debug__:
if not expression1: raise AssertionError(expression2)
These equivalences assume that __debug__ and AssertionError refer to the built-in variables with those
names. In the current implementation, the built-in variable __debug__ is True under normal circumstances,
False when optimization is requested (command line option -O). The current code generator emits no code for an
assert statement when optimization is requested at compile time. Note that it is unnecessary to include the source
code for the expression that failed in the error message; it will be displayed as part of the stack trace.
Assignments to __debug__ are illegal. The value for the built-in variable is determined when the interpreter starts.
7.4 The pass statement
pass_stmt ::= "pass"
pass is a null operation — when it is executed, nothing happens. It is useful as a placeholder when a statement is
required syntactically, but no code needs to be executed, for example:
def f(arg): pass # a function that does nothing (yet)
class C: pass # a class with no methods (yet)
7.5 The del statement
del_stmt ::= "del" target_list
Deletion is recursively defined very similar to the way assignment is defined. Rather than spelling it out in full details,
here are some hints.
Deletion of a target list recursively deletes each target, from left to right.
Deletion of a name removes the binding of that name from the local or global namespace, depending on whether the
name occurs in a global statement in the same code block. If the name is unbound, a NameError exception will
be raised.
7.3. The assert statement 95
The Python Language Reference, Release 3.12.0
Deletion of attribute references, subscriptions and slicings is passed to the primary object involved; deletion of a
slicing is in general equivalent to assignment of an empty slice of the right type (but even this is determined by the
sliced object).
Changed in version 3.2: Previously it was illegal to delete a name from the local namespace if it occurs as a free
variable in a nested block.
7.6 The return statement
return_stmt ::= "return" [expression_list]
return may only occur syntactically nested in a function definition, not within a nested class definition.
If an expression list is present, it is evaluated, else None is substituted.
return leaves the current function call with the expression list (or None) as return value.
When return passes control out of a try statement with a finally clause, that finally clause is executed
before really leaving the function.
In a generator function, the return statement indicates that the generator is done and will cause StopIteration
to be raised. The returned value (if any) is used as an argument to construct StopIteration and becomes the
StopIteration.value attribute.
In an asynchronous generator function, an empty return statement indicates that the asynchronous generator is
done and will cause StopAsyncIteration to be raised. A non-empty return statement is a syntax error in
an asynchronous generator function.
7.7 The yield statement
yield_stmt ::= yield_expression
A yield statement is semantically equivalent to a yield expression. The yield statement can be used to omit the
parentheses that would otherwise be required in the equivalent yield expression statement. For example, the yield
statements
yield <expr>
yield from <expr>
are equivalent to the yield expression statements
(yield <expr>)
(yield from <expr>)
Yield expressions and statements are only used when defining a generator function, and are only used in the body of
the generator function. Using yield in a function definition is sufficient to cause that definition to create a generator
function instead of a normal function.
For full details of yield semantics, refer to the Yield expressions section.
96 Chapter 7. Simple statements
The Python Language Reference, Release 3.12.0
7.8 The raise statement
raise_stmt ::= "raise" [expression ["from" expression]]
If no expressions are present, raise re-raises the exception that is currently being handled, which is also known as
the active exception. If there isn’t currently an active exception, a RuntimeError exception is raised indicating
that this is an error.
Otherwise, raise evaluates the first expression as the exception object. It must be either a subclass or an instance
of BaseException. If it is a class, the exception instance will be obtained when needed by instantiating the class
with no arguments.
The type of the exception is the exception instance’s class, the value is the instance itself.
A traceback object is normally created automatically when an exception is raised and attached to it as the __trace-
back__ attribute, which is writable. You can create an exception and set your own traceback in one step using the
with_traceback() exception method (which returns the same exception instance, with its traceback set to its
argument), like so:
raise Exception("foo occurred").with_traceback(tracebackobj)
The from clause is used for exception chaining: if given, the second expression must be another exception class
or instance. If the second expression is an exception instance, it will be attached to the raised exception as the
__cause__ attribute (which is writable). If the expression is an exception class, the class will be instantiated and
the resulting exception instance will be attached to the raised exception as the __cause__ attribute. If the raised
exception is not handled, both exceptions will be printed:
>>> try:
... print(1 / 0)
... except Exception as exc:
... raise RuntimeError("Something bad happened") from exc
...
Traceback (most recent call last):
File "<stdin>", line 2, in <module>
ZeroDivisionError: division by zero
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
File "<stdin>", line 4, in <module>
RuntimeError: Something bad happened
A similar mechanism works implicitly if a new exception is raised when an exception is already being handled. An
exception may be handled when an except or finally clause, or a with statement, is used. The previous
exception is then attached as the new exception’s __context__ attribute:
>>> try:
... print(1 / 0)
... except:
... raise RuntimeError("Something bad happened")
...
Traceback (most recent call last):
File "<stdin>", line 2, in <module>
ZeroDivisionError: division by zero
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
File "<stdin>", line 4, in <module>
RuntimeError: Something bad happened
Exception chaining can be explicitly suppressed by specifying None in the from clause:
7.8. The raise statement 97
The Python Language Reference, Release 3.12.0
>>> try:
... print(1 / 0)
... except:
... raise RuntimeError("Something bad happened") from None
...
Traceback (most recent call last):
File "<stdin>", line 4, in <module>
RuntimeError: Something bad happened
Additional information on exceptions can be found in section Exceptions, and information about handling exceptions
is in section The try statement.
Changed in version 3.3: None is now permitted as Y in raise X from Y.
New in version 3.3: The __suppress_context__ attribute to suppress automatic display of the exception
context.
Changed in version 3.11: If the traceback of the active exception is modified in an except clause, a subsequent
raise statement re-raises the exception with the modified traceback. Previously, the exception was re-raised with
the traceback it had when it was caught.
7.9 The break statement
break_stmt ::= "break"
break may only occur syntactically nested in a for or while loop, but not nested in a function or class definition
within that loop.
It terminates the nearest enclosing loop, skipping the optional else clause if the loop has one.
If a for loop is terminated by break, the loop control target keeps its current value.
When break passes control out of a try statement with a finally clause, that finally clause is executed
before really leaving the loop.
7.10 The continue statement
continue_stmt ::= "continue"
continue may only occur syntactically nested in a for or while loop, but not nested in a function or class
definition within that loop. It continues with the next cycle of the nearest enclosing loop.
When continue passes control out of a try statement with a finally clause, that finally clause is executed
before really starting the next loop cycle.
7.11 The import statement
import_stmt ::= "import" module ["as" identifier] ("," module ["as" identifier])*
| "from" relative_module "import" identifier ["as" identifier]
("," identifier ["as" identifier])*
| "from" relative_module "import" "(" identifier ["as" identifier
("," identifier ["as" identifier])* [","] ")"
| "from" relative_module "import" "*"
module ::= (identifier ".")* identifier
98 Chapter 7. Simple statements
The Python Language Reference, Release 3.12.0
relative_module ::= "."* module | "."+
The basic import statement (no from clause) is executed in two steps:
1. find a module, loading and initializing it if necessary
2. define a name or names in the local namespace for the scope where the import statement occurs.
When the statement contains multiple clauses (separated by commas) the two steps are carried out separately for each
clause, just as though the clauses had been separated out into individual import statements.
The details of the first step, finding and loading modules, are described in greater detail in the section on the import
system, which also describes the various types of packages and modules that can be imported, as well as all the hooks
that can be used to customize the import system. Note that failures in this step may indicate either that the module
could not be located, or that an error occurred while initializing the module, which includes execution of the module’s
code.
If the requested module is retrieved successfully, it will be made available in the local namespace in one of three
ways:
• If the module name is followed by as, then the name following as is bound directly to the imported module.
• If no other name is specified, and the module being imported is a top level module, the module’s name is bound
in the local namespace as a reference to the imported module
• If the module being imported is not a top level module, then the name of the top level package that contains
the module is bound in the local namespace as a reference to the top level package. The imported module must
be accessed using its full qualified name rather than directly
The from form uses a slightly more complex process:
1. find the module specified in the from clause, loading and initializing it if necessary;
2. for each of the identifiers specified in the import clauses:
3. check if the imported module has an attribute by that name
4. if not, attempt to import a submodule with that name and then check the imported module again for that
attribute
1. if the attribute is not found, ImportError is raised.
2. otherwise, a reference to that value is stored in the local namespace, using the name in the as clause if
it is present, otherwise using the attribute name
Examples:
import foo # foo imported and bound locally
import foo.bar.baz # foo, foo.bar, and foo.bar.baz imported, foo bound␣
↪→locally
import foo.bar.baz as fbb # foo, foo.bar, and foo.bar.baz imported, foo.bar.baz␣
↪→bound as fbb
from foo.bar import baz # foo, foo.bar, and foo.bar.baz imported, foo.bar.baz␣
↪→bound as baz
from foo import attr # foo imported and foo.attr bound as attr
If the list of identifiers is replaced by a star ('*'), all public names defined in the module are bound in the local
namespace for the scope where the import statement occurs.
The public names defined by a module are determined by checking the module’s namespace for a variable named
__all__; if defined, it must be a sequence of strings which are names defined or imported by that module. The
names given in __all__ are all considered public and are required to exist. If __all__ is not defined, the set of
public names includes all names found in the module’s namespace which do not begin with an underscore character
('_'). __all__ should contain the entire public API. It is intended to avoid accidentally exporting items that are
not part of the API (such as library modules which were imported and used within the module).
The wild card form of import — from module import * — is only allowed at the module level. Attempting
to use it in class or function definitions will raise a SyntaxError.
7.11. The import statement 99
The Python Language Reference, Release 3.12.0
When specifying what module to import you do not have to specify the absolute name of the module. When a module
or package is contained within another package it is possible to make a relative import within the same top package
without having to mention the package name. By using leading dots in the specified module or package after from
you can specify how high to traverse up the current package hierarchy without specifying exact names. One leading
dot means the current package where the module making the import exists. Two dots means up one package level.
Three dots is up two levels, etc. So if you execute from . import mod from a module in the pkg package
then you will end up importing pkg.mod. If you execute from ..subpkg2 import mod from within pkg.
subpkg1 you will import pkg.subpkg2.mod. The specification for relative imports is contained in the Package
Relative Imports section.
importlib.import_module() is provided to support applications that determine dynamically the modules to
be loaded.
Raises an auditing event import with arguments module, filename, sys.path, sys.meta_path, sys.
path_hooks.
7.11.1 Future statements
A future statement is a directive to the compiler that a particular module should be compiled using syntax or semantics
that will be available in a specified future release of Python where the feature becomes standard.
The future statement is intended to ease migration to future versions of Python that introduce incompatible changes to
the language. It allows use of the new features on a per-module basis before the release in which the feature becomes
standard.
future_stmt ::= "from" "__future__" "import" feature ["as" identifier]
("," feature ["as" identifier])*
| "from" "__future__" "import" "(" feature ["as" identifier]
("," feature ["as" identifier])* [","] ")"
feature ::= identifier
A future statement must appear near the top of the module. The only lines that can appear before a future statement
are:
• the module docstring (if any),
• comments,
• blank lines, and
• other future statements.
The only feature that requires using the future statement is annotations (see PEP 563).
All historical features enabled by the future statement are still recognized by Python 3. The list in-
cludes absolute_import, division, generators, generator_stop, unicode_literals,
print_function, nested_scopes and with_statement. They are all redundant because they are al-
ways enabled, and only kept for backwards compatibility.
A future statement is recognized and treated specially at compile time: Changes to the semantics of core constructs
are often implemented by generating different code. It may even be the case that a new feature introduces new incom-
patible syntax (such as a new reserved word), in which case the compiler may need to parse the module differently.
Such decisions cannot be pushed off until runtime.
For any given release, the compiler knows which feature names have been defined, and raises a compile-time error if
a future statement contains a feature not known to it.
The direct runtime semantics are the same as for any import statement: there is a standard module __future__,
described later, and it will be imported in the usual way at the time the future statement is executed.
The interesting runtime semantics depend on the specific feature enabled by the future statement.
Note that there is nothing special about the statement:
100 Chapter 7. Simple statements
The Python Language Reference, Release 3.12.0
import __future__ [as name]
That is not a future statement; it’s an ordinary import statement with no special semantics or syntax restrictions.
Code compiled by calls to the built-in functions exec() and compile() that occur in a module M containing a
future statement will, by default, use the new syntax or semantics associated with the future statement. This can be
controlled by optional arguments to compile() — see the documentation of that function for details.
A future statement typed at an interactive interpreter prompt will take effect for the rest of the interpreter session.
If an interpreter is started with the -i option, is passed a script name to execute, and the script includes a future
statement, it will be in effect in the interactive session started after the script is executed.
See also:
PEP 236 - Back to the __future__ The original proposal for the __future__ mechanism.
7.12 The global statement
global_stmt ::= "global" identifier ("," identifier)*
The global statement is a declaration which holds for the entire current code block. It means that the listed
identifiers are to be interpreted as globals. It would be impossible to assign to a global variable without global,
although free variables may refer to globals without being declared global.
Names listed in a global statement must not be used in the same code block textually preceding that global
statement.
Names listed in a global statement must not be defined as formal parameters, or as targets in with statements
or except clauses, or in a for target list, class definition, function definition, import statement, or variable
annotation.
CPython implementation detail: The current implementation does not enforce some of these restrictions, but
programs should not abuse this freedom, as future implementations may enforce them or silently change the meaning
of the program.
Programmer’s note: global is a directive to the parser. It applies only to code parsed at the same time as the
global statement. In particular, a global statement contained in a string or code object supplied to the built-in
exec() function does not affect the code block containing the function call, and code contained in such a string is
unaffected by global statements in the code containing the function call. The same applies to the eval() and
compile() functions.
7.13 The nonlocal statement
nonlocal_stmt ::= "nonlocal" identifier ("," identifier)*
The nonlocal statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing
scope excluding globals. This is important because the default behavior for binding is to search the local namespace
first. The statement allows encapsulated code to rebind variables outside of the local scope besides the global (module)
scope.
Names listed in a nonlocal statement, unlike those listed in a global statement, must refer to pre-existing bind-
ings in an enclosing scope (the scope in which a new binding should be created cannot be determined unambiguously).
Names listed in a nonlocal statement must not collide with pre-existing bindings in the local scope.
See also:
PEP 3104 - Access to Names in Outer Scopes The specification for the nonlocal statement.
7.12. The global statement 101
The Python Language Reference, Release 3.12.0
7.14 The type statement
type_stmt ::= 'type' identifier [type_params] "=" expression
The type statement declares a type alias, which is an instance of typing.TypeAliasType.
For example, the following statement creates a type alias:
type Point = tuple[float, float]
This code is roughly equivalent to:
annotation-def VALUE_OF_Point():
return tuple[float, float]
Point = typing.TypeAliasType("Point", VALUE_OF_Point())
annotation-def indicates an annotation scope, which behaves mostly like a function, but with several small
differences.
The value of the type alias is evaluated in the annotation scope. It is not evaluated when the type alias is created, but
only when the value is accessed through the type alias’s __value__ attribute (see Lazy evaluation). This allows the
type alias to refer to names that are not yet defined.
Type aliases may be made generic by adding a type parameter list after the name. See Generic type aliases for more.
type is a soft keyword.
New in version 3.12.
See also:
PEP 695 - Type Parameter Syntax Introduced the type statement and syntax for generic classes and functions.
102 Chapter 7. Simple statements
CHAPTER
EIGHT
COMPOUND STATEMENTS
Compound statements contain (groups of) other statements; they affect or control the execution of those other state-
ments in some way. In general, compound statements span multiple lines, although in simple incarnations a whole
compound statement may be contained in one line.
The if, while and for statements implement traditional control flow constructs. try specifies exception handlers
and/or cleanup code for a group of statements, while the with statement allows the execution of initialization and
finalization code around a block of code. Function and class definitions are also syntactically compound statements.
A compound statement consists of one or more ‘clauses.’ A clause consists of a header and a ‘suite.’ The clause headers
of a particular compound statement are all at the same indentation level. Each clause header begins with a uniquely
identifying keyword and ends with a colon. A suite is a group of statements controlled by a clause. A suite can be one
or more semicolon-separated simple statements on the same line as the header, following the header’s colon, or it can
be one or more indented statements on subsequent lines. Only the latter form of a suite can contain nested compound
statements; the following is illegal, mostly because it wouldn’t be clear to which if clause a following else clause
would belong:
if test1: if test2: print(x)
Also note that the semicolon binds tighter than the colon in this context, so that in the following example, either all
or none of the print() calls are executed:
if x < y < z: print(x); print(y); print(z)
Summarizing:
compound_stmt ::= if_stmt
| while_stmt
| for_stmt
| try_stmt
| with_stmt
| match_stmt
| funcdef
| classdef
| async_with_stmt
| async_for_stmt
| async_funcdef
suite ::= stmt_list NEWLINE | NEWLINE INDENT statement+ DEDENT
statement ::= stmt_list NEWLINE | compound_stmt
stmt_list ::= simple_stmt (";" simple_stmt)* [";"]
Note that statements always end in a NEWLINE possibly followed by a DEDENT. Also note that optional continuation
clauses always begin with a keyword that cannot start a statement, thus there are no ambiguities (the ‘dangling else’
problem is solved in Python by requiring nested if statements to be indented).
The formatting of the grammar rules in the following sections places each clause on a separate line for clarity.
103
The Python Language Reference, Release 3.12.0
8.1 The if statement
The if statement is used for conditional execution:
if_stmt ::= "if" assignment_expression ":" suite
("elif" assignment_expression ":" suite)*
["else" ":" suite]
It selects exactly one of the suites by evaluating the expressions one by one until one is found to be true (see section
Boolean operations for the definition of true and false); then that suite is executed (and no other part of the if
statement is executed or evaluated). If all expressions are false, the suite of the else clause, if present, is executed.
8.2 The while statement
The while statement is used for repeated execution as long as an expression is true:
while_stmt ::= "while" assignment_expression ":" suite
["else" ":" suite]
This repeatedly tests the expression and, if it is true, executes the first suite; if the expression is false (which may be
the first time it is tested) the suite of the else clause, if present, is executed and the loop terminates.
A break statement executed in the first suite terminates the loop without executing the else clause’s suite. A
continue statement executed in the first suite skips the rest of the suite and goes back to testing the expression.
8.3 The for statement
The for statement is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable
object:
for_stmt ::= "for" target_list "in" starred_list ":" suite
["else" ":" suite]
The starred_list expression is evaluated once; it should yield an iterable object. An iterator is created for that
iterable. The first item provided by the iterator is then assigned to the target list using the standard rules for assignments
(see Assignment statements), and the suite is executed. This repeats for each item provided by the iterator. When the
iterator is exhausted, the suite in the else clause, if present, is executed, and the loop terminates.
A break statement executed in the first suite terminates the loop without executing the else clause’s suite. A
continue statement executed in the first suite skips the rest of the suite and continues with the next item, or with
the else clause if there is no next item.
The for-loop makes assignments to the variables in the target list. This overwrites all previous assignments to those
variables including those made in the suite of the for-loop:
for i in range(10):
print(i)
i = 5 # this will not affect the for-loop
# because i will be overwritten with the next
# index in the range
104 Chapter 8. Compound statements
The Python Language Reference, Release 3.12.0
Names in the target list are not deleted when the loop is finished, but if the sequence is empty, they will not have
been assigned to at all by the loop. Hint: the built-in type range() represents immutable arithmetic sequences of
integers. For instance, iterating range(3) successively yields 0, 1, and then 2.
Changed in version 3.11: Starred elements are now allowed in the expression list.
8.4 The try statement
The try statement specifies exception handlers and/or cleanup code for a group of statements:
try_stmt ::= try1_stmt | try2_stmt | try3_stmt
try1_stmt ::= "try" ":" suite
("except" [expression ["as" identifier]] ":" suite)+
["else" ":" suite]
["finally" ":" suite]
try2_stmt ::= "try" ":" suite
("except" "*" expression ["as" identifier] ":" suite)+
["else" ":" suite]
["finally" ":" suite]
try3_stmt ::= "try" ":" suite
"finally" ":" suite
Additional information on exceptions can be found in section Exceptions, and information on using the raise state-
ment to generate exceptions may be found in section The raise statement.
8.4.1 except clause
The except clause(s) specify one or more exception handlers. When no exception occurs in the try clause, no
exception handler is executed. When an exception occurs in the try suite, a search for an exception handler is started.
This search inspects the except clauses in turn until one is found that matches the exception. An expression-less
except clause, if present, must be last; it matches any exception. For an except clause with an expression, that
expression is evaluated, and the clause matches the exception if the resulting object is “compatible” with the exception.
An object is compatible with an exception if the object is the class or a non-virtual base class of the exception object,
or a tuple containing an item that is the class or a non-virtual base class of the exception object.
If no except clause matches the exception, the search for an exception handler continues in the surrounding code
and on the invocation stack.1
If the evaluation of an expression in the header of an except clause raises an exception, the original search for a
handler is canceled and a search starts for the new exception in the surrounding code and on the call stack (it is treated
as if the entire try statement raised the exception).
When a matching except clause is found, the exception is assigned to the target specified after the as keyword
in that except clause, if present, and the except clause’s suite is executed. All except clauses must have an
executable block. When the end of this block is reached, execution continues normally after the entire try statement.
(This means that if two nested handlers exist for the same exception, and the exception occurs in the try clause of
the inner handler, the outer handler will not handle the exception.)
When an exception has been assigned using as target, it is cleared at the end of the except clause. This is as
if
except E as N:
foo
was translated to
1 The exception is propagated to the invocation stack unless there is a finally clause which happens to raise another exception. That new
exception causes the old one to be lost.
8.4. The try statement 105
The Python Language Reference, Release 3.12.0
except E as N:
try:
foo
finally:
del N
This means the exception must be assigned to a different name to be able to refer to it after the except clause.
Exceptions are cleared because with the traceback attached to them, they form a reference cycle with the stack frame,
keeping all locals in that frame alive until the next garbage collection occurs.
Before an except clause’s suite is executed, the exception is stored in the sys module, where it can be accessed
from within the body of the except clause by calling sys.exception(). When leaving an exception handler,
the exception stored in the sys module is reset to its previous value:
>>> print(sys.exception())
None
>>> try:
... raise TypeError
... except:
... print(repr(sys.exception()))
... try:
... raise ValueError
... except:
... print(repr(sys.exception()))
... print(repr(sys.exception()))
...
TypeError()
ValueError()
TypeError()
>>> print(sys.exception())
None
8.4.2 except* clause
The except* clause(s) are used for handling ExceptionGroups. The exception type for matching is interpreted
as in the case of except, but in the case of exception groups we can have partial matches when the type matches
some of the exceptions in the group. This means that multiple except* clauses can execute, each handling part of
the exception group. Each clause executes at most once and handles an exception group of all matching exceptions.
Each exception in the group is handled by at most one except* clause, the first that matches it.
>>> try:
... raise ExceptionGroup("eg",
... [ValueError(1), TypeError(2), OSError(3), OSError(4)])
... except* TypeError as e:
... print(f'caught {type(e)} with nested {e.exceptions}')
... except* OSError as e:
... print(f'caught {type(e)} with nested {e.exceptions}')
...
caught <class 'ExceptionGroup'> with nested (TypeError(2),)
caught <class 'ExceptionGroup'> with nested (OSError(3), OSError(4))
+ Exception Group Traceback (most recent call last):
| File "<stdin>", line 2, in <module>
| ExceptionGroup: eg
+-+---------------- 1 ----------------
| ValueError: 1
+------------------------------------
Any remaining exceptions that were not handled by any except* clause are re-raised at the end, along with all
exceptions that were raised from within the except* clauses. If this list contains more than one exception to
reraise, they are combined into an exception group.
106 Chapter 8. Compound statements
The Python Language Reference, Release 3.12.0
If the raised exception is not an exception group and its type matches one of the except* clauses, it is caught and
wrapped by an exception group with an empty message string.
>>> try:
... raise BlockingIOError
... except* BlockingIOError as e:
... print(repr(e))
...
ExceptionGroup('', (BlockingIOError()))
An except* clause must have a matching type, and this type cannot be a subclass of BaseExceptionGroup. It
is not possible to mix except and except* in the same try. break, continue and return cannot appear
in an except* clause.
8.4.3 else clause
The optional else clause is executed if the control flow leaves the try suite, no exception was raised, and no
return, continue, or break statement was executed. Exceptions in the else clause are not handled by the
preceding except clauses.
8.4.4 finally clause
If finally is present, it specifies a ‘cleanup’ handler. The try clause is executed, including any except and
else clauses. If an exception occurs in any of the clauses and is not handled, the exception is temporarily saved.
The finally clause is executed. If there is a saved exception it is re-raised at the end of the finally clause. If
the finally clause raises another exception, the saved exception is set as the context of the new exception. If the
finally clause executes a return, break or continue statement, the saved exception is discarded:
>>> def f():
... try:
... 1/0
... finally:
... return 42
...
>>> f()
42
The exception information is not available to the program during execution of the finally clause.
When a return, break or continue statement is executed in the try suite of a try…finally statement,
the finally clause is also executed ‘on the way out.’
The return value of a function is determined by the last return statement executed. Since the finally clause
always executes, a return statement executed in the finally clause will always be the last one executed:
>>> def foo():
... try:
... return 'try'
... finally:
... return 'finally'
...
>>> foo()
'finally'
Changed in version 3.8: Prior to Python 3.8, a continue statement was illegal in the finally clause due to a
problem with the implementation.
8.4. The try statement 107
The Python Language Reference, Release 3.12.0
8.5 The with statement
The with statement is used to wrap the execution of a block with methods defined by a context manager (see
section With Statement Context Managers). This allows common try…except…finally usage patterns to be
encapsulated for convenient reuse.
with_stmt ::= "with" ( "(" with_stmt_contents ","? ")" | with_stmt_contents
with_stmt_contents ::= with_item ("," with_item)*
with_item ::= expression ["as" target]
The execution of the with statement with one “item” proceeds as follows:
1. The context expression (the expression given in the with_item) is evaluated to obtain a context manager.
2. The context manager’s __enter__() is loaded for later use.
3. The context manager’s __exit__() is loaded for later use.
4. The context manager’s __enter__() method is invoked.
5. If a target was included in the with statement, the return value from __enter__() is assigned to it.
Note: The with statement guarantees that if the __enter__() method returns without an error, then
__exit__() will always be called. Thus, if an error occurs during the assignment to the target list, it will
be treated the same as an error occurring within the suite would be. See step 7 below.
1. The suite is executed.
2. The context manager’s __exit__() method is invoked. If an exception caused the suite to be exited, its
type, value, and traceback are passed as arguments to __exit__(). Otherwise, three None arguments are
supplied.
If the suite was exited due to an exception, and the return value from the __exit__() method was false, the
exception is reraised. If the return value was true, the exception is suppressed, and execution continues with
the statement following the with statement.
If the suite was exited for any reason other than an exception, the return value from __exit__() is ignored,
and execution proceeds at the normal location for the kind of exit that was taken.
The following code:
with EXPRESSION as TARGET:
SUITE
is semantically equivalent to:
manager = (EXPRESSION)
enter = type(manager).__enter__
exit = type(manager).__exit__
value = enter(manager)
hit_except = False
try:
TARGET = value
SUITE
except:
hit_except = True
if not exit(manager, *sys.exc_info()):
raise
finally:
(continues on next page)
108 Chapter 8. Compound statements
The Python Language Reference, Release 3.12.0
(continued from previous page)
if not hit_except:
exit(manager, None, None, None)
With more than one item, the context managers are processed as if multiple with statements were nested:
with A() as a, B() as b:
SUITE
is semantically equivalent to:
with A() as a:
with B() as b:
SUITE
You can also write multi-item context managers in multiple lines if the items are surrounded by parentheses. For
example:
with (
A() as a,
B() as b,
):
SUITE
Changed in version 3.1: Support for multiple context expressions.
Changed in version 3.10: Support for using grouping parentheses to break the statement in multiple lines.
See also:
PEP 343 - The “with” statement The specification, background, and examples for the Python with statement.
8.6 The match statement
New in version 3.10.
The match statement is used for pattern matching. Syntax:
match_stmt ::= 'match' subject_expr ":" NEWLINE INDENT case_block+ DEDENT
subject_expr ::= star_named_expression "," star_named_expressions?
| named_expression
case_block ::= 'case' patterns [guard] ":" block
Note: This section uses single quotes to denote soft keywords.
Pattern matching takes a pattern as input (following case) and a subject value (following match). The pattern
(which may contain subpatterns) is matched against the subject value. The outcomes are:
• A match success or failure (also termed a pattern success or failure).
• Possible binding of matched values to a name. The prerequisites for this are further discussed below.
The match and case keywords are soft keywords.
See also:
• PEP 634 – Structural Pattern Matching: Specification
• PEP 636 – Structural Pattern Matching: Tutorial
8.6. The match statement 109
The Python Language Reference, Release 3.12.0
8.6.1 Overview
Here’s an overview of the logical flow of a match statement:
1. The subject expression subject_expr is evaluated and a resulting subject value obtained. If the subject
expression contains a comma, a tuple is constructed using the standard rules.
1. Each pattern in a case_block is attempted to match with the subject value. The specific rules for success
or failure are described below. The match attempt can also bind some or all of the standalone names within
the pattern. The precise pattern binding rules vary per pattern type and are specified below. Name bindings
made during a successful pattern match outlive the executed block and can be used after the match
statement.
Note: During failed pattern matches, some subpatterns may succeed. Do not rely on bindings being
made for a failed match. Conversely, do not rely on variables remaining unchanged after a failed
match. The exact behavior is dependent on implementation and may vary. This is an intentional
decision made to allow different implementations to add optimizations.
1. If the pattern succeeds, the corresponding guard (if present) is evaluated. In this case all name bindings are
guaranteed to have happened.
• If the guard evaluates as true or is missing, the block inside case_block is executed.
• Otherwise, the next case_block is attempted as described above.
• If there are no further case blocks, the match statement is completed.
Note: Users should generally never rely on a pattern being evaluated. Depending on implementation, the interpreter
may cache values or use other optimizations which skip repeated evaluations.
A sample match statement:
>>> flag = False
>>> match (100, 200):
... case (100, 300): # Mismatch: 200 != 300
... print('Case 1')
... case (100, 200) if flag: # Successful match, but guard fails
... print('Case 2')
... case (100, y): # Matches and binds y to 200
... print(f'Case 3, y: {y}')
... case _: # Pattern not attempted
... print('Case 4, I match anything!')
...
Case 3, y: 200
In this case, if flag is a guard. Read more about that in the next section.
8.6.2 Guards
guard ::= "if" named_expression
A guard (which is part of the case) must succeed for code inside the case block to execute. It takes the form:
if followed by an expression.
The logical flow of a case block with a guard follows:
1. Check that the pattern in the case block succeeded. If the pattern failed, the guard is not evaluated and the
next case block is checked.
1. If the pattern succeeded, evaluate the guard.
110 Chapter 8. Compound statements
The Python Language Reference, Release 3.12.0
• If the guard condition evaluates as true, the case block is selected.
• If the guard condition evaluates as false, the case block is not selected.
• If the guard raises an exception during evaluation, the exception bubbles up.
Guards are allowed to have side effects as they are expressions. Guard evaluation must proceed from the first to the
last case block, one at a time, skipping case blocks whose pattern(s) don’t all succeed. (I.e., guard evaluation must
happen in order.) Guard evaluation must stop once a case block is selected.
8.6.3 Irrefutable Case Blocks
An irrefutable case block is a match-all case block. A match statement may have at most one irrefutable case block,
and it must be last.
A case block is considered irrefutable if it has no guard and its pattern is irrefutable. A pattern is considered irrefutable
if we can prove from its syntax alone that it will always succeed. Only the following patterns are irrefutable:
• AS Patterns whose left-hand side is irrefutable
• OR Patterns containing at least one irrefutable pattern
• Capture Patterns
• Wildcard Patterns
• parenthesized irrefutable patterns
8.6.4 Patterns
Note: This section uses grammar notations beyond standard EBNF:
• the notation SEP.RULE+ is shorthand for RULE (SEP RULE)*
• the notation !RULE is shorthand for a negative lookahead assertion
The top-level syntax for patterns is:
patterns ::= open_sequence_pattern | pattern
pattern ::= as_pattern | or_pattern
closed_pattern ::= | literal_pattern
| capture_pattern
| wildcard_pattern
| value_pattern
| group_pattern
| sequence_pattern
| mapping_pattern
| class_pattern
The descriptions below will include a description “in simple terms” of what a pattern does for illustration purposes
(credits to Raymond Hettinger for a document that inspired most of the descriptions). Note that these descriptions
are purely for illustration purposes and may not reflect the underlying implementation. Furthermore, they do not
cover all valid forms.
8.6. The match statement 111
The Python Language Reference, Release 3.12.0
OR Patterns
An OR pattern is two or more patterns separated by vertical bars |. Syntax:
or_pattern ::= "|".closed_pattern+
Only the final subpattern may be irrefutable, and each subpattern must bind the same set of names to avoid ambiguity.
An OR pattern matches each of its subpatterns in turn to the subject value, until one succeeds. The OR pattern is
then considered successful. Otherwise, if none of the subpatterns succeed, the OR pattern fails.
In simple terms, P1 | P2 | ... will try to match P1, if it fails it will try to match P2, succeeding immediately
if any succeeds, failing otherwise.
AS Patterns
An AS pattern matches an OR pattern on the left of the as keyword against a subject. Syntax:
as_pattern ::= or_pattern "as" capture_pattern
If the OR pattern fails, the AS pattern fails. Otherwise, the AS pattern binds the subject to the name on the right of
the as keyword and succeeds. capture_pattern cannot be a _.
In simple terms P as NAME will match with P, and on success it will set NAME = <subject>.
Literal Patterns
A literal pattern corresponds to most literals in Python. Syntax:
literal_pattern ::= signed_number
| signed_number "+" NUMBER
| signed_number "-" NUMBER
| strings
| "None"
| "True"
| "False"
| signed_number: NUMBER | "-" NUMBER
The rule strings and the token NUMBER are defined in the standard Python grammar. Triple-quoted strings are
supported. Raw strings and byte strings are supported. Formatted string literals are not supported.
The forms signed_number '+' NUMBER and signed_number '-' NUMBER are for expressing complex
numbers; they require a real number on the left and an imaginary number on the right. E.g. 3 + 4j.
In simple terms, LITERAL will succeed only if <subject> == LITERAL. For the singletons None, True and
False, the is operator is used.
112 Chapter 8. Compound statements
The Python Language Reference, Release 3.12.0
Capture Patterns
A capture pattern binds the subject value to a name. Syntax:
capture_pattern ::= !'_' NAME
A single underscore _ is not a capture pattern (this is what !'_' expresses). It is instead treated as a wild-
card_pattern.
In a given pattern, a given name can only be bound once. E.g. case x, x: ... is invalid while case [x] |
x: ... is allowed.
Capture patterns always succeed. The binding follows scoping rules established by the assignment expression operator
in PEP 572; the name becomes a local variable in the closest containing function scope unless there’s an applicable
global or nonlocal statement.
In simple terms NAME will always succeed and it will set NAME = <subject>.
Wildcard Patterns
A wildcard pattern always succeeds (matches anything) and binds no name. Syntax:
wildcard_pattern ::= '_'
_ is a soft keyword within any pattern, but only within patterns. It is an identifier, as usual, even within match subject
expressions, guards, and case blocks.
In simple terms, _ will always succeed.
Value Patterns
A value pattern represents a named value in Python. Syntax:
value_pattern ::= attr
attr ::= name_or_attr "." NAME
name_or_attr ::= attr | NAME
The dotted name in the pattern is looked up using standard Python name resolution rules. The pattern succeeds if the
value found compares equal to the subject value (using the == equality operator).
In simple terms NAME1.NAME2 will succeed only if <subject> == NAME1.NAME2
Note: If the same value occurs multiple times in the same match statement, the interpreter may cache the first value
found and reuse it rather than repeat the same lookup. This cache is strictly tied to a given execution of a given match
statement.
8.6. The match statement 113
The Python Language Reference, Release 3.12.0
Group Patterns
A group pattern allows users to add parentheses around patterns to emphasize the intended grouping. Otherwise, it
has no additional syntax. Syntax:
group_pattern ::= "(" pattern ")"
In simple terms (P) has the same effect as P.
Sequence Patterns
A sequence pattern contains several subpatterns to be matched against sequence elements. The syntax is similar to
the unpacking of a list or tuple.
sequence_pattern ::= "[" [maybe_sequence_pattern] "]"
| "(" [open_sequence_pattern] ")"
open_sequence_pattern ::= maybe_star_pattern "," [maybe_sequence_pattern]
maybe_sequence_pattern ::= ",".maybe_star_pattern+ ","?
maybe_star_pattern ::= star_pattern | pattern
star_pattern ::= "*" (capture_pattern | wildcard_pattern)
There is no difference if parentheses or square brackets are used for sequence patterns (i.e. (...) vs [...] ).
Note: A single pattern enclosed in parentheses without a trailing comma (e.g. (3 | 4)) is a group pattern. While
a single pattern enclosed in square brackets (e.g. [3 | 4]) is still a sequence pattern.
At most one star subpattern may be in a sequence pattern. The star subpattern may occur in any position. If no
star subpattern is present, the sequence pattern is a fixed-length sequence pattern; otherwise it is a variable-length
sequence pattern.
The following is the logical flow for matching a sequence pattern against a subject value:
1. If the subject value is not a sequence2, the sequence pattern fails.
2. If the subject value is an instance of str, bytes or bytearray the sequence pattern fails.
3. The subsequent steps depend on whether the sequence pattern is fixed or variable-length.
If the sequence pattern is fixed-length:
1. If the length of the subject sequence is not equal to the number of subpatterns, the sequence pattern fails
2 In pattern matching, a sequence is defined as one of the following:
• a class that inherits from collections.abc.Sequence
• a Python class that has been registered as collections.abc.Sequence
• a builtin class that has its (CPython) Py_TPFLAGS_SEQUENCE bit set
• a class that inherits from any of the above
The following standard library classes are sequences:
• array.array
• collections.deque
• list
• memoryview
• range
• tuple
Note: Subject values of type str, bytes, and bytearray do not match sequence patterns.
114 Chapter 8. Compound statements
The Python Language Reference, Release 3.12.0
1. Subpatterns in the sequence pattern are matched to their corresponding items in the subject sequence
from left to right. Matching stops as soon as a subpattern fails. If all subpatterns succeed in matching
their corresponding item, the sequence pattern succeeds.
Otherwise, if the sequence pattern is variable-length:
1. If the length of the subject sequence is less than the number of non-star subpatterns, the sequence pattern
fails.
1. The leading non-star subpatterns are matched to their corresponding items as for fixed-length sequences.
2. If the previous step succeeds, the star subpattern matches a list formed of the remaining subject items,
excluding the remaining items corresponding to non-star subpatterns following the star subpattern.
1. Remaining non-star subpatterns are matched to their corresponding subject items, as for a fixed-length
sequence.
Note: The length of the subject sequence is obtained via len() (i.e. via the __len__() protocol). This
length may be cached by the interpreter in a similar manner as value patterns.
In simple terms [P1, P2, P3, … , P<N>] matches only if all the following happens:
• check <subject> is a sequence
• len(subject) == <N>
• P1 matches <subject>[0] (note that this match can also bind names)
• P2 matches <subject>[1] (note that this match can also bind names)
• … and so on for the corresponding pattern/element.
Mapping Patterns
A mapping pattern contains one or more key-value patterns. The syntax is similar to the construction of a dictionary.
Syntax:
mapping_pattern ::= "{" [items_pattern] "}"
items_pattern ::= ",".key_value_pattern+ ","?
key_value_pattern ::= (literal_pattern | value_pattern) ":" pattern
| double_star_pattern
double_star_pattern ::= "**" capture_pattern
At most one double star pattern may be in a mapping pattern. The double star pattern must be the last subpattern in
the mapping pattern.
Duplicate keys in mapping patterns are disallowed. Duplicate literal keys will raise a SyntaxError. Two keys
that otherwise have the same value will raise a ValueError at runtime.
The following is the logical flow for matching a mapping pattern against a subject value:
1. If the subject value is not a mapping3,the mapping pattern fails.
2. If every key given in the mapping pattern is present in the subject mapping, and the pattern for each key matches
the corresponding item of the subject mapping, the mapping pattern succeeds.
3 In pattern matching, a mapping is defined as one of the following:
• a class that inherits from collections.abc.Mapping
• a Python class that has been registered as collections.abc.Mapping
• a builtin class that has its (CPython) Py_TPFLAGS_MAPPING bit set
• a class that inherits from any of the above
The standard library classes dict and types.MappingProxyType are mappings.
8.6. The match statement 115
The Python Language Reference, Release 3.12.0
1. If duplicate keys are detected in the mapping pattern, the pattern is considered invalid. A SyntaxError is
raised for duplicate literal values; or a ValueError for named keys of the same value.
Note: Key-value pairs are matched using the two-argument form of the mapping subject’s get() method.
Matched key-value pairs must already be present in the mapping, and not created on-the-fly via __missing__()
or __getitem__().
In simple terms {KEY1: P1, KEY2: P2, ... } matches only if all the following happens:
• check <subject> is a mapping
• KEY1 in <subject>
• P1 matches <subject>[KEY1]
• … and so on for the corresponding KEY/pattern pair.
Class Patterns
A class pattern represents a class and its positional and keyword arguments (if any). Syntax:
class_pattern ::= name_or_attr "(" [pattern_arguments ","?] ")"
pattern_arguments ::= positional_patterns ["," keyword_patterns]
| keyword_patterns
positional_patterns ::= ",".pattern+
keyword_patterns ::= ",".keyword_pattern+
keyword_pattern ::= NAME "=" pattern
The same keyword should not be repeated in class patterns.
The following is the logical flow for matching a class pattern against a subject value:
1. If name_or_attr is not an instance of the builtin type , raise TypeError.
2. If the subject value is not an instance of name_or_attr (tested via isinstance()), the class pattern
fails.
1. If no pattern arguments are present, the pattern succeeds. Otherwise, the subsequent steps depend on whether
keyword or positional argument patterns are present.
For a number of built-in types (specified below), a single positional subpattern is accepted which will match
the entire subject; for these types keyword patterns also work as for other types.
If only keyword patterns are present, they are processed as follows, one by one:
I. The keyword is looked up as an attribute on the subject.
• If this raises an exception other than AttributeError, the exception bubbles up.
• If this raises AttributeError, the class pattern has failed.
• Else, the subpattern associated with the keyword pattern is matched against the subject’s attribute value.
If this fails, the class pattern fails; if this succeeds, the match proceeds to the next keyword.
II. If all keyword patterns succeed, the class pattern succeeds.
If any positional patterns are present, they are converted to keyword patterns using the __match_args__
attribute on the class name_or_attr before matching:
I. The equivalent of getattr(cls, "__match_args__", ()) is called.
• If this raises an exception, the exception bubbles up.
• If the returned value is not a tuple, the conversion fails and TypeError is raised.
116 Chapter 8. Compound statements
The Python Language Reference, Release 3.12.0
• If there are more positional patterns than len(cls.__match_args__), TypeError is
raised.
• Otherwise, positional pattern i is converted to a keyword pattern using
__match_args__[i] as the keyword. __match_args__[i] must be a string;
if not TypeError is raised.
• If there are duplicate keywords, TypeError is raised.
See also:
Customizing positional arguments in class pattern matching
II. Once all positional patterns have been converted to keyword patterns, the match proceeds as if there
were only keyword patterns.
For the following built-in types the handling of positional subpatterns is different:
• bool
• bytearray
• bytes
• dict
• float
• frozenset
• int
• list
• set
• str
• tuple
These classes accept a single positional argument, and the pattern there is matched against the whole object
rather than an attribute. For example int(0|1) matches the value 0, but not the value 0.0.
In simple terms CLS(P1, attr=P2) matches only if the following happens:
• isinstance(<subject>, CLS)
• convert P1 to a keyword pattern using CLS.__match_args__
• For each keyword argument attr=P2:
– hasattr(<subject>, "attr")
– P2 matches <subject>.attr
• … and so on for the corresponding keyword argument/pattern pair.
See also:
• PEP 634 – Structural Pattern Matching: Specification
• PEP 636 – Structural Pattern Matching: Tutorial
8.6. The match statement 117
The Python Language Reference, Release 3.12.0
8.7 Function definitions
A function definition defines a user-defined function object (see section The standard type hierarchy):
funcdef ::= [decorators] "def" funcname [type_params] "(" [paramete
["->" expression] ":" suite
decorators ::= decorator+
decorator ::= "@" assignment_expression NEWLINE
parameter_list ::= defparameter ("," defparameter)* "," "/" ["," [paramete
| parameter_list_no_posonly
parameter_list_no_posonly ::= defparameter ("," defparameter)* ["," [parameter_list_s
| parameter_list_starargs
parameter_list_starargs ::= "*" [parameter] ("," defparameter)* ["," ["**" paramete
| "**" parameter [","]
parameter ::= identifier [":" expression]
defparameter ::= parameter ["=" expression]
funcname ::= identifier
A function definition is an executable statement. Its execution binds the function name in the current local namespace
to a function object (a wrapper around the executable code for the function). This function object contains a reference
to the current global namespace as the global namespace to be used when the function is called.
The function definition does not execute the function body; this gets executed only when the function is called.4
A function definition may be wrapped by one or more decorator expressions. Decorator expressions are evaluated
when the function is defined, in the scope that contains the function definition. The result must be a callable, which
is invoked with the function object as the only argument. The returned value is bound to the function name instead
of the function object. Multiple decorators are applied in nested fashion. For example, the following code
@f1(arg)
@f2
def func(): pass
is roughly equivalent to
def func(): pass
func = f1(arg)(f2(func))
except that the original function is not temporarily bound to the name func.
Changed in version 3.9: Functions may be decorated with any valid assignment_expression. Previously, the
grammar was much more restrictive; see PEP 614 for details.
A list of type parameters may be given in square brackets between the function’s name and the opening parenthesis for
its parameter list. This indicates to static type checkers that the function is generic. At runtime, the type parameters
can be retrieved from the function’s __type_params__ attribute. See Generic functions for more.
Changed in version 3.12: Type parameter lists are new in Python 3.12.
When one or more parameters have the form parameter = expression, the function is said to have “default parameter
values.” For a parameter with a default value, the corresponding argument may be omitted from a call, in which case
the parameter’s default value is substituted. If a parameter has a default value, all following parameters up until the
“*” must also have a default value — this is a syntactic restriction that is not expressed by the grammar.
Default parameter values are evaluated from left to right when the function definition is executed. This means
that the expression is evaluated once, when the function is defined, and that the same “pre-computed” value is used
for each call. This is especially important to understand when a default parameter value is a mutable object, such as
a list or a dictionary: if the function modifies the object (e.g. by appending an item to a list), the default parameter
4 A string literal appearing as the first statement in the function body is transformed into the function’s __doc__ attribute and therefore the
function’s docstring.
118 Chapter 8. Compound statements
The Python Language Reference, Release 3.12.0
value is in effect modified. This is generally not what was intended. A way around this is to use None as the default,
and explicitly test for it in the body of the function, e.g.:
def whats_on_the_telly(penguin=None):
if penguin is None:
penguin = []
penguin.append("property of the zoo")
return penguin
Function call semantics are described in more detail in section Calls. A function call always assigns values to all pa-
rameters mentioned in the parameter list, either from positional arguments, from keyword arguments, or from default
values. If the form “*identifier” is present, it is initialized to a tuple receiving any excess positional parameters,
defaulting to the empty tuple. If the form “**identifier” is present, it is initialized to a new ordered mapping
receiving any excess keyword arguments, defaulting to a new empty mapping of the same type. Parameters after
“*” or “*identifier” are keyword-only parameters and may only be passed by keyword arguments. Parameters
before “/” are positional-only parameters and may only be passed by positional arguments.
Changed in version 3.8: The / function parameter syntax may be used to indicate positional-only parameters. See
PEP 570 for details.
Parameters may have an annotation of the form “: expression” following the parameter name. Any parameter
may have an annotation, even those of the form *identifier or **identifier. Functions may have “return”
annotation of the form “-> expression” after the parameter list. These annotations can be any valid Python
expression. The presence of annotations does not change the semantics of a function. The annotation values are
available as values of a dictionary keyed by the parameters’ names in the __annotations__ attribute of the
function object. If the annotations import from __future__ is used, annotations are preserved as strings at
runtime which enables postponed evaluation. Otherwise, they are evaluated when the function definition is executed.
In this case annotations may be evaluated in a different order than they appear in the source code.
It is also possible to create anonymous functions (functions not bound to a name), for immediate use in expressions.
This uses lambda expressions, described in section Lambdas. Note that the lambda expression is merely a shorthand
for a simplified function definition; a function defined in a “def” statement can be passed around or assigned to
another name just like a function defined by a lambda expression. The “def” form is actually more powerful since
it allows the execution of multiple statements and annotations.
Programmer’s note: Functions are first-class objects. A “def” statement executed inside a function definition
defines a local function that can be returned or passed around. Free variables used in the nested function can access
the local variables of the function containing the def. See section Naming and binding for details.
See also:
PEP 3107 - Function Annotations The original specification for function annotations.
PEP 484 - Type Hints Definition of a standard meaning for annotations: type hints.
PEP 526 - Syntax for Variable Annotations Ability to type hint variable declarations, including class variables
and instance variables
PEP 563 - Postponed Evaluation of Annotations Support for forward references within annotations by preserv-
ing annotations in a string form at runtime instead of eager evaluation.
8.8 Class definitions
A class definition defines a class object (see section The standard type hierarchy):
classdef ::= [decorators] "class" classname [type_params] [inheritance] ":" suite
inheritance ::= "(" [argument_list] ")"
classname ::= identifier
8.8. Class definitions 119
The Python Language Reference, Release 3.12.0
A class definition is an executable statement. The inheritance list usually gives a list of base classes (see Metaclasses
for more advanced uses), so each item in the list should evaluate to a class object which allows subclassing. Classes
without an inheritance list inherit, by default, from the base class object; hence,
class Foo:
pass
is equivalent to
class Foo(object):
pass
The class’s suite is then executed in a new execution frame (see Naming and binding), using a newly created local
namespace and the original global namespace. (Usually, the suite contains mostly function definitions.) When the
class’s suite finishes execution, its execution frame is discarded but its local namespace is saved.5 A class object is
then created using the inheritance list for the base classes and the saved local namespace for the attribute dictionary.
The class name is bound to this class object in the original local namespace.
The order in which attributes are defined in the class body is preserved in the new class’s __dict__. Note that this
is reliable only right after the class is created and only for classes that were defined using the definition syntax.
Class creation can be customized heavily using metaclasses.
Classes can also be decorated: just like when decorating functions,
@f1(arg)
@f2
class Foo: pass
is roughly equivalent to
class Foo: pass
Foo = f1(arg)(f2(Foo))
The evaluation rules for the decorator expressions are the same as for function decorators. The result is then bound
to the class name.
Changed in version 3.9: Classes may be decorated with any valid assignment_expression. Previously, the
grammar was much more restrictive; see PEP 614 for details.
A list of type parameters may be given in square brackets immediately after the class’s name. This indicates to
static type checkers that the class is generic. At runtime, the type parameters can be retrieved from the class’s
__type_params__ attribute. See Generic classes for more.
Changed in version 3.12: Type parameter lists are new in Python 3.12.
Programmer’s note: Variables defined in the class definition are class attributes; they are shared by instances.
Instance attributes can be set in a method with self.name = value. Both class and instance attributes are
accessible through the notation “self.name”, and an instance attribute hides a class attribute with the same name
when accessed in this way. Class attributes can be used as defaults for instance attributes, but using mutable values
there can lead to unexpected results. Descriptors can be used to create instance variables with different implementation
details.
See also:
PEP 3115 - Metaclasses in Python 3000 The proposal that changed the declaration of metaclasses to the current
syntax, and the semantics for how classes with metaclasses are constructed.
PEP 3129 - Class Decorators The proposal that added class decorators. Function and method decorators were
introduced in PEP 318.
5 A string literal appearing as the first statement in the class body is transformed into the namespace’s __doc__ item and therefore the class’s
docstring.
120 Chapter 8. Compound statements
The Python Language Reference, Release 3.12.0
8.9 Coroutines
New in version 3.5.
8.9.1 Coroutine function definition
async_funcdef ::= [decorators] "async" "def" funcname "(" [parameter_list] ")"
["->" expression] ":" suite
Execution of Python coroutines can be suspended and resumed at many points (see coroutine). await expressions,
async for and async with can only be used in the body of a coroutine function.
Functions defined with async def syntax are always coroutine functions, even if they do not contain await or
async keywords.
It is a SyntaxError to use a yield from expression inside the body of a coroutine function.
An example of a coroutine function:
async def func(param1, param2):
do_stuff()
await some_coroutine()
Changed in version 3.7: await and async are now keywords; previously they were only treated as such inside the
body of a coroutine function.
8.9.2 The async for statement
async_for_stmt ::= "async" for_stmt
An asynchronous iterable provides an __aiter__ method that directly returns an asynchronous iterator, which can
call asynchronous code in its __anext__ method.
The async for statement allows convenient iteration over asynchronous iterables.
The following code:
async for TARGET in ITER:
SUITE
else:
SUITE2
Is semantically equivalent to:
iter = (ITER)
iter = type(iter).__aiter__(iter)
running = True
while running:
try:
TARGET = await type(iter).__anext__(iter)
except StopAsyncIteration:
running = False
else:
SUITE
else:
SUITE2
8.9. Coroutines 121
The Python Language Reference, Release 3.12.0
See also __aiter__() and __anext__() for details.
It is a SyntaxError to use an async for statement outside the body of a coroutine function.
8.9.3 The async with statement
async_with_stmt ::= "async" with_stmt
An asynchronous context manager is a context manager that is able to suspend execution in its enter and exit methods.
The following code:
async with EXPRESSION as TARGET:
SUITE
is semantically equivalent to:
manager = (EXPRESSION)
aenter = type(manager).__aenter__
aexit = type(manager).__aexit__
value = await aenter(manager)
hit_except = False
try:
TARGET = value
SUITE
except:
hit_except = True
if not await aexit(manager, *sys.exc_info()):
raise
finally:
if not hit_except:
await aexit(manager, None, None, None)
See also __aenter__() and __aexit__() for details.
It is a SyntaxError to use an async with statement outside the body of a coroutine function.
See also:
PEP 492 - Coroutines with async and await syntax The proposal that made coroutines a proper standalone con-
cept in Python, and added supporting syntax.
8.10 Type parameter lists
New in version 3.12.
type_params ::= "[" type_param ("," type_param)* "]"
type_param ::= typevar | typevartuple | paramspec
typevar ::= identifier (":" expression)?
typevartuple ::= "*" identifier
paramspec ::= "**" identifier
Functions (including coroutines), classes and type aliases may contain a type parameter list:
def max[T](args: list[T]) -> T:
...
(continues on next page)
122 Chapter 8. Compound statements
The Python Language Reference, Release 3.12.0
(continued from previous page)
async def amax[T](args: list[T]) -> T:
...
class Bag[T]:
def __iter__(self) -> Iterator[T]:
...
def add(self, arg: T) -> None:
...
type ListOrSet[T] = list[T] | set[T]
Semantically, this indicates that the function, class, or type alias is generic over a type variable. This information is
primarily used by static type checkers, and at runtime, generic objects behave much like their non-generic counter-
parts.
Type parameters are declared in square brackets ([]) immediately after the name of the function, class, or type
alias. The type parameters are accessible within the scope of the generic object, but not elsewhere. Thus, after a
declaration def func[T](): pass, the name T is not available in the module scope. Below, the semantics of
generic objects are described with more precision. The scope of type parameters is modeled with a special function
(technically, an annotation scope) that wraps the creation of the generic object.
Generic functions, classes, and type aliases have a __type_params__ attribute listing their type parameters.
Type parameters come in three kinds:
• typing.TypeVar, introduced by a plain name (e.g., T). Semantically, this represents a single type to a type
checker.
• typing.TypeVarTuple, introduced by a name prefixed with a single asterisk (e.g., *Ts). Semantically,
this stands for a tuple of any number of types.
• typing.ParamSpec, introduced by a name prefixed with two asterisks (e.g., **P). Semantically, this
stands for the parameters of a callable.
typing.TypeVar declarations can define bounds and constraints with a colon (:) followed by an expression. A
single expression after the colon indicates a bound (e.g. T: int). Semantically, this means that the typing.
TypeVar can only represent types that are a subtype of this bound. A parenthesized tuple of expressions after the
colon indicates a set of constraints (e.g. T: (str, bytes)). Each member of the tuple should be a type (again,
this is not enforced at runtime). Constrained type variables can only take on one of the types in the list of constraints.
For typing.TypeVars declared using the type parameter list syntax, the bound and constraints are not evaluated
when the generic object is created, but only when the value is explicitly accessed through the attributes __bound__
and __constraints__. To accomplish this, the bounds or constraints are evaluated in a separate annotation
scope.
typing.TypeVarTuples and typing.ParamSpecs cannot have bounds or constraints.
The following example indicates the full set of allowed type parameter declarations:
def overly_generic[
SimpleTypeVar,
TypeVarWithBound: int,
TypeVarWithConstraints: (str, bytes),
*SimpleTypeVarTuple,
**SimpleParamSpec,
](
a: SimpleTypeVar,
b: TypeVarWithBound,
c: Callable[SimpleParamSpec, TypeVarWithConstraints],
*d: SimpleTypeVarTuple,
): ...
8.10. Type parameter lists 123
The Python Language Reference, Release 3.12.0
8.10.1 Generic functions
Generic functions are declared as follows:
def func[T](arg: T): ...
This syntax is equivalent to:
annotation-def TYPE_PARAMS_OF_func():
T = typing.TypeVar("T")
def func(arg: T): ...
func.__type_params__ = (T,)
return func
func = TYPE_PARAMS_OF_func()
Here annotation-def indicates an annotation scope, which is not actually bound to any name at runtime. (One
other liberty is taken in the translation: the syntax does not go through attribute access on the typing module, but
creates an instance of typing.TypeVar directly.)
The annotations of generic functions are evaluated within the annotation scope used for declaring the type parameters,
but the function’s defaults and decorators are not.
The following example illustrates the scoping rules for these cases, as well as for additional flavors of type parameters:
@decorator
def func[T: int, *Ts, **P](*args: *Ts, arg: Callable[P, T] = some_default):
...
Except for the lazy evaluation of the TypeVar bound, this is equivalent to:
DEFAULT_OF_arg = some_default
annotation-def TYPE_PARAMS_OF_func():
annotation-def BOUND_OF_T():
return int
# In reality, BOUND_OF_T() is evaluated only on demand.
T = typing.TypeVar("T", bound=BOUND_OF_T())
Ts = typing.TypeVarTuple("Ts")
P = typing.ParamSpec("P")
def func(*args: *Ts, arg: Callable[P, T] = DEFAULT_OF_arg):
...
func.__type_params__ = (T, Ts, P)
return func
func = decorator(TYPE_PARAMS_OF_func())
The capitalized names like DEFAULT_OF_arg are not actually bound at runtime.
124 Chapter 8. Compound statements
The Python Language Reference, Release 3.12.0
8.10.2 Generic classes
Generic classes are declared as follows:
class Bag[T]: ...
This syntax is equivalent to:
annotation-def TYPE_PARAMS_OF_Bag():
T = typing.TypeVar("T")
class Bag(typing.Generic[T]):
__type_params__ = (T,)
...
return Bag
Bag = TYPE_PARAMS_OF_Bag()
Here again annotation-def (not a real keyword) indicates an annotation scope, and the name
TYPE_PARAMS_OF_Bag is not actually bound at runtime.
Generic classes implicitly inherit from typing.Generic. The base classes and keyword arguments of generic
classes are evaluated within the type scope for the type parameters, and decorators are evaluated outside that scope.
This is illustrated by this example:
@decorator
class Bag(Base[T], arg=T): ...
This is equivalent to:
annotation-def TYPE_PARAMS_OF_Bag():
T = typing.TypeVar("T")
class Bag(Base[T], typing.Generic[T], arg=T):
__type_params__ = (T,)
...
return Bag
Bag = decorator(TYPE_PARAMS_OF_Bag())
8.10.3 Generic type aliases
The type statement can also be used to create a generic type alias:
type ListOrSet[T] = list[T] | set[T]
Except for the lazy evaluation of the value, this is equivalent to:
annotation-def TYPE_PARAMS_OF_ListOrSet():
T = typing.TypeVar("T")
annotation-def VALUE_OF_ListOrSet():
return list[T] | set[T]
# In reality, the value is lazily evaluated
return typing.TypeAliasType("ListOrSet", VALUE_OF_ListOrSet(), type_params=(T,
↪→))
ListOrSet = TYPE_PARAMS_OF_ListOrSet()
Here, annotation-def (not a real keyword) indicates an annotation scope. The capitalized names like
TYPE_PARAMS_OF_ListOrSet are not actually bound at runtime.
8.10. Type parameter lists 125
The Python Language Reference, Release 3.12.0
126 Chapter 8. Compound statements
CHAPTER
NINE
TOP-LEVEL COMPONENTS
The Python interpreter can get its input from a number of sources: from a script passed to it as standard input or as
program argument, typed in interactively, from a module source file, etc. This chapter gives the syntax used in these
cases.
9.1 Complete Python programs
While a language specification need not prescribe how the language interpreter is invoked, it is useful to have a notion
of a complete Python program. A complete Python program is executed in a minimally initialized environment: all
built-in and standard modules are available, but none have been initialized, except for sys (various system services),
builtins (built-in functions, exceptions and None) and __main__. The latter is used to provide the local and
global namespace for execution of the complete program.
The syntax for a complete Python program is that for file input, described in the next section.
The interpreter may also be invoked in interactive mode; in this case, it does not read and execute a complete program
but reads and executes one statement (possibly compound) at a time. The initial environment is identical to that of a
complete program; each statement is executed in the namespace of __main__.
A complete program can be passed to the interpreter in three forms: with the -c string command line option, as a
file passed as the first command line argument, or as standard input. If the file or standard input is a tty device, the
interpreter enters interactive mode; otherwise, it executes the file as a complete program.
9.2 File input
All input read from non-interactive files has the same form:
file_input ::= (NEWLINE | statement)*
This syntax is used in the following situations:
• when parsing a complete Python program (from a file or from a string);
• when parsing a module;
• when parsing a string passed to the exec() function;
127
The Python Language Reference, Release 3.12.0
9.3 Interactive input
Input in interactive mode is parsed using the following grammar:
interactive_input ::= [stmt_list] NEWLINE | compound_stmt NEWLINE
Note that a (top-level) compound statement must be followed by a blank line in interactive mode; this is needed to
help the parser detect the end of the input.
9.4 Expression input
eval() is used for expression input. It ignores leading whitespace. The string argument to eval() must have the
following form:
eval_input ::= expression_list NEWLINE*

## Builtin functions

<table>
<tbody>
<tr>
    <td>
        <div>
            <div><strong>A</strong></div>
            <div><a href="#builtin-abs"><code>abs()</code></a></div>
            <div><a href="#builtin-aiter"><code>aiter()</code></a></div>
            <div><a href="#builtin-all"><code>all()</code></a></div>
            <div><a href="#builtin-anext"><code>anext()</code></a></div>
            <div><a href="#builtin-any"><code>any()</code></a></div>
            <div><a href="#builtin-ascii"><code>ascii()</code></a></div>
            <div><br></div>
            <div><strong>B</strong></div>
            <div><a href="#builtin-bin"><code>bin()</code></a></div>
            <div><a href="#builtin-bool"><code>bool()</code></a></div>
            <div><a href="#builtin-breakpoint"><code>breakpoint()</code></a></div>
            <div><a href="#builtin-func-bytearray"><code >bytearray()</code></a></div>
            <div><a href="#builtin-func-bytes"><code >bytes()</code></a></div>
            <div><br></div>
            <div><strong>C</strong></div>
            <div><a href="#builtin-callable"><code>callable()</code></a></div>
            <div><a href="#builtin-chr"><code>chr()</code></a></div>
            <div><a href="#builtin-classmethod"><code>classmethod()</code></a></div>
            <div><a href="#builtin-compile"><code>compile()</code></a></div>
            <div><a href="#builtin-complex"><code>complex()</code></a></div>
            <div><br></div>
            <div><strong>D</strong></div>
            <div><a href="#builtin-delattr"><code>delattr()</code></a></div>
            <div><a href="#builtin-func-dict"><code >dict()</code></a></div>
            <div><a href="#builtin-dir"><code>dir()</code></a></div>
            <div><a href="#builtin-divmod"><code>divmod()</code></a></div>
            <div><br></div>
        </div>
    </td>
    <td>
        <div>
            <div><strong>E</strong></div>
            <div><a href="#builtin-enumerate"><code>enumerate()</code></a></div>
            <div><a href="#builtin-eval"><code>eval()</code></a></div>
            <div><a href="#builtin-exec"><code>exec()</code></a></div>
            <div><br></div>
            <div><strong>F</strong></div>
            <div><a href="#builtin-filter"><code>filter()</code></a></div>
            <div><a href="#builtin-float"><code>float()</code></a></div>
            <div><a href="#builtin-format"><code>format()</code></a></div>
            <div><a href="#builtin-func-frozenset"><code >frozenset()</code></a></div>
            <div><br></div>
            <div><strong>G</strong></div>
            <div><a href="#builtin-getattr"><code>getattr()</code></a></div>
            <div><a href="#builtin-globals"><code>globals()</code></a></div>
            <div><br></div>
            <div><strong>H</strong></div>
            <div><a href="#builtin-hasattr"><code>hasattr()</code></a></div>
            <div><a href="#builtin-hash"><code>hash()</code></a></div>
            <div><a href="#builtin-help"><code>help()</code></a></div>
            <div><a href="#builtin-hex"><code>hex()</code></a></div>
            <div><br></div>
            <div><strong>I</strong></div>
            <div><a href="#builtin-id"><code>id()</code></a></div>
            <div><a href="#builtin-input"><code>input()</code></a></div>
            <div><a href="#builtin-int"><code>int()</code></a></div>
            <div><a href="#builtin-isinstance"><code>isinstance()</code></a></div>
            <div><a href="#builtin-issubclass"><code>issubclass()</code></a></div>
            <div><a href="#builtin-iter"><code>iter()</code></a></div>
        </div>
    </td>
    <td>
        <div>
            <div><strong>L</strong></div>
            <div><a href="#builtin-len"><code>len()</code></a></div>
            <div><a href="#builtin-func-list"><code >list()</code></a></div>
            <div><a href="#builtin-locals"><code>locals()</code></a></div>
            <div><br></div>
            <div><strong>M</strong></div>
            <div><a href="#builtin-map"><code>map()</code></a></div>
            <div><a href="#builtin-max"><code>max()</code></a></div>
            <div><a href="#builtin-func-memoryview"><code >memoryview()</code></a></div>
            <div><a href="#builtin-min"><code>min()</code></a></div>
            <div><br></div>
            <div><strong>N</strong></div>
            <div><a href="#builtin-next"><code>next()</code></a></div>
            <div><br></div>
            <div><strong>O</strong></div>
            <div><a href="#builtin-object"><code>object()</code></a></div>
            <div><a href="#builtin-oct"><code>oct()</code></a></div>
            <div><a href="#builtin-open"><code>open()</code></a></div>
            <div><a href="#builtin-ord"><code>ord()</code></a></div>
            <div><br></div>
            <div><strong>P</strong></div>
            <div><a href="#builtin-pow"><code>pow()</code></a></div>
            <div><a href="#builtin-print"><code>print()</code></a></div>
            <div><a href="#builtin-property"><code>property()</code></a></div>
            <div><br></div>
            <div><br></div>
            <div><br></div>
            <div><br></div>
        </div>
    </td>
    <td>
        <div>
            <div><strong>R</strong></div>
            <div><a href="#builtin-func-range"><code >range()</code></a></div>
            <div><a href="#builtin-repr"><code>repr()</code></a></div>
            <div><a href="#builtin-reversed"><code>reversed()</code></a></div>
            <div><a href="#builtin-round"><code>round()</code></a></div>
            <div><br></div>
            <div><strong>S</strong></div>
            <div><a href="#builtin-func-set"><code >set()</code></a></div>
            <div><a href="#builtin-setattr"><code>setattr()</code></a></div>
            <div><a href="#builtin-slice"><code>slice()</code></a></div>
            <div><a href="#builtin-sorted"><code>sorted()</code></a></div>
            <div><a href="#builtin-staticmethod"><code>staticmethod()</code></a></div>
            <div><a href="#builtin-func-str"><code >str()</code></a></div>
            <div><a href="#builtin-sum"><code>sum()</code></a></div>
            <div><a href="#builtin-super"><code>super()</code></a></div>
            <div><br></div>
            <div><strong>T</strong></div>
            <div><a href="#builtin-func-tuple"><code >tuple()</code></a></div>
            <div><a href="#builtin-type"><code>type()</code></a></div>
            <div><br></div>
            <div><strong>V</strong></div>
            <div><a href="#builtin-vars"><code>vars()</code></a></div>
            <div><br></div>
            <div><strong>Z</strong></div>
            <div><a href="#builtin-zip"><code>zip()</code></a></div>
            <div><br></div>
            <div><strong>_</strong></div>
            <div><a href="#builtin-import"><code>__import__()</code></a></div>
        </div>
    </td>
</tr>
</tbody>
</table>


abs(x)

    Return the absolute value of a number. The argument may be an integer, a floating point number, or an object implementing __abs__(). If the argument is a complex number, its magnitude is returned.

aiter(async_iterable)

    Return an asynchronous iterator for an asynchronous iterable. Equivalent to calling x.__aiter__().

    Note: Unlike iter(), aiter() has no 2-argument variant.

    New in version 3.10.

all(iterable)

    Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:

    def all(iterable):
        for element in iterable:
            if not element:
                return False
        return True

awaitable anext(async_iterator)
awaitable anext(async_iterator, default)

    When awaited, return the next item from the given asynchronous iterator, or default if given and the iterator is exhausted.

    This is the async variant of the next() builtin, and behaves similarly.

    This calls the __anext__() method of async_iterator, returning an awaitable. Awaiting this returns the next value of the iterator. If default is given, it is returned if the iterator is exhausted, otherwise StopAsyncIteration is raised.

    New in version 3.10.

any(iterable)

    Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:

    def any(iterable):
        for element in iterable:
            if element:
                return True
        return False

ascii(object)

    As repr(), return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by repr() using \x, \u, or \U escapes. This generates a string similar to that returned by repr() in Python 2.

bin(x)

    Convert an integer number to a binary string prefixed with “0b”. The result is a valid Python expression. If x is not a Python int object, it has to define an __index__() method that returns an integer. Some examples:
    >>>

bin(3)
'0b11'

bin(-10)
'-0b1010'

If the prefix “0b” is desired or not, you can use either of the following ways.
>>>

format(14, '#b'), format(14, 'b')
('0b1110', '1110')

    f'{14:#b}', f'{14:b}'
    ('0b1110', '1110')

    See also format() for more information.

class bool(x=False)

    Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing procedure. If x is false or omitted, this returns False; otherwise, it returns True. The bool class is a subclass of int (see Numeric Types — int, float, complex). It cannot be subclassed further. Its only instances are False and True (see Boolean Type - bool).

    Changed in version 3.7: x is now a positional-only parameter.

breakpoint(*args, **kws)

    This function drops you into the debugger at the call site. Specifically, it calls sys.breakpointhook(), passing args and kws straight through. By default, sys.breakpointhook() calls pdb.set_trace() expecting no arguments. In this case, it is purely a convenience function so you don’t have to explicitly import pdb or type as much code to enter the debugger. However, sys.breakpointhook() can be set to some other function and breakpoint() will automatically call that, allowing you to drop into the debugger of choice. If sys.breakpointhook() is not accessible, this function will raise RuntimeError.

    By default, the behavior of breakpoint() can be changed with the PYTHONBREAKPOINT environment variable. See sys.breakpointhook() for usage details.

    Note that this is not guaranteed if sys.breakpointhook() has been replaced.

    Raises an auditing event builtins.breakpoint with argument breakpointhook.

    New in version 3.7.

class bytearray(source=b'')
class bytearray(source, encoding)
class bytearray(source, encoding, errors)

    Return a new array of bytes. The bytearray class is a mutable sequence of integers in the range 0 <= x < 256. It has most of the usual methods of mutable sequences, described in Mutable Sequence Types, as well as most methods that the bytes type has, see Bytes and Bytearray Operations.

    The optional source parameter can be used to initialize the array in a few different ways:

        If it is a string, you must also give the encoding (and optionally, errors) parameters; bytearray() then converts the string to bytes using str.encode().

        If it is an integer, the array will have that size and will be initialized with null bytes.

        If it is an object conforming to the buffer interface, a read-only buffer of the object will be used to initialize the bytes array.

        If it is an iterable, it must be an iterable of integers in the range 0 <= x < 256, which are used as the initial contents of the array.

    Without an argument, an array of size 0 is created.

    See also Binary Sequence Types — bytes, bytearray, memoryview and Bytearray Objects.

class bytes(source=b'')
class bytes(source, encoding)
class bytes(source, encoding, errors)

    Return a new “bytes” object which is an immutable sequence of integers in the range 0 <= x < 256. bytes is an immutable version of bytearray – it has the same non-mutating methods and the same indexing and slicing behavior.

    Accordingly, constructor arguments are interpreted as for bytearray().

    Bytes objects can also be created with literals, see String and Bytes literals.

    See also Binary Sequence Types — bytes, bytearray, memoryview, Bytes Objects, and Bytes and Bytearray Operations.

callable(object)

    Return True if the object argument appears callable, False if not. If this returns True, it is still possible that a call fails, but if it is False, calling object will never succeed. Note that classes are callable (calling a class returns a new instance); instances are callable if their class has a __call__() method.

    New in version 3.2: This function was first removed in Python 3.0 and then brought back in Python 3.2.

chr(i)

    Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. This is the inverse of ord().

    The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16). ValueError will be raised if i is outside that range.

@classmethod

    Transform a method into a class method.

    A class method receives the class as an implicit first argument, just like an instance method receives the instance. To declare a class method, use this idiom:

    class C:
        @classmethod
        def f(cls, arg1, arg2): ...

    The @classmethod form is a function decorator – see Function definitions for details.

    A class method can be called either on the class (such as C.f()) or on an instance (such as C().f()). The instance is ignored except for its class. If a class method is called for a derived class, the derived class object is passed as the implied first argument.

    Class methods are different than C++ or Java static methods. If you want those, see staticmethod() in this section. For more information on class methods, see The standard type hierarchy.

    Changed in version 3.9: Class methods can now wrap other descriptors such as property().

    Changed in version 3.10: Class methods now inherit the method attributes (__module__, __name__, __qualname__, __doc__ and __annotations__) and have a new __wrapped__ attribute.

    Changed in version 3.11: Class methods can no longer wrap other descriptors such as property().

compile(source, filename, mode, flags=0, dont_inherit=False, optimize=- 1)

    Compile the source into a code or AST object. Code objects can be executed by exec() or eval(). source can either be a normal string, a byte string, or an AST object. Refer to the ast module documentation for information on how to work with AST objects.

    The filename argument should give the file from which the code was read; pass some recognizable value if it wasn’t read from a file ('<string>' is commonly used).

    The mode argument specifies what kind of code must be compiled; it can be 'exec' if source consists of a sequence of statements, 'eval' if it consists of a single expression, or 'single' if it consists of a single interactive statement (in the latter case, expression statements that evaluate to something other than None will be printed).

    The optional arguments flags and dont_inherit control which compiler options should be activated and which future features should be allowed. If neither is present (or both are zero) the code is compiled with the same flags that affect the code that is calling compile(). If the flags argument is given and dont_inherit is not (or is zero) then the compiler options and the future statements specified by the flags argument are used in addition to those that would be used anyway. If dont_inherit is a non-zero integer then the flags argument is it – the flags (future features and compiler options) in the surrounding code are ignored.

    Compiler options and future statements are specified by bits which can be bitwise ORed together to specify multiple options. The bitfield required to specify a given future feature can be found as the compiler_flag attribute on the _Feature instance in the __future__ module. Compiler flags can be found in ast module, with PyCF_ prefix.

    The argument optimize specifies the optimization level of the compiler; the default value of -1 selects the optimization level of the interpreter as given by -O options. Explicit levels are 0 (no optimization; __debug__ is true), 1 (asserts are removed, __debug__ is false) or 2 (docstrings are removed too).

    This function raises SyntaxError if the compiled source is invalid, and ValueError if the source contains null bytes.

    If you want to parse Python code into its AST representation, see ast.parse().

    Raises an auditing event compile with arguments source and filename. This event may also be raised by implicit compilation.

    Note

    When compiling a string with multi-line code in 'single' or 'eval' mode, input must be terminated by at least one newline character. This is to facilitate detection of incomplete and complete statements in the code module.

    Warning

    It is possible to crash the Python interpreter with a sufficiently large/complex string when compiling to an AST object due to stack depth limitations in Python’s AST compiler.

    Changed in version 3.2: Allowed use of Windows and Mac newlines. Also, input in 'exec' mode does not have to end in a newline anymore. Added the optimize parameter.

    Changed in version 3.5: Previously, TypeError was raised when null bytes were encountered in source.

    New in version 3.8: ast.PyCF_ALLOW_TOP_LEVEL_AWAIT can now be passed in flags to enable support for top-level await, async for, and async with.

class complex(real=0, imag=0)
class complex(string)

    Return a complex number with the value real + imag*1j or convert a string or number to a complex number. If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter. The second parameter can never be a string. Each argument may be any numeric type (including complex). If imag is omitted, it defaults to zero and the constructor serves as a numeric conversion like int and float. If both arguments are omitted, returns 0j.

    For a general Python object x, complex(x) delegates to x.__complex__(). If __complex__() is not defined then it falls back to __float__(). If __float__() is not defined then it falls back to __index__().

    Note

    When converting from a string, the string must not contain whitespace around the central + or - operator. For example, complex('1+2j') is fine, but complex('1 + 2j') raises ValueError.

    The complex type is described in Numeric Types — int, float, complex.

    Changed in version 3.6: Grouping digits with underscores as in code literals is allowed.

    Changed in version 3.8: Falls back to __index__() if __complex__() and __float__() are not defined.

delattr(object, name)

    This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of the object’s attributes. The function deletes the named attribute, provided the object allows it. For example, delattr(x, 'foobar') is equivalent to del x.foobar. name need not be a Python identifier (see setattr()).

class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)

    Create a new dictionary. The dict object is the dictionary class. See dict and Mapping Types — dict for documentation about this class.

    For other containers see the built-in list, set, and tuple classes, as well as the collections module.

dir()
dir(object)

    Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.

    If the object has a method named __dir__(), this method will be called and must return the list of attributes. This allows objects that implement a custom __getattr__() or __getattribute__() function to customize the way dir() reports their attributes.

    If the object does not provide __dir__(), the function tries its best to gather information from the object’s __dict__ attribute, if defined, and from its type object. The resulting list is not necessarily complete and may be inaccurate when the object has a custom __getattr__().

    The default dir() mechanism behaves differently with different types of objects, as it attempts to produce the most relevant, rather than complete, information:

        If the object is a module object, the list contains the names of the module’s attributes.

        If the object is a type or class object, the list contains the names of its attributes, and recursively of the attributes of its bases.

        Otherwise, the list contains the object’s attributes’ names, the names of its class’s attributes, and recursively of the attributes of its class’s base classes.

    The resulting list is sorted alphabetically. For example:
    >>>

import struct

dir()   # show the names in the module namespace  
['__builtins__', '__name__', 'struct']

dir(struct)   # show the names in the struct module 
['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
 '__initializing__', '__loader__', '__name__', '__package__',
 '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
 'unpack', 'unpack_from']

class Shape:

    def __dir__(self):

        return ['area', 'perimeter', 'location']


s = Shape()

    dir(s)
    ['area', 'location', 'perimeter']

    Note

    Because dir() is supplied primarily as a convenience for use at an interactive prompt, it tries to supply an interesting set of names more than it tries to supply a rigorously or consistently defined set of names, and its detailed behavior may change across releases. For example, metaclass attributes are not in the result list when the argument is a class.

divmod(a, b)

    Take two (non-complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division. With mixed operand types, the rules for binary arithmetic operators apply. For integers, the result is the same as (a // b, a % b). For floating point numbers the result is (q, a % b), where q is usually math.floor(a / b) but may be 1 less than that. In any case q * b + a % b is very close to a, if a % b is non-zero it has the same sign as b, and 0 <= abs(a % b) < abs(b).

enumerate(iterable, start=0)

    Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.
    >>>

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

    list(enumerate(seasons, start=1))
    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

    Equivalent to:

    def enumerate(iterable, start=0):
        n = start
        for elem in iterable:
            yield n, elem
            n += 1

eval(expression, globals=None, locals=None)

    The arguments are a string and optional globals and locals. If provided, globals must be a dictionary. If provided, locals can be any mapping object.

    The expression argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the globals and locals dictionaries as global and local namespace. If the globals dictionary is present and does not contain a value for the key __builtins__, a reference to the dictionary of the built-in module builtins is inserted under that key before expression is parsed. That way you can control what builtins are available to the executed code by inserting your own __builtins__ dictionary into globals before passing it to eval(). If the locals dictionary is omitted it defaults to the globals dictionary. If both dictionaries are omitted, the expression is executed with the globals and locals in the environment where eval() is called. Note, eval() does not have access to the nested scopes (non-locals) in the enclosing environment.

    The return value is the result of the evaluated expression. Syntax errors are reported as exceptions. Example:
    >>>

x = 1

    eval('x+1')
    2

    This function can also be used to execute arbitrary code objects (such as those created by compile()). In this case, pass a code object instead of a string. If the code object has been compiled with 'exec' as the mode argument, eval()'s return value will be None.

    Hints: dynamic execution of statements is supported by the exec() function. The globals() and locals() functions return the current global and local dictionary, respectively, which may be useful to pass around for use by eval() or exec().

    If the given source is a string, then leading and trailing spaces and tabs are stripped.

    See ast.literal_eval() for a function that can safely evaluate strings with expressions containing only literals.

    Raises an auditing event exec with the code object as the argument. Code compilation events may also be raised.

exec(object, globals=None, locals=None, /, *, closure=None)

    This function supports dynamic execution of Python code. object must be either a string or a code object. If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs). 1 If it is a code object, it is simply executed. In all cases, the code that’s executed is expected to be valid as file input (see the section File input in the Reference Manual). Be aware that the nonlocal, yield, and return statements may not be used outside of function definitions even within the context of code passed to the exec() function. The return value is None.

    In all cases, if the optional parts are omitted, the code is executed in the current scope. If only globals is provided, it must be a dictionary (and not a subclass of dictionary), which will be used for both the global and the local variables. If globals and locals are given, they are used for the global and local variables, respectively. If provided, locals can be any mapping object. Remember that at the module level, globals and locals are the same dictionary. If exec gets two separate objects as globals and locals, the code will be executed as if it were embedded in a class definition.

    If the globals dictionary does not contain a value for the key __builtins__, a reference to the dictionary of the built-in module builtins is inserted under that key. That way you can control what builtins are available to the executed code by inserting your own __builtins__ dictionary into globals before passing it to exec().

    The closure argument specifies a closure–a tuple of cellvars. It’s only valid when the object is a code object containing free variables. The length of the tuple must exactly match the number of free variables referenced by the code object.

    Raises an auditing event exec with the code object as the argument. Code compilation events may also be raised.

    Note

    The built-in functions globals() and locals() return the current global and local dictionary, respectively, which may be useful to pass around for use as the second and third argument to exec().

    Note

    The default locals act as described for function locals() below: modifications to the default locals dictionary should not be attempted. Pass an explicit locals dictionary if you need to see effects of the code on locals after function exec() returns.

    Changed in version 3.11: Added the closure parameter.

filter(function, iterable)

    Construct an iterator from those elements of iterable for which function is true. iterable may be either a sequence, a container which supports iteration, or an iterator. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.

    Note that filter(function, iterable) is equivalent to the generator expression (item for item in iterable if function(item)) if function is not None and (item for item in iterable if item) if function is None.

    See itertools.filterfalse() for the complementary function that returns elements of iterable for which function is false.

class float(x=0.0)

    Return a floating point number constructed from a number or string x.

    If the argument is a string, it should contain a decimal number, optionally preceded by a sign, and optionally embedded in whitespace. The optional sign may be '+' or '-'; a '+' sign has no effect on the value produced. The argument may also be a string representing a NaN (not-a-number), or positive or negative infinity. More precisely, the input must conform to the floatvalue production rule in the following grammar, after leading and trailing whitespace characters are removed:

    sign        ::=  "+" | "-"
    infinity    ::=  "Infinity" | "inf"
    nan         ::=  "nan"
    digitpart   ::=  digit (["_"] digit)*
    number      ::=  [digitpart] "." digitpart | digitpart ["."]
    exponent    ::=  ("e" | "E") ["+" | "-"] digitpart
    floatnumber ::=  number [exponent]
    floatvalue  ::=  [sign] (floatnumber | infinity | nan)

    Here digit is a Unicode decimal digit (character in the Unicode general category Nd). Case is not significant, so, for example, “inf”, “Inf”, “INFINITY”, and “iNfINity” are all acceptable spellings for positive infinity.

    Otherwise, if the argument is an integer or a floating point number, a floating point number with the same value (within Python’s floating point precision) is returned. If the argument is outside the range of a Python float, an OverflowError will be raised.

    For a general Python object x, float(x) delegates to x.__float__(). If __float__() is not defined then it falls back to __index__().

    If no argument is given, 0.0 is returned.

    Examples:
    >>>

float('+1.23')
1.23

float('   -12345\n')
-12345.0

float('1e-003')
0.001

float('+1E6')
1000000.0

    float('-Infinity')
    -inf

    The float type is described in Numeric Types — int, float, complex.

    Changed in version 3.6: Grouping digits with underscores as in code literals is allowed.

    Changed in version 3.7: x is now a positional-only parameter.

    Changed in version 3.8: Falls back to __index__() if __float__() is not defined.

format(value, format_spec='')

    Convert a value to a “formatted” representation, as controlled by format_spec. The interpretation of format_spec will depend on the type of the value argument; however, there is a standard formatting syntax that is used by most built-in types: Format Specification Mini-Language.

    The default format_spec is an empty string which usually gives the same effect as calling str(value).

    A call to format(value, format_spec) is translated to type(value).__format__(value, format_spec) which bypasses the instance dictionary when searching for the value’s __format__() method. A TypeError exception is raised if the method search reaches object and the format_spec is non-empty, or if either the format_spec or the return value are not strings.

    Changed in version 3.4: object().__format__(format_spec) raises TypeError if format_spec is not an empty string.

class frozenset(iterable=set())

    Return a new frozenset object, optionally with elements taken from iterable. frozenset is a built-in class. See frozenset and Set Types — set, frozenset for documentation about this class.

    For other containers see the built-in set, list, tuple, and dict classes, as well as the collections module.

getattr(object, name)
getattr(object, name, default)

    Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute. For example, getattr(x, 'foobar') is equivalent to x.foobar. If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised. name need not be a Python identifier (see setattr()).

    Note

    Since private name mangling happens at compilation time, one must manually mangle a private attribute’s (attributes with two leading underscores) name in order to retrieve it with getattr().

globals()

    Return the dictionary implementing the current module namespace. For code within functions, this is set when the function is defined and remains the same regardless of where the function is called.

hasattr(object, name)

    The arguments are an object and a string. The result is True if the string is the name of one of the object’s attributes, False if not. (This is implemented by calling getattr(object, name) and seeing whether it raises an AttributeError or not.)

hash(object)

    Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).

    Note

    For objects with custom __hash__() methods, note that hash() truncates the return value based on the bit width of the host machine. See __hash__ for details.

help()
help(request)

    Invoke the built-in help system. (This function is intended for interactive use.) If no argument is given, the interactive help system starts on the interpreter console. If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed on the console. If the argument is any other kind of object, a help page on the object is generated.

    Note that if a slash(/) appears in the parameter list of a function when invoking help(), it means that the parameters prior to the slash are positional-only. For more info, see the FAQ entry on positional-only parameters.

    This function is added to the built-in namespace by the site module.

    Changed in version 3.4: Changes to pydoc and inspect mean that the reported signatures for callables are now more comprehensive and consistent.

hex(x)

    Convert an integer number to a lowercase hexadecimal string prefixed with “0x”. If x is not a Python int object, it has to define an __index__() method that returns an integer. Some examples:
    >>>

hex(255)
'0xff'

hex(-42)
'-0x2a'

If you want to convert an integer number to an uppercase or lower hexadecimal string with prefix or not, you can use either of the following ways:
>>>

'%#x' % 255, '%x' % 255, '%X' % 255
('0xff', 'ff', 'FF')

format(255, '#x'), format(255, 'x'), format(255, 'X')
('0xff', 'ff', 'FF')

    f'{255:#x}', f'{255:x}', f'{255:X}'
    ('0xff', 'ff', 'FF')

    See also format() for more information.

    See also int() for converting a hexadecimal string to an integer using a base of 16.

    Note

    To obtain a hexadecimal string representation for a float, use the float.hex() method.

id(object)

    Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.

    CPython implementation detail: This is the address of the object in memory.

    Raises an auditing event builtins.id with argument id.

input()
input(prompt)

    If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised. Example:
    >>>

s = input('--> ')  
--> Monty Python's Flying Circus

    s  
    "Monty Python's Flying Circus"

    If the readline module was loaded, then input() will use it to provide elaborate line editing and history features.

    Raises an auditing event builtins.input with argument prompt before reading input

    Raises an auditing event builtins.input/result with the result after successfully reading input.

class int(x=0)
class int(x, base=10)

    Return an integer object constructed from a number or string x, or return 0 if no arguments are given. If x defines __int__(), int(x) returns x.__int__(). If x defines __index__(), it returns x.__index__(). If x defines __trunc__(), it returns x.__trunc__(). For floating point numbers, this truncates towards zero.

    If x is not a number or if base is given, then x must be a string, bytes, or bytearray instance representing an integer in radix base. Optionally, the string can be preceded by + or - (with no space in between), have leading zeros, be surrounded by whitespace, and have single underscores interspersed between digits.

    A base-n integer string contains digits, each representing a value from 0 to n-1. The values 0–9 can be represented by any Unicode decimal digit. The values 10–35 can be represented by a to z (or A to Z). The default base is 10. The allowed bases are 0 and 2–36. Base-2, -8, and -16 strings can be optionally prefixed with 0b/0B, 0o/0O, or 0x/0X, as with integer literals in code. For base 0, the string is interpreted in a similar way to an integer literal in code, in that the actual base is 2, 8, 10, or 16 as determined by the prefix. Base 0 also disallows leading zeros: int('010', 0) is not legal, while int('010') and int('010', 8) are.

    The integer type is described in Numeric Types — int, float, complex.

    Changed in version 3.4: If base is not an instance of int and the base object has a base.__index__ method, that method is called to obtain an integer for the base. Previous versions used base.__int__ instead of base.__index__.

    Changed in version 3.6: Grouping digits with underscores as in code literals is allowed.

    Changed in version 3.7: x is now a positional-only parameter.

    Changed in version 3.8: Falls back to __index__() if __int__() is not defined.

    Changed in version 3.11: The delegation to __trunc__() is deprecated.

    Changed in version 3.11: int string inputs and string representations can be limited to help avoid denial of service attacks. A ValueError is raised when the limit is exceeded while converting a string x to an int or when converting an int into a string would exceed the limit. See the integer string conversion length limitation documentation.

isinstance(object, classinfo)

    Return True if the object argument is an instance of the classinfo argument, or of a (direct, indirect, or virtual) subclass thereof. If object is not an object of the given type, the function always returns False. If classinfo is a tuple of type objects (or recursively, other such tuples) or a Union Type of multiple types, return True if object is an instance of any of the types. If classinfo is not a type or tuple of types and such tuples, a TypeError exception is raised. TypeError may not be raised for an invalid type if an earlier check succeeds.

    Changed in version 3.10: classinfo can be a Union Type.

issubclass(class, classinfo)

    Return True if class is a subclass (direct, indirect, or virtual) of classinfo. A class is considered a subclass of itself. classinfo may be a tuple of class objects (or recursively, other such tuples) or a Union Type, in which case return True if class is a subclass of any entry in classinfo. In any other case, a TypeError exception is raised.

    Changed in version 3.10: classinfo can be a Union Type.

iter(object)
iter(object, sentinel)

    Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument. Without a second argument, object must be a collection object which supports the iterable protocol (the __iter__() method), or it must support the sequence protocol (the __getitem__() method with integer arguments starting at 0). If it does not support either of those protocols, TypeError is raised. If the second argument, sentinel, is given, then object must be a callable object. The iterator created in this case will call object with no arguments for each call to its __next__() method; if the value returned is equal to sentinel, StopIteration will be raised, otherwise the value will be returned.

    See also Iterator Types.

    One useful application of the second form of iter() is to build a block-reader. For example, reading fixed-width blocks from a binary database file until the end of file is reached:

    from functools import partial
    with open('mydata.db', 'rb') as f:
        for block in iter(partial(f.read, 64), b''):
            process_block(block)

len(s)

    Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

    CPython implementation detail: len raises OverflowError on lengths larger than sys.maxsize, such as range(2 ** 100).

class list
class list(iterable)

    Rather than being a function, list is actually a mutable sequence type, as documented in Lists and Sequence Types — list, tuple, range.

locals()

    Update and return a dictionary representing the current local symbol table. Free variables are returned by locals() when it is called in function blocks, but not in class blocks. Note that at the module level, locals() and globals() are the same dictionary.

    Note

    The contents of this dictionary should not be modified; changes may not affect the values of local and free variables used by the interpreter.

map(function, iterable, *iterables)

    Return an iterator that applies function to every item of iterable, yielding the results. If additional iterables arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted. For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().

max(iterable, *, key=None)
max(iterable, *, default, key=None)
max(arg1, arg2, *args, key=None)

    Return the largest item in an iterable or the largest of two or more arguments.

    If one positional argument is provided, it should be an iterable. The largest item in the iterable is returned. If two or more positional arguments are provided, the largest of the positional arguments is returned.

    There are two optional keyword-only arguments. The key argument specifies a one-argument ordering function like that used for list.sort(). The default argument specifies an object to return if the provided iterable is empty. If the iterable is empty and default is not provided, a ValueError is raised.

    If multiple items are maximal, the function returns the first one encountered. This is consistent with other sort-stability preserving tools such as sorted(iterable, key=keyfunc, reverse=True)[0] and heapq.nlargest(1, iterable, key=keyfunc).

    New in version 3.4: The default keyword-only argument.

    Changed in version 3.8: The key can be None.

class memoryview(object)

    Return a “memory view” object created from the given argument. See Memory Views for more information.

min(iterable, *, key=None)
min(iterable, *, default, key=None)
min(arg1, arg2, *args, key=None)

    Return the smallest item in an iterable or the smallest of two or more arguments.

    If one positional argument is provided, it should be an iterable. The smallest item in the iterable is returned. If two or more positional arguments are provided, the smallest of the positional arguments is returned.

    There are two optional keyword-only arguments. The key argument specifies a one-argument ordering function like that used for list.sort(). The default argument specifies an object to return if the provided iterable is empty. If the iterable is empty and default is not provided, a ValueError is raised.

    If multiple items are minimal, the function returns the first one encountered. This is consistent with other sort-stability preserving tools such as sorted(iterable, key=keyfunc)[0] and heapq.nsmallest(1, iterable, key=keyfunc).

    New in version 3.4: The default keyword-only argument.

    Changed in version 3.8: The key can be None.

next(iterator)
next(iterator, default)

    Retrieve the next item from the iterator by calling its __next__() method. If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.

class object

    Return a new featureless object. object is a base for all classes. It has methods that are common to all instances of Python classes. This function does not accept any arguments.

    Note

    object does not have a __dict__, so you can’t assign arbitrary attributes to an instance of the object class.

oct(x)

    Convert an integer number to an octal string prefixed with “0o”. The result is a valid Python expression. If x is not a Python int object, it has to define an __index__() method that returns an integer. For example:
    >>>

oct(8)
'0o10'

oct(-56)
'-0o70'

If you want to convert an integer number to an octal string either with the prefix “0o” or not, you can use either of the following ways.
>>>

'%#o' % 10, '%o' % 10
('0o12', '12')

format(10, '#o'), format(10, 'o')
('0o12', '12')

    f'{10:#o}', f'{10:o}'
    ('0o12', '12')

    See also format() for more information.

open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

    Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised. See Reading and Writing Files for more examples of how to use this function.

    file is a path-like object giving the pathname (absolute or relative to the current working directory) of the file to be opened or an integer file descriptor of the file to be wrapped. (If a file descriptor is given, it is closed when the returned I/O object is closed unless closefd is set to False.)

    mode is an optional string that specifies the mode in which the file is opened. It defaults to 'r' which means open for reading in text mode. Other common values are 'w' for writing (truncating the file if it already exists), 'x' for exclusive creation, and 'a' for appending (which on some Unix systems, means that all writes append to the end of the file regardless of the current seek position). In text mode, if encoding is not specified the encoding used is platform-dependent: locale.getencoding() is called to get the current locale encoding. (For reading and writing raw bytes use binary mode and leave encoding unspecified.) The available modes are:

    Character
    	

    Meaning

    'r'
    	

    open for reading (default)

    'w'
    	

    open for writing, truncating the file first

    'x'
    	

    open for exclusive creation, failing if the file already exists

    'a'
    	

    open for writing, appending to the end of file if it exists

    'b'
    	

    binary mode

    't'
    	

    text mode (default)

    '+'
    	

    open for updating (reading and writing)

    The default mode is 'r' (open for reading text, a synonym of 'rt'). Modes 'w+' and 'w+b' open and truncate the file. Modes 'r+' and 'r+b' open the file with no truncation.

    As mentioned in the Overview, Python distinguishes between binary and text I/O. Files opened in binary mode (including 'b' in the mode argument) return contents as bytes objects without any decoding. In text mode (the default, or when 't' is included in the mode argument), the contents of the file are returned as str, the bytes having been first decoded using a platform-dependent encoding or using the specified encoding if given.

    Note

    Python doesn’t depend on the underlying operating system’s notion of text files; all the processing is done by Python itself, and is therefore platform-independent.

    buffering is an optional integer used to set the buffering policy. Pass 0 to switch buffering off (only allowed in binary mode), 1 to select line buffering (only usable in text mode), and an integer > 1 to indicate the size in bytes of a fixed-size chunk buffer. Note that specifying a buffer size this way applies for binary buffered I/O, but TextIOWrapper (i.e., files opened with mode='r+') would have another buffering. To disable buffering in TextIOWrapper, consider using the write_through flag for io.TextIOWrapper.reconfigure(). When no buffering argument is given, the default buffering policy works as follows:

        Binary files are buffered in fixed-size chunks; the size of the buffer is chosen using a heuristic trying to determine the underlying device’s “block size” and falling back on io.DEFAULT_BUFFER_SIZE. On many systems, the buffer will typically be 4096 or 8192 bytes long.

        “Interactive” text files (files for which isatty() returns True) use line buffering. Other text files use the policy described above for binary files.

    encoding is the name of the encoding used to decode or encode the file. This should only be used in text mode. The default encoding is platform dependent (whatever locale.getencoding() returns), but any text encoding supported by Python can be used. See the codecs module for the list of supported encodings.

    errors is an optional string that specifies how encoding and decoding errors are to be handled—this cannot be used in binary mode. A variety of standard error handlers are available (listed under Error Handlers), though any error handling name that has been registered with codecs.register_error() is also valid. The standard names include:

        'strict' to raise a ValueError exception if there is an encoding error. The default value of None has the same effect.

        'ignore' ignores errors. Note that ignoring encoding errors can lead to data loss.

        'replace' causes a replacement marker (such as '?') to be inserted where there is malformed data.

        'surrogateescape' will represent any incorrect bytes as low surrogate code units ranging from U+DC80 to U+DCFF. These surrogate code units will then be turned back into the same bytes when the surrogateescape error handler is used when writing data. This is useful for processing files in an unknown encoding.

        'xmlcharrefreplace' is only supported when writing to a file. Characters not supported by the encoding are replaced with the appropriate XML character reference &#nnn;.

        'backslashreplace' replaces malformed data by Python’s backslashed escape sequences.

        'namereplace' (also only supported when writing) replaces unsupported characters with \N{...} escape sequences.

    newline determines how to parse newline characters from the stream. It can be None, '', '\n', '\r', and '\r\n'. It works as follows:

        When reading input from the stream, if newline is None, universal newlines mode is enabled. Lines in the input can end in '\n', '\r', or '\r\n', and these are translated into '\n' before being returned to the caller. If it is '', universal newlines mode is enabled, but line endings are returned to the caller untranslated. If it has any of the other legal values, input lines are only terminated by the given string, and the line ending is returned to the caller untranslated.

        When writing output to the stream, if newline is None, any '\n' characters written are translated to the system default line separator, os.linesep. If newline is '' or '\n', no translation takes place. If newline is any of the other legal values, any '\n' characters written are translated to the given string.

    If closefd is False and a file descriptor rather than a filename was given, the underlying file descriptor will be kept open when the file is closed. If a filename is given closefd must be True (the default); otherwise, an error will be raised.

    A custom opener can be used by passing a callable as opener. The underlying file descriptor for the file object is then obtained by calling opener with (file, flags). opener must return an open file descriptor (passing os.open as opener results in functionality similar to passing None).

    The newly created file is non-inheritable.

    The following example uses the dir_fd parameter of the os.open() function to open a file relative to a given directory:
    >>>

import os

dir_fd = os.open('somedir', os.O_RDONLY)

def opener(path, flags):

    return os.open(path, flags, dir_fd=dir_fd)


with open('spamspam.txt', 'w', opener=opener) as f:

    print('This will be written to somedir/spamspam.txt', file=f)


    os.close(dir_fd)  # don't leak a file descriptor

    The type of file object returned by the open() function depends on the mode. When open() is used to open a file in a text mode ('w', 'r', 'wt', 'rt', etc.), it returns a subclass of io.TextIOBase (specifically io.TextIOWrapper). When used to open a file in a binary mode with buffering, the returned class is a subclass of io.BufferedIOBase. The exact class varies: in read binary mode, it returns an io.BufferedReader; in write binary and append binary modes, it returns an io.BufferedWriter, and in read/write mode, it returns an io.BufferedRandom. When buffering is disabled, the raw stream, a subclass of io.RawIOBase, io.FileIO, is returned.

    See also the file handling modules, such as fileinput, io (where open() is declared), os, os.path, tempfile, and shutil.

    Raises an auditing event open with arguments file, mode, flags.

    The mode and flags arguments may have been modified or inferred from the original call.

    Changed in version 3.3:

        The opener parameter was added.

        The 'x' mode was added.

        IOError used to be raised, it is now an alias of OSError.

        FileExistsError is now raised if the file opened in exclusive creation mode ('x') already exists.

    Changed in version 3.4:

        The file is now non-inheritable.

    Changed in version 3.5:

        If the system call is interrupted and the signal handler does not raise an exception, the function now retries the system call instead of raising an InterruptedError exception (see PEP 475 for the rationale).

        The 'namereplace' error handler was added.

    Changed in version 3.6:

        Support added to accept objects implementing os.PathLike.

        On Windows, opening a console buffer may return a subclass of io.RawIOBase other than io.FileIO.

    Changed in version 3.11: The 'U' mode has been removed.

ord(c)

    Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().

pow(base, exp, mod=None)

    Return base to the power exp; if mod is present, return base to the power exp, modulo mod (computed more efficiently than pow(base, exp) % mod). The two-argument form pow(base, exp) is equivalent to using the power operator: base**exp.

    The arguments must have numeric types. With mixed operand types, the coercion rules for binary arithmetic operators apply. For int operands, the result has the same type as the operands (after coercion) unless the second argument is negative; in that case, all arguments are converted to float and a float result is delivered. For example, pow(10, 2) returns 100, but pow(10, -2) returns 0.01. For a negative base of type int or float and a non-integral exponent, a complex result is delivered. For example, pow(-9, 0.5) returns a value close to 3j.

    For int operands base and exp, if mod is present, mod must also be of integer type and mod must be nonzero. If mod is present and exp is negative, base must be relatively prime to mod. In that case, pow(inv_base, -exp, mod) is returned, where inv_base is an inverse to base modulo mod.

    Here’s an example of computing an inverse for 38 modulo 97:
    >>>

pow(38, -1, mod=97)
23

    23 * 38 % 97 == 1
    True

    Changed in version 3.8: For int operands, the three-argument form of pow now allows the second argument to be negative, permitting computation of modular inverses.

    Changed in version 3.8: Allow keyword arguments. Formerly, only positional arguments were supported.

print(*objects, sep=' ', end='\n', file=None, flush=False)

    Print objects to the text stream file, separated by sep and followed by end. sep, end, file, and flush, if present, must be given as keyword arguments.

    All non-keyword arguments are converted to strings like str() does and written to the stream, separated by sep and followed by end. Both sep and end must be strings; they can also be None, which means to use the default values. If no objects are given, print() will just write end.

    The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. Since printed arguments are converted to text strings, print() cannot be used with binary mode file objects. For these, use file.write(...) instead.

    Output buffering is usually determined by file. However, if flush is true, the stream is forcibly flushed.

    Changed in version 3.3: Added the flush keyword argument.

class property(fget=None, fset=None, fdel=None, doc=None)

    Return a property attribute.

    fget is a function for getting an attribute value. fset is a function for setting an attribute value. fdel is a function for deleting an attribute value. And doc creates a docstring for the attribute.

    A typical use is to define a managed attribute x:

    class C:
        def __init__(self):
            self._x = None

        def getx(self):
            return self._x

        def setx(self, value):
            self._x = value

        def delx(self):
            del self._x

        x = property(getx, setx, delx, "I'm the 'x' property.")

    If c is an instance of C, c.x will invoke the getter, c.x = value will invoke the setter, and del c.x the deleter.

    If given, doc will be the docstring of the property attribute. Otherwise, the property will copy fget’s docstring (if it exists). This makes it possible to create read-only properties easily using property() as a decorator:

    class Parrot:
        def __init__(self):
            self._voltage = 100000

        @property
        def voltage(self):
            """Get the current voltage."""
            return self._voltage

    The @property decorator turns the voltage() method into a “getter” for a read-only attribute with the same name, and it sets the docstring for voltage to “Get the current voltage.”

    A property object has getter, setter, and deleter methods usable as decorators that create a copy of the property with the corresponding accessor function set to the decorated function. This is best explained with an example:

    class C:
        def __init__(self):
            self._x = None

        @property
        def x(self):
            """I'm the 'x' property."""
            return self._x

        @x.setter
        def x(self, value):
            self._x = value

        @x.deleter
        def x(self):
            del self._x

    This code is exactly equivalent to the first example. Be sure to give the additional functions the same name as the original property (x in this case.)

    The returned property object also has the attributes fget, fset, and fdel corresponding to the constructor arguments.

    Changed in version 3.5: The docstrings of property objects are now writeable.

class range(stop)
class range(start, stop, step=1)

    Rather than being a function, range is actually an immutable sequence type, as documented in Ranges and Sequence Types — list, tuple, range.

repr(object)

    Return a string containing a printable representation of an object. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(); otherwise, the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a __repr__() method. If sys.displayhook() is not accessible, this function will raise RuntimeError.

reversed(seq)

    Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).

round(number, ndigits=None)

    Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.

    For the built-in types supporting round(), values are rounded to the closest multiple of 10 to the power minus ndigits; if two multiples are equally close, rounding is done toward the even choice (so, for example, both round(0.5) and round(-0.5) are 0, and round(1.5) is 2). Any integer value is valid for ndigits (positive, zero, or negative). The return value is an integer if ndigits is omitted or None. Otherwise, the return value has the same type as number.

    For a general Python object number, round delegates to number.__round__.

    Note

    The behavior of round() for floats can be surprising: for example, round(2.675, 2) gives 2.67 instead of the expected 2.68. This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float. See Floating Point Arithmetic: Issues and Limitations for more information.

class set
class set(iterable)

    Return a new set object, optionally with elements taken from iterable. set is a built-in class. See set and Set Types — set, frozenset for documentation about this class.

    For other containers see the built-in frozenset, list, tuple, and dict classes, as well as the collections module.

setattr(object, name, value)

    This is the counterpart of getattr(). The arguments are an object, a string, and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it. For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.

    name need not be a Python identifier as defined in Identifiers and keywords unless the object chooses to enforce that, for example in a custom __getattribute__() or via __slots__. An attribute whose name is not an identifier will not be accessible using the dot notation, but is accessible through getattr() etc..

    Note

    Since private name mangling happens at compilation time, one must manually mangle a private attribute’s (attributes with two leading underscores) name in order to set it with setattr().

class slice(stop)
class slice(start, stop, step=None)

    Return a slice object representing the set of indices specified by range(start, stop, step). The start and step arguments default to None. Slice objects have read-only data attributes start, stop, and step which merely return the argument values (or their default). They have no other explicit functionality; however, they are used by NumPy and other third-party packages. Slice objects are also generated when extended indexing syntax is used. For example: a[start:stop:step] or a[start:stop, i]. See itertools.islice() for an alternate version that returns an iterator.

    Changed in version 3.12: Slice objects are now hashable (provided start, stop, and step are hashable).

sorted(iterable, /, *, key=None, reverse=False)

    Return a new sorted list from the items in iterable.

    Has two optional arguments which must be specified as keyword arguments.

    key specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). The default value is None (compare the elements directly).

    reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

    Use functools.cmp_to_key() to convert an old-style cmp function to a key function.

    The built-in sorted() function is guaranteed to be stable. A sort is stable if it guarantees not to change the relative order of elements that compare equal — this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade).

    The sort algorithm uses only < comparisons between items. While defining an __lt__() method will suffice for sorting, PEP 8 recommends that all six rich comparisons be implemented. This will help avoid bugs when using the same data with other ordering tools such as max() that rely on a different underlying method. Implementing all six comparisons also helps avoid confusion for mixed type comparisons which can call reflected the __gt__() method.

    For sorting examples and a brief sorting tutorial, see Sorting HOW TO.

@staticmethod

    Transform a method into a static method.

    A static method does not receive an implicit first argument. To declare a static method, use this idiom:

    class C:
        @staticmethod
        def f(arg1, arg2, argN): ...

    The @staticmethod form is a function decorator – see Function definitions for details.

    A static method can be called either on the class (such as C.f()) or on an instance (such as C().f()). Moreover, they can be called as regular functions (such as f()).

    Static methods in Python are similar to those found in Java or C++. Also, see classmethod() for a variant that is useful for creating alternate class constructors.

    Like all decorators, it is also possible to call staticmethod as a regular function and do something with its result. This is needed in some cases where you need a reference to a function from a class body and you want to avoid the automatic transformation to instance method. For these cases, use this idiom:

    def regular_function():
        ...

    class C:
        method = staticmethod(regular_function)

    For more information on static methods, see The standard type hierarchy.

    Changed in version 3.10: Static methods now inherit the method attributes (__module__, __name__, __qualname__, __doc__ and __annotations__), have a new __wrapped__ attribute, and are now callable as regular functions.

class str(object='')
class str(object=b'', encoding='utf-8', errors='strict')

    Return a str version of object. See str() for details.

    str is the built-in string class. For general information about strings, see Text Sequence Type — str.

sum(iterable, /, start=0)

    Sums start and the items of an iterable from left to right and returns the total. The iterable’s items are normally numbers, and the start value is not allowed to be a string.

    For some use cases, there are good alternatives to sum(). The preferred, fast way to concatenate a sequence of strings is by calling ''.join(sequence). To add floating point values with extended precision, see math.fsum(). To concatenate a series of iterables, consider using itertools.chain().

    Changed in version 3.8: The start parameter can be specified as a keyword argument.

    Changed in version 3.12: Summation of floats switched to an algorithm that gives higher accuracy on most builds.

class super
class super(type, object_or_type=None)

    Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class.

    The object_or_type determines the method resolution order to be searched. The search starts from the class right after the type.

    For example, if __mro__ of object_or_type is D -> B -> C -> A -> object and the value of type is B, then super() searches C -> A -> object.

    The __mro__ attribute of the object_or_type lists the method resolution search order used by both getattr() and super(). The attribute is dynamic and can change whenever the inheritance hierarchy is updated.

    If the second argument is omitted, the super object returned is unbound. If the second argument is an object, isinstance(obj, type) must be true. If the second argument is a type, issubclass(type2, type) must be true (this is useful for classmethods).

    There are two typical use cases for super. In a class hierarchy with single inheritance, super can be used to refer to parent classes without naming them explicitly, thus making the code more maintainable. This use closely parallels the use of super in other programming languages.

    The second use case is to support cooperative multiple inheritance in a dynamic execution environment. This use case is unique to Python and is not found in statically compiled languages or languages that only support single inheritance. This makes it possible to implement “diamond diagrams” where multiple base classes implement the same method. Good design dictates that such implementations have the same calling signature in every case (because the order of calls is determined at runtime, because that order adapts to changes in the class hierarchy, and because that order can include sibling classes that are unknown prior to runtime).

    For both use cases, a typical superclass call looks like this:

    class C(B):
        def method(self, arg):
            super().method(arg)    # This does the same thing as:
                                   # super(C, self).method(arg)

    In addition to method lookups, super() also works for attribute lookups. One possible use case for this is calling descriptors in a parent or sibling class.

    Note that super() is implemented as part of the binding process for explicit dotted attribute lookups such as super().__getitem__(name). It does so by implementing its own __getattribute__() method for searching classes in a predictable order that supports cooperative multiple inheritance. Accordingly, super() is undefined for implicit lookups using statements or operators such as super()[name].

    Also note that, aside from the zero argument form, super() is not limited to use inside methods. The two argument form specifies the arguments exactly and makes the appropriate references. The zero argument form only works inside a class definition, as the compiler fills in the necessary details to correctly retrieve the class being defined, as well as accessing the current instance for ordinary methods.

    For practical suggestions on how to design cooperative classes using super(), see guide to using super().

class tuple
class tuple(iterable)

    Rather than being a function, tuple is actually an immutable sequence type, as documented in Tuples and Sequence Types — list, tuple, range.

class type(object)
class type(name, bases, dict, **kwds)

    With one argument, return the type of an object. The return value is a type object and generally the same object as returned by object.__class__.

    The isinstance() built-in function is recommended for testing the type of an object, because it takes subclasses into account.

    With three arguments, return a new type object. This is essentially a dynamic form of the class statement. The name string is the class name and becomes the __name__ attribute. The bases tuple contains the base classes and becomes the __bases__ attribute; if empty, object, the ultimate base of all classes, is added. The dict dictionary contains attribute and method definitions for the class body; it may be copied or wrapped before becoming the __dict__ attribute. The following two statements create identical type objects:
    >>>

class X:

    a = 1


    X = type('X', (), dict(a=1))

    See also Type Objects.

    Keyword arguments provided to the three argument form are passed to the appropriate metaclass machinery (usually __init_subclass__()) in the same way that keywords in a class definition (besides metaclass) would.

    See also Customizing class creation.

    Changed in version 3.6: Subclasses of type which don’t override type.__new__ may no longer use the one-argument form to get the type of an object.

vars()
vars(object)

    Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.

    Objects such as modules and instances have an updateable __dict__ attribute; however, other objects may have write restrictions on their __dict__ attributes (for example, classes use a types.MappingProxyType to prevent direct dictionary updates).

    Without an argument, vars() acts like locals(). Note, the locals dictionary is only useful for reads since updates to the locals dictionary are ignored.

    A TypeError exception is raised if an object is specified but it doesn’t have a __dict__ attribute (for example, if its class defines the __slots__ attribute).

zip(*iterables, strict=False)

    Iterate over several iterables in parallel, producing tuples with an item from each one.

    Example:
    >>>

for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):

    print(item)


(1, 'sugar')
(2, 'spice')
(3, 'everything nice')

More formally: zip() returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument iterables.

Another way to think of zip() is that it turns rows into columns, and columns into rows. This is similar to transposing a matrix.

zip() is lazy: The elements won’t be processed until the iterable is iterated on, e.g. by a for loop or by wrapping in a list.

One thing to consider is that the iterables passed to zip() could have different lengths; sometimes by design, and sometimes because of a bug in the code that prepared these iterables. Python offers three different approaches to dealing with this issue:

    By default, zip() stops when the shortest iterable is exhausted. It will ignore the remaining items in the longer iterables, cutting off the result to the length of the shortest iterable:
    >>>

list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
[(0, 'fee'), (1, 'fi'), (2, 'fo')]

zip() is often used in cases where the iterables are assumed to be of equal length. In such cases, it’s recommended to use the strict=True option. Its output is the same as regular zip():
>>>

list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))
[('a', 1), ('b', 2), ('c', 3)]

Unlike the default behavior, it raises a ValueError if one iterable is exhausted before the others:
>>>

for item in zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True):  

    print(item)


    (0, 'fee')
    (1, 'fi')
    (2, 'fo')
    Traceback (most recent call last):
      ...
    ValueError: zip() argument 2 is longer than argument 1

    Without the strict=True argument, any bug that results in iterables of different lengths will be silenced, possibly manifesting as a hard-to-find bug in another part of the program.

    Shorter iterables can be padded with a constant value to make all the iterables have the same length. This is done by itertools.zip_longest().

Edge cases: With a single iterable argument, zip() returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.

Tips and tricks:

    The left-to-right evaluation order of the iterables is guaranteed. This makes possible an idiom for clustering a data series into n-length groups using zip(*[iter(s)]*n, strict=True). This repeats the same iterator n times so that each output tuple has the result of n calls to the iterator. This has the effect of dividing the input into n-length chunks.

    zip() in conjunction with the * operator can be used to unzip a list:
    >>>

x = [1, 2, 3]

y = [4, 5, 6]

list(zip(x, y))
[(1, 4), (2, 5), (3, 6)]

x2, y2 = zip(*zip(x, y))

        x == list(x2) and y == list(y2)
        True

    Changed in version 3.10: Added the strict argument.

__import__(name, globals=None, locals=None, fromlist=(), level=0)

    Note

    This is an advanced function that is not needed in everyday Python programming, unlike importlib.import_module().

    This function is invoked by the import statement. It can be replaced (by importing the builtins module and assigning to builtins.__import__) in order to change semantics of the import statement, but doing so is strongly discouraged as it is usually simpler to use import hooks (see PEP 302) to attain the same goals and does not cause issues with code which assumes the default import implementation is in use. Direct use of __import__() is also discouraged in favor of importlib.import_module().

    The function imports the module name, potentially using the given globals and locals to determine how to interpret the name in a package context. The fromlist gives the names of objects or submodules that should be imported from the module given by name. The standard implementation does not use its locals argument at all and uses its globals only to determine the package context of the import statement.

    level specifies whether to use absolute or relative imports. 0 (the default) means only perform absolute imports. Positive values for level indicate the number of parent directories to search relative to the directory of the module calling __import__() (see PEP 328 for the details).

    When the name variable is of the form package.module, normally, the top-level package (the name up till the first dot) is returned, not the module named by name. However, when a non-empty fromlist argument is given, the module named by name is returned.

    For example, the statement import spam results in bytecode resembling the following code:

    spam = __import__('spam', globals(), locals(), [], 0)

    The statement import spam.ham results in this call:

    spam = __import__('spam.ham', globals(), locals(), [], 0)

    Note how __import__() returns the toplevel module here because this is the object that is bound to a name by the import statement.

    On the other hand, the statement from spam.ham import eggs, sausage as saus results in

    _temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
    eggs = _temp.eggs
    saus = _temp.sausage

    Here, the spam.ham module is returned from __import__(). From this object, the names to import are retrieved and assigned to their respective names.

    If you simply want to import a module (potentially within a package) by name, use importlib.import_module().

## Builtin constants

A small number of constants are defined in the builtin namespace: `False`, `True`, `None`, `NotImplemented`, `Ellipsis`, and `__debug__`. These names cannot be reassigned, and assignments to them, even as an attribute name, raise `SyntaxError`.

Additionally, the site module (which is imported automatically during startup, except if the `-S` command-line option is given) adds some constants to the builtin namespace. These are `quit()`, `exit()`, `copyright`, `credits`, and `license`. They are useful for the interactive interpreter shell and should not be used in programs.

`False`
: The false value of the `bool` type. Assignments to `False` are illegal and raise a `SyntaxError`.

`True`
: The true value of the `bool` type. Assignments to `True` are illegal and raise a `SyntaxError`.

`None`
: An object frequently used to represent the absence of a value, such as when default arguments are not passed to a function. Assignments to `None` are illegal and raise a `SyntaxError`. None is the sole instance of the `NoneType` type.

`NotImplemented`
: A special value which should be returned by the binary special methods (such as `__eq__()`, `__lt__()`, `__add__()`, and `__rsub__()`) to indicate that the operation is not implemented with respect to the other type. It may be returned by the in-place binary special methods (such as `__imul__()` and `__iand__()`) for the same purpose. It should not be evaluated in a boolean context. `NotImplemented` is the sole instance of the `types.NotImplementedType` type.

`Ellipsis`
: The same as the ellipsis literal `...`. It is a special value used mostly in conjunction with extended slicing syntax for user-defined container data types. `Ellipsis` is the sole instance of the `types.EllipsisType` type.

`__debug__`
: This constant is true if Python was not started with an `-O` option.

`quit(code=None)`
: Object that when printed, prints the mwssage "Use quit() or Ctrl-D (EOF) to exit", and when called, raises `SystemExit` with the specified exit code.

`exit(code=None)`
: Object that when printed, prints the mwssage "Use quit() or Ctrl-D (EOF) to exit", and when called, raises `SystemExit` with the specified exit code.

`copyright`
: Object that when printed or called, prints the text of copyright.

`credits`
: Object that when printed or called, prints the text of credits.

`license`
: Object that when printed, prints the message "Type license() to see the full license text", and when called, displays the full license text in a pager-like fashion.

