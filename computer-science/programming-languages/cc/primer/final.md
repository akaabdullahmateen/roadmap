# Data types

## Data types

A data type (or simply a "type") is a description of a set of values that dictate the set of allowed operations on those values and how those operations are interpreted.

### Data type in C++

In C++, objects, references, functions (including template specializations), and expressions have a property called type, which both restricts the operations that are permitted for those entities and provides semantic meaning to the otherwise generic sequences of bits.

## Type classification

The C++ type system consists of the following types:

- Fundamental types
- Compound types

A complete hierarchy for the type system is as follows:

- fundamental type
    - `void`
    - `nullptr_t`
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

### Fundamental types

Fundamental data types are the data types that are predefined in the language. They usually correspond to the basic storage units on a computer system.

Fundamental types consists of the following types:

- Void type (`void`)
- Null pointer type (`nullptr_t`)
- Arithmetic types

#### Void type

The void type (`void`) is a type with an empty set of values. It is an incomplete type that can not be completed (consequently, objects of type `void` are disallowed). There are no arrays of `void`, nor references to `void`. However, pointers to `void` and functions returning `void` are permitted.

#### Null pointer type

The null pointer type (`std::nullptr_t`) is the type of the null pointer literal (`nullptr`). It is a distinct type that is not itself a pointer type or a pointer to member type. Its values are null pointer constant (`NULL`), and may be implicitly converted to any pointer type or pointer to member type. 

#### Arithmetic types

Integral and floating-point types are collectively termed arithmetic types.

The arithmetic types consist of the following types:

- Integral types
- Floating-point types

##### Integral types

The character types, boolean type, signed and unsigned integer types, and cv qualified versions of them, are collectively termed "integral types" (or synonymously "integer types").

The integral types consist of the following types:

- Boolean type (`bool`)
- Character types
- Signed integer types
- Unsigned integer types

###### Boolean type

Boolean type (`bool`) is a distinct type that has the same object representation, value representation, and alignment requirements as an implementation-defined unsigned integer type. The values of type `bool` are `true` and `false`.

There are no `signed bool`, `unsigned bool`, `short bool`, or `long bool` types or values.

###### Character types

The character types consist of the following types:

- Narrow character types
- Wide character types

####### Narrow character types

For narrow character types, each possible bit pattern of the object representation represents a distinct value. A bit-field for narrow character type whose width is larger than the width of that type has padding bits.

The narrow character types consist of the following types:

- Ordinary character types
- Type `char8_t`

######## Ordinary character types

The ordinary character types consist of the following types:

- Type `char`
- Type `unsigned char`
- Type `signed char`

######### Type `char`

The type `char` is a type for character representation. It is a distinct type that has an implementation-defined choice of `signed char` or `unsigned char` as its underlying type, whichever can be most efficiently processed on the target system (the default for ARM and PowerPC is usually `unsigned char`, and the default for x86 and x64 is usually `signed char`).

For every value of type `unsigned char` in range [0, 255], converting the value to `char` and then back to `unsigned char` produces the original value.

######### Type `unsigned char`

The type `unsigned char` is a type for unsigned character representation. It is often used to inspect object representations (raw memory).

######### Type `signed char`

The type `signed char` is a type for signed character representation.

######## Type `char8_t`

The type `char8_t` is a type for UTF-8 character representation. It is required to be large enough to represent any UTF-8 code unit. It has the same size, signedness, and alignment as `unsigned char` (and therefore, the same size and alignment as `char` and `signed char`), but is a distinct type.

####### Wide character types

The wide character types consist of the following types:

- Type `wchar_t`
- Type `char16_t`
- Type `char32_t`

######## Type `wchar_t`

The type `wchar_t` is a type for wide character representation. It has an implementation-defined choice of signed or unsigned integer type as its underlying type. The values of type `wchar_t` can represent distinct codes for all members of the largest extended character set specified among the supported locales.

It has the same size, signedness, and alignment as one of the integer types, but is a distinct type. In practice, it is 32 bits and holds UTF-32 code units on Linux and many other non-Windows systems, but 16 bit and holds UTF-16 code units on Windows.

######## Type `char16_t`

The type `char16_t` is a type for UTF-16 character representation. It is required to be large enough to represent any UTF-16 code unit. It has the same size, signedness, and alignment as `std::uint_least16_t`, but is a distinct type.

######## Type `char32_t`

The type `char32_t` is a type for UTF-32 character representation. It is required to be large enough to represent any UTF-32 code unit. It has the same size, signedness, and alignment as `std::uint_least32_t`, but is a distinct type.

### Compound types

Compound data types are the data types that are defined in terms of another another.

<!-- TODO: Yet to be completed -->
