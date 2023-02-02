## Type system

Type system is a logical system that comprises a set of rules which assign a type to every "term" (program constructs such as variables, expressions, functions, and modules). The type system dictates the operations that can be performed on a term.

Type systems are often specified as part of a programming language and built into interpreters and compilers, although the type system of a language can be extended by optional tools that perform additional checks using the language's original type syntax and grammar. The main purpose of a type system is to reduce possibilities for bugs due to type errors.

Type systems allow defining interfaces between different parts of a program, and then checking that the parts have been connected in a consistent way. This checking can happen statically (at compile time), dynamically (at run time), or as a combination of both.

If a language specification requires its typing rules strongly (allowing only those automatic type conversions that do not lose information), then it is classified as *strongly typed*; otherwise, *weakly typed*.

## Type

Objects, references, functions (including function template specializations), and expressions have a property called *type*, which restricts the operations that are permitted for those entities, and provide semantic meaning to the otherwise generic sequences of bits.

### Type classification

The C++ type system consists of the following types:

Fundamental types
: If T is a fundamental type (arithmetic type, `void`, or `nullptr_t`), `std::is_fundamental` provides the member constant value equal to `true`; for any other type, the value is `false`.

Compound types
: If T is a compound type (array, function, object pointer, function pointer, member object pointer, member function pointer, reference, class, union, or enumeration, including cv-qualified variants), `std::is_compound` provides the member constant value equal to `true`; for any other type, the value is `false`.

- fundamental type
  - `void`
  - `std::nullptr_t`
  - arithmetic type
    - floating-point type
      - `float` and cv-qualified version
      - `double` and cv-qualified version
      - `long double` and cv-qualified version
    - integral type
      - `bool`
      - character type
        - narrow character type
          - ordinary character type
            - `char`
            - `signed char`
            - `unsigned char`
          - `char8_t`
        - wide character type
          - `char16_t`
          - `char32_t`
          - `wchar_t`
      - signed integral type
        - `short int`
        - `int`
        - `long int`
        - `long long int`
      - unsigned integral type
        - `unsigned short int`
        - `unsigned int`
        - `unsigned long int`
        - `unsigned long long int`
- compound type
  - reference type
    - lvalue reference type
      - lvalue reference to object type
      - lvalue reference to function type
    - rvalue reference type
      - rvalue reference to object type
      - rvalue reference to function type
  - pointer type
    - pointer to object type
    - pointer to function type
  - pointer to member type
    - pointer to data member type
    - pointer to member function type
  - array type
  - function type
  - enumerated type
    - unscoped enumeration type
    - scope enumeration type
  - class type
    - non-union type
    - union type

For every type other than reference and function, the type system supports three additional cv-qualified versions of that type (`const`, `volatile`, and `const volatile`).

Types are grouped into various categories based on their properties:

- Object types are (possibly cv-qualified) types that are not function types, reference types, or possibly cv-qualified `void`.
- Scalar types are (possibly cv-qualified) object types that are not array types or class types.
- Trivial types, literal types, and other categories listed in the type traits library or as named type requirements.

Constructing a complete object such that the number of bytes in its object representation is not representable in the type `std::size_t`, is ill-formed.

### Incomplete type

The following types are incomplete types; all other types are complete:

- the type `void` (possibly cv-qualified)
- incompletely defined object types
  - class type that has been declared but not defined
  - array of unknown bound
  - array of elements of incomplete type
  - enumeration type from the point of declaration until its underlying type is determined

### Additional basic types

Defined in header `<cstddef>`

| Type          | Description                                                                  |
| ------------- | ---------------------------------------------------------------------------- |
| `size_t`      | unsigned integer type returned by the `sizeof` operator                      |
| `ptrdiff_t`   | signed integer type returned when subtracting two pointers                   |
| `nullptr_t`   | the type of the null pointer literal `nullptr`                               |
| `NULL`        | implementation-defined null pointer constant                                 |
| `max_align_t` | trivial type with alignment requirement as great as any other scalar type    |
| `offsetof`    | byte offset from the beginning of a standard-layout type to specified member |
| `byte`        | the byte type                                                                |

### Fixed width integer types

#### Types

Defined in header `<cstdint>`

| Type             | Description                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------- |
| `int8_t`         | signed integer type with width of exactly 8 bits with no padding bits and using 2's complement for negative values  |
| `int16_t`        | signed integer type with width of exactly 16 bits with no padding bits and using 2's complement for negative values |
| `int32_t`        | signed integer type with width of exactly 32 bits with no padding bits and using 2's complement for negative values |
| `int64_t`        | signed integer type with width of exactly 64 bits with no padding bits and using 2's complement for negative values |
| `int_fast8_t`    | fastest signed integer type with width of at least 8 bits                                                           |
| `int_fast16_t`   | fastest signed integer type with width of at least 16 bits                                                          |
| `int_fast32_t`   | fastest signed integer type with width of at least 32 bits                                                          |
| `int_fast64_t`   | fastest signed integer type with width of at least 64 bits                                                          |
| `int_least8_t`   | smallest signed integer type with width of at least 8 bits                                                          |
| `int_least16_t`  | smallest signed integer type with width of at least 16 bits                                                         |
| `int_least32_t`  | smallest signed integer type with width of at least 32 bits                                                         |
| `int_least64_t`  | smallest signed integer type with width of at least 64 bits                                                         |
| `intmax_t`       | maximum-width signed integer type                                                                                   |
| `intptr_t`       | signed integer type capable of holding a pointer to `void`                                                          |
| `uint8_t`        | unsigned integer type with width of exactly 8 bits                                                                  |
| `uint16_t`       | unsigned integer type with width of exactly 16 bits                                                                 |
| `uint32_t`       | unsigned integer type with width of exactly 32 bits                                                                 |
| `uint64_t`       | unsigned integer type with width of exactly 64 bits                                                                 |
| `uint_fast8_t`   | fastest unsigned integer type with width of at least 8 bits                                                         |
| `uint_fast16_t`  | fastest unsigned integer type with width of at least 16 bits                                                        |
| `uint_fast32_t`  | fastest unsigned integer type with width of at least 32 bits                                                        |
| `uint_fast64_t`  | fastest unsigned integer type with width of at least 64 bits                                                        |
| `uint_least8_t`  | smallest unsigned integer type with width of at least 8 bits                                                        |
| `uint_least16_t` | smallest unsigned integer type with width of at least 16 bits                                                       |
| `uint_least32_t` | smallest unsigned integer type with width of at least 32 bits                                                       |
| `uint_least64_t` | smallest unsigned integer type with width of at least 64 bits                                                       |
| `uintmax_t`      | maximum-width unsigned integer type                                                                                 |
| `uintptr_t`      | unsigned integer type capable of holding a pointer to `void`                                                        |

!!! note

The implementation may define typedef names `intN_t`, `int_fastN_t`, `int_leastN_t`, `uintN_t`, `uint_fastN_t`, and `uint_leastN_t` when `N` is not 8, 16, 32, or 64. Typedef names of the form `intN_t` may only be defined if the implementation supports an integer type of that width with no padding. Thus, `uint24_t` denotes an unsigned integer type with a width of exactly 24 bits.

#### Macro constants

##### Signed integers : minimum value

| Macro             | Description                                        |
| ----------------- | -------------------------------------------------- |
| `INT8_MIN`        | minimum value of an object of type `int8_t`        |
| `INT16_MIN`       | minimum value of an object of type `int16_t`       |
| `INT32_MIN`       | minimum value of an object of type `int32_t`       |
| `INT64_MIN`       | minimum value of an object of type `int64_t`       |
| `INT_FAST8_MIN`   | minimum value of an object of type `int_fast8_t`   |
| `INT_FAST16_MIN`  | minimum value of an object of type `int_fast16_t`  |
| `INT_FAST32_MIN`  | minimum value of an object of type `int_fast32_t`  |
| `INT_FAST64_MIN`  | minimum value of an object of type `int_fast64_t`  |
| `INT_LEAST8_MIN`  | minimum value of an object of type `int_least8_t`  |
| `INT_LEAST16_MIN` | minimum value of an object of type `int_least16_t` |
| `INT_LEAST32_MIN` | minimum value of an object of type `int_least32_t` |
| `INT_LEAST64_MIN` | minimum value of an object of type `int_least64_t` |
| `INTPTR_MIN`      | minimum value of an object of type `intptr_t`      |
| `INTMAX_MIN`      | minimum value of an object of type `intmax_t`      |

##### Signed integers : maximum value

| Macro             | Description                                        |
| ----------------- | -------------------------------------------------- |
| `INT8_MAX`        | maximum value of an object of type `int8_t`        |
| `INT16_MAX`       | maximum value of an object of type `int16_t`       |
| `INT32_MAX`       | maximum value of an object of type `int32_t`       |
| `INT64_MAX`       | maximum value of an object of type `int64_t`       |
| `INT_FAST8_MAX`   | maximum value of an object of type `int_fast8_t`   |
| `INT_FAST16_MAX`  | maximum value of an object of type `int_fast16_t`  |
| `INT_FAST32_MAX`  | maximum value of an object of type `int_fast32_t`  |
| `INT_FAST64_MAX`  | maximum value of an object of type `int_fast64_t`  |
| `INT_LEAST8_MAX`  | maximum value of an object of type `int_least8_t`  |
| `INT_LEAST16_MAX` | maximum value of an object of type `int_least16_t` |
| `INT_LEAST32_MAX` | maximum value of an object of type `int_least32_t` |
| `INT_LEAST64_MAX` | maximum value of an object of type `int_least64_t` |
| `INTPTR_MAX`      | maximum value of an object of type `intptr_t`      |
| `INTMAX_MAX`      | maximum value of an object of type `intmax_t`      |

##### Unigned integers : maximum value

| Macro             | Description                                        |
| ----------------- | -------------------------------------------------- |
| `UINT8_MAX`        | maximum value of an object of type `uint8_t`        |
| `UINT16_MAX`       | maximum value of an object of type `uint16_t`       |
| `UINT32_MAX`       | maximum value of an object of type `uint32_t`       |
| `UINT64_MAX`       | maximum value of an object of type `uint64_t`       |
| `UINT_FAST8_MAX`   | maximum value of an object of type `uint_fast8_t`   |
| `UINT_FAST16_MAX`  | maximum value of an object of type `uint_fast16_t`  |
| `UINT_FAST32_MAX`  | maximum value of an object of type `uint_fast32_t`  |
| `UINT_FAST64_MAX`  | maximum value of an object of type `uint_fast64_t`  |
| `UINT_LEAST8_MAX`  | maximum value of an object of type `uint_least8_t`  |
| `UINT_LEAST16_MAX` | maximum value of an object of type `uint_least16_t` |
| `UINT_LEAST32_MAX` | maximum value of an object of type `uint_least32_t` |
| `UINT_LEAST64_MAX` | maximum value of an object of type `uint_least64_t` |
| `UINTPTR_MAX`      | maximum value of an object of type `uintptr_t`      |
| `UINTMAX_MAX`      | maximum value of an object of type `uintmax_t`      |

#### Function macros for minimum-width integer constants

Defined in `<cstdint>`

| Macro       | Description                                                                                                                                   |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `INT8_C`    | expands to an integer constant expression having the values specified by its argument and whose type is the promoted type of `int_least8_t`   |
| `INT16_C`   | expands to an integer constant expression having the values specified by its argument and whose type is the promoted type of `int_least16_t`  |
| `INT32_C`   | expands to an integer constant expression having the values specified by its argument and whose type is the promoted type of `int_least32_t`  |
| `INT64_C`   | expands to an integer constant expression having the values specified by its argument and whose type is the promoted type of `int_least64_t`  |
| `INTMAX_C`  | expands to an integer constant expression having the values specified by its argument and whose type is the `intmax_t`                        |
| `UINT8_C`   | expands to an integer constant expression having the values specified by its argument and whose type is the promoted type of `uint_least8_t`  |
| `UINT16_C`  | expands to an integer constant expression having the values specified by its argument and whose type is the promoted type of `uint_least16_t` |
| `UINT32_C`  | expands to an integer constant expression having the values specified by its argument and whose type is the promoted type of `uint_least32_t` |
| `UINT64_C`  | expands to an integer constant expression having the values specified by its argument and whose type is the promoted type of `uint_least64_t` |
| `UINTMAX_C` | expands to an integer constant expression having the values specified by its argument and whose type is the `uintmax_t`                       |

!!! note "Usage"
    ```cpp
    #include <cstdint>
    UINT64_C(0x123) // expands to a literal of type uint_least64_t and value 0x123
    ```

#### Format constants

Defined in `<cinttypes>`

##### Format constants for the `std::fprintf` family of functions

For the macros of data types, replace `x` with `8`, `16`, `32`, `64`, or any other width defined by the implementation.

| Equivalent for `int` or `unsigned int` | Description                                               | `std::intx_t` | `std::int_leastx_t` | `std::int_fastx_t` | `std::intmax_t` | `std::intptr_t` |
| -------------------------------------- | --------------------------------------------------------- | ------------- | ------------------- | ------------------ | --------------- | --------------- |
| `d`                                    | output of a signed decimal integer value                  | PRId**x**     | PRIdLEAST**x**      | PRIdFAST**x**      | PRIdMAX         | PRIdPTR         |
| `i`                                    | output of a signed decimal integer value                  | PRIi**x**     | PRIiLEAST**x**      | PRIiFAST**x**      | PRIiMAX         | PRIiPTR         |
| `u`                                    | output of an unsigned decimal integer value               | PRIu**x**     | PRIuLEAST**x**      | PRIuFAST**x**      | PRIuMAX         | PRIuPTR         |
| `o`                                    | output of an unsigned octal integer value                 | PRIo**x**     | PRIoLEAST**x**      | PRIoFAST**x**      | PRIoMAX         | PRIoPTR         |
| `x`                                    | output of an unsigned lowercase hexadecimal integer value | PRIx**x**     | PRIxLEAST**x**      | PRIxFAST**x**      | PRIxMAX         | PRIxPTR         |
| `X`                                    | output of an unsigned uppercase hexadecimal integer value | PRIX**x**     | PRIXLEAST**x**      | PRIXFAST**x**      | PRIXMAX         | PRIXPTR         |

##### Format constants for the `std::fscanf` family of functions

For the macros of data types, replace `x` with `8`, `16`, `32`, `64`, or any other width defined by the implementation.

| Equivalent for `int` or `unsigned int` | Description                                     | `std::intx_t` | `std::int_leastx_t` | `std::int_fastx_t` | `std::intmax_t` | `std::intptr_t` |
| -------------------------------------- | ----------------------------------------------- | ------------- | ------------------- | ------------------ | --------------- | --------------- |
| `d`                                    | output of a signed decimal integer value        | SCNd**x**     | SCNdLEAST**x**      | SCNdFAST**x**      | SCNdMAX         | SCNdPTR         |
| `i`                                    | output of a signed decimal integer value        | SCNi**x**     | SCNiLEAST**x**      | SCNiFAST**x**      | SCNiMAX         | SCNiPTR         |
| `u`                                    | output of an unsigned decimal integer value     | SCNu**x**     | SCNuLEAST**x**      | SCNuFAST**x**      | SCNuMAX         | SCNuPTR         |
| `o`                                    | output of an unsigned octal integer value       | SCNo**x**     | SCNoLEAST**x**      | SCNoFAST**x**      | SCNoMAX         | SCNoPTR         |
| `x`                                    | output of an unsigned hexadecimal integer value | SCNx**x**     | SCNxLEAST**x**      | SCNxFAST**x**      | SCNxMAX         | SCNxPTR         |

!!! note

     The type `std::int8_t` may be `signed char` and `std::uint8_t` may be `unsigned char`, but neither can be `char` regardless of its signedness (because `char` is not considered a *signed integer type* or *unsigned integer type*).

### Fixed with floating-point types

Defined in `<stdfloat>`

| Type name         | Literal suffix   | Predefined macro        | C language type | Storage bits | Precision bits | Exponent bits | Max exponent |
| ----------------- | ---------------- | ----------------------- | --------------- | ------------ | -------------- | ------------- | ------------ |
| `std::float16_t`  | `f16` or `F16`   | `__STDCPP_FLOAT16_T__`  | `_Float16`      | 16           | 11             | 5             | 15           |
| `std::float32_t`  | `f32` or `F32`   | `__STDCPP_FLOAT32_T__`  | `_Float32`      | 32           | 24             | 8             | 127          |
| `std::float64_t`  | `f64` or `F64`   | `__STDCPP_FLOAT64_T__`  | `_Float64`      | 64           | 53             | 11            | 1023         |
| `std::float128_t` | `f128` or `F128` | `__STDCPP_FLOAT128_T__` | `_Float128`     | 128          | 113            | 15            | 16383        |
| `std::bfloat16_t` | `bf16` or `BF16` | `__STDCPP_BFLOAT16_T__` | (n/a)           | 16           | 8              | 8             | 127          |

!!! note

    The type `std::bfloat16_t` is known as Brain Floating Point.

    Unlike the fixed width integer types, which may be aliases to standard integer types, the fixed width floating-point types must be aliases to extended floating-point types (not `float`, `double`, or `long double`).

### Numeric limits

Defined in header `<limits>` and called `std::numeric_limits`

