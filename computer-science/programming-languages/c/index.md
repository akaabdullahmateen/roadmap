# C programming language

## Introduction

C (pronounced like the letter *c*) is a general-purpose programming language. It was created in the 1970s by Dennis Ritchie, and remains very widely used and influential. By design, C's features cleanly reflect the capabilities of the targeted CPU. It has found lasting use in operating systems, device drivers, protocol stacks, and (though decreasingly) application software. C is commonly used on computer architectures that range from the largest super computers to the smallest micro-controllers and embedded systems.

C is an imperative procedural language, supporting structured programming, lexical variable scope and recursion, with a static type system. It was designed to be compiled to provide low-level access to memory and language constructs that map efficiently to machine instructions, all with minimal runtime support. Despite its low-level capabilities, the language was designed to encourage cross-platform programming. A standards-compliant C program written with portability in mind can be compiled for a wide variety of computer platforms and operating systems with a few changes to its source code.

## History

The origin of C is closely tied to the development of the Unix operating system by Dennis Ritchie and Ken Thompson. Thompson desired a programming language to make utilities for the Unix operating system. At first, he tried to make a Fortran compiler, but soon gave up. Instead, he created a cut-down version of the BCPL systems programming language and named it *B*. However, B was not powerful and slow, therefore, Ritchie improved B and called it *New B* or *NB*. Afterwards, more features were added, a new compiler was written, and the language was renamed *C*.

In 1978, Brian Kernighan and Dennis Ritchie published the first edition of *The C Programming Language*. This book, known to C programmers as *K&R*, served for many years as an informal specification of the language. The version of C that it describes is commonly referred to as *K&R C*. As this was released in 1978, it is also referred to as *C78*. The second edition of the book covers the later *ANSI C* standard.

The large number of extensions and lack of agreement on a standard library, together with the language popularity and the fact that not even the Unix compilers precisely implemented the K&R specification, led to the necessity of standardization.

In 1983, the American National Standards Institute (ANSI) formed a committee called *X3J11* to establish a standard specification of C. X3J11 based the C standard on the Unix implementation; however, the non-portable portion of the Unix C library was handed off to the IEEE working group 1003 to become the basis for the 1988 POSIX standard. In 1989, the C standard was ratified as *ANSI X3.159-1989 Programming Language C*. This version of the language is often referred to as ANSI C, or sometimes C89.

In 1990, the ANSI C standard (with formatting changes) was adopted by the International Organization for Standardization (ISO) as *ISO/IEC 9899:1990*, which is sometimes called *C90*. Therefore, the terms C89 and C90 refer to the same programming language.

ANSI, like other national standards bodies, no longer develops the C standard independently, but defers to the international C standard, maintained by the working group *ISO/IEC JTC1/SC22/WG14*.

| Year      | Informal name | C standard        | `__STDC_VERSION__` |
| --------- | ------------- | ----------------- | ------------------ |
| 1972      | Birth         |                   |                    |
| 1978      | K&R C         |                   |                    |
| 1989/1990 | ANSI C, ISO C | ISO/IEC 9899:1990 |                    |
| 1999      | C99           | ISO/IEC 9899:1999 | `199901L`          |
| 2011      | C11, C1x      | ISO/IEC 9899:2011 | `201112L`          |
| 2018      | C17           | ISO/IEC 9899:2018 | `201710L`          |


