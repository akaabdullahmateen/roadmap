## What is a data type in a programming language?

A data type (or simply a "type") is a description of a set of values that dictate the set of allowed operations on those values and how those operations are interpreted.

## What is a type in C++ programming language?

Objects, references, functions (including template specializations), and expressions have a property called type, which both restricts the operations that are permitted for those entities and provides semantic meaning to the otherwise generic sequences of bits.

## How are the types classified?

The C++ type system divides the types into two major categories:

- fundamental types
- compound types

<!-- Compound types will be discussed later -->

## What are fundamental types?

Fundamental data types are the data types which are predefined in the language. They usually correspond to the basic storage units on a computer system.

## What are subcategories of fundamental types?

Fundamental types include:

- Void type (`void`)
- `nullptr_t`
- arithmetic types

<!-- Void type and std::nullptr_t are short descriptions, therefore, although not discussed now in the book, I am writing their descriptions here -->
#STARTIF

## What is void type?

`void` is a type with an empty set of values. It is an incomplete type that can not be completed (consequently, objects of type `void` are disallowed). There are no arrays of `void`, nor references to `void`. However, pointers to `void` and functions returning `void` are permitted.

## What is `std::nullptr_t` type?

`std::nullptr_t` is the type of the null pointer literal (`nullptr`). It is a distinct type that is not itself a pointer type or a pointer to member type. Its values are null pointer constant (`NULL`), and may be implicitly converted to any pointer type or pointer to member type.

<!-- This begs the question: What is the nullptr and NULL -->

## What is the null pointer literal?

The keyword `nullptr` denotes the null pointer literal. It is a prvalue of type `std::nullptr_t`. There exist implicit conversions from `nullptr` to null pointer value of any pointer type and any pointer to member type. Similar conversions exist for any null pointer constant, which includes values of type `std::nullptr_t` as well as the macro `NULL`.

## What is the `NULL` macro?

The macro `NULL` is an implementation-defined null pointer constant, which may be an integer literal with value zero, or a prvalue of type `std::nullptr_t`. A null pointer constant may be implicitly converted to any pointer or pointer to member type; such conversion results in the null pointer value of that type. If a null pointer constant has integer type, it may be converted to a prvalue of type `std::nullptr_t`.

Some implementations define `NULL` as the compiler extensions `__null` with the following properties:

- `__null` is equivalent to a zero-valued integer literal (and this compatible with the C++ standard) and has the same size as `void*` (therefore, it is equivalent to `0` on ILP32 platforms and `0L` on LP64 platforms).
- conversions from `__null` to an arithmetic type, including the type of `__null` itself, may trigger a warning.