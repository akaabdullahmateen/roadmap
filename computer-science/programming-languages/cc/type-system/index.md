## Type system

Type system is a logical system that comprises a set of rules which assign a type to every "term" (program constructs such as variables, expressions, functions, and modules). The type system dictates the operations that can be performed on a term.

Type systems are often specified as part of a programming language and built into interpreters and compilers, although the type system of a language can be extended by optional tools that perform additional checks using the language's original type syntax and grammar. The main purpose of a type system is to reduce possibilities for bugs due to type errors.

Type systems allow defining interfaces between different parts of a program, and then checking that the parts have been connected in a consistent way. This checking can happen statically (at compile time), dynamically (at run time), or as a combination of both.

If a language specification requires its typing rules strongly (allowing only those automatic type conversions that do not lose information), then it is classified as *strongly typed*; otherwise, *weakly typed*.

## Type

### Type classification

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


### Fixed width integer types

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