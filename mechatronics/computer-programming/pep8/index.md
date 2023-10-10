# PEP8

<!-- omit in toc -->
## Table of contents

- [Indentation](#indentation)
  - [General guidelines](#general-guidelines)
  - [Aligning continuation lines](#aligning-continuation-lines)
  - [Dealing with visual conflict of indentation](#dealing-with-visual-conflict-of-indentation)
  - [Aligning closing delimiter](#aligning-closing-delimiter)
- [Tabs or Spaces?](#tabs-or-spaces)
- [Maximum line length](#maximum-line-length)
- [Breaking line around binary operators](#breaking-line-around-binary-operators)
- [Blank lines](#blank-lines)
- [Source file encoding](#source-file-encoding)

## Indentation

### General guidelines

- Use 4 spaces per indentation level.

### Aligning continuation lines

- Continuation lines should align wrapped elements either vertically or using a hanging indent.
- When using a hanging indent, there should be no arguments on the first line and further indentation should be used to clearly distinguish itself as a continuation line.

Correct
: ```py
    # Aligned with opening delimiter.
    foo = long_function_name(var_one, var_two,
                             var_three, var_four)

    # More indentation included to distinguish this from the rest.
    def long_function_name(
            var_one, var_two, var_three,
            var_four):
        print(var_one)

    # Hanging indents should add a level.
    foo = long_function_name(
        var_one, var_two,
        var_three, var_four)
    ```

Wrong
: ```py
    # Arguments on first line forbidden when hanging indentation.
    foo = long_function_name(var_one, var_two,
        var_three, var_four)

    # Further indentation required as indentation is not distinguishable.
    def long_function_name(
        var_one, var_two, var_three,
        var_four):
        print(var_one)
    ```

Optional
: ```py
    # Hanging indents *may* be indented to other than 4 spaces.
    foo = long_function_name(
      var_one, var_two,
      var_three, var_four)
    ```

### Dealing with visual conflict of indentation

Sometimes, the combination of a two character keyword (such as `if`), plus a single space, plus an opening parenthesis creates a natural 4-space indent, which produces a visual conflict with the indentation of the nested statements. In such cases, acceptable options include:

- Add no extra indentation.

    ```py
    if (this_is_one_thing and
        that_is_another_thing):
        do_something()
    ```

- If syntax highlighting is support, add a comment, which will provide some distinction in editors.

    ```py
    if (this_is_one_thing and
        that_is_another_thing):
        # This is a comment for separation.
        do_something()
    ```

- Add some extra indentation on the conditional continuation line.

    ```py
    if (this_is_one_thing
            and that_is_another_thing):
        do_something()
    ```

### Aligning closing delimiter

The closing delimiter on multiline constructs may be aligned in either of the two styles:

- Aligned under the first non-whitespace character of the last line of list.

    ```py
    my_list = [
        1, 2, 3,
        4, 5, 6,
        ]
    ```
- Aligned under the first character of the line that starts the multi-line construct.

    ```py
    my_list = [
        1, 2, 3,
        4, 5, 6,
    ]
    ```

## Tabs or Spaces?

- Spaces are the preferred indentation method.
- Tabs should be used solely to remain consistent with code that is already indented with tabs.
- Python 3 disallows mixing the use of tabs and spaces for indentation.
- Python 2 code indented with a mixture of tabs and spaces should be converted to using spaces exclusively.
- When invoking the Python 2 command line interpreter with the `-t` option, it issues warnings about code that illegally mixes tabs and spaces. When using `-tt` these warnings become errors. These options are highly recommended!

## Maximum line length

- Line length of all lines should be limited to 79 characters.
- Line length of docstrings and comments should be limited to 72 characters.
- Line wrapping through implied line continuation (with parenthesis, brackets, and braces) should be preferred over explicit line continuation (with backslashes).
- Backslashes are appropriate to use when implicit continuation is not allowed by the statement syntax.

## Breaking line around binary operators

- Line should be broken after the binary operator. This allows the operators to be easily matched with the corresponding operands.
- Line can be broken before a binary operator as long as this convention is used consistently.

## Blank lines

- Top-level functions and classes should be surrounded by two blank lines.
- Method definitions inside classes should be surrounded by a single blank line.
- Blank lines should be used, sparingly, to separate groups of related functions.
- Blank lines may be omitted between a bunch of related one-liners.
- Blank lines should be used, sparingly, in functions to indicate logical sections.

## Source file encoding

- Files written in Python3 should always use UTF-8 encoding, and files written in Python2 should use ASCII encoding.
- Files using UTF-8 encoding, in Python3, and ASCII encoding, in Python2, should not have an encoding declaration.
- Non-default encodings should only be used for test purposes and author names.
- Escape sequences (`\x`, `\u`, `\U`, or `\N`) should be used to include non-ASCII data in string literals, if necessary.
