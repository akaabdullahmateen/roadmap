# Unicode

## About Unicode

### Quick facts

- Founded in 1988, incorporated in 1991
- Public benefit, 501(c)3 non-profit organization
- Open source standards, data, and software development
- Orchestrates the contributions of 100s of professionals, expert volunteers, and language experts
- 30+ organizational members across corporate, academic, and government institutions
- Funded by membership dues and donations

### Operating values

- Local solutions require global collaboration
- Localization respects and empowers users
- Interoperability across platforms serves you - and the greater good
- Transparency and open source ensure: Reliability - Security - Stability

### How did Unicode gets its name

The Unicode Consortium started out as the standards body for character encoding and derives its name from three main goals:

- Universal (addressing the needs of worlds languages)
- Uniform (fixed-width codes for efficient access)
- Unique (bit sequence has only one interpretation into character codes)

Since that time, it has expanded to be far more than character encoding. Its work now includes the character properties and algorithms, language and locale data for internationalization, and production software libraries to make everything accessible to programs.

### Characters before Unicode

Fundamentally, computers just deal with numbers. They store letters and other characters by assigning a number for each one. Before the Unicode standard was developed, there were many different systems, called character encodings, for assigning these numbers. These earlier character encodings were limited and did not cover characters for all the world's languages. Even for a single language, like English, no single encoding covered all the letters, punctuation, and technical symbols in common use. Pictographic languages, such as Japanese, were a challenge to support with these earlier encoding standards.

Early character encodings also conflicted with one another. That is, two encodings could use the same number for two different characters, or use different numbers for the same character. Any given computer might have to support many different encodings. However, when data is passed between computers and different encodings it increased the risk of data corruption or errors.

Character encodings existed for a handful of *large* languages. But many languages lacked character support altogether.

## Technical quick start guide

### What is internationalization and why does it matter?

To ensure that end users can seamlessly work, collaborate, communicate, and much more in their native languages around the world, software developers deploy the Unicode architecture and standards across all software and services.

Internalization (also known as *i18n*, since there are 18 letters between *i* and *n*) is the design and development of a product that is enabled for target audiences that vary in culture, region, or language. Internationalizing your software means you can support across different regions and languages in the way humans expect to interact wih an application, including the presentation of text, numbers, dates, and the layout of the user interface.

Localization is the adaptation of software for specific languages and cultures. Typically, this involves providing translations or providing alternate, locally acceptable content such as stylesheets or images. Internationalized software makes localization very efficient.

Unicode establishes the foundational layers (character set, locale data, algorithms) that make it possible to design code that handles the requirements of all languages and regions at the same time, while minimizing the need for lower-level details and quirks to interfere with that design.

Architect once for a global solution that supports local implementations.

### What is Unicode?

The Unicode Consortium is the premier standards organization for internationalization of software and services, including the encoding of text for all modern computing systems. The Consortium supports internationalization with the Unicode Standard and by providing core libraries, software algorithms, and structured data.

The Unicode Standard refers to the standard character set that represents all natural language characters. Unicode can encode up to roughly 1.1 million characters, allowing it to support all of the world's languages and scripts in a single, universal standard.

All modern operating systems, computing environments, programming languages, and applications support the core of the Unicode Standard. Since the Unicode Standard specifies the handling of characters for all languages in a uniform way, it simplifies and enables locale-sensitive internationalization algorithms that would not have been possible otherwise, such as:

- Sorting and string searching/matching
- Word-boundary/sentence-boundary detection and line breaking
- Right-to-left text region boundary analysis
- Formatting of numbers, times, lists, and plural messages

There are many more features supported by Unicode data and libraries. Higher level computing applications rely upon these features to achieve their goals. Examples include products like web browsers and text editors, and services based on natural language processing like machine translation and voice assistants.

| Standards body                             | Task                      | Description                                                                                   |
| ------------------------------------------ | ------------------------- | --------------------------------------------------------------------------------------------- |
| International Components for Unicode (ICU) | Code Libraries            | Allow easy integration into operating systems, applications, and services.                    |
| Common Locale Data Repository (CLDR)       | Structured Data           | Language-specific data for processing of dates, times, numbers, and currencies.               |
| Unicode Technical Committees (UTC)         | Properties and Algorithms | Provide character/emoji properties to ensure correct and consistent use across all platforms. |
| Unicode Technical Committees (UTC)         | Standard                  | Encoding of nearly 150,000 characters covering the world's languages and symbols.             |

## Chapter 1: Introduction

The Unicode Standard is the universal character encoding standard for written characters and text. It defines a consistent way of encoding multilingual text that enables the exchange of text data internationally.

The Unicode Standard extends the American Standard Code for Information Interchange (ASCII) character set to encode all characters for most of the world's languages - 1,114,112 characters. No escape sequence or control code is required to specify any character in any language. The alphabetic characters, ideographic characters, and symbols are treated equivalently, so they can be used in any mixture with equal facility.

The Unicode Standard specifies a numeric value (code point), name, case, directionality, and alphabetic properties of each character. These semantic values and application data, such as case mapping tables and character property tables, are defined as part of the Unicode Character Database.

Unicode characters are represented in one of three encoding forms: 32-bit form (UTF- 32), 16-bit form (UTF-16), and 8-bit form (UTF-8). The 8-bit, byte-oriented form, UTF-8, has been designed for ease of use with existing ASCII-based systems.

The Unicode Standard is code-for-code identical with International Standard ISO/IEC 10646. Therefore, any implementation conformant to Unicode is also conformant to ISO/IEC 10646. The majority of the common characters used in the major languages of the world are encoded in the first 65,536 code points, also known as the Basic Multilingual Plane (BMP). The overall capacity for more than 1 million characters is more than sufficient for all known character encoding requirements.

### Coverage

The Unicode Standard, Version 15.0, contains 149,186 characters from the world’s scripts. The standard includes the European alphabetic scripts, Middle Eastern right-to-left scripts, archaic scripts,scripts of Asia and Africa, archaic and historic, Han script. In addition, the Unicode Standard contains many important symbol sets, including currency symbols, punctuation marks, mathematical symbols, technical symbols, geometric shapes, dingbats, and emoji.

Note, however, that the Unicode Standard does not encode idiosyncratic, personal, novel,
or private-use characters, nor does it encode logos or graphics. Graphologies unrelated to
text, such as dance notations, are likewise outside the scope of the Unicode Standard. Font
variants are explicitly not encoded. The Unicode Standard reserves 6,400 code points in
the BMP for private use, which may be used to assign codes to characters not included in
the repertoire of the Unicode Standard. Another 131,068 private-use code points are avail-
able outside the BMP, should 6,400 prove insufficient for particular applications.
Standards Coverage
The Unicode Standard is a superset of all characters in widespread use today. It contains
the characters from major international and national standards as well as prominent
industry character sets. For example, Unicode incorporates the ISO/IEC 6937 and ISO/
IEC 8859 families of standards, the SGML standard ISO/IEC 8879, and bibliographic stan-
dards such as ISO 5426. Important national standards contained within Unicode include
ANSI Z39.64, KS X 1001, JIS X 0208, JIS X 0212, JIS X 0213, GB 2312, GB 18030, HKSCS,
and CNS 11643. Industry code pages and character sets from Adobe, Apple, Fujitsu, Hewl-
ett-Packard, IBM, Lotus, Microsoft, NEC, and Xerox are fully represented as well.
The Unicode Standard is fully conformant with the International Standard ISO/IEC
10646:2020, Information Technology—Universal Coded Character Set (UCS), known as the
Universal Character Set (UCS). For more information, see Appendix C, Relationship to
ISO/IEC 10646.
New Characters
The Unicode Standard continues to respond to new and changing industry demands by
encoding important new characters. As the universal character encoding, the Unicode
Standard also responds to scholarly needs. To preserve world cultural heritage, important
archaic scripts are encoded as consensus about the encoding is developed.
Introduction 4 1.2 Design Goals
1.2 Design Goals
The Unicode Standard began with a simple goal: to unify the many hundreds of conflicting
ways to encode characters, replacing them with a single, universal standard. The pre-exist-
ing legacy character encodings were both inconsistent and incomplete—two encodings
could use the same codes for two different characters and use different codes for the same
characters, while none of the encodings handled any more than a small fraction of the
world’s languages. Whenever textual data was converted between different programs or
platforms, there was a substantial risk of corruption. Programs often were written only to
support particular encodings, making development of international versions expensive. As
a result, developing countries were particularly hard-hit, as it was not economically feasible
to adapt specific versions of programs for smaller markets. Technical fields such as mathe-
matics were also disadvantaged, because they were forced to use special fonts to represent
arbitrary characters, often leading to garbled content.
The designers of the Unicode Standard envisioned a uniform method of character identifi-
cation that would be more efficient and flexible than previous encoding systems. The new
system would satisfy the needs of technical and multilingual computing and would encode
a broad range of characters for all purposes, including worldwide publication.
The Unicode Standard was designed to be:
• Universal. The repertoire must be large enough to encompass all characters
that are likely to be used in general text interchange, including those in major
international, national, and industry character sets.
• Efficient. Plain text is simple to parse: software does not have to maintain state
or look for special escape sequences, and character synchronization from any
point in a character stream is quick and unambiguous. A fixed character code
allows for efficient sorting, searching, display, and editing of text.
• Unambiguous. Any given Unicode code point always represents the same char-
acter.
Figure 1-2 demonstrates some of these features, contrasting the Unicode encoding with
mixtures of single-byte character sets with escape sequences to shift the meanings of bytes
in the ISO/IEC 2022 framework using multiple character encoding standards.

1.3 Text Handling
The assignment of characters is only a small fraction of what the Unicode Standard and its
associated specifications provide. The specifications give programmers extensive descrip-
tions and a vast amount of data about the handling of text, including how to:
• divide words and break lines
• sort text in different languages
• format numbers, dates, times, and other elements appropriate to different
locales
• display text for languages whose written form flows from right to left, such as
Arabic or Hebrew
• display text in which the written form splits, combines, and reorders, such as
for the languages of South Asia
• deal with security concerns regarding the many look-alike characters from
writing systems around the world
Without the properties, algorithms, and other specifications in the Unicode Standard and
its associated specifications, interoperability between different implementations would be
impossible. With the Unicode Standard as the foundation of text representation, all of the
text on the Web can be stored, searched, and matched with the same program code.
Characters and Glyphs
The difference between identifying a character and rendering it on screen or paper is cru-
cial to understanding the Unicode Standard’s role in text processing. The character identi-
fied by a Unicode code point is an abstract entity, such as “latin capital letter a” or
“bengali digit five”. The mark made on screen or paper, called a glyph, is a visual repre-
sentation of the character.
The Unicode Standard does not define glyph images. That is, the standard defines how
characters are interpreted, not how glyphs are rendered. Ultimately, the software or hard-
ware rendering engine of a computer is responsible for the appearance of the characters on
the screen. The Unicode Standard does not specify the precise shape, size, or orientation of
on-screen characters.
Text Elements
The successful encoding, processing, and interpretation of text requires appropriate defini-
tion of useful elements of text and the basic rules for interpreting text. The definition of text
elements often changes depending on the process that handles the text. For example, when
searching for a particular word or character written with the Latin script, one often wishes
to ignore differences of case. However, correct spelling within a document requires case
sensitivity.
Introduction 7 1.3 Text Handling
The Unicode Standard does not define what is and is not a text element in different pro-
cesses; instead, it defines elements called encoded characters. An encoded character is rep-
resented by a number from 0 to 10FFFF 16, called a code point. A text element, in turn, is
represented by a sequence of one or more encoded characters.