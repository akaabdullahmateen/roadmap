<style>
th:empty {
  display: none;
}
</style>

#IF --> STANDARD DOCUMENTATION

# IEEE 754

## Floating-point formats

### Overview

Floating-point formats are used to represent a finite subset of real numbers. Formats are characterized by their radix, precision, exponent range, and each format can represent a unique set of floating-point data.

All formats can be supported as arithmetic formats (they may be used to represent floating-point operands or results for the operations).

Specific fixed-width encodings for binary and decimal formats are defined for a subset of formats. These interchange formats are identified by their size and can be used for the exchange of floating-point data between implementations.

Five basic formats are defined:

- Three binary formats, with encodings in lengths of 32, 64, and 128 bits.
- Two decimal formats, with encodings in lengths of 64 and 128 bits.

Additional arithmetic formats are recommended for extending these basic formats.

### Specification levels

Floating-point arithmetic is a systemic approximation of real numbers. Floating-point arithmetic can only represent a finite subset of the continuum of real numbers. Consequently, certain properties of real numbers (such as associativity of addition) do not always hold for floating-point arithmetic.

|                |                                                        |                                                   |
| -------------- | ------------------------------------------------------ | ------------------------------------------------- |
| Level 1        | {-∞ ... 0 ... +∞}                                      | Extended real numbers                             |
| many-to-one ↓ | rounding                                               | ↑ projection (except for NaN)                    |
| Level 2        | {-∞ ... -0} ∪ {+0 ... +∞} ∪ NaN                        | Floating-point data (algebraically closed system) |
| one-to-many ↓ | representation specification                           | ↑ many-to-one                                    |
| Level 3        | (sign, exponent, significand) ∪ {-∞, +∞} ∪ qNaN ∪ sNaN | Representation of floating-point data             |
| one-to-many ↓ | encoding for representation of floating-point data     | ↑ many-to-one                                    |
| Level 4        | 0111000...                                             | Bit strings                                       |

The mathematical structure underpinning the arithmetic is the extended reals (set of real numbers together with positive and negative infinity). For a given format, the process of rounding maps an extended real number to a floating-point number included in that format. A floating-point datum, which can be a signed zero, finite non-zero number, signed infinity, or a NaN (not-a-number), can be mapped to one or more representations of floating-point data in a format.

The representations of floating-point data in a format consist fo:

- triples (sign, exponent, significand); in radix b, the floating-point number represented by a triple is `(-1)^sign * b^exponent * significand`
- +∞, -∞
- qNaN (quiet), sNaN (signaling)

An encoding maps a representation of a floating-point datum to a bit string. An encoding might map some representations of floating-point data to more than one bit string. Multiple NaN bit strings should be used to store retrospective diagnostic information.

### Sets of floating-point data

The set of finite floating-point numbers representable within a particular format is determined by the following integer parameters:

- `b` which is the radix (2 or 10)
- `p` which is the precision (the number of digits in the significand)
- `emax` which is the maximum exponent `e`
- `emin` which is the minimum exponent `e` (`emin` shall be `1 - emax` for all formats)

Within each format, the following floating-point data shall be represented:

- Signed zero and non-zero floating-point numbers of the form `(-1)^s * b^e * m`, where:
  - `s` is `0` or `1`
  - `e` is any integer `emin <= e <= emax`
  - `m` is a number represented by a digit string of the form:
    
    d<sub>0</sub>·d<sub>1</sub>d<sub>2</sub>...d<sub>p - 1</sub>, where:
      - `·` is the radix point
      - d<sub>i</sub> is an integer digit such that 0 <= d<sub>i</sub> < b (therefore, `0 <= m < b`)
  - Two infinities, +∞ and -∞
  - Two NaN, qNaN (quiet) and sNaN (signaling)

These are the only floating-point data represented.

In the foregoing description, the significand `m` is viewed in a scientific form, with the radix point immediately following the first digit. It is also convenient for some purposes to view the significand as an integer; in which case the finite floating-point numbers are described thus:

- Signed zero and non-zero floating-point numbers of the form `(-1)^s * b^q * m`, where:
  - `s` is `0` or `1`
  - `q` is any integer `emin <= q + p - 1 <= emax`
  - `c` is a number represented by a digit string of the form:
    
    d<sub>0</sub>d<sub>1</sub>d<sub>2</sub>...d<sub>p - 1</sub>, where:
      - d<sub>i</sub> is an integer digit such that 0 <= d<sub>i</sub> < b (`c` is therefore an integer such that `0 <= c < b^p`)

This view of the significand as an integer `c`, with its corresponding exponent `q`, describes exactly the same set of zero and non-zero floating-point numbers as the view in scientific form. For finite floating-points numbers, `e = q + p - 1` and `m = c * b ^(1-p)`.

The smallest positive normal floating-point number is b<sup>emin</sup> and the largest is b<sup>emax</sup>(b - b<sup>1 - p</sup>). The non-zero floating-point numbers for a format with magnitude less than b<sup>emin</sup> are called subnormal because their magnitudes lie between zero and the smallest normal magnitude. They always have fewer than `p` significant digits. Every finite floating-point number is an integral multiple of the smallest subnormal magnitude b<sup>emin</sup>(b - b<sup>1 - p</sup>).

For a floating-point number that has the value zero, the sign bit `s` provides an extra bit of information. Although all formats have distinct representations for `+0` and `-0`, the sign of zero is significant in some circumstances, such as division by zero, but in others. Binary interchange formats have just one representation each for `+0` and `-0`, but decimal formats have many. In this standard, `0` and ∞ are written without a sign when the sign is not important.

Parameters defining basic format floating-point numbers:

Binary format (b = 2)

| parameter | binary32 | binary64 | binary128 |
| --------- | -------- | -------- | --------- |
| p, digits | 24       | 53       | 113       |
| emax      | +127     | +1023    | +16383    |

Decimal format (b = 10)

| parameter | decimal64 | decimal128 |
| --------- | --------- | ---------- |
| p, digits | 16        | 34         |
| emax      | +384      | +6144      |

#ENDIF --> STANDARD DOCUMENTATION
---

#IF --> WIKIPEDIA

# IEEE 754

The IEEE Standard for Floating-Point Arithmetic (IEEE 754) is a technical standard for floating-point arithmetic established in 1985 by the Institute of Electrical and Electronics Engineering (IEEE). The standard addressed many problems found in the diverse floating-point implementations that made them difficult to use reliably and portably. Many hardware floating-point units use the IEEE 754 standard.

// REASON FOR ENDIF: SECURE CONNECTION TO WIKIPEDIA COULD NOT BE ESTABLISHED :/
#ENDIF --> WIKIPEDIA