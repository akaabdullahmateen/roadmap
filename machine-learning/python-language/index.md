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
