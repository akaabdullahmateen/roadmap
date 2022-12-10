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
  - [Basic selectors](#basic-selectors)
  - [Combinators](#combinators)
  - [Attribute selectors](#attribute-selectors)
  - [Pseudo-elements](#pseudo-elements)
  - [Pseudo-classes](#pseudo-classes)
- [Cascade, Specificity, Importance, and Inheritance](#cascade-specificity-importance-and-inheritance)
  - [Cascade](#cascade)
- [Origin types](#origin-types)
  - [User-agent stylesheets](#user-agent-stylesheets)
  - [Author stylesheets](#author-stylesheets)
  - [User stylesheets](#user-stylesheets)
  - [Cascade layers](#cascade-layers)
- [Cascading order](#cascading-order)
- [Basic example](#basic-example)
- [Author styles: inline styles, layers, and precedence](#author-styles-inline-styles-layers-and-precedence)
  - [Inline styles](#inline-styles-1)
  - [Importance and layers](#importance-and-layers)
- [Complete cascade order](#complete-cascade-order)
- [Which CSS entities participate in the cascade](#which-css-entities-participate-in-the-cascade)
- [CSS animations and the cascade](#css-animations-and-the-cascade)
- [Resetting styles](#resetting-styles)
  - [Specificity](#specificity)
- [Appendix](#appendix)
  - [Style guide / Lint](#style-guide--lint)
  - [Pseudo-elements](#pseudo-elements-1)
  - [Pseudo-classes](#pseudo-classes-1)
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

Any statement which is not a ruleset or an at-rule is invalid and ignored. CSS ignores whitespaces around comma in a selectors list, and around properties and values. CSS is case-insensitive within the ASCII range, except for parts that are not under its control.

### Rulesets

The ruleset (or rule) is a structure formed by adding a declarations list, enclosed within curly braces, after a selectors list.

```css
style-rule ::=
  selectors-list {
    declarations-list
  }
```

The selectors list is a comma-separated list of selectors, which selects nodes that matches with any single selector in the list. If any single selector in a selectors list is invalid or unsupported, the entire selectors list is considered invalid, and therefore the associated ruleset is ignored.

```css
selectors-list ::=
  selector[:pseudo-class] [::pseudo-element]
  [, selectors-list]
```

The declarations list is a semicolon-separated list of declarations - which are pairs of properties and values. The last declaration is not required to be terminated by a semicolon. If any invalid value is passed to a property, that accepts multiple values, the entire declaration is ignored.

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

A selector defines a pattern to select a set of elements or a single element in the document tree. In rulesets, selectors are used for binding style declarations to elements in the source document. The elements selected by a selector are called the *subjects of the selector*. 

### Basic selectors

A basic selector matches elements based on their tag name, class name, or ID name. A universal selector exists that matches all elements. Optionally, the universal selector can be restricted to a specific namespace or to all namespaces.

| Name               | Syntax             | Target                                       |
| ------------------ | ------------------ | -------------------------------------------- |
| Type selector      | `tag`              | Elements with the specified tag name.        |
| Class selector     | `.class`           | Elements with the specified class attribute. |
| ID selector        | `#id`              | Elements with the specified id attribute.    |
| Universal selector | `*`, `ns|*`, `*|*` | All elements.                                |

### Combinators

A combinator matches elements based on their relationship with another selected element. There are no combinators to select parent elements, siblings of parents, or children of parent siblings.

| Name                        | Syntax  | Target                                               |
| --------------------------- | ------- | ---------------------------------------------------- |
| Descendant combinator       | `A B`   | Descendants of the first element.                    |
| Child combinator            | `A > B` | Direct children of the first element.                |
| General sibling combinator  | `A ~ B` | Following siblings of the first element.             |
| Adjacent sibling combinator | `A + B` | Immediately following siblings of the first element. |

### Attribute selectors

An attribute selector matches elements based on the presence of a specified attribute and conditions for its associated value. By default, the values are tested case-sensitively, however, the addition of the character `i` or `I` before the closing bracket causes the value to be tested case-insensitively.

| Name                           | Syntax            | Attribute value                                                               |
| ------------------------------ | ----------------- | ----------------------------------------------------------------------------- |
| General attribute selector     | `[attr]`          | Any value to the specified attribute.                                         |
| Exact attribute selector       | `[attr="value"]`  | Value exactly matches the specified string.                                   |
| Starts-with attribute selector | `[attr^="value"]` | Value starts with the specified string.                                       |
| Ends-with attribute selector   | `[attr$="value"]` | Value ends with the specified string.                                         |
| Contains attribute selector    | `[attr*="value"]` | Value contains the specified string.                                          |
| List attribute selector        | `[attr~="value"]` | Value is a space-separated list, one of which matches the specified string.   |
| Hyphenated attribute selector  | `[attr|="value"]` | Value either matches, or starts with and is immediately followed by a hyphen. |

### Pseudo-elements

A [pseudo-element](#pseudo-elements-1) is a keyword added to a selector that described a specific part of the selected element. A pseudo-element consists of double colons followed by the pseudo-element identifier. Although, most browsers also support the single colon syntax for pseudo-elements, it is recommended to use the double colons syntax for pseudo-elements, to distinguish them from pseudo-classes. A selector can contain at most one pseudo-element, and it must appear after any other syntax in the selector.

### Pseudo-classes

A [pseudo-class](#pseudo-classes-1) is a keyword added to a selector that describes a specific state of the selected element. A pseudo-class consists of a colon followed by the pseudo-class identifier. A functional pseudo-class is additionally followed by a pair of parenthesis which enclose the arguments. The element that a pseudo-class is attached to is called the *anchor element*.

The functional pseudo-classes (`:is()`, `:has()`, and `:where()`) accept a forgiving selector list, where incorrect or unsupported selectors are simply ignored, rather than invalidating the whole selector list. The selector list can not contain the functional pseudo-class itself and any pseudo-elements. The specificity of a functional pseudo-class is replaced by the specificity of the most specific selector in its argument selector list.

The functional pseudo-classes (`:nth-child()`, `:nth-last-child()`, `:nth-of-type()`, and `nth-last-of-type()`) take a single argument of the form `A * n + B`, where `A` is the integer step size, `B` is the integer offset, and `n` is the domain of all non-negative integers, starting from `0`. Two keywords exist as an argument, that are `odd` and `even`, which match elements at either odd positions or even positions. A single integer can be also be used as an argument, which selects only the element at that specified position.

Styles defined by a link-related pseudo-class are overridden by any subsequent link-related pseudo-class, that has at least equal specificity. To style links appropriately, follow the *LVHA-order*, which is `:link` then `:visited` then `:hover` and finally `:active`.

## Cascade, Specificity, Importance, and Inheritance

1. Specificity only applies when the same element is targeted by multiple declarations in the same cascade layer or origin. Specificity only matters for declarations of the same importance and same origin and cascade layer. If matching selectors are in different origins, the cascade determines which declaration takes precedence.

2. When two selectors in the same cascade layer and origin have the same specificity, proximity is important; the last selector wins.

3. As per CSS rules, directly targeted elements will always take precedence over rules which an element inherits from its ancestor, regardless of the specificity of the inherited rule.

4. Proximity of elements in the document tree has no effect on the specificity.

### Cascade

The cascade is an algorithm that defines how user agents combine property values originating from different sources. The cascade defines the origin and layer that takes precedence when declarations in more than one origin or cascade layer set a value for a property on an element.

The cascade lies at the core of CSS, as emphasized by the name: _**Cascading** Style Sheets_. When a selector matches an element, the property value from the origin with the highest precedence gets applied, even if the selector from a lower precedence origin or layer has greater specificity.

This article explains what the cascade is and the order in which declarations cascade, covering cascade layers and origin type. Understanding origin precedence is key to understanding the cascade.

## Origin types

The CSS cascade algorithm's job is to select CSS declarations in order to determine the correct values for CSS properties. CSS declarations come from different origin types: **User-agent stylesheets**, **Author stylesheets**, and **User stylesheets**.

Though style sheets come from these different origins and can be within different layers in each of these origins, they overlap in scope; to make this work, the cascade algorithm defines how they interact. Before addressing the interactions, let's define some terms:

### User-agent stylesheets

User-agent, or browsers, have basic style sheets that give default styles to any document. These style sheets are named **user-agent stylesheets**. Most browsers use actual stylesheets for this purpose, while others simulate them in code. The end result is the same.

Some browsers let users modify the user-agent stylesheet, but this is rare and not something that can be controlled.

Although some constraints on user-agent stylesheets are set by the HTML specification, browsers have a lot of latitude: that means some differences exist between browsers. To simplify the development process, Web developers may use a CSS reset stylesheet, such as _normalize.css_, which sets common properties values to a known state for all browsers before beginning to make alterations to suit their specific needs.

Unless the user-agent stylesheet includes an `!important` next to a property, styles declared by author stylesheets, including a reset stylesheet, take precedence over the user-agent styles, regardless of the specificity of the associated selector.

### Author stylesheets

**Author stylesheets** are the most common type of style sheet; these are the styles written by web developers. These styles can reset user-agent styles, as noted above, and define the styles for the design of a given web page or application. The author, or web developer, defines the styles for the document using one or more linked or imported stylesheets, `<style>` blocks, and inline styles defined with the `style` attribute. These author styles define the look and feel of the website — its theme.

### User stylesheets

In most browsers, the user (or reader) of the web site can choose to override styles using a custom **user stylesheet** designed to tailor the experience to the user's wishes. Depending on the user agent, user styles can be configured directly or added via browser extensions.

### Cascade layers

The cascade order is based on origin type. The cascade within each origin type is based on the declaration order of cascade layers within that type. For all origins - user-agent, author, or user - styles can be declared within or outside of named or anonymous layers. When declared using `layer`, `layer()` or `@layer`, styles are placed into the specified named layer, or into an anonymous layer if no name is provided. Styles declared outside of a layer are treated as being part of an anonymous last declared layer.

Let's take a look at cascading origin type before diving into cascade layers within each origin type.

## Cascading order

The cascading algorithm determines how to find the value to apply for each property for each document element. The following steps apply to the cascading algorithm:

1. **Relevance**: It first filters all the rules from the different sources to keep only the rules that apply to a given element. That means rules whose selector matches the given element and which are part of an appropriate `media` at-rule.

2. **Origin and importance**: Then it sorts these rules according to their importance, that is, whether or not they are followed by `!important`, and by their origin. Ignoring layers for the moment, the cascade order is as follows:

   | Order (low to high) | Origin                       | Importance   |
   | ------------------- | ---------------------------- | ------------ |
   | 1                   | **user-agent** (browser)     | normal       |
   | 2                   | **user**                     | normal       |
   | 3                   | **author** (developer)       | normal       |
   | 4                   | CSS `@keyframe` animations   |              |
   | 5                   | **author** (developer)       | `!important` |
   | 6                   | **user**                     | `!important` |
   | 7                   | **user-agent** (browser)     | `!important` |
   | 8                   | CSS transitions              |              |

3. **Specificity:** In case of equality with an origin, the specificity of a rule is considered to choose one value or another. The specificity of the selectors are compared, and the declaration with the highest specificity wins.

4. **Order of appearance**: In the origin with precedence, if there are competing values for a property that are in style block matching selectors of equal specificity, the last declaration in the style order is applied.

The cascade is in ascending order, meaning animations have precedence of normal values, whether those are declared in user, author, or user-agent styles, important values take precedence over animations, and transitions have precedence over important values.

> **Note:** **Transitions and animations**
>
> Property values set by animation `@keyframes` are more important than all normal styles (those with no `!important` flag set).
>
> Property values set in a `transition` take precedence over all other values set, even those marked with `!important` flag.

The cascade algorithm is applied _before_ the specificity algorithm, meaning if `:root p { color: red;}` is declared in the user stylesheet (line 2) and a less specific `p {color: blue;}` is in the author stylesheet (line 3), the paragraphs will be blue.

## Basic example

Before taking a deeper look at how cascade layers impact the cascade, let's look at an example involving multiple sources of CSS across the various origins, and work through the steps of the cascade algorithm:

Here we have a user agent style sheet, two author style sheets, a user stylesheet, and inline styles within the HTML:

**User-agent CSS:**

```css
li {
  margin-left: 10px;
}
```

**Author CSS 1:**

```css
li {
  margin-left: 0;
} /* This is a reset */
```

**Author CSS 2:**

```css
@media screen {
  li {](#cascading_order
    margin-left: 3px;
  }
}

@media print {
  li {
    margin-left: 1px;
  }
}

@layer namedLayer {
  li {
    margin-left: 5px;
  }
}
```

**User CSS:**

```css
.specific {
  margin-left: 1em;
}
```

**HTML:**

```html
<ul>
  <li class="specific">1<sup>st</sup></li>
  <li>2<sup>nd</sup></li>
</ul>
```

In this case, declarations inside `li` and `.specific` rules should apply.

Once again, there are four steps in the cascade algorithm, in order:

1. Relevance
2. Origin and importance
3. Specificity
4. Order of appearance

The `1px` is for print media. Due to lack of _relevance_ based on its media type, it is removed from consideration.

No declaration is marked as `!important`, so the precedence order is author style sheets over user style sheets over user-agent stylesheet. Based on _origin and importance_, the `1em` from the user stylesheet and the `10px` from the user-agent stylesheet are removed from consideration.

Note that even though the user style on `.specific` of `1em` has a higher specificity, it's a normal declaration in a user style sheet. As such, it has a lower precedence than any author styles, and gets removed by the origin and importance step of the algorithm before specificity even comes into play.

There are three declarations in author stylesheets:

```css
li {
  margin-left: 0;
} /* from author css 1 */
```

```css
@media screen {
  li {
    margin-left: 3px;
  }
}
```

```css
@layer namedLayer {
  li {
    margin-left: 5px;
  }
}
```

The last one, the `5px` is part of a cascade layer. Normal declarations in layers have lower precedence than normal styles not in a layer within the same origin type. This is also removed by step 2 of the algorithm, _origin and importance_.

This leaves the `0` and the `3px`, which both have the same selector, hence the same _specificity_.

We then look at _order of appearance_. The second one, the last of the two unlayered author styles, wins:

```css
@media screen {
  li {
    margin-left: 3px;
  }
}
```

> **Note:** The declaration defined in the user CSS, while it may have greater specificity, is not chosen as the cascade algorithm's _origin and importance_ is applied before the _specificity_ algorithm. The declaration defined in a cascade layer, though it may come later in the code, will not have precedence either, as normal styles in cascade layers have less precedence than normal unlayered styles. _Order of appearance_ only matters when both origin, importance, and specificity are equal.

## Author styles: inline styles, layers, and precedence

The table in _Cascading order_ provided a precedence order overview, summarizing the user-agent, user, and author origin type styles in two lines each with "origin type - normal" and "origin type - !important". The precedence within each origin type is more nuanced. Styles can be contained within layers within their origin type, and, with author styles, there is also the issue of where inline styles land in the cascade order.

The order in which layers are declared is important in determining precedence. Normal styles in a layer take precedence over styles declared in prior layers; with normal styles declared outside of any layer taking precedence over normal layered styles regardless of specificity.

In this example, the author used CSS `@import` rule to import five external stylesheets within an HTML `<style>` element.

```html
<style>
  @import unlayeredStyles.css;
  @import AStyles.css layer(A);
  @import moreUnlayeredStyles.css;
  @import BStyles.css layer(B);
  @import CStyles.css layer(C);
  p {
    color: red;
    padding: 1em !important;
  }
</style>
```

and then in the body of the document we have inline styles:

```html
<p style="line-height: 1.6em; text-decoration: overline !important;">Hello</p>
```

In the CSS code block above, three cascade layers named "_A_", "_B_", and "_C_", were created, in that order. Three stylesheets were imported directly into layers and two were imported without creating or being assigned to a layer.
The "_All unlayered styles_" in the list below (normal author style precedence - order 4) includes styles from these two stylesheets and the additional unlayered CSS style blocks. In addition, there are two inline styles, a normal `line-height` declaration and an important `text-decoration` declaration:

| Order (low to high) | Author style         | Importance   |
| ------------------- | -------------------- | ------------ |
| 1                   | A - first layer      | normal       |
| 2                   | B - second layer     | normal       |
| 3                   | C - last layer       | normal       |
| 4                   | All unlayered styles | normal       |
| 5                   | inline `style`       | normal       |
| 6                   | animations           |              |
| 7                   | All unlayered styles | `!important` |
| 8                   | C - last layer       | `!important` |
| 9                   | B - second layer     | `!important` |
| 10                  | A - first layer      | `!important` |
| 11                  | inline `style`       | `!important` |
| 12                  | transitions          |              |

In all origin types, the non-important styles contained in layers have the lowest precedence. In our example, the normal styles associated with the first declared layer (A) have lower precedence than normal styles in the second declared layer (B), which have lower precedence than normal styles in the third declared layer (C). These layered styles have lower precedence than all normal unlayered styles, which includes normal styles from `unlayeredStyles.css`, `moreUnlayeredStyles.css`, and the `color` of `p` in the `<style>` itself.

If any of the layered styles in A, B, or C, have selectors with higher specificity matching an element, similar to `:root body p { color: black;}`, it doesn't matter. Those declarations are removed from consideration because of _origin_; normal layered styles have less precedence than normal unlayered styles. If, however, the more specific selector `:root body p { color: black;}` was found in `unlayeredStyles.css`, as both _origin and importance_ have the same precedence, _specificity_ would mean the more specific, black declaration would win.

The layer order of precedence is inverted for styles declared as `!important`. Important styles declared in a layer take precedence over important styles declared outside of a layer. Important styles in the first declared layer (A) take precedence over important declarations found in layer B, which takes precedence over C, which have precedence over important declarations in the unlayered styles.

### Inline styles

Only relevant to author styles are inline styles, declared with the `style` attribute. Normal inline styles take precedence over any other normal author styles, no matter the specificity of the selector. If `line-height: 2;` were declared in a `:root body p` selector block in any of the five imported stylesheets, the line height would still be `1.6`.

Normal inline styles take precedence over any other normal author styles unless the property is being altered by a CSS animation.

All important inline styles take precedence over all author styles, important and not, inline and not, layered and not. Important styles also take precedence over animated properties, but not transitioning properties. Three things can override an important inline style: 1) an important user style, 2) an important user agent style, or 3) a property value being transitioned.

### Importance and layers

The origin type precedence order is inverted for important styles. Important styles declared outside of any cascade layer have lower precedence than those declared as part of a layer. Important values that come in early layers have precedence over important styles declared in subsequent cascade layers.

Take for example the following CSS:

```css
p {
  color: red;
}
@layer B {
  :root p {
    color: blue;
  }
}
```

Even though the red is declared first and has a less specific selector, because unlayered CSS takes precedence over layered CSS, the paragraph will be red. Had we included an inline style on the paragraph setting it to a different color, such as `<p style="color: black">`, the paragraph would be black.

When we add `!important` to this bit of CSS, the precedence order is reversed with the stylesheet:

```css
p {
  color: red !important;
}
@layer B {
  :root p {
    color: blue !important;
  }
}
```

Now the paragraph will be blue. The `!important` in the earliest declared layer takes precedence of subsequent layers and unlayered important declarations. If the inline style contained `!important`, such as `<p style="color: black !important">`, again the paragraph would be black. Inline importance does take precedence over all other author declared `!important` declarations, no matter the specificity.

> **Note:** `!important` reverses the precedence of cascade layers. For this reason, rather than using `!important` to override external styles, import frameworks, third party styles, widget stylesheets, etc., into layers, demoting their precedence. `!important` should only be used sparingly, if ever, to guard required styles against later overrides, in the first declared layer.

Styles that are transitioning take precedence over all important styles, no matter who or how they are declared.

## Complete cascade order

Now that we have a better understanding of origin type and cascade layer precedence, we realize the table in _Cascading order_ could have more accurately been represented by the following table:

<table>
  <thead>
    <tr>
      <th>Precedence Order <br/>(low to high)</th>
      <th>Style Origin</th>
      <th>Importance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">1</td>
      <td>user-agent - first declared layer</td>
      <td rowspan="3">normal</td>
    </tr>
    <tr>
      <td>user-agent - last declared layer</td>
    </tr>
    <tr>
      <td>user-agent - unlayered styles</td>
    </tr>
    <tr>
      <td rowspan="3">2</td>
      <td>user - first declared layer</td>
      <td rowspan="3">normal</td>
    </tr>
    <tr>
      <td>user - last declared layer</td>
    </tr>
    <tr>
      <td>user - unlayered styles</td>
    </tr>
    <tr>
      <td rowspan="4">3</td>
      <td>author - first declared layer</td>
      <td rowspan="4">normal</td>
    </tr>
    <tr>
      <td>author - last declared layer</td>
    </tr>
    <tr>
      <td>author - unlayered styles</td>
    </tr>
    <tr>
      <td>inline <code>style</code></td>
    </tr>
    <tr>
      <td>4</td>
      <td>animations</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">5</td>
      <td>author - unlayered styles</td>
      <td rowspan="4"><code>!important</code></td>
    </tr>
    <tr>
      <td>author - last declared layer</td>
    </tr>
    <tr>
      <td>author - first declared layer</td>
    </tr>
    <tr>
      <td>inline <code>style</code></td>
    </tr>
    <tr>
      <td rowspan="3">6</td>
      <td>user - unlayered styles</td>
      <td rowspan="3"><code>!important</td>
    </tr>
    <tr>
      <td>user - last declared layer</td>
    </tr>
    <tr>
      <td>user - first declared layer</td>
    </tr>
    <tr>
      <td rowspan="3">7</td>
      <td>user-agent - unlayered styles</td>
      <td rowspan="3"><code>!important</code></td>
    </tr>
    <tr>
      <td>user-agent - last declared layer</td>
    </tr>
    <tr>
      <td>user-agent - first declared layer</td>
    </tr>
    <tr>
      <td>8</td>
      <td>transitions</td>
      <td></td>
    </tr>
  </tbody>
</table>

## Which CSS entities participate in the cascade

Only CSS property / value pair declarations participate in the cascade. This means that at-rules containing entities other than declarations, such as a `@font-face` rule containing _descriptors_, don't participate in the cascade.

For the most part, the properties and descriptors defined in at-rules don't participate in the cascade. Only at-rules as a whole participate in the cascade. For example, within a `@font-face` rule, font names are identified by `font-family` descriptors. If several `@font-face` rules with the same descriptor are defined, only the most appropriate `@font-face`, as a whole, is considered. If more than one are identically appropriate, the entire `@font-face` declarations are compared using steps 1, 2, and 4 of the algorithm (there is no specificity when it comes to at-rules).

While the declarations contained in most at-rules — such as those in `@media`, `@document`, or `@supports` — participate in the cascade, the at-rule may make an entire selector not relevant, as we saw with the print style in the basic example.

Declarations in `@keyframes` don't participate in the cascade. As with `@font-face`, only the `@keyframes` as a whole is selected via the cascade algorithm. The precedence order of animation is described below.

When it comes to `@import`, the `@import` doesn't participate itself in the cascade, but all of the imported styles do participate. If the `@import` defines a named or anonymous layer, the contents of the imported stylesheet are placed into the specified layer. All other CSS imported with `@import` is, which is treated as the last declared layer.

Finally, `@charset` obeys specific algorithms and isn't affected by the cascade algorithm.

## CSS animations and the cascade

CSS animations, using `@keyframes` at-rules, define animations between states. Keyframes don't cascade, meaning that at any given time CSS takes values from only one single `@keyframes`, and never mixes multiple ones together.

If the several keyframe animations are defined with the same animation name, the last defined `@keyframes` in the origin and layer with the greatest precedence. Only one `@keyframes` definition is used, even if the `@keyframes` animate different property. `@keyframes` with the same name are never combined.

```css
p {
  animation: infinite 5s alternate repeatedName;
}
@keyframes repeatedName {
  from {
    font-size: 1rem;
  }
  to {
    font-size: 3rem;
  }
}

@layer A {
  @keyframes repeatedName {
    from {
      background-color: yellow;
    }
    to {
      background-color: orange;
    }
  }
}
@layer B {
  @keyframes repeatedName {
    from {
      color: white;
    }
    to {
      color: black;
    }
  }
}
```

In this example, there are three separate animation declaration named `repeatedName`. When `animation: infinite 5s alternate repeatedName` is applied to the paragraph, only one animation is applied: the keyframe animation defined in the unlayered CSS takes precedence over the layered keyframe animation declarations based on origin and cascade layer precedence order. In this example, only the element's font size will be animated.

> **Note:** There are no important animations. The property declarations in a `@keyframes` block that contain `!important` as part of the value are ignored.

## Resetting styles

After your content has finished altering styles, it may find itself in a situation where it needs to restore them to a known state. This may happen in cases of animations, theme changes, and so forth. The CSS property `all` lets you quickly set (almost) everything in CSS back to a known state.

`all` lets you opt to immediately restore all properties to any of their initial (default) state, the state inherited from the previous level of the cascade, a specific origin (the user-agent stylesheet, the author stylesheet, or the user stylesheet), or even to clear the values of the properties entirely.

### Specificity

Specificity is the algorithm used by browsers to choose a declaration from competing declarations with the same cascade origin and importance. The specificity algorithm calculates the weights of CSS selectors to determine which declarations get applied to an element.

The specificity algorithm calculates a value based on three weight categories: *ID*, *CLASS*, and *TYPE*. The value represents the count of selector components in each weight category, and is written as *ID - CLASS - TYPE*. The selector weight categories are listed below in the order of decreasing specificity.

| Column  | Selectors                                                | Weight |
| ------- | -------------------------------------------------------- | ------ |
| ID      | ID selectors                                             | 1-0-0  |
| CLASS   | Class selectors, attribute selectors, and pseudo-classes | 0-1-0  |
| TYPE    | Type selectors and pseudo-elements                       | 0-0-1  |
| NEUTRAL | Universal selector and `:where()` pseudo-class           | 0-0-0  |

The specificities are compared from left to right. The selector with a higher value in a left column wins regardless of the value in further columns. Further columns are only compared if the values in the left column are equal.

Combinators may make a selector more specific in what is selected but they do not add any value to the specificity weight. The `:not()`, `:is()`, and `:has()` functional pseudo-classes do not have any specificity of their own. Their specificity is replaced by the specificity of the most specific selector in their argument selector list.

## Appendix

### Style guide / Lint

Add semicolon after the last declaration in a ruleset.
Each declaration should go on a separate line.
Each selector should go on a separate line.
The opening curly brace should be placed after the last selector with one space in between.
The closing curly brace should be placed on the next line after the last declaration.
Each ruleset should be separated from the other with one blank line.
There should be a blank line at the end of the document.
There should be no blank line at the start of the document.

### Pseudo-elements

`::after`
: It creates a pseudo-element that is the last child of the selected element and is inline by default. The pseudo-element created is contained by the formatting box of the selected element, and thus do not apply to replaced elements.

`::before`
: It creates a pseudo-element that is the first child of the selected element and is inline by default. The pseudo-element created is contained by the formatting box of the selected element, and thus do not apply to replaced elements.

`::first-letter`
: It selects the first letter of the first line of a block-level element, but only when it is not preceded by other content. Punctuation that precedes or immediately follows the first letter is included in the match. If generated content is injected with the `::before` pseudo-element, the `::first-letter` will match the first letter of this generated content.

`::first-line`
: It selects the first line of a block-level element. The `::first-line` has no effect when the first child of the element is an inline block-level element.

`::file-selector-button`
: It selects the button of an `<input>` element with `type="file"`. The `::file-selector-button` is a whole element, and hence, rather than inheriting, it matches rules from the user agent stylesheet.

`::marker`
: It selects the marker box of a list item, which typically contains a bullet or number. It has effect on any element or pseudo-element with the declaration `display: list-item` set.

`::placeholder`
: It selects the placeholder text in an `<input>` or `<textarea>` element.

`::selection`
: It selects part of the selected element that has been highlighted by the user.

### Pseudo-classes

`:fullscreen`
: It matches an element, including its children, that is currently in fullscreen mode. An element matches `:fullscreen` when it enters fullscreen mode using the Fullscreen API, and not when the browser is switched to fullscreen mode.

`:modal`              
: It selects an element that is in a state where it excludes all interaction with elements outside it until the interaction has been dismissed. Multiple elements can be selected by the `:modal` pseudo-class, but only one of them will be interactive.

`:picture-in-picture` 
: It selects an element that is currently in picture-in-picture mode.

`:autofill`           
: It selects an `<input>` element that has its value autofilled by the browser. It stops selecting the element if the user edits the field.

`:enabled`            
: It selects an element that can be activated or accept focus, and has a disabled state where it can not be activated or accept focus.

`:disabled`           
: It selects an element that can not be activated or accept focus, and has an enabled state where it can be activated or accept focus.

`:read-only`          
: It selects an element that is not editable by the user.

`:read-write`         
: It selects an element that is editable by the user.

`:placeholder-shown`  
: It selects an `<input>` or `<textarea>` element that is currently displaying placeholder text.

`:default`
: It selects a form element that is the default in a group of related elements. It selects a `<button>` element, or `<input>` element with a type that submits form, if that is the default submission button of a `<form>`.

`:checked`            
: It selects an `<input type="radio">` element, `<input type="checkbox">` element, or `<option>` element that is checked.

`:indeterminate`
: It selects a form element that has an indeterminate state.

`:valid`
: It selects a form element whose contents validate successfully.

`:invalid`            
: It selects a form element whose contents do not validate successfully.

`:in-range`           
: It selects an `<input>` element whose current value is inside the range limit specified by the `min` and `max` attributes.

`:out-of-range`       
: It selects an `<input>` element whose current value is outside the range limit specified by the `min` and `max` attributes. An empty `<input>` element will not be selected using the `:out-of-range` pseudo-class selector.

`:required`           
: It selects an `<input>`, `<select>`, or `<textarea>` element that has the `required` attribute set on it.

`:optional`           
: It selects an `<input>`, `<select>`, or `<textarea>` element that does not have the `required` attribute set on it.

`:any-link`           
: It selects an element that acts as the source anchor of a hyperlink, regardless of whether it has been visited. It matches every `<a>` or `<area>` element that has an `href` attribute.

`:link`               
: It selects a link element that has not yet been visited. It matches every unvisited `<a>` or `<area>` element that has an `href` attribute.

`:visited`            
: It selects a link element that has already been visited. For privacy reasons, the styles that can be modified using this selector are very limited.

`:local-link`
: It selects a link element that points to the same document. Therefore, an element that is the source anchor of a hyperlink whose target's absolute URL matches the element's own document URL.

`:target`
: It selects a link element with an `id` attribute whose value matches the document's URL fragment.

`:playing`            
: It selects an audio, video, or other resource element that is capable of being played or paused, when the element is playing. A resource is playing even if in buffering state or paused for any reason other than a user interaction to caus it to be explicitly paused.

`:paused`             
: It selects an audio, video, or other resource element that is capable of being played or paused, when the element is paused. A resource is paused if the user explicitly paused it, or if it in a non-activated state.
                                    
`:hover`              
: It selects an element when the user interacts with it through a pointing device, but does not necessarily activate it. The `:hover` pseudo-class is problematic on touchscreens as it might match for incorrect period of time.

`:active`             
: It selects an element when the user activates it. This activation generally starts when the user presses down the primary mouse button, and continues until the primary mouse button is released.

`:focus`              
: It selects an element when it has received focus. This pseudo-class only applies to the focused element itself, and is not triggered when a contained element receives focus.

`:focus-within`       
: It selects an element when it has received focus or any of its descendants, including descendants in the shadow tree, have received focus.

`:focus-visible`      
: It selects an element that is matched by the `:focus` pseudo-class, and the user agent determines through heuristics that the focus should be made evident on the element.

`:root`               
: It selects the root element of a tree representing the document. In HTML, `:root` matches the `<html>` element, and is identical to the selector `html`, except that it has a higher specificity.

`:empty`              
: It selects an element that has no children. Children can be either element nodes or text, including whitespace. Comments, processing instructions, and CSS `content` do not affect whether an element is considered empty.

`:first-child`        
: It selects the first element among a group of sibling elements.

`:last-child`         
: It selects the last element among a group of sibling elements.

`:only-child`         
: It selects an element without any siblings. This behaves the same way as `:first-child:last-child` or `:nth-child(1):nth-last-child(1)`, but with lower specificity.

`:first-of-type`      
: It selects the first element of its type among a group of sibling elements.

`:last-of-type`       
: It selects the last element of its type among a group of sibling elements.

`:only-of-type`       
: It selects an element that has no siblings of the same type.

`:nth-child()`
: It selects elements based on their position among a group of siblings. The child count starts from `1`, and includes children of any element type, but it is only considered a match if the element at that child position is of the specified element type.

`:nth-last-child()`
: It selects elements based on their position among a group of siblings, counting from the end. The child count starts from `1` counting from the end, and includes children of any element type, but it is only considered a match if the element at that child position is of the specified element type.

`:nth-of-type()`
: It selects elements based on their position among a group of siblings with the same type. The child count starts from `1`, and excludes children of other element type.

`:nth-last-of-type()`
: It selects elements based on their position among a group of siblings with the same type, counting from the end. The child count starts from `1` counting from the end, and excludes children of other element type.

`:is()`
: It selects an element that can be selected by one of the selectors in its argument selector list.

`:not()`
: It selects elements that do not match any selector in its argument selector list. Since prevents specific items from being selected, it is called the *negation pseudo-class*. It does not accept a forgiving selector list.

`:where()`
: It select an element that can be selected by one of the selectors in its argument selector list. It is functionally similar to the `:is()` pseudo-class, but has no specificity.

`:has()`
: It selects an element if any of the relative selectors that are passed as an argument match at least one element when anchored against this element.

`:dir()`
: It selects an element based on the directionality of the text contained within that element. It uses only the semantic value of the directionality, which is defined by the document itself, and thus does not account for the directionality set by CSS properties.

`:lang()`
: It selects an element based on the language they are determined to be in. In HTML, the language is determined by a combination of the `lang` attribute, the `<meta>` element, and possibly by information from the HTTP headers.

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
