# Types

<!-- omit in toc -->
## Table of contents

- [Data types](#data-types)
- [Type classification](#type-classification)
- [Fundamental types](#fundamental-types)
  - [Character types](#character-types)
  - [Integer types](#integer-types)
    - [Modifiers](#modifiers)
    - [Data models](#data-models)
    - [Properties](#properties)

## Data types

A *data type* (or simply a *type*) is a description of a set of values that dictate the set of allowed operations on those values and how those operations are interpreted.

In C++, objects, references, functions (including template specializations), and expressions have a property called *type*, which both restricts the operations that are permitted for those entities and provides semantic meaning to the otherwise generic sequences of bits.

## Type classification

The C++ type system classifies each type as either a *fundamental type* or a *compound type*. A *fundamental type* is a type that is predefined in the C++ language; whereas, a *compound type* is a type that is defined in terms of another type. The C++ type system consists of the following types:

- Fundamental types
    - Void type (`void`)
    - Null pointer type (`nullptr_t`)
    - Arithmetic types
        - Integral types
            - Boolean type (`bool`)
            - Character types
                - Narrow character types
                    - Ordinary character types
                        - Type `char`
                        - Type `signed char`
                        - Type `unsigned char`
                    - Type `char8_t`
                - Wide character types
                    - Type `char16_t`
                    - Type `char32_t`
                    - Type `wchar_t`
            - Signed and unsigned integral types
                - Signed integral types
                    - Type `signed char`
                    - Type `short int`
                    - Type `int`
                    - Type `long int`
                    - Type `long long int`
                - Unsigned integral types
                    - Type `unsigned char`
                    - Type `unsigned short int`
                    - Type `unsigned int`
                    - Type `unsigned long int`
                    - Type `unsigned long long int`
        - Floating-point types
            - Single-precision floating-point type (`float`)
            - Double-precision floating-point type (`double`)
            - Extended-precision floating-point type (`long double`)
- Compound types
    - Reference types
        - L-value reference types
            - L-value reference to object types
            - L-value reference to function types
        - R-value reference types
            - R-value reference to object types
            - R-value reference to function types
    - Pointer types
        - Pointer to object types
        - Pointer to function types
    - Pointer to member types
        - Pointer to data member types
        - Pointer to member function types
    - Array types
    - Function types
    - Enumerated types
        - Unscoped enumeration types
        - Scope enumeration types
    - Class types
        - Non-union types
        - Union types

## Fundamental types

Void type
: The void type (`void`) is a type with an empty set of values. It is an incomplete type that can not be completed; consequently, objects of type `void` are disallowed. There are no arrays of `void`, nor references to `void`. However, pointers to `void` and functions returning `void` are permitted.

Null pointer type
: The null pointer type (`nullptr_t`) is the type of the null pointer literal (`nullptr`). It is a distinct type that is not itself a pointer type or a pointer to member type. Its values are null pointer constant (`NULL`), and may be implicitly converted to any pointer type or pointer to member type.

Boolean type
: The boolean type (`bool`) is a distinct type that has one of the two values: `true` and `false`. It has the same object representation, value representation, and alignment requirements as an implementation-defined unsigned integer type.

### Character types

Type `char`
: The type `char` is a type for character representation. It is a distinct type that has an implementation-defined choice of `signed char` or `unsigned char` as its underlying type.

  The signedness depends on the efficiency of processing of character processing on the target system (the default for ARM and PowerPC is usually `unsigned char`, and the default for x86 and x64 is usually `signed char`).

  For every value of type `unsigned char` in range: [0, 255], converting the value to `char` and then back to `unsigned char` produces the original value.

Type `unsigned char`
: The type `unsigned char` is a type for unsigned character representation. It is often used to inspect object representations (raw memory).

Type `signed char`
: The type `signed char` is a type for signed character representation.

Type `wchar_t`
: The type `wchar_t` is a type for wide character representation. It has an implementation-defined choice of signed or unsigned integer type as its underlying type. The values of type `wchar_t` can represent distinct codes for all members of the largest extended character set specified among the supported locales.

  It has the same size, signedness, and alignment as one of the integer types, but is a distinct type. In practice, it is 32 bits and holds UTF-32 code units on Linux and many other non-Windows systems, but 16 bit and holds UTF-16 code units on Windows.

Type `char8_t`
: The type `char8_t` is a type for UTF-8 character representation. It is required to be large enough to represent any UTF-8 code unit. It has the same size, signedness, and alignment as an `unsigned char` (and therefore, the same size and alignment as `char` and `signed char`), but is a distinct type.

Type `char16_t`
: The type `char16_t` is a type for UTF-16 character representation. It is required to be large enough to represent any UTF-16 code unit. It has the same size, signedness, and alignment as `std::uint_least16_t`, but is a distinct type.

Type `char32_t`
: The type `char32_t` is a type for UTF-32 character representation. It is required to be large enough to represent any UTF-32 code unit. It has the same size, signedness, and alignment as `std::uint_least32_t`, but is a distinct type.

### Integer types

The integer types includes the *standard integer types* and implementation-defined *extended integer types*. The *standard integer types* includes the five *standard signed integer types* and five corresponding *standard unsigned integer types*.

The *standard signed integer types* along with their minimum width constraints are specified in the table below. The width (`N`) of a signed integer type is implementation-defined, but must be at least the minimum width specified for that integer type, and must be at least equal to the width of the preceding type.

| Type            | Minimum width (`N`) |
| --------------- | ------------------- |
| `signed char`   | 8                   |
| `short int`     | 16                  |
| `int`           | 16                  |
| `long int`      | 32                  |
| `long long int` | 64                  |

For each of the standard signed integer type, there exists a corresponding (but distinct) *standard unsigned integer type*. An unsigned integer type has the same width (`N`), object representation, value representation, and alignment requirements, as the corresponding signed integer type; but the range of representable values is different.

| Integer type          | Range of representable values                         |
| --------------------- | ----------------------------------------------------- |
| Signed integer type   | -2<sup>N-1</sup> to 2<sup>N-1</sup> - 1 *(inclusive)* |
| Unsigned integer type | 0 to 2<sup>N</sup> - 1 *(inclusive)*                  |

Overflow
: Overflow for signed integer type yield undefined behavior. Unsigned integer types do not overflow; instead, the arithmetic is performed module 2<sup>N</sup>.

Value representation
: For each value `x` of a signed integer type, the value of the corresponding unsigned integer type congruent to `x` module 2<sup>N</sup> has the same value of corresponding bits in its value representation. This is also known as 2's complement representation.

  Each value `x` of an unsigned integer type with width `N` has a unique representation: x = x<sub>0</sub>2<sup>0</sup> + x<sub>1</sub>2<sup>1</sup> + ... + x<sub>N-1</sub>2<sup>N-1</sup>, where each coefficient of `x` is either `0` or `1`; this is called base-2 representation of `x`. The base-2 representation of a value of signed integer type is the base-2 representation of the congruent value of the corresponding unsigned integer type.

#### Modifiers

The basic integer type (`int`) is intended to have the natural width suggested by the architecture of the execution environment; the other signed and unsigned integer types are provided to meet special needs. These other signed and unsigned integer types can be viewed as the basic integer type (`int`) with modifiers for signedness and size.

These modifiers are listed in the table below, and can appear in any order, but only one from each category can be present in a type name. If no size modifiers are present, then one of the signedness modifiers must be present; in which case, the type is equivalent to the basic integer type (either `signed int` or `unsigned int`). If no signedness modifiers are present, then one of the size modifiers must be present; in which case, the type is equivalent to the unsigned integer type (either `short`, `int`, `long`, or `long long`).

| Modifier    | Category   | Description                                      |
| ----------- | ---------- | ------------------------------------------------ |
| `signed`    | Signedness | Target type will have signed representation.     |
| `unsigned`  | Signedness | Target type will have unsigned representation.   |
| `short`     | Size       | Target type will have width of at least 16 bits. |
| `long`      | Size       | Target type will have width of at least 32 bits. |
| `long long` | Size       | Target type will have width of at least 64 bits. |

#### Data models

The choices made by each implementation about the sizes of the fundamental types are collectively known as a *data model*. Four data models are widely accepted:

| Data model             | System architecture | `int` width | `long` width | `ptr` width | Used by                       |
| ---------------------- | ------------------- | ----------- | ------------ | ----------- | ----------------------------- |
| **LP32** or **2/4/4**  | 32-bit              | 16          | 32           | 32          | Win16 API                     |
| **ILP32** or **4/4/4** | 32-bit              | 32          | 32           | 32          | Win32 API, Unix, Linux, macOS |
| **LLP64** or **4/4/8** | 64-bit              | 32          | 32           | 64          | Wind64 API                    |
| **LP64** or **4/8/8**  | 64-bit              | 32          | 64           | 64          | Unix, Linux, macOS            |
| **ILP64** or **8/8/8** | 64-bit              | 64          | 64           | 64          | UNICOX on Cray                |

#### Properties

The following table summarizes all standard integer types and their widths in common data models:

| Type specifier           | Equivalent type      | Minimum width | LP32 | ILP32 | LLP64 | LP64 |
| ------------------------ | -------------------- | ------------- | ---- | ----- | ----- | ---- |
| `signed char`            | `signed char`        | 8             | 8    | 8     | 8     | 8    |
| `unsigned char`          | `unsigned char`      | 8             | 8    | 8     | 8     | 8    |
| `short`                  | `short int`          | 16            | 16   | 16    | 16    | 16   |
| `short int`              | `short int`          | 16            | 16   | 16    | 16    | 16   |
| `signed short`           | `short int`          | 16            | 16   | 16    | 16    | 16   |
| `signed short int`       | `short int`          | 16            | 16   | 16    | 16    | 16   |
| `unsigned short`         | `unsigned short int` | 16            | 16   | 16    | 16    | 16   |
| `unsigned short int`     | `unsigned short int` | 16            | 16   | 16    | 16    | 16   |
| `int`                    | `int`                | 16            | 16   | 32    | 32    | 32   |
| `signed`                 | `int`                | 16            | 16   | 32    | 32    | 32   |
| `signed int`             | `int`                | 16            | 16   | 32    | 32    | 32   |
| `unsigned`               | `unsigned int`       | 16            | 16   | 32    | 32    | 32   |
| `unsigned int`           | `unsigned int`       | 16            | 16   | 32    | 32    | 32   |
| `long`                   | `long int`           | 32            | 32   | 32    | 32    | 64   |
| `long int`               | `long int`           | 32            | 32   | 32    | 32    | 64   |
| `signed long`            | `long int`           | 32            | 32   | 32    | 32    | 64   |
| `signed long int`        | `long int`           | 32            | 32   | 32    | 32    | 64   |
| `unsigned long`          | `unsigned long int`  | 32            | 32   | 32    | 32    | 64   |
| `unsigned long int`      | `unsigned long int`  | 32            | 32   | 32    | 32    | 64   |
| `long long`              | `long long int`      | 64            | 64   | 64    | 64    | 64   |
| `long long int`          | `long long int`      | 64            | 64   | 64    | 64    | 64   |
| `signed long long`       | `long long int`      | 64            | 64   | 64    | 64    | 64   |
| `signed long long int`   | `long long int`      | 64            | 64   | 64    | 64    | 64   |
| `unsigned long long`     | `unsigned long int`  | 64            | 64   | 64    | 64    | 64   |
| `unsigned long long int` | `unsigned long int`  | 64            | 64   | 64    | 64    | 64   |

