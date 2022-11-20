# Cascading style sheets

<!-- omit in toc -->
## Table of contents

- [Introduction](#introduction)
- [Processing model](#processing-model)
- [Definitions](#definitions)
  - [Glossary](#glossary)
- [Syntax](#syntax)
  - [Selectors list](#selectors-list)
  - [Properties list](#properties-list)
  - [Style rule](#style-rule)


## Introduction

Cascading Style Sheet (CSS) is a stylesheet language used to describe the presentation (or rendering) of a document written in HTML or XML (including XML dialects such as SVG, MathML, or XHTML).

CSS Level 3: CSS Level 3 builds on CSS Level 2 module by module, using the CSS2.1 specification as its core. Each module adds functionality and/or replaces part of the CSS2.1 specification. The CSS Working Group intends that the new CSS modules will not contradict the CSS2.1 specification: only that they will add functionality and refine definitions. As each module is completed, it will be plugged in to the existing system of CSS2.1 plus previously-completed modules.

From this level on modules are levelled independently: for example Selectors Level 4 may well be completed before CSS Line Module Level 3. Modules with no CSS Level 2 equivalent start at Level 1; modules that update features that existed in CSS Level 2 start at Level 3. CSS the language no longer has levels; "CSS Level 3" as a term is used only to differentiate it from the previous monolithic versions.

## Processing model

This section presents one possible model of how user agents that support CSS work. This is only a conceptual model; real implementations may vary.

In this model, a user agent processes a source by going through the following steps:

1. Parse the source document and create a document tree.
2. Identify the target media type.
3. Retrieve all style sheets associated with the document that are specified for the target media type.
4. Annotate every element of the document tree by assigning a single value to every property that is applicable to the target media type. Properties are assigned values according to the mechanisms described in the section on cascading and inheritance. Part of the calculation of values depends on the formatting algorithm appropriate for the target media type. For example, if the target medium is the screen, user agents apply the visual formatting model.
5. From the annotated document tree, generate a formatting structure. Often, the formatting structure closely resembles the document tree, but it may also differ significantly, notably when authors make use of pseudo-elements and generated content. First, the formatting structure need not be "tree-shaped" at all -- the nature of the structure depends on the implementation. Second, the formatting structure may contain more or less information than the document tree. For instance, if an element in the document tree has a value of 'none' for the 'display' property, that element will generate nothing in the formatting structure. A list element, on the other hand, may generate more information in the formatting structure: the list element's content and list style information (e.g., a bullet image). Note that the CSS user agent does not alter the document tree during this phase. In particular, content generated due to style sheets is not fed back to the document language processor (e.g., for reparsing).
6. Transfer the formatting structure to the target medium (e.g., print the results, display them on the screen, render them as speech, etc.). 

## Definitions

- Source document: The document to which one or more style sheets apply. This is encoded in some language that represents the document as a tree of elements. Each element consists of a name that identifies the type of element, optionally a number of attributes, and a (possibly empty) content. For example, the source document could be an XML or SGML instance.
- Document language: The encoding language of the source document (e.g., HTML, XHTML, or SVG). CSS is used to describe the presentation of document languages and CSS does not change the underlying semantics of the document languages. 
- Element: (An SGML term, see [ISO8879].) The primary syntactic constructs of the document language. Most CSS style sheet rules use the names of these elements (such as P, TABLE, and OL in HTML) to specify how the elements should be rendered. 
- Replaced element: An element whose content is outside the scope of the CSS formatting model, such as an image, embedded document, or applet. For example, the content of the HTML IMG element is often replaced by the image that its "src" attribute designates. Replaced elements often have intrinsic dimensions: an intrinsic width, an intrinsic height, and an intrinsic ratio. For example, a bitmap image has an intrinsic width and an intrinsic height specified in absolute units (from which the intrinsic ratio can obviously be determined). On the other hand, other documents may not have any intrinsic dimensions (for example, a blank HTML document). User agents may consider a replaced element to not have any intrinsic dimensions if it is believed that those dimensions could leak sensitive information to a third party. For example, if an HTML document changed intrinsic size depending on the user's bank balance, then the UA might want to act as if that resource had no intrinsic dimensions. The content of replaced elements is not considered in the CSS rendering model. 
- Intrinsic dimensions: The width and height as defined by the element itself, not imposed by the surroundings. CSS does not define how the intrinsic dimensions are found. In CSS 2.1 only replaced elements can come with intrinsic dimensions. For raster images without reliable resolution information, a size of 1 px unit per image source pixel must be assumed. 
- Attribute: A value associated with an element, consisting of a name, and an associated (textual) value. 
- Content: The content associated with an element in the source document. Some elements have no content, in which case they are called empty. The content of an element may include text, and it may include a number of sub-elements, in which case the element is called the parent of those sub-elements. 
- Ignore: This term has two slightly different meanings in this specification. First, a CSS parser must follow certain rules when it discovers unknown or illegal syntax in a style sheet. The parser must then ignore certain parts of the style sheets. The exact rules for which parts must be ignored are described in these sections (Declarations and properties, Rules for handling parsing errors, Unsupported Values) or may be explained in the text where the term "ignore" appears. Second, a user agent may (and, in some cases must) disregard certain properties or values in the style sheet, even if the syntax is legal. For example, table-column elements cannot affect the font of the column, so the font properties must be ignored. 
- Rendered content: The content of an element after the rendering that applies to it according to the relevant style sheets has been applied. How a replaced element's content is rendered is not defined by this specification. Rendered content may also be alternate text for an element (e.g., the value of the XHTML "alt" attribute), and may include items inserted implicitly or explicitly by the style sheet, such as bullets, numbering, etc. 
- Document tree: The tree of elements encoded in the source document. Each element in this tree has exactly one parent, with the exception of the root element, which has none. 
- Child: An element A is called the child of element B if and only if B is the parent of A. 
- Descendant: An element A is called a descendant of an element B, if either (1) A is a child of B, or (2) A is the child of some element C that is a descendant of B. 
- Ancestor: An element A is called an ancestor of an element B, if and only if B is a descendant of A. 
- Sibling: An element A is called a sibling of an element B, if and only if B and A share the same parent element. Element A is a preceding sibling if it comes before B in the document tree. Element B is a following sibling if it comes after A in the document tree. 
- Preceding element: An element A is called a preceding element of an element B, if and only if (1) A is an ancestor of B or (2) A is a preceding sibling of B. 
- Following element: An element A is called a following element of an element B, if and only if B is a preceding element of A. 
- Author: An author is a person who writes documents and associated style sheets. An authoring tool is a User Agent that generates style sheets.
- User: A user is a person who interacts with a user agent to view, hear, or otherwise use a document and its associated style sheet. The user may provide a personal style sheet that encodes personal preferences. 
- User Agent (UA): A user agent is any program that interprets a document written in the document language and applies associated style sheets according to the terms of this specification. A user agent may display a document, read it aloud, cause it to be printed, convert it to another format, etc. An HTML user agent is one that supports one or more of the HTML specifications. A user agent that supports XHTML [XHTML], but not HTML is not considered an HTML user agent for the purpose of conformance with this specification. 
- Property: CSS defines a finite set of parameters, called properties, that direct the rendering of a document. Each property has a name (e.g., 'color', 'font', or border') and a value (e.g., 'red', '12pt Times', or 'dotted'). Properties are attached to various parts of the document and to the page on which the document is to be displayed by the mechanisms of specificity, cascading, and inheritance (see the chapter on Assigning property values, Cascading, and Inheritance). 

### Glossary

| Term                  | Definition                                                                                                             | Note                                                                                                                       |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Property**          | A human-readable identifier that defines which presentational feature is considered.                                   | Both properties and values are case-insensitive.                                                                           |
| **Value**             | An expression that described how the feature must be handled by the CSS engine.                                        | If a value is not valid for its associated property, the entire declaration is invalid.                                    |
| **Declaration**       | A property and value pair separated by a colon (`:`).                                                                  | White spaces around declarations are ignored.                                                                              |
| **Declaration block** | A structure containing a group of declarations delimited by an opening brace (`{`) and a closing brace (`}`).          | It is good style to terminate the last declaration with a semicolon.                                                       |
| **Ruleset**           | A comma-separated selector group followed by an associated declaration block.                                          | If any single selector in a selectors group is invalid, the entire selector, and therefore the entire ruleset, is invalid. |
| **Statement**         | A structure that begins with any non-space character and ends at the first closing brace (`}`) or semicolon (`;`).     | Any statement which is not a ruleset or an at-rule is invalid and ignored.                                                 |
| **At-rule**           | Rules that start with an _at_ sign (`@`) followed by an identifier and then continuing up to the end of the statement. | Each type of at-rules, defined by its identifier, may have its own internal syntax and semantics.                          |


## Syntax

### Selectors list

```css
selectors-list ::=
  selector[:pseudo-class] [::pseudo-element]
  [, selectors-list]
```

### Properties list

```css
properties-list ::=
  [property: value]
  [; properties-list]
```

### Style rule

```css
style-rule ::=
  selectors-list {
    properties-list
  }
```
