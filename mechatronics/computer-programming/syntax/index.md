# Syntax

<!-- omit in toc -->
## Table of contents

- [Comments](#comments)
  - [Single line comments](#single-line-comments)
  - [Multiline comments](#multiline-comments)
- [Line structure](#line-structure)
  - [Line categories](#line-categories)
    - [Physical lines](#physical-lines)
    - [Logical lines](#logical-lines)
    - [Blank lines](#blank-lines)
  - [Line joining](#line-joining)
    - [Explicit line joining](#explicit-line-joining)
    - [Implicit line joining](#implicit-line-joining)
- [Indentation](#indentation)
  - [Rules](#rules)
  - [Whitespace between tokens](#whitespace-between-tokens)
- [Grammar](#grammar)
  - [Identifiers](#identifiers)
  - [Keywords](#keywords)
  - [Soft keywords](#soft-keywords)
  - [Reserved classes of identifiers](#reserved-classes-of-identifiers)
  - [Literals](#literals)
  - [Operators](#operators)
  - [Delimiters](#delimiters)

## Comments

A comment is a text added to the program for documentation purposes. It is ignored by the program parser.

### Single line comments

In Python, a comment starts with a hash character (`#`) and continues till the end of the physical line.

```py
# This is a comment
print("something") # This is another comment
```

### Multiline comments

Although Python does not support multiline comments, they can be be artificially created by wrapping the multiline comment text inside a pair of triple quotes.

```py
"""
This is a multiline comment
This is part of the multiline comment
"""
```

This hack works because it is a string that is not assigned to any variable, so it is not called or referenced by the program. Therefore, it is ignored at runtime, behaving similar to an actual comment.

## Line structure

### Line categories

#### Physical lines

A physical line is a sequence of characters terminated by an end-of-line sequence.

The following end-of-lines sequences can be used equally regardless of the platform:

- Unix-style LF (line feed)
- Windows-style CRLF (carriage return followed by line feed)
- Old Macintosh-style CR (carriage return)

#### Logical lines

Some statements allow continuing over multiple physical lines. In those cases, a logical line is constructed from one or more physical lines by following explicit or implicit line joining rules. In other cases, a logical line is equivalent to the physical line.

#### Blank lines

A blank line is a logical line that contains only whitespaces and comments. An entirely blank line does not even contain whitespaces or comments.

- When parsing the source file, blank lines are ignored.
- In the standard interactive interpreter, an entirely blank line terminates a multiline statement.
- In other read-eval-print loops (REPL), the handling of a blank line is implementation-defined.

### Line joining

#### Explicit line joining

Explicit line joining occurs when the statement syntax allows splitting over multiple physical lines, with a backslash character (`\`). Such statements include:

Statements
: Any statement, as long as individual tokens are kept intact.

    ```py
    m_int = 1 + 2 + \
            3 + 4
    ```

Strings
: Any string, as long as individual words are kept intact.

    ```py
    m_string = "Long long long  \
                long long line"
    ```

When joining such physical lines into a single logical line, the backslash characters (and the following end-of-line sequence) are deleted. Moreover, a line ending in backslash can not carry a comment.

#### Implicit line joining

Implicit line joining occurs when the statement syntax allows splitting over multiple physical lines, without the need for backslashes. Such statements includes:

Expressions
: Expressions that are enclosed within a pair of parentheses, square brackets, or curly braces. These can carry comments.

    ```py
    alphabets = ["A", "B", "C",
                "D", "E", "F"]
    ```

Strings
: Strings that are enclosed within a pair of triple quotes.

    ```py
    long_lines = """Long long long
                    long long line"""
    ```

The indentation of the continuation lines is not important. Moreover, blank continuation lines are allowed. 

## Indentation

Indentation is determined from the number leading whitespace characters (spaces and tabs).

Each tab is replaced by eight space characters. The space characters are then used to determine the indentation according to the following process:

- If consecutive lines have the same number of leading spaces, they are considered to be at the same indentation level.
- If the next line has more number of leading spaces, it is considered to be at a higher indentation level.
- If the next line has less number of leading spaces, it is considered to be at a lower indentation level.

### Rules

- Statements at the global indentation level must have zero leading spaces.
- Statements returning to a lower indentation level must have the same number of spaces as any other outer indentation level. In which case, it is considered to be at that indentation level.
- If tabs are mixed with spaces in a way that requires knowing the worth of a tab in spaces, indentation is rejected as inconsistent, and `TabError` is raised.

### Whitespace between tokens

- Except at the beginning of a logical line or inside string literals, the whitespace characters (space, tab, and form feed) can be used interchangeably to separate tokens.
- Whitespace is needed between two tokens only if their concatenation could otherwise be misinterpreted as a different token.

## Grammar

### Identifiers

- An identifier can include uppercase and lowercase letters `A` through `Z`, underscore characters `_`, and, except for the first character, digits `0` through `9`.
- Identifiers are unlimited in length.
- Identifiers are case-sensitive.

### Keywords

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

### Soft keywords

Some identifiers are only reserved under specific contexts, and can be used as identifier names in other contexts.

- `match`
- `case`
- `_`

### Reserved classes of identifiers

Certain classes of identifiers, besides keywords, have special meaning. These classes are identified by the patterns of leading and trailing underscore characters.

| Pattern | Description |
| - | - |
| `_*` | Names that are not imported by the `from module import *` statement. |
| `_` | In a `case` pattern within a `match` statement, `_` denotes a wildcard. |
| `__*__` | Names defined by the interpreter and implementation (including the standard library). |
| `__*` | Private names of a class. These names are mangled with the class name to prevent clashes between private names of the base and derived classes.|

### Literals

<!-- TODO: Missing details -->
Literals are notations for constant values of some built-in types.

### Operators

The following tokens act as operators in the grammar.

```py
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=
```

### Delimiters

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