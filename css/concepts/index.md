# Cascading style sheets

<!-- omit in toc -->
## Table of contents

- [Introduction](#introduction)
  - [Processing model](#processing-model)
- [Syntax](#syntax)
  - [Rulesets](#rulesets)
  - [At-rules](#at-rules)
- [Adding CSS](#adding-css)
  - [Inline styles](#inline-styles)
  - [Internal style sheet](#internal-style-sheet)
  - [External style sheet](#external-style-sheet)
- [Selectors](#selectors)
- [Appendix](#appendix)
  - [Glossary](#glossary)

<!-- general information about CSS that does not fall into any subcategory -->
## Introduction

Cascading Style Sheet (CSS) is a style sheet language used to describe the presentation of a document written in HTML or XML, including XML dialects such as SVG, MathML, or XHTML.

CSS Level 3 builds on CSS Level 2 Revision 1 module by module, using the CSS 2.1 specification as its core. Each module adds functionality and/or replaces part of the CSS 2.1 specification. From this level on modules are levelled independently. Modules with no CSS Level 2 equivalent start at Level 1 and modules that update features that existed in CSS Level 2 start at Level 3. CSS specification, itself, no longer has levels, therefore, "CSS Level 3" as a term is used only to differentiate it from the previous monolithic versions.

### Processing model

This section presents one possible model of how user agents that support CSS work. This is only a conceptual model and real implementations may vary. In this model, a user agent processes a source by going through the following steps:

1. Parse the source document and create a document tree.
2. Identify the target media type.
3. Retrieve all style sheets associated with the document that are specified for the target media type.
4. Annotate every element of the document tree by assigning a single value to every property based on cascading and inheritance.
5. From the annotated document tree, generate a formatting structure.).
6. Transfer the formatting structure to the target medium for rendering. 

<!-- Syntactical constructs for rulesets and at-rules with general validation information -->
## Syntax

The primary construct in a style sheet is a statement. A statement begins with any non-space character and ends at the first closing brace or semicolon that is encountered non-escaped, outside a string, and not nested into another brace pair. There are two categories of statements in style sheets:

- **Rulesets:** A structure that associates a comma-separated selectors list with a declaration block.
- **At-rules:** A structure that starts with an _at_ symbol, followed by an identifier, and continues up to the end of the statement.

Any statement which is not a ruleset or an at-rule is invalid and ignored.

### Rulesets

The ruleset (or rule) is a structure formed by adding a declarations list, enclosed within curly braces, after a selectors list.

```css
style-rule ::=
  selectors-list {
    declarations-list
  }
```

The selectors list is one ore more selectors separated by comma. Whitespaces before and after selectors are ignored, however whitespace between simple selectors in a compound selector has semantic meaning. Selectors syntax is case-insensitive within the ASCII range. If any single selector in a selectors list is invalid, the entire selectors list, and therefore the ruleset itself, is invalid.

```css
selectors-list ::=
  selector[:pseudo-class] [::pseudo-element]
  [, selectors-list]
```

The declarations list is one or more declarations - which are pairs of properties and values - separated by semicolons. The last declaration is not required to be terminated by a semicolon, though it is good practice to do it. Whitespaces before, between, and after properties and values are ignored. Both properties and values are case-insensitive. If a value is not valid for its associated property, the entire declaration is invalid.

```css
declarations-list ::=
  [property: value]
  [; declarations-list]
```

<!-- TODO: Add introduction and syntax information -->
### At-rules

Each type of at-rule, defined by its identifier, may have its own internal syntax and semantics.

## Adding CSS

A style sheet is used to describe the presentation of a document written in a supported markup language. For the styling to take effect, the source document must either contain or link to the style sheet. In HTML, there are three methods to add a style sheet:

- **Inline styles:** Applied by using the `style` attribute of an HTML element.
- **Internal style sheet:** Applied by using the `<style>` element in the `<head>` element.
- **External style sheet:** Applied by using the `<link>` element to link to an external CSS file.

### Inline styles

Inline styles are applied to a particular HTML element by providing a semicolon separated list of declarations inside its `style` attribute. Quotation marks can be used by escaping them as `&quot;`. However, avoid adding CSS through this method, unless the working environment is very restrictive. It is the least efficient method in terms of maintenance, and it mixes the presentation with the content.

```html
<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="utf-8">
    <title>Inline Styles</title>
  </head>
    <body>
      <p style="
        color: red;
        font-weight: bold;
        font-size: 24px;
        font-family: &quot;Open Sans&quot;">PARAGRAPH TEXT</p>
    </body>
</html>
```

### Internal style sheet

Internal style sheet resides within the source document, as content of the `<style>` element contained within the `<head>` of the document. The content of an internal style sheet is identical to an external style sheet. Internal style sheet, however, is an inefficient method for adding consistent styling to a website of more than one page.

```html
<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="utf-8">
    <title>Internal Style Sheet</title>
    <style>
      p {
        color: red;
        font-weight: bold;
        font-size: 24px;
        font-family: "Open Sans";
      }
    </style>
  </head>
    <body>
      <p>PARAGRAPH TEXT</p>
    </body>
</html>
```

### External style sheet

External style sheet is a file with a `.css` file extension, linked through the `<link>` element. The `href` attribute of the `<link>` element contains the path to the file, and the `ref` attribute must be provided the `stylesheet` value. The `type` attribute should not be provided if the style sheet has `text/css` type, because user agents already assume this as the default value. This is the recommended method of adding CSS to an HTML document, as a single style sheet can be referenced from multiple source documents, and the presentation is cleanly separated from the content.

```html
<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="utf-8">
    <title>External Style Sheet</title>
    <link rel="stylesheet" href="style.css">
  </head>
    <body>
      <p>PARAGRAPH TEXT</p>
    </body>
</html>
```

```css
p {
  color: red;
  font-weight: bold;
  font-size: 24px;
  font-family: "Open Sans";
}
```

## Selectors

A selector represents a structure used as a condition to select a set of elements or a single element in the document tree. In rulesets, selectors are used for binding style declarations to elements in the source document. The elements selected by a selector are called the *subjects of the selector*. 

## Appendix

### Glossary

Source document
 : The document to which one or more style sheets apply. This is encoded in some markup language that represents the document as a tree of elements.

Document language
 : The encoding language of the source document, such as HTML, XHTML, or SVG.

Element
 : The primary syntactic constructs of the document language.

Replaced element
 : An element whose content is outside the scope of the CSS formatting model, such as an image, embedded document, or applet.

Intrinsic dimensions
 : The width and height as defined by the element itself, not imposed by the surroundings.

Attribute
 : A value associated with an element, consisting of a name, and an associated textual value. 

Content
 : The content associated with an element in the source document. Some elements have no content, in which case they are called empty. The content of an element may include text, and it may include a number of sub-elements, in which case the element is called the parent of those sub-elements. 

Rendered content
 : The content of an element after the rendering has been applied.

Document tree
 : The tree of elements encoded in the source document. Each element in this tree has exactly one parent, with the exception of the root element, which has none.

Child
 : An element A is called the child of element B if and only if B is the parent of A.

Descendant
 : An element A is called a descendant of an element B, if either A is a child of B, or A is the child of some element C that is a descendant of B.

Ancestor
 : An element A is called an ancestor of an element B, if and only if B is a descendant of A.

Sibling
 : An element A is called a sibling of an element B, if and only if B and A share the same parent element. Element A is a preceding sibling if it comes before B in the document tree. Element B is a following sibling if it comes after A in the document tree.

Preceding element
 : An element A is called a preceding element of an element B, if and only if A is an ancestor of B or A is a preceding sibling of B.

Following element
 : An element A is called a following element of an element B, if and only if B is a preceding element of A.

Author
 : An author is a person who writes documents and associated style sheets. An authoring tool is a user agent that generates style sheets.

User
 : A user is a person who interacts with a user agent to view, hear, or otherwise use a document and its associated style sheet. The user may provide a personal style sheet that encodes personal preferences.

User agent (UA)
 : A user agent is any program that interprets a document written in the document language and applies associated style sheets. A user agent may display a document, read it aloud, cause it to be printed, or convert it to another format.

Property
 : A human-readable identifier that defines a presentational feature to be considered.

Value
 : An expression that describes how the presentational feature, defined by the associated property, must be handled.

Declaration
 : A property and value pair separated by a colon, that together controls a presentational feature.

Declaration block
 : A structure containing a list of declarations separated by semicolons and delimited by an opening brace and a closing brace.

Ruleset
 : A structure that associates a comma-separated selectors list with a declaration block.

Statement
 : A structure that begins with any non-space character and ends at the first closing brace or semicolon.

At-rule
 : A structure that starts with an _at_ symbol, followed by an identifier, and continues up to the end of the statement.
