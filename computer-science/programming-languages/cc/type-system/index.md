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

The `numeric_limits` class template provides a standardized way to query various properties of arithmetic types (such as the largest possible value for type `int` through `std::numeric_limits<int>::max()`). The standard library makes specializations available for all arithmetic types.

- `template<> class numeric_limits<bool>;`
- `template<> class numeric_limits<char>;`
- `template<> class numeric_limits<signed char>;`
- `template<> class numeric_limits<unsigned char>;`
- `template<> class numeric_limits<wchar_t>;`
- `template<> class numeric_limits<char8_t>;`
- `template<> class numeric_limits<char16_t>;`
- `template<> class numeric_limits<char32_t>;`
- `template<> class numeric_limits<short>;`
- `template<> class numeric_limits<unsigned short>;`
- `template<> class numeric_limits<int>;`
- `template<> class numeric_limits<unsigned int>;`
- `template<> class numeric_limits<long>;`
- `template<> class numeric_limits<unsigned long>;`
- `template<> class numeric_limits<long long>;`
- `template<> class numeric_limits<unsigned long long>;`
- `template<> class numeric_limits<float>;`
- `template<> class numeric_limits<double>;`
- `template<> class numeric_limits<long double>;`

Additionally, a specialization exists for every cv-qualified version of each cv-unqualified type for which the specialization exists, identical to the unqualified specialization (such as `std::numeric_limits<const int>`, `std::numeric_limits<volatile int>`, and `std::numeric_limits<const volatile int>` are provided and are equivalent to `std::numeric_limits<int>`).

Aliases of arithmetic types (such as `std::size_t` or `std::streamsize`) may also be examined with the `std::numeric_limits` type traits.

Implementations may also provide specializations of `std::numeric_limits` for implementation-specific types (such as GCC provides `std::numeric_limits<__int128>`). Non-standard libraries may add specializations for library-provided types (such as OpenEXR provides `std::numeric_limits<half>` for a 16-bit floating-point type).

#### Member constants

| Member constant                | Description                                                                                                              |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `is_specialized` *[static]*    | identifies types for which `std::numeric_limits` is specialized                                                          |
| `is_signed` *[static]*         | identifies signed types                                                                                                  |
| `is_integer` *[static]*        | identifies integer types                                                                                                 |
| `is_exact` *[static]*          | identifies exact types                                                                                                   |
| `has_infinity` *[static]*      | identifies floating-point types that can represent the special value *positive infinity*                                 |
| `has_quiet_NaN` *[static]*     | identifies floating-point types that can represent the special value *quiet not-a-number*                                |
| `has_signaling_NaN` *[static]* | identifies floating-point types that can represent the special value *signaling not-a-number*                            |
| `has_denorm` *[static]*        | identifies the denormalization style used by the floating-point type                                                     |
| `has_denorm_loss` *[static]*   | identifies the floating-point types that can detect loss of precision as denormalization loss rather than inexact result |
| `round_style` *[static]*       | identifies the rounding style used by the type                                                                           |
| `is_iec559` *[static]*         | identifies the IEC 559 / IEEE-754 floating-point types                                                                   |
| `is_bounded` *[static]*        | identifies types that represent a finite set of values                                                                   |
| `is_modulo` *[static]*         | identifies types that handle overflow with module arithmetic                                                             |
| `digits` *[static]*            | number of radix digits that can be represented without change                                                            |
| `digits10` *[static]*          | number of decimal digits that can be represented without change                                                          |
| `max_digits10` *[static]*      | number of decimal digits necessary to differentiate all values of this type                                              |
| `radix` *[static]*             | the radix or integer base used by the representation of the given type                                                   |
| `min_exponent` *[static]*      | one more than the smallest negative power of the radix that is a valid normalized floating-point value                   |
| `min_exponent10` *[static]*    | the smallest negative power of 10 that is a valid normalized floating-point value                                        |
| `max_exponent` *[static]*      | one more than the largest integer power of the radix that is a valid finite floating-point value                         |
| `max_exponent10` *[static]*    | the largest integer power of 10 that is a valid finite floating-point value                                              |
| `traps` *[static]*             | identifies types which can cause arithmetic operations to trap                                                           |
| `tinyness_before` *[static]*   | identifies floating-point types that detect tinyness before rounding                                                     |

#### Member functions

| Function        | Description                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------------ |
| `min`           | returns the smallest finite value of the given type                                                    |
| `lowest`        | returns the lowest finite value of the given type                                                      |
| `max`           | returns the largest finite value of the given type                                                     |
| `epsilon`       | returns the difference between `1.0` and the next representable value of the given floating-point type |
| `round_error`   | returns the maximum rounding error of the given floating-point type                                    |
| `infinity`      | returns the positive infinity value of the given floating-point type                                   |
| `quiet_NaN`     | returns a quiet NaN value of the given floating-point type                                             |
| `signaling_NaN` | returns a signaling NaN value of the given floating-point type                                         |
| `denorm_min`    | returns the smallest positive subnormal value of the given floating-point type                         |

#### Helper classes

| Class                | Description                                    |
| -------------------- | ---------------------------------------------- |
| `float_round_style`  | indicates floating-point rounding modes        |
| `float_denorm_style` | indicates floating-point denormalization modes |

### Fundamental types

#### Void type

The type `void` is a type with an empty set of values. It is an incomplete type that can not be completed (consequently, objects of type `void` are not allowed). There are no arrays of `void`, nor references to `void`. However, pointers to `void` and functions returning type `void` are permitted.

#### Null pointer type

Defined in header `<cstddef>`

`std::nullptr_t` is the type of the null pointer literal (`nullptr`). It is a distinct type that is not itself a pointer type or a pointer to member type. Its values are null pointer constant (`NULL`), and may be implicitly converted to any pointer and pointer to member type.

`sizeof(std::nullptr_t)` is equal to `sizeof(void *)`.

#### Data models

The choices made by each implementation about the sizes of the fundamental types are collectively known as data model. Four data models are widely accepted:

32 bit systems
:   - **LP32** or **2/4/4** (`int` is 16 bit, `long` is 32 bit, and pointer is 32 bit)
        - Win16 API
    - **ILP32** or **4/4/4** (`int` is 32 bit, `long` is 32 bit, and pointer is 32 bit)
        - Win32 API
        - Unix and Unix-like systems (Linux, macOS)


64 bit systems
:   - **LLP64** or **4/4/8** (`int` is 32 bit, `long` is 32 bit, and pointer is 64 bit)
        - Win64 API
    - **LP64** or **4/8/8** (`int` is 32 bit, `long` is 64 bit, and pointer is 64 bit)
        - Unix and Unix-like systems (Linux, macOS)

Other models are very rare. For example, **ILP64** or **8/8/8** (`int` is 64 bit, `long` is 64 bit, and pointer is 64 bit) only appeared in some early 64 bit Unix systems (such as UNICOS on Cray).

#### Signed and unsigned integer types

`int` is the basic integer type. The keyword `int` may be omitted if any of the modifiers listed below are used. If no length modifiers are present, it is guaranteed to have a width of at least 16 bits. However, on 32/64 bit systems, it is almost exclusively guaranteed to have a width of at least 32 bits.

##### Modifiers

Modifiers modifies the basic integer type. They can be mixed in any order, but only of each group can be present in a type name (`unsigned long long int` and `long int unsigned long` name the same type, which is an integer type with unsigned representation and width of at least 64 bits).

Signedness
:   - `signed`
        : target type will have a signed representation (this is the default if omitted)
    - `unsigned`
        : target type will have an unsigned representation

Size
:   - `short`
        : target type will be optimized for space and will have width of at least 16 bits
    - `long`
        : target type will have width of at least 32 bits
    - `long long`
        : target type will have width of at least 64 bits

##### Properties

The following table summarizes all available integer types and their widths in various common data models:

| Type specifier           | Equivalent type      | C++ standard | LP32 | ILP32 | LLP64 | LP64 |
| ------------------------ | -------------------- | ------------ | ---- | ----- | ----- | ---- |
| `signed char`            | `signed char`        | at least 8   | 8    | 8     | 8     | 8    |
| `unsigned char`          | `unsigned char`      | at least 8   | 8    | 8     | 8     | 8    |
| `short`                  | `short int`          | at least 16  | 16   | 16    | 16    | 16   |
| `short int`              | `short int`          | at least 16  | 16   | 16    | 16    | 16   |
| `signed short`           | `short int`          | at least 16  | 16   | 16    | 16    | 16   |
| `signed short int`       | `short int`          | at least 16  | 16   | 16    | 16    | 16   |
| `unsigned short`         | `unsigned short int` | at least 16  | 16   | 16    | 16    | 16   |
| `unsigned short int`     | `unsigned short int` | at least 16  | 16   | 16    | 16    | 16   |
| `int`                    | `int`                | at least 16  | 16   | 32    | 32    | 32   |
| `signed`                 | `int`                | at least 16  | 16   | 32    | 32    | 32   |
| `signed int`             | `int`                | at least 16  | 16   | 32    | 32    | 32   |
| `unsigned`               | `unsigned int`       | at least 16  | 16   | 32    | 32    | 32   |
| `unsigned int`           | `unsigned int`       | at least 16  | 16   | 32    | 32    | 32   |
| `long`                   | `long int`           | at least 32  | 32   | 32    | 32    | 64   |
| `long int`               | `long int`           | at least 32  | 32   | 32    | 32    | 64   |
| `signed long`            | `long int`           | at least 32  | 32   | 32    | 32    | 64   |
| `signed long int`        | `long int`           | at least 32  | 32   | 32    | 32    | 64   |
| `unsigned long`          | `unsigned long int`  | at least 32  | 32   | 32    | 32    | 64   |
| `unsigned long int`      | `unsigned long int`  | at least 32  | 32   | 32    | 32    | 64   |
| `long long`              | `long long int`      | at least 64  | 64   | 64    | 64    | 64   |
| `long long int`          | `long long int`      | at least 64  | 64   | 64    | 64    | 64   |
| `signed long long`       | `long long int`      | at least 64  | 64   | 64    | 64    | 64   |
| `signed long long int`   | `long long int`      | at least 64  | 64   | 64    | 64    | 64   |
| `unsigned long long`     | `unsigned long int`  | at least 64  | 64   | 64    | 64    | 64   |
| `unsigned long long int` | `unsigned long int`  | at least 64  | 64   | 64    | 64    | 64   |

#### Boolean type

`bool` is the boolean type, capable of holding one of the two values: `true` or `false`. The value of `sizeof(bool)` is implementation-defined and might be different from 1.

#### Character types

- `signed char`
    : type for signed character representation
- `unsigned char`
    : type for signed character representation. Also used to inspect object representation (raw memory).
- `char`
    : type for character representation which can be most efficiently processed on the target system (it has the same representation and alignment as either `signed char` or `unsigned char`, but is always a distinct type). Multibyte character strings use this type to represent code units. For each value of type `unsigned char` in range [0, 255], converting the value to `char` and then back to `unsigned char` produces the original value. The signedness of `char` depends on the compiler and the target platform (the default for ARM and PowerPC is usually unsigned, and the default for x86 and x64 is usually signed).
- `wchar_t`
    : type for wide character representation. It has the same size, signedness, and alignment as one of the integer types, but is a distinct type. In practice, it is 32 bits and holds UTF-32 code units on Linux and many other non-Windows systems, but 16 bit and holds UTF-16 code units on Windows.
- `char8_t`
    : type for UTF-8 character representation, required to be large enough to represent any UTF-8 code unit (8 bits). It has the same size, signedness, and alignment as `unsigned char` (and therefore, the same size and alignment as `char` and `signed char`), but is a distinct type.
- `char16_t`
    : type for UTF-16 character representation, required to be large enough to represent any UTF-16 code unit (16 bits). It has the same size, signedness, and alignment as `std::uint_least16_t`, but is a distinct type.
- `char32_t`
    : type for UTF-32 character representation, required to be large enough to represent any UTF-32 code unit (32 bits). It has the same size, signedness, and alignment as `std::uint_least32_t`, but is a distinct type.

Besides the minimal bit counts, the C++ standard guarantees that:

```cpp
1 == sizeof(char) <= sizeof(short) <= sizeof(int) <= sizeof(long) <= sizeof(long long)
```

##### Null-terminated wide strings

A null-terminated wide string is a sequence of valid wide characters, ending with a null character.

###### Character classification

Defined in header `<cwctype>`

| Function    | Description                                                                |
| ----------- | -------------------------------------------------------------------------- |
| `iswalnum`  | checks if a wide character is alphanumeric                                 |
| `iswalpha`  | checks if a wide character is alphabetic                                   |
| `iswlower`  | checks if a wide character is lowercase                                    |
| `iswupper`  | checks if a wide character is an uppercase character                       |
| `iswdigit`  | checks if a wide character is a digit                                      |
| `iswxdigit` | checks if a character is a hexadecimal character                           |
| `iswcntrl`  | checks if a wide character is a control character                          |
| `iswgraph`  | checks if a wide character is a graphical character                        |
| `iswspace`  | checks if a wide character is a space character                            |
| `iswblank`  | checks if a wide character is a blank character                            |
| `iswprint`  | checks if a wide character is a printing character                         |
| `iswpunct`  | checks if a wide character is a punctuation character                      |
| `iswctype`  | classifies a wide character according to the specified `LC_CTYPE` category |
| `wctype`    | looks up a character classification category in the current C locale       |

The following table defines the outputs of the character classification functions for the ASCII character set.

| ASCII   | characters        | `iswcntrl` | `iswprint` | `iswspace` | `iswblank` | `iswgraph` | `iswpunct` | `iswalnum` | `iswalpha` | `iswupper` | `iswlower` | `iswdigit` | `iswxdigit` |
| ------- | ----------------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ----------- |
| 0–8     | control codes     | `true`     | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`     |
| 9       | tab               | `true`     | `false`    | `true`     | `true`     | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`     |
| 10–13   | whitespaces       | `true`     | `false`    | `true`     | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`     |
| 14–31   | control codes     | `true`     | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`     |
| 32      | space             | `false`    | `true`     | `true`     | `true`     | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`     |
| 33–47   | !"#$%&'()*+,-./   | `false`    | `true`     | `false`    | `false`    | `true`     | `true`     | `false`    | `false`    | `false`    | `false`    | `false`    | `false`     |
| 48–57   | 0-9               | `false`    | `true`     | `false`    | `false`    | `true`     | `false`    | `true`     | `false`    | `false`    | `false`    | `true`     | `true`      |
| 58–64   | :;<=>?@           | `false`    | `true`     | `false`    | `false`    | `true`     | `true`     | `false`    | `false`    | `false`    | `false`    | `false`    | `false`     |
| 65–70   | A-F               | `false`    | `true`     | `false`    | `false`    | `true`     | `false`    | `true`     | `true`     | `true`     | `false`    | `false`    | `true`      |
| 71–90   | G-Z               | `false`    | `true`     | `false`    | `false`    | `true`     | `false`    | `true`     | `true`     | `true`     | `false`    | `false`    | `false`     |
| 91–96   | [&bsol;]^_&grave; | `false`    | `true`     | `false`    | `false`    | `true`     | `true`     | `false`    | `false`    | `false`    | `false`    | `false`    | `false`     |
| 97–102  | a-f               | `false`    | `true`     | `false`    | `false`    | `true`     | `false`    | `true`     | `true`     | `false`    | `true`     | `false`    | `true`      |
| 103–122 | g-z               | `false`    | `true`     | `false`    | `false`    | `true`     | `false`    | `true`     | `true`     | `false`    | `true`     | `false`    | `false`     |
| 123–126 | {&verbar;}~       | `false`    | `true`     | `false`    | `false`    | `true`     | `true`     | `false`    | `false`    | `false`    | `false`    | `false`    | `false`     |
| 127     | backspace         | `true`     | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`    | `false`     |

###### Character manipulation

Defined in header `<cwctype>`

| Function    | Description                                                                       |
| ----------- | --------------------------------------------------------------------------------- |
| `towlower`  | converts a wide character to lowercase                                            |
| `towupper`  | converts a wide character to uppercase                                            |
| `towctrans` | performs character mapping according to the specified `LC_CTYPE` mapping category |
| `wctrans`   | looks up a character mapping category in the current C locale                     |

###### Conversions to numeric formats

Defined in headers `<cwchar>` and `<cinttypes>`

| Function                      | Description                                                   |
| ----------------------------- | ------------------------------------------------------------- |
| `wcstol`, `wcstoll`           | converts a wide string to an integer value                    |
| `wcstoul`, `wcstoull`         | converts a wide string to an unsigned integer value           |
| `wcstof`, `wcstod`, `wcstold` | converts a wide string to a floating point value              |
| `wcstoimax`, `wcstoumax`      | converts a wide string to `std::intmax_t` or `std::uintmax_t` |

###### String manipulation

Defined in header `<cwchar>`

| Function  | Description                                                                         |
| --------- | ----------------------------------------------------------------------------------- |
| `wcscpy`  | copies one wide string to another                                                   |
| `wcsncpy` | copies a certain amount of wide characters from one string to another               |
| `wcscat`  | appends a copy of one wide string to another                                        |
| `wcsncat` | appends a certain amount of wide characters from one wide string to another         |
| `wcsxfrm` | transform a wide string so that `wcscmp` would produce the same result as `wcscoll` |

###### String examination

Defined in header `<cwchar>`

| Function  | Description                                                                                                                 |
| --------- | --------------------------------------------------------------------------------------------------------------------------- |
| `wcslen`  | returns the length of a wide string                                                                                         |
| `wcscmp`  | compares two wide strings                                                                                                   |
| `wcsncmp` | compares a certain amount of characters from two wide strings                                                               |
| `wcscoll` | compares two wide strings in accordance to the current locale                                                               |
| `wcschr`  | finds the first occurrence of a wide character in a wide string                                                             |
| `wcsrchr` | finds the last occurrence of a wide character in a wide string                                                              |
| `wcsspn`  | returns the length of the maximum initial segment that consists of only the wide characters found in another wide string    |
| `wcscspn` | returns the length of the maximum initial segment that consists of only the wide characters not found in another wide sting |
| `wcspbrk` | finds the first location of any wide character in one wide string, in another wide string                                   |
| `wcsstr`  | finds the first occurrence of a wide string within another wide string                                                      |
| `wcstok`  | finds the next token in a wide string                                                                                       |

###### Wide character array manipulation

Defined in header `<cwchar>`

| Function   | Description                                                                          |
| ---------- | ------------------------------------------------------------------------------------ |
| `wmemcpy`  | copies a certain amount of wide characters between two non-overlapping arrays        |
| `wmemmove` | copies a certain amount of wide characters between two, possibly overlapping, arrays |
| `wmemcmp`  | compares a certain amount of wide characters from two arrays                         |
| `wmemchr`  | finds the first occurrence of a wide character in a wide character array             |
| `wmemset`  | copies the given wide character to every position in a wide character array          |

###### Types

Defined in header `<cwctype>` and `<cwchar>`

| Function    | Description                                                                     |
| ----------- | ------------------------------------------------------------------------------- |
| `wctrans_t` | scalar type that holds locale-specific character mapping                        |
| `wctype_t`  | scalar type that holds locale-specific character classification                 |
| `wint_t`    | integer type that can hold any valid wide character and at least one more value |

###### Macros

Defined in header `<cwchar>`

| Macro       | Description                                                    |
| ----------- | -------------------------------------------------------------- |
| `WEOF`      | a non-character value of type `wint_t` used to indicate errors |
| `WCHAR_MIN` | the smallest valid value of `wchar_t`                          |
| `WCHAR_MAX` | the largest valid value of `wchar_t`                           |

#### Floating-point types

The following three types and their cv-qualified versions are collectively called floating-point types:

- `float`
    : single precision floating-point type. Matches IEEE-754 binary32 format if supported. 
- `double`
    : double precision floating-point type. Matches IEEE-754 binary64 format if supported. 
- `long double`
    : extended precision floating-point type. Matches IEEE-754 binary128 format if supported, otherwise matches IEEE-754 binary64-extended format if supported, otherwise matches some non-IEEE-754 extended floating-point format as long as its precision is better than binary64 and range is at least as good as binary64, otherwise matches IEEE-754 binary64 format.

    - binary128 format is used by some HP-UX, SPARC, MIPS, ARM64, and z/OS implementations.
    - The most well known IEEE-754 binary64-extended format is 80-bit x87 extended precision format. It is used by many x86 and x64 implementations (a notable exception is MSVC, which implements `long double` in the same format as `double`, which is binary64).

##### Properties

Floating-point types may support special values:

- infinity (*INFINITY* and *-INFINITY*)
    : If the implementation supports floating-point infinities, the macro `INFINITY` expands to constant expression of type `float` which evaluates to positive or unsigned infinity. If the implementation does not support floating-point infinities, the macro `INFINITY` expands to a positive value that is guaranteed to overflow a `float` at compile time, and the use of this macro generates a compiler warning.
- negative zero (*-0.0*)
    : it compares equal to positive zero, but is meaningful in some mathematics (such as `1.0/0.0 == INFINITY` but `1.0/-0.0 == -INFINITY`).
- NaN (*not-a-number*)
    : which does not compare equal with anything, including itself. Multiple bit patterns represent NaN (such as `std::nan` and `NAN`). Note that C++ takes no special notice of signaling NaN other than detecting their support by `std::numeric_limits::has_signaling_NaN`, and treats all NaN as quiet.

Real floating-point numbers may be used with arithmetic operators and various mathematical functions from `<cmath>`. Both built-in operators and library functions may raise floating-point exceptions and set `errno`.

Floating-point expressions may have greater range and precision than indicated by their types. Floating-point expressions may also be contracted (calculated as if all intermediate values have infinite range and precision). Standard C++ does not restrict the accuracy of floating-point operations.

Some operations on floating-point numbers are affected by and modify the state of the floating-point environment (most notably, rounding direction).

Implicit conversions are defined between real floating-point types and integer types.

#### Range of values

The following table provides a reference for the limits of common numeric representations.

Prior to C++20, the C++ Standard allowed any signed integer representation, and the minimum guaranteed range of N-bit signed integers was from -(2<sup>N-1</sup> - 1) to +2<sup>N-1</sup> - 1 (such as -127 to 127 for a signed 8-bit type), which corresponds to the limits of one's complement.

However, all C++ compilers use two's complement representation, and as of C++20, it is the only representation allowed by the standard, with the guaranteed range from -2<sup>N-1</sup> to +2<sup>N-1</sup> - 1 (such as -128 to 127 for a signed 8-bit type).

8-bit one's complement representation for `char` have been disallowed since C++11, because a UTF-8 code unit of value `0x80` used in a UTF-8 string literal must be stored in a `char` element object.

| Type      | Size in bits | Format   | Value range                                             |
| --------- | ------------ | -------- | ------------------------------------------------------- |
| character | 8            | signed   | -128 to 127                                             |
| character | 8            | unsigned | 0 to 255                                                |
| character | 16           | UTF-16   | 0 to 65535                                              |
| character | 32           | UTF-32   | 0 to 1114111 (0x10ffff)                                 |
| integer   | 16           | signed   | -32768 to 32767                                         |
| integer   | 16           | unsigned | 0 to 65535                                              |
| integer   | 32           | signed   | -2,147,483,648 to 2,147,483,647                         |
| integer   | 32           | unsigned | 0 to 4,294,967,295                                      |
| integer   | 64           | signed   | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| integer   | 64           | unsigned | 0 to 18,446,744,073,709,551,615                         |

The following table provides a reference for the limits of binary floating-point representations in common formats. The values for limits are only absolute values (signedness is not included for brevity).

| Type                  | Size in bits | Format   | Min subnormal | Min normal | Max                                     |
| --------------------- | ------------ | -------- | ------------- | ---------- | --------------------------------------- |
| binary floating-point | 32           | IEEE 754 | 0x1p-149      | 0x1p-126   | 0x1.fffffep+127                         |
| binary floating-point | 64           | IEEE 754 | 0x1p-1074     | 0x1p-1022  | 0x1.fffffffffffffp+1023                 |
| binary floating-point | 80           | x86      | 0x1p-16446    | 0x1p-16382 | 0x1.fffffffffffffffep+16383             |
| binary floating-point | 128          | IEEE 754 | 0x1p-16494    | 0x1p-16382 | 0x1.ffffffffffffffffffffffffffffp+16383 |

### Arithmetic operators

| Operator name       | Syntax   | Overloadable | Inside class definition               | Outside class definition                 |
| ------------------- | -------- | ------------ | ------------------------------------- | ---------------------------------------- |
| unary plus          | `+a`     | Yes          | `T T::operator+() const;`             | `T operator+(const T &a);`               |
| unary minus         | `-a`     | Yes          | `T T::operator-() const;`             | `T operator-(const T &a);`               |
| addition            | `a + b`  | Yes          | `T T::operator+(const T2 &b) const;`  | `T operator+(const T &a, const T2 &b);`  |
| subtraction         | `a - b`  | Yes          | `T T::operator-(const T2 &b) const;`  | `T operator-(const T &a, const T2 &b);`  |
| multiplication      | `a * b`  | Yes          | `T T::operator*(const T2 &b) const;`  | `T operator*(const T &a, const T2 &b);`  |
| division            | `a / b`  | Yes          | `T T::operator/(const T2 &b) const;`  | `T operator/(const T &a, const T2 &b);`  |
| remainder           | `a % b`  | Yes          | `T T::operator%(const T2 &b) const;`  | `T operator%(const T &a, const T2 &b);`  |
| bitwise NOT         | `~a`     | Yes          | `T T::operator~() const;`             | `T operator~(const T &a);`               |
| bitwise AND         | `a & b`  | Yes          | `T T::operator&(const T2 &b) const;`  | `T operator&(const T &a, const T2 &b);`  |
| bitwise OR          | `a | b`  | Yes          | `T T::operator|(const T2 &b) const;`  | `T operator|(const T &a, const T2 &b);`  |
| bitwise XOR         | `a ^ b`  | Yes          | `T T::operator^(const T2 &b) const;`  | `T operator^(const T &a, const T2 &b);`  |
| bitwise left shift  | `a << b` | Yes          | `T T::operator<<(const T2 &b) const;` | `T operator<<(const T &a, const T2 &b);` |
| bitwise right shift | `a >> b` | Yes          | `T T::operator>>(const T2 &b) const;` | `T operator>>(const T &a, const T2 &b);` |

!!! note

    - All built-in operators return values, and most user-defined overloads also return values so that the user-defined operators can be used in the same manner as the built-in operators. However, in a user-defined operator overload, any type can be used as return type (including `void`). In particular, stream insertion and stream extraction overloads of `operator<<` and `operator>>` return `T&`.
    - `T2` can be be any type including `T`.

#### Explanation

All arithmetic operators compute the result of a specific arithmetic operation and returns its result. The arguments are not modified.

#### Conversions

If the operand passed to an arithmetic operator is integral or unscoped enumeration type, then before any other action (but after lvalue-to-rvalue conversion, if applicable), the operand undergoes integral promotion. If an operand has array or function type, array-to-pointer and function-to-pointer conversions are applied.

For the binary operators (except shifts), if the promotion operands have different types, additional set of implicit conversions is applied, known as usual arithmetic conversions with the goal to produce the common type (also accessible via the `std::common_type` type trait). If prior to any integral promotion, one operand is of enumeration type and the other operand is of a floating-point type or a different enumeration type, this behavior is depreciated.

- If either operand has scoped enumeration type, no conversion is performed