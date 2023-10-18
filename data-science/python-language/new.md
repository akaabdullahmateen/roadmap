# Python

<!-- omit in toc -->
## Table of contents

- [Arithmetic conversions](#arithmetic-conversions)

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