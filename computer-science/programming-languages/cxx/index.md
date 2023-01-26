# C++ Programming Language

<!-- References: -->
<!-- C++ Primer -->
<!-- The C++ Programming Language -->
<!-- Wikipedia -->

<!-- Necessary for proper formatting of tables where header is not required -->
<style>
th:empty {
  display: none;
}
</style>

## Part 1: The Basics

C++ (pronounced "C plus plus") is a high-level, general-purpose, multi-paradigm, statically typed, free-form, compiled programming language created by Danish computer scientist Bjarne Stroustrup as an extension of the C programming language, or "C with classes". The language has expanded significantly over time, and modern C++ now has object-oriented, generic, and functional features in addition to facilities for low-level memory manipulation.

C++ was designed with performance, efficiency, and flexibility in mind, because of which, it is used widely for the development of operating systems, browsers, video games, desktop applications, libraries, graphics, cloud systems, databases, servers, banking applications, embedded systems, telephone switches, compilers, and other performance-critical or resource-constrained applications.

|                       |                                                                                                                  |
| --------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Logo                  | ![C++ logo endorsed by the C++ standards committee](assets/cxx-logo.png)                                         |
| Paradigms             | Multi-paradigm: procedural, imperative, functional, object-oriented, generic, modular                            |
| Family                | C                                                                                                                |
| Designed by           | Bjarne Stroustrup                                                                                                |
| Developer             | ISO/IEC JTC 1 (Joint Technical Committee 1) / SC 22 (Subcommittee 22) / WG 21 (Working Group 21)                 |
| First appeared        | 1985                                                                                                             |
| Stable release        | C++20 (ISO/IEC 14882:2020) / 15 December 2020                                                                    |
| Preview release       | C++23 / 18 December 2022                                                                                         |
| Typing discipline     | Static, nominative, partially inferred                                                                           |
| OS                    | Cross-platform                                                                                                   |
| Filename extensions   | .C, .cc, .cpp, .cxx, .c++, .h, .H, .hh, .hpp, .hxx, .h++                                                         |
| Website               | [isocpp.org](isocpp.org)                                                                                         |
| Major implementations | GCC, LLVM, Clang, Microsoft Visual C++, Embarcadero C++ Builder, Intel C++ Compiler, IBM XL C++, EDG             |
| Influenced by         | Ada, ALGOL 68, BCPL, C, CLU, F#, ML, Mesa, Modula-2, Simula, Smalltalk                                           |
| Influenced            | Ada 95, C#, C99, Carbon, Chapel, Clojure, D, Java, JS++, Lua, Nim, Objective C++, Perl, PHP, Python, Rust, Seed7 |

### History

The C++ programming language was first standardized in 1998 as ISO/IEC 14882:1998. Before the initial standardization in 1998, C++ was developed by Stroustrup at Bell Labs since 1979 as an extension of the C programming language, as he wanted an efficient and flexible language similar to C that also provided high-level features for program organization. Since 2012, C++ has been on a three-year release schedule with C++23 as the next planned standard.

| Year | C++ standard       | Informal name |
| ---- | ------------------ | ------------- |
| 1998 | ISO/IEC 14882:1998 | C++98         |
| 2003 | ISO/IEC 14882:2003 | C++03         |
| 2011 | ISO/IEC 14882:2011 | C++11, C++0x  |
| 2014 | ISO/IEC 14882:2014 | C++14, C++1y  |
| 2017 | ISO/IEC 14882:2017 | C++17, C++1z  |
| 2020 | ISO/IEC 14882:2020 | C++20, C++2a  |
| 2023 | ISO/IEC 14882:2023 | C++23         |

### Philosophy

The development and evolution of C++ has been guided by a set of principles:

- It must be driven by actual problems and its features should be immediately useful in real world programs.
- Every feature should be implementable with a reasonably obvious way.
- Programmers should be free to pick a programming style, and that style should be fully supported by C++.
- Allowing a useful feature is more important than preventing every possible misuse of C++.
- It should provide facilities for organizing programs into separate, well-defined parts, and provide facilities for combining separately developed parts.
- No implicit violations of the type system should be allowed (however explicit violations, that are explicitly requested by the programmer, are allowed).
- User-created types need to have the same support and performance as built-in types.
- Unused features should not negatively impact created executables by hurting performance.
- There should not language beneath C++ (except assembly language).
- C++ should work alongside other existing programming languages, rather than fostering its own separate and incompatible programming environment.
- If the programmer's intent is unknown, allow the programmer to specify it by providing manual control.

