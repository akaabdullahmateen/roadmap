# ABC.XYZ

## MATLAB

MATLAB (Matrix Laboratory) is a programming language and numeric computing environment developed by MathWorks. MATLAB allows matrix manipulations, plotting of functions and data, implementation of algorithms, creation of user interfaces, and interfacing with programs written in other languages.

## Simulink

Simulink is a MATLAB-based graphical programming environment for modelling, simulating, and analyzing multidomain dynamical systems. Its primary interface is a graphical block diagramming tool and a customizable set of block libraries. It offers tight integration with the rest of the MATLAB environment and can either drive MATLAB or be scripted from it.

## Misc

| Functions | Description |
| - | - |
| `ans` | Most recent answer |
| `clc` | Clear command window |
| `iskeyword` | Determines whether input is MATLAB keyword |
| `ver` | Displays MATLAB, Simulink, and toolbox version information |
| `commandhistory` | Opens command history window |
| `home` | Send cursor home |
| `more` | Control paged output in command window |
| `format` | Set output display format |
| `diary` | Log command window text to file |
| `commandwindow` | Selects the command window |

---

| Action | Procedure |
| - | - |
| Enter multiple statements before executing them | Enter the multiple statements at the command line, pressing **Shift+Enter** in between. *This key combination is unnecessary when entering a paired keyword statement on multiple lines, such as `for` and `end`*. |
| Clear a statement from the command line without executing it | Press the **Esc** key. |
| Recall previous statements | Press the Up arrow key. The command history window opens and displays a log of previous statements. To recall a specific statement, type any part of the statement and then press the Up arrow key. |
| Clear the command window | Call the `clc` function. To clear the command window without deleting any text, call the `home` function. Calling the `home` function moves the cursor to the upper-left corner of the command window and scrolls all visible text out of view, giving the appearance of clearing the screen without deleting any text. |
| Evaluate a statement already in the command window | Select the statement, right-click, and then select **Evaluate selection**. |
| Execute only portion of the code currently at the command line | Select the code at the command line and press **Enter**.

## Syntax

### Comments

Single line comments are added by starting them with the percent `%` symbol. Single line comments can be appended to the end of a line of code.

```matlab
% This is a single line comment
y = sum(x) % This is also a single line comment
```

Multiple line comments are added by enclosing them within the block comment operators `%{` and `%}`. The block comment operators must appear alone on their lines, and no other text is allowed on these lines.

```matlab
%{
This is a multiple line comment
that spans two lines
%}
y = sum(x)
```

### Arithmetic operators

| Symbol | Role | Name |
| - | - | - |
| `+` | Addition | `plus` |
| `+` | Unary plus | `uplus` |
| `-` | Subtraction | `minus` |
| `-` | Unary minus | `uminus` |
| `.*` | Element-wise multiplication | `times` |
| `*` | Matrix multiplication | `mtimes` |
| `./` | Element-wise right division | `rdivide` |
| `/` | Matrix right division | `mrdivide` |
| `.\` | Element-wise left division | `ldivide` |
| `\` | Matrix left division | `mldivide` |
| `.^` | Element-wise power | `power` |
| `^` | Matrix power | `mpower` |
| `.'` | Transpose | `transpose` |
| `'` | Complex conjugate transpose | `ctranspose` |

### Relational operators

| Symbol | Role | Name |
| - | - | - |
| `==` | Equal to | `eq` |
| `~=` | Not equal to | `ne` |
| `>` | Greater than | `gt` |
| `>=` | Greater than or equal to | `ge` |
| `<` | Less than | `lt` |
| `<=` | Less than or equal to | `le` |

### Logical operators

| Symbol | Role | Name |
| - | - | - |
| `&` | Logical AND | `and` |
| `|` | Logical OR | `or` |
| `&&` | Logical AND with short-circuiting | `Short-Circuit AND` |
| `||` | Logical OR with short-circuiting | `Short-Circuit OR` |
| `~` | Logical NOT | `not` |

### String formatting

There are certain special characters that can not be used in ordinary text. Instead they are represented as unique character sequences to format strings and character vectors.

| Symbol | Effect |
| - | - |
| `''` | Single quotation mark |
| `%%` | Single percent sign |
| `\\` | Single backslash |
| `\a` | Alarm |
| `\b` | Backspace |
| `\f` | Form feed |
| `\n` | New line |
| `\r` | Carriage return |
| `\t` | Horizontal tab |
| `\v` | Vertical tab |
| `\xN` | Hexadecimal number *N* |
| `\N` | Octal number *N* |

### ans

If an output is returned without a specified output argument to store the result, the `ans` variable is created and initialized with this output value. However, the `ans` is specific to the current workspace. The base workspace and each function workspace can have its own instance of `ans` variable.

## Loops and conditional statements

### if-elseif-else

The if-elseif-else block evaluates an expression, and executes a group of statements when the expression is true. An expression is true when its result is nonempty and contains only nonzero elements (logical or real numeric).

The `elseif` and `else` blocks are optional, and the statements are executed only when previous expressions in the `if` block are false. An `if` block can include multiple `elseif` blocks.

```matlab
if expression
    statements
elseif expression
    statements
elseif expression
    statements
...
else
    statements
end
```

### switch-case-otherwise

The switch-case-otherwise block evaluates an expression and chooses to execute one of several groups of statements. The `switch` block tests each case until one of the case expressions is true. A case is true when:

- For numbers, `case_expression == switch_expression`
- For character vectors, `strcmp(case_expression,switch_expression) == 1`
- For objects that support the `eq` function, `case_expression == switch_expression`
- For a cell array `case_expression`, at least one of the elements of the cell array matches `switch_expression`, as defined above for numbers, character vectors, and objects.

The `otherwise` block is optional, and the statements are executed only when no case is true.

```matlab
switch switch_expression
    case case_expression
        statements
    case case_expression
        statements
    ...
    otherwise
        statements
end
```

### for

The `for` loop executes a statement in a loop for a specified number of times. The `values` has one of the following forms:

- `initial_value:end_value` - Increment the `index` variable from `initial_value` to `end_value` by 1, and repeat execution of `statements` until `index` is greater than `end_value`.
- `initial_value:step:end_value` - Increment `index` by the value `step` on each iteration, or decrement `index` if `step` is negative.
- `value_array` - Create a column vector `index`, from subsequent columns of the array `value_array` on each iteration. 

```matlab
for index = values
    statements
end
```

### while

The `while` loop evaluates an expression, and repeats the execution of a group of statements in a loop while the expression is true. An expression is true when its result is nonempty and contains only nonzero elements (logical or real numeric). Otherwise the expression is false.

```matlab
while expression
    statements
end
```

### try-catch

The try-catch block executes the statements in the `try` block and catches resulting errors in the `catch` block. This allows to override the default error behavior by defining custom error handling. The `catch` block assigns the current exception object to the variable in `exception`. Both `try` and `catch` blocks can contain nested try-catch statements.

```matlab
try
    statements
catch exception
    statements
end
```

### break

The `break` keyword terminates the execution of a `for` or `while` loop. Statements in the loop after the `break` statement are not executed. In nested loops, `break` only exits from the loop in which it occurs, and control passes to the statement that follows the `end` of that loop.

```matlab
while expression
    if expression == condition
        break
    expression = modify(expression) 
end
```

### return

The `return` keyword forces the execution to return back to the invoking program before it reaches the end of the script or function. The invoking program is the script or function that calls the script or function containing the `return` statement. If `return` is called directly, there is no invoking program and control is returned to the command prompt.

```matlab
function ret = function_name(args)
    if args == condition
        return
    end
    ret = args
end
```

