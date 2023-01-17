# Cascading style sheets

<!-- omit in toc -->
## Table of contents

- [Introduction](#introduction)
  - [Processing model](#processing-model)
  - [Browser support](#browser-support)
  - [Debugging CSS](#debugging-css)
  - [Organizing CSS](#organizing-css)
- [Syntax](#syntax)
  - [Rulesets](#rulesets)
  - [At-rules](#at-rules)
  - [Values](#values)
  - [Shorthands](#shorthands)
  - [Comments](#comments)
  - [Whitespace](#whitespace)
- [Selectors](#selectors)
  - [Basic selectors](#basic-selectors)
  - [Combinators](#combinators)
  - [Attribute selectors](#attribute-selectors)
  - [Pseudo-elements](#pseudo-elements)
  - [Pseudo-classes](#pseudo-classes)
- [Cascade](#cascade)
  - [Origin](#origin)
  - [Importance](#importance)
  - [Specificity](#specificity)
  - [Inheritance](#inheritance)
- [Box model](#box-model)
  - [Display](#display)
  - [Formatting context](#formatting-context)
  - [Margin collapsing](#margin-collapsing)
  - [Backgrounds and borders](#backgrounds-and-borders)
  - [Overflowing content](#overflowing-content)
  - [Sizing items in CSS](#sizing-items-in-css)
- [Flex layout](#flex-layout)
  - [Formatting context](#formatting-context-1)
  - [Orientation](#orientation)
  - [Ordering](#ordering)
  - [Flexibility](#flexibility)
- [Grid layout](#grid-layout)
- [Table layout](#table-layout)
- [Positioning](#positioning)
- [Text styling](#text-styling)
  - [Handling different text directions](#handling-different-text-directions)
- [Images, media, and form elements](#images-media-and-form-elements)
- [Styling tables](#styling-tables)
- [Appendix](#appendix)
  - [Style guide](#style-guide)
  - [Reset style sheets](#reset-style-sheets)
  - [Pseudo-elements](#pseudo-elements-1)
  - [Pseudo-classes](#pseudo-classes-1)
  - [At-rules](#at-rules-1)

---

- Introduction

- Syntax
- Box model
- Selectors

- Cascade
- Specificity
- Inheritance

- Colors
- Backgrounds
- Borders
- Gradients
- Shadows

- Layout
- Values
- Focus
- Functions
- Logical properties
- Spacing
- Stacking context
- Visual formatting
- Overflow
- Floating
- Positioning

- Flexbox
- Grid
- Table

- Transforms
- Transitions
- Animations

- Filters
- Blend modes
- Clips
- Masks

- Fonts
- Text

- Lists
- Generated content

- Media-dependent styles

- Linking CSS in HTML
  - The `link` tag
  - The `style` attribute
  - The `@import` directive
  - HTTP linking
  - Inline styles

---

Spellings:

- style sheet
- whitespace

Formatting:

- and/or

---

## Introduction

Cascading Style Sheet (CSS) is a style sheet language used to describe the presentation of a document written in HTML or XML, including XML dialects such as SVG, MathML, or XHTML.

CSS Level 3 builds on CSS Level 2 Revision 1 module by module, using the CSS 2.1 specification as its core. Each module adds functionality and/or replaces part of the CSS 2.1 specification. From this level on modules are levelled independently. Modules with no CSS Level 2 equivalent start at Level 1 and modules that update features that existed in CSS Level 2 start at Level 3. CSS specification, itself, no longer has levels, therefore, "CSS Level 3" as a term is used only to differentiate it from the previous monolithic versions.


### Processing model

This section presents one possible model of how user agents that support CSS work. This is only a conceptual model and real implementations may vary. In this model, a user agent processes a source by going through the following steps:

1. Parse the source document and create a document tree.
2. Identify the target media type.
3. Retrieve all style sheets associated with the document that are specified for the target media type.
4. Annotate every element of the document tree by assigning a single value to every property based on cascading and inheritance.
5. From the annotated document tree, generate a formatting structure.
6. Transfer the formatting structure to the target medium for rendering. 

### Browser support
<!-- Add information about what happens when a CSS value is not supported by the browser -->
<!-- Add information about why not all browsers are equal and support all features at the same time -->
<!-- Give brief fallback mechanisms of CSS and introductions to how fallback can be provided -->
<!-- And similar information -->

### Debugging CSS

### Organizing CSS

---

## Syntax

<!-- 
- Syntax
- - Keywords
- - Characters
- - Statements
- - At-rules
- - Blocks
- - Rulesets
- - Declarations
- - Comments
- - Errors

- Values
- - Numbers
- - Lengths
- - Percentages
- - URI
- - Counters
- - Colors
- - Strings
- - Unsupported values
-->

The primary construct in a style sheet is a statement. A statement begins with any non-space character and ends at the first closing brace or semicolon that is encountered non-escaped, outside a string, and not nested into another brace pair. There are two categories of statements in style sheets:

- **Rulesets:** A structure that associates a selector list with a declaration block.
- **At-rules:** A structure that starts with an _at_ symbol, followed by an identifier, and continues up to the end of the statement.

Any statement which is not a ruleset or an at-rule is invalid and ignored. CSS is case-insensitive within the ASCII range, except for parts that are not under its control. In CSS, US English spelling is deemed correct where there is spelling variation.

### Rulesets

The ruleset (or rule) is a structure formed by adding a declarations list, enclosed within curly braces, after a selector list.

```css
style-rule ::=
  selectors-list {
    declarations-list
  }
```

The selector list is a comma-separated list of selectors, which selects nodes that matches with any single selector in the list. If any single selector in a selector list is invalid or unsupported, the entire selector list is considered invalid, and therefore the associated ruleset is ignored.

```css
selectors-list ::=
  selector[:pseudo-class] [::pseudo-element]
  [, selectors-list]
```

The declarations list is a semicolon-separated list of declarations - which are pairs of properties and values. The last declaration is not required to be terminated by a semicolon. If any invalid value is passed to a property, the entire declaration is ignored.

```css
declarations-list ::=
  [property: value]
  [; declarations-list]
```

### At-rules

An [at-rule](#at-rules-1) is a statement that controls the CSS engine behavior in specific conditions. An at-rule begins with an `@` symbol, followed by an identifier, and continues up to the next semicolon, or the next block, whichever comes first.

Besides the `@` symbol and the identifier, each at-rule has a different syntax. Nevertheless, several of them can be grouped as either *regular at-rules* or *conditional group rules*. The conditional group rules share a common syntax and optionally include nested statements.

```css
/* Regular at-rule */
@identifier (RULE);

/* Condition group rule */
@identifier (RULE) {
}
```

### Values


### Shorthands

Shorthand properties are CSS properties that allow setting values for multiple closely related CSS properties simultaneously. Values not specified in a shorthand property reset to their initial value. This means that an omission in a shorthand can override previously set values.

Shorthand properties does not force a specific order for the values of the properties they replace, provided these properties use values of different types. However, a specific order is required when several of these properties have identical value types, such as those describing the edges of a box.

| Syntax         | First value    | Second value     | Third value | Fourth value |
| -------------- | -------------- | ---------------- | ----------- | ------------ |
| 1-value syntax | All edges      |                  |             |              |
| 2-value syntax | Vertical edges | Horizontal edges |             |              |
| 3-value syntax | Top edge       | Horizontal edges | Bottom edge |              |
| 4-value syntax | Top edge       | Right edge       | Bottom edge | Left edge    |

CSS provides a universal shorthand property, `all`, which applies its value to every property of the selected element. Its purpose is to change the inheritance model of the element properties.

### Comments

A comment in CSS is used to add explanatory note to the code or prevent the browser from interpreting specific part of the style sheet. Comments can be placed wherever whitespace is allowed within a style sheet. Both single line and multiple lines comments are supported in CSS.

```css
/* Single line comment */

/* Multiple
   Lines
   Comment */
```

The `/*` and `*/` pair is used to delimit both single line and multiple lines comments. There is no other way to specify comments in external style sheets. Comments can not be nested, the first instance of `*/` that follows the `/*` closes the comment.

### Whitespace

Whitespace are characters that are used to indent the source code for readability. The characters considered as whitespace include **`U+0009 TAB`**, **`U+000A LF`**, **`U+000C FF`**, **`U+000D CR`**, and **`U+0020 SPACE`**. CSS largely ignores whitespaces between tokens, however, some instances require whitespace as syntax.

- No whitespace is allowed between the colon and pseudo-class, and between the base selector and colon.
- No whitespace is allowed between the two colons and pseudo-element, and between the base selector and two colons.
- A single whitespace character is required between values to separate them.
- Property names never contain whitespaces.
- Any amount of whitespace is allowed between each selector and comma in a selector list.

---

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

An attribute selector matches elements based on the presence of a specified attribute and conditions for its associated value. By default, the values are tested based on the case-sensitivity of the document language, however, the addition of the character `i` or `I` before the closing bracket causes the value to be tested case-insensitively.

| Name                           | Syntax            | Attribute value                                                               |
| ------------------------------ | ----------------- | ----------------------------------------------------------------------------- |
| General attribute selector     | `[attr]`          | Any value to the specified attribute.                                         |
| Exact attribute selector       | `[attr="value"]`  | Value exactly matches the specified string.                                   |
| List attribute selector        | `[attr~="value"]` | Value is a space-separated list, one of which matches the specified string.   |
| Starts-with attribute selector | `[attr^="value"]` | Value starts with the specified string.                                       |
| Ends-with attribute selector   | `[attr$="value"]` | Value ends with the specified string.                                         |
| Contains attribute selector    | `[attr*="value"]` | Value contains the specified string.                                          |
| Hyphenated attribute selector  | `[attr|="value"]` | Value either matches, or starts with and is immediately followed by a hyphen. |

### Pseudo-elements

A [pseudo-element](#pseudo-elements-1) is a keyword added to a selector that described a specific part of the selected element. A pseudo-element consists of double colons followed by the pseudo-element identifier. Although, most browsers also support the single colon syntax for pseudo-elements, it is recommended to use the double colons syntax for pseudo-elements, to distinguish them from pseudo-classes. A selector can contain at most one pseudo-element, and it must appear after any other syntax in the selector.

### Pseudo-classes

A [pseudo-class](#pseudo-classes-1) is a keyword added to a selector that describes a specific state of the selected element. A pseudo-class consists of a colon followed by the pseudo-class identifier. A functional pseudo-class is additionally followed by a pair of parenthesis which enclose the arguments. The element that a pseudo-class is attached to is called the *anchor element*.

The functional pseudo-classes (`:is()`, `:has()`, and `:where()`) accept a forgiving selector list, where incorrect or unsupported selectors are simply ignored, rather than invalidating the whole selector list. The selector list can not contain the functional pseudo-class itself and any pseudo-elements.

The functional pseudo-classes (`:nth-child()`, `:nth-last-child()`, `:nth-of-type()`, and `nth-last-of-type()`) take a single argument of the form `A * n + B`, where `A` is the integer step size, `B` is the integer offset, and `n` is the domain of all non-negative integers, starting from `0`. Two keywords exist as an argument, that are `odd` and `even`, which match elements at either odd positions or even positions. A single integer can be also be used as an argument, which selects only the element at that specified position.

Styles defined by a link-related pseudo-class are overridden by any subsequent link-related pseudo-class, that has at least equal specificity. To style links appropriately, follow the *LVHA-order*, which is `:link` then `:visited` then `:hover` and finally `:active`.

---

## Cascade

The cascade is an algorithm that determines how to find the value for each property of each document element. The following steps apply to the cascading algorithm:

1. **Relevance**: It first filters all the rules from the different sources to keep only the rules that apply to a given element. That means rules whose selector matches the given element, and which are part of an appropriate `media` at-rule.
2. **Origin and importance**: It then sorts these rules according to their origin and importance (presence of the `!important` flag).
3. **Specificity:** In the origin with precedence, if there are competing values for a property, the specificity of the selectors are compared, and the declaration with the highest specificity wins.
4. **Order of appearance**: In the origin with precedence, if there are competing values for a property, that are in rulesets with selectors that have the same specificity, the last declaration in the style order is applied.

Specificity only applies when the same element is targeted by multiple declarations of the same importance, in the origin with precedence. If matching selectors are in different origins, the cascade determines which declaration takes precedence.

When multiple selectors in the origin with precedence have the same specificity, the proximity rule is applied, whereby the declaration that appears last wins.

Directly targeted elements will always take precedence over rules which an element inherits from its ancestor, regardless of the specificity of the inherited rule. Proximity of elements in the document tree has no effect on the specificity.

Declarations are the only constructs in CSS that participate in the cascade, whether contained inside rulesets or at-rules. However note that the at-rule may make the entire selector irrelevant. For the most part, properties and descriptors within at-rules do not participate in the cascade, however, some at-rules, as a whole, participate in the cascade. Since, at-rules do not have specificity, they are compared using a stripped down version of the cascade algorithm.

| At-rule      | Description                                                                          |
| ------------ | ------------------------------------------------------------------------------------ |
| `@media`     | Enclosed declarations participate in the cascade.                                    |
| `@supports`  | Enclosed declarations participate in the cascade.                                    |
| `@font-face` | Entire at-rules, with the same `font-family` descriptor, participate in the cascade. |
| `@keyframes` | Entire keyframes participate in the cascade, but not individual declarations.        |
| `@import`    | Imported styles participate in the cascade, but not itself.                          |
| `@charset`   | Obeys other algorithms, and is not affected by the cascade.                          |

### Origin

The cascade algorithm defines how user agents combine property values originating from different origins. The cascade defines the origin and layer that takes precedence when declarations in more than one origin or cascade layer set a value for the same property on an element.

When a selector matches an element, the property value from the origin or layer with the highest precedence gets applied, even if the selector from a lower precedence origin or layer has greater specificity. The cascade order is based on origin type, which can be either user agent, author, or user.

| Order (low to high) | Origin          |
| ------------------- | --------------- |
| 1                   | User agent      |
| 2                   | User            |
| 3                   | Author          |
| 4                   | CSS animations  |
| 5                   | CSS transitions |

The cascade within each origin type is based on the declaration order of cascade layers within that type. For all origins, styles can be declared within or outside of named or anonymous layers. When declared using `layer`, `layer()` or `@layer`, styles are placed into the specified named layer, or into an anonymous layer if no name is provided. Styles declared outside of a layer are treated as being part of an anonymous last declared layer.

Normal layered styles take precedence over normal styles in prior layers. Normal unlayered styles take precedence over normal layered styles, regardless of specificity. Normal inline styles take precedence over normal author styles, unless the property is being altered by a CSS animation.

| Order (low to high) | Origin           |
| ------------------- | ---------------- |
| 1                   | First layer      |
| 2                   | Last layer       |
| 3                   | Unlayered styles |
| 4                   | Inline `style`   |
| 5                   | CSS animations   |
| 10                  | CSS Transitions  |

### Importance

The `!important` flag reverses the precedence order of origin types and cascade layers. Important styles declared outside of any cascade layer have lower precedence than those declared as part of a layer. Important values that come in early layers have precedence over important styles declared in subsequent cascade layers. Styles that are transitioning take precedence over all important styles, no matter who or how they are declared.

| Order (low to high) | Origin          | Layer        | Importance   |
| ------------------- | --------------- | ------------ | ------------ |
| 1                   | User agent      | First        | Normal       |
| 2                   | User agent      | Last         | Normal       |
| 3                   | User agent      | Unlayered    | Normal       |
| 4                   | User            | First        | Normal       |
| 5                   | User            | Last         | Normal       |
| 6                   | User            | Unlayered    | Normal       |
| 7                   | Author          | First        | Normal       |
| 8                   | Author          | Last         | Normal       |
| 9                   | Author          | Unlayered    | Normal       |
| 10                  | Author          | Inline style | Normal       |
| 11                  | CSS animations  | All layers   | Normal       |
| 12                  | Author          | Unlayered    | `!important` |
| 13                  | Author          | Last         | `!important` |
| 14                  | Author          | First        | `!important` |
| 15                  | Author          | Inline style | `!important` |
| 16                  | User            | Unlayered    | `!important` |
| 17                  | User            | Last         | `!important` |
| 18                  | User            | First        | `!important` |
| 19                  | User agent      | Unlayered    | `!important` |
| 20                  | User agent      | Last         | `!important` |
| 21                  | User agent      | First        | `!important` |
| 22                  | CSS transitions | All layers   | Normal       |

### Specificity

Specificity is the algorithm used by user agents to choose a declaration from competing declarations with the same cascade origin and importance. The specificity algorithm calculates a value based on three weight categories: *A*, *B*, and *C*. The specificity is calculated by counting the selector components in each weight category.

| Column | Selectors                                                | Weight |
| ------ | -------------------------------------------------------- | ------ |
| A      | ID selectors                                             | 1-0-0  |
| B      | Class selectors, attribute selectors, and pseudo-classes | 0-1-0  |
| C      | Type selectors and pseudo-elements                       | 0-0-1  |

The specificities are compared from left to right. The selector with a higher value in a left column wins regardless of the value in further columns. Further columns are only compared if the values in all left columns are equal. Some exceptions to the general specificity algorithm exist.

- The specificity of a selector list is replaced by the specificity of the most specific selector in the list.
- The specificity of an `:is()`, `:not()`, or `:has()` pseudo-class is replaced by the specificity of the most specific selector in its selector list argument.
- The specificity of an `:nth-child()` or `:nth-last-child()` selector is the specificity of the pseudo-class itself (counting as one pseudo-class selector) plus the specificity of the most specific selector in its selector list argument, if any.
- Combinators may make a selector more specific in what is selected but they do not add any value to the specificity weight.
- The specificity of a universal selector or `:where()` pseudo-class is replaced by zero.

### Inheritance

Inheritance controls what happens when no value is specified for a property on an element. However, inheritance only applies when no value for the property is specified by any style sheet from any origin type.

The root element of the document gets the initial value for properties that have no associated values. For all other elements, the treatment varies depending on whether the property is inherited or non-inherited.

| Property               | Value                         |
| ---------------------- | ----------------------------- |
| Inherited property     | Computed value of the parent  |
| Non-inherited property | Initial value of the property |

Inheritance can be explicitly controlled using special keywords that applies to all CSS properties. These keywords work on both inherited and non-inherited properties. Inheritance for all properties of an element can be controlled at once using the `all` shorthand property, which applies the associated value to all the properties of that element.

| Keyword   | Effect                                                                                                            |
| --------- | ----------------------------------------------------------------------------------------------------------------- |
| `inherit` | Explicitly sets the property to inherit the computed value of the parent element.                                 |
| `initial` | Explicitly sets the property to take the initial value.                                                           |
| `revert`  | Reverts the property value to the value that would have been if no changes were made by the current style origin. |
| `unset`   | Resets an inherited property to the inherited value and non-inherited property to the initial value.              |

---

## Box model

<!-- Introduction -->
The CSS box model describes how each element and string of text in a source document is laid out by transforming the document tree into boxes. Each box has a rectangular content area, which contains text, descendant boxes, or replaced elements, and optionally surrounding padding, border, and margin areas. The size of each area can be zero, or even negative in the case of margins. The perimeter of each area is called an *edge*, and the four edges (top, right, bottom, left) of an area define its size.

<!-- Necessary to center align and add spacing above and below the image -->
<br><div align="center"><img src="assets/box-model.png"></div><br>

<!-- Anatomy of box model -->
| Area         | Edge         | Description                                                     |
| ------------ | ------------ | --------------------------------------------------------------- |
| Content area | Content edge | It contains the rendered content of the element.                |
| Padding area | Padding edge | It extends the content area to include the surrounding padding. |
| Border area  | Border edge  | It extends the padding area to include the surrounding border.  |
| Margin area  | Margin edge  | It extends the border area to include the box margin.           |

<!-- Sizing properties -->
For block elements, the CSS properties (`width`, `min-width`, `max-width`, `height`, `min-height`, and `max-height`) explicitly controls the size of either content area or border area, based on whether the `box-sizing` property is set to `content-area` (default) or `border-box`. For non-replaced inline elements, the box height is defined by the `line-height` property, since inline layout does not respect height, although the border and padding are still displayed. The thickness of padding, border, and margin can be explicitly controlled by `padding` and its longhand properties, `border` and its longhand properties, and `margin` and its longhand properties, respectively.

<!-- Background styling -->
The background style of content area, padding area, or border area can be specified with the `background` shorthand property. However, margins are always transparent. Backgrounds specified on a box are, by default, painted within the padding edges, and additionally painted underneath the border. This behavior can be adjusted with `background-origin` and `background-clip` properties. 

<!-- Margin collapsing -->
Adjoining margins in block layout can collapse to form a single [*collapsed margin*](#margin-collapsing). When margin collapsing occurs, the margin areas are not clearly defined since margins are shared between boxes.

### Display

<!-- Introduction -->
CSS takes a source document organized as a tree of elements and text nodes, and generates an intermediary structure called the *box tree*. For each element or text node, zero or more boxes are generated, as specified by its `display` property.

<!-- Principal and anonymous box -->
Typically, an element generates a single box, called the *principal box*, however, some `display` values generate no box or more than than one box. An *anonymous box* is generated in certain circumstances when a particular nested structure is required but none is available. Anonymous boxes inherit from their direct parent and can not be directly targeted for styling.

<!-- Display types -->
Text runs have no display type. For elements, the `display` property defines its display type, which consists of the two basic qualities of how an element generates boxes:

- **Outer display type:** It defines how the principal box itself participates in flow layout.

  | Value    | Generated box    |
  | -------- | ---------------- |
  | `block`  | Block-level box  |
  | `inline` | Inline-level box |
  | `run-in` | Inline-level box |

- **Inner display type:** It defines the formatting context generated, dictating how its descendants are laid out.

  | Value       | Generated box       |
  | ----------- | ------------------- |
  | `flow`      | Any                 |
  | `flow-root` | Block container box |
  | `table`     | Table wrapper box   |
  | `flex`      | Flex container box  |
  | `grid`      | Grid container box  |
  | `ruby`      | Ruby container box  |

<!-- Run-in box -->
A run-in box is a box that merges into a block that comes after it, inserting itself at the beginning of the inline content of that box. This is useful for cases, like run-in headings, where the appropriate DOM structure is to have a heading preceding the following prose, but the desired display is an inline heading layout out with the text.

<!-- Additional properties -->
In flex and grid formatting contexts, the `order` property can be used to rearrange the order of boxes within the container, by assigning them to ordinal groups. Items with the same ordinal group are laid out in the order they appear in the source document. The `visibility` property specifies whether the box is rendered. Invisible boxes still effect layout and occupy space, unlike those with `display: none`, which are not rendered at all. Some `display` values have additional side effects.

<!-- Special display values -->
| Value       | Effect                                                  |
| ----------- | ------------------------------------------------------- |
| `none`      | The element and its descendants generate no boxes.      |
| `content`   | The element is replaced with its content/descendants.   |
| `list-item` | The element also generates a `::marker` pseudo-element. |

### Formatting context
- Block formatting context
- Inline formatting context
- etc

### Margin collapsing

### Backgrounds and borders

### Overflowing content

### Sizing items in CSS

--

## Flex layout

A flex container is the box generated by an element with `display: flex` or `display: inline-flex`. In-flow children of a flex container are called *flex items* and are laid out using the flex layout model. Unlike block or inline layout, whose layout calculations are biased to the block and inline flow directions, flex layout is biased to the *flex directions*.

<!-- Necessary to center align and add spacing above and below the image -->
<br><div align="center"><img src="assets/flexbox.png"></div><br>

<!-- Anatomy of flexbox -->
| Term            | Definition                                                                          |
| --------------- | ----------------------------------------------------------------------------------- |
| main axis       | The primary axis along which flex items are laid out.                               |
| main direction  | The direction in which flex items are laid out along the main axis.                 |
| main start      | The start of the main axis in the main direction.                                   |
| main end        | The end of the main axis in the main direction.                                     |
| main size       | The size (either width or height) of a flex item or container along the main axis.  |
| cross axis      | The axis perpendicular to the main axis.                                            |
| cross direction | The direction in which flex items wrap along the cross axis.                        |
| cross start     | The start of the cross axis in the cross direction.                                 |
| cross end       | The end of the cross axis in the cross direction.                                   |
| cross size      | The size (either width or height) of a flex item or container along the cross axis. |

### Formatting context

<!-- Differences from block layout -->
A flex container establishes a new *flex formatting context* for its content. Flex containers form a containing block for their contents exactly like block containers do. The `overflow` property applies to flex containers. However, some properties that were designed with the assumption of block layout do not apply in the context of flex layout:

- `float` and `clear` do not create floating or clearance of flex item, and do not take it out-of-flow.
- `vertical-align` has no effect on a flex item.
- `::first-line` and `::first-letter` pseudo-elements do not apply to flex containers, and flex containers do not contribute a first formatted line or first letter to their ancestors.

<!-- Formation of flex items -->
Each in-flow child of a flex container becomes a flex item, and each contiguous sequence of child text runs is wrapped in an anonymous block container flex item. However, if the entire sequence of child text runs contains only document whitespace characters, it is instead not rendered.

<!-- Behavior of margins and paddings -->
The margins of adjacent flex items do not collapse. Percentage margins and paddings on flex items are resolved against the inline size of their containing block. Auto margins expand to absorb extra space in the corresponding dimension.

### Orientation

<!-- Flex direction -->
The `flex-direction` property specifies the direction of the flex container's main axis, which determines the direction in which flex items are laid out. The table below compares the orientation, start direction, and end direction of the flex container's main axis with an axis of the current writing mode, for different values of the `flex-direction` property.

| Value            | Main axis   | Main start   | Main end     |
| ---------------- | ----------- | ------------ | ------------ |
| `row`            | Inline axis | Inline start | Inline end   |
| `row-reverse`    | Inline axis | Inline end   | Inline start |
| `column`         | Block axis  | Block start  | Block end    |
| `column-reverse` | Block axis  | Block end    | Block start  |

<!-- Flex wrap -->
The `flex-wrap` property controls whether the flex container spans a single line or breaks into multiple lines, and the direction of the cross axis, which determines the direction new lines are stacked in.

When `flex-wrap` has a value other than `wrap-reverse`, the cross start direction is equivalent to either the inline start or block start direction of the current writing mode, whichever is in the cross axis orientation, and the cross end direction is the opposite direction of cross start. When `flex-wrap` is `wrap-reverse`, the cross start and cross end directions are swapped.

| Value          | Line span     | Cross start                | Cross end                  |
| -------------- | ------------- | -------------------------- | -------------------------- |
| `nowrap`       | Single line   | Inline start / Block start | Inline end / Block end     |
| `wrap`         | Multiple line | Inline start / Block start | Inline end / Block end     |
| `wrap-reverse` | Single line   | Inline end / Block end     | Inline start / Block start |

A single line flex container lays out all of its children in a single line, even if that would cause its content to overflow. A multiple line flex container breaks its flex items across multiple lines.

When additional lines are created, they are stacked in the flex container along the cross axis according to the `flex-wrap` property. Once content is broken into lines, each line is laid out independently, therefore, `flex`, `justify-content`, and `align-self` properties only consider the items on an individual line.

<!-- Flex flow shorthand -->
The `flex-flow` property is a shorthand for setting the `flex-direction` and `flex-wrap` properties, which together define the flex container's main and cross axis. The `flex-flow` directions are sensitive to the current writing mode of the document.

```css
/* English */
flex-flow: row wrap;
writing-mode: horizontal-tb;
```

```css
/* Japanese */
flex-flow: row wrap;
writing-mode: vertical-rl;
```

### Ordering

<!-- Introduction -->
Flex items are, by default, displayed and laid out in the same order as they appear in the source document, which represents their logical ordering. The `order` property is used to change the ordering of flex items, by assigning them to ordinal groups. It takes a single integer value, which specifies the ordinal group of an item.

<!-- Information about non-trivial ordering -->
Flex containers lay out their contents in order-modified document order, starting from the lowest numbered ordinal group. Items with the same ordinal group are laid out in the order they appear in the source document. Absolutely positioned children of a flex container are treated as having `order: 0` for the purpose of determining their painting order relative to other flex items.

<!-- Accessibility warning -->
The `order` property must only be used for spatial reordering of content, rather than logical reordering. Style sheets that use `order` to perform logical reordering are non-conforming.

### Flexibility

<!-- Introduction -->
The defining aspect of flex layout is the ability to make the flex items *flex*, altering their width/height to fill the available space in the main direction. The flexibility of a flex item is controlled using the `flex` shorthand property.

<!-- Flex shorthand -->
The `flex` shorthand property specifies the flex growth factor, flex shrink factor, and the flex basis size. If a box is not a flex item, `flex` has no effect. The `flex` shorthand should be used to control flexibility rather than the longhand properties, as the shorthand correctly resets any unspecified component to accommodate common uses.

| Property      | Description                                                                      | Reset value |
| ------------- | -------------------------------------------------------------------------------- | ----------- |
| `flex-grow`   | Relative growth factor of the flex item when positive free space is distributed. | `1`         |
| `flex-shrink` | Relative shrink factor of the flex item when negative free space is distributed. | `1`         |
| `flex-basis`  | Initial main size of the flex item before free space is distributed.             | `0`         |

A flex item is fully inflexible if both its `flex-grow` and `flex-shrink` values are zero, and flexible otherwise.

<!-- Description of longhand properties -->
If the sum of flex growth factors on a line is less than 1, the flex items will not expand to absorb the entirety of the free space available. The flex shrink factor is multiplied by the flex basis size when distributing negative space. This distributes negative space in proportion to how much the item is able to shrink. The `flex-basis` property accepts two keywords and a number.

| Value      | Description                                                                        |
| ---------- | ---------------------------------------------------------------------------------- |
| `auto`     | Equivalent to `content` if main size is `auto`, otherwise equivalent to main size. |
| `content`  | Automatic size based on the content of the flex item.                              |
| `<number>` | Size resolved from the number.                                                     |


The list below summarizes the effects of the four flex values that represent most commonly desired effects:

| `initial` | `0 1 auto` | Makes the item inflexible when free space is available, but allows it to shrink to its minimum size. |
| `auto` | `1 1 auto` | Makes the item fully flexible 

flex: initial
    Equivalent to flex: 0 1 auto. (This is the initial value.) Sizes the item based on the width/height properties. (If the item’s main size property computes to auto, this will size the flex item based on its contents.) Makes the flex item inflexible when there is positive free space, but allows it to shrink to its minimum size when there is insufficient space. The alignment abilities or auto margins can be used to align flex items along the main axis. 
flex: auto
    Equivalent to flex: 1 1 auto. Sizes the item based on the width/height properties, but makes them fully flexible, so that they absorb any free space along the main axis. If all items are either flex: auto, flex: initial, or flex: none, any positive free space after the items have been sized will be distributed evenly to the items with flex: auto. 
flex: none
    Equivalent to flex: 0 0 auto. This value sizes the item according to the width/height properties, but makes the flex item fully inflexible. This is similar to initial, except that flex items are not allowed to shrink, even in overflow situations. 
''flex: <number [1,∞]>''
    Equivalent to ''flex: <number [1,∞]> 1 0''. Makes the flex item flexible and sets the flex basis to zero, resulting in an item that receives the specified proportion of the free space in the flex container. If all items in the flex container use this pattern, their sizes will be proportional to the specified flex factor. 

By default, flex items won’t shrink below their minimum content size (the length of the longest word or fixed-size element). To change this, set the min-width or min-height property. (See § 4.5 Automatic Minimum Size of Flex Items.)

The flex-basis property sets the flex basis. It accepts the same values as the width and height property, plus content.

For all values other than auto and content (defined above), flex-basis is resolved the same way as width in horizontal writing modes [CSS2], except that if a value would resolve to auto for width, it instead resolves to content for flex-basis. For example, percentage values of flex-basis are resolved against the flex item’s containing block (i.e. its flex container); and if that containing block’s size is indefinite, the used value for flex-basis is content. As another corollary, flex-basis determines the size of the content box, unless otherwise specified such as by box-sizing.

After a flex container’s contents have finished their flexing and the dimensions of all flex items are finalized, they can then be aligned within the flex container.

The margin properties can be used to align items in a manner similar to, but more powerful than, what margins can do in block layout. Flex items also respect the alignment properties from CSS Box Alignment, which allow easy keyword-based alignment of items in both the main axis and cross axis. These properties make many common types of alignment trivial, including some things that were very difficult in CSS 2.1, like horizontal and vertical centering.

Auto margins on flex items have an effect very similar to auto margins in block flow:

    During calculations of flex bases and flexible lengths, auto margins are treated as 0.

    Prior to alignment via justify-content and align-self, any positive free space is distributed to auto margins in that dimension.

    Overflowing boxes ignore their auto margins and overflow in the end direction.

The justify-content property aligns flex items along the main axis of the current line of the flex container. This is done after any flexible lengths and any auto margins have been resolved. Typically it helps distribute extra free space leftover when either all the flex items on a line are inflexible, or are flexible but have reached their maximum size. It also exerts some control over the alignment of items when they overflow the line.

flex-start
    Flex items are packed toward the start of the line. The main-start margin edge of the first flex item on the line is placed flush with the main-start edge of the line, and each subsequent flex item is placed flush with the preceding item. 
flex-end
    Flex items are packed toward the end of the line. The main-end margin edge of the last flex item is placed flush with the main-end edge of the line, and each preceding flex item is placed flush with the subsequent item.
    Tests
center
    Flex items are packed toward the center of the line. The flex items on the line are placed flush with each other and aligned in the center of the line, with equal amounts of space between the main-start edge of the line and the first item on the line and between the main-end edge of the line and the last item on the line. (If the leftover free-space is negative, the flex items will overflow equally in both directions.) 
space-between
    Flex items are evenly distributed in the line. If the leftover free-space is negative or there is only a single flex item on the line, this value is identical to flex-start. Otherwise, the main-start margin edge of the first flex item on the line is placed flush with the main-start edge of the line, the main-end margin edge of the last flex item on the line is placed flush with the main-end edge of the line, and the remaining flex items on the line are distributed so that the spacing between any two adjacent items is the same. 
space-around
    Flex items are evenly distributed in the line, with half-size spaces on either end. If the leftover free-space is negative or there is only a single flex item on the line, this value is identical to center. Otherwise, the flex items on the line are distributed such that the spacing between any two adjacent flex items on the line is the same, and the spacing between the first/last flex items and the flex container edges is half the size of the spacing between flex items. 

Flex items can be aligned in the cross axis of the current line of the flex container, similar to justify-content but in the perpendicular direction. align-items sets the default alignment for all of the flex container’s items, including anonymous flex items. align-self allows this default alignment to be overridden for individual flex items. (For anonymous flex items, align-self always matches the value of align-items on their associated flex container.)

If either of the flex item’s cross-axis margins are auto, align-self has no effect.

Values have the following meanings:

auto
    Defers cross-axis alignment control to the value of align-items on the parent box. (This is the initial value of align-self.)
    Tests
flex-start
    The cross-start margin edge of the flex item is placed flush with the cross-start edge of the line.
    Tests
flex-end
    The cross-end margin edge of the flex item is placed flush with the cross-end edge of the line.
    Tests
center
    The flex item’s margin box is centered in the cross axis within the line. (If the cross size of the flex line is less than that of the flex item, it will overflow equally in both directions.)
    Tests
baseline
    The flex item participates in baseline alignment: all participating flex items on the line are aligned such that their baselines align, and the item with the largest distance between its baseline and its cross-start margin edge is placed flush against the cross-start edge of the line. If the item does not have a baseline in the necessary axis, then one is synthesized from the flex item’s border box.
    Tests
stretch
    If the cross size property of the flex item computes to auto, and neither of the cross-axis margins are auto, the flex item is stretched. Its used value is the length necessary to make the cross size of the item’s margin box as close to the same size as the line as possible, while still respecting the constraints imposed by min-height/min-width/max-height/max-width.

    Note: If the flex container’s height is constrained this value may cause the contents of the flex item to overflow the item.

    The cross-start margin edge of the flex item is placed flush with the cross-start edge of the line.
    Tests

The `align-content` property aligns a flex container’s lines within the flex container when there is extra space in the cross-axis, similar to how justify-content aligns individual items within the main-axis. Note, this property has no effect on a single-line flex container. Values have the following meanings:

flex-start
    Lines are packed toward the start of the flex container. The cross-start edge of the first line in the flex container is placed flush with the cross-start edge of the flex container, and each subsequent line is placed flush with the preceding line. 
flex-end
    Lines are packed toward the end of the flex container. The cross-end edge of the last line is placed flush with the cross-end edge of the flex container, and each preceding line is placed flush with the subsequent line. 
center
    Lines are packed toward the center of the flex container. The lines in the flex container are placed flush with each other and aligned in the center of the flex container, with equal amounts of space between the cross-start content edge of the flex container and the first line in the flex container, and between the cross-end content edge of the flex container and the last line in the flex container. (If the leftover free-space is negative, the lines will overflow equally in both directions.) 
space-between
    Lines are evenly distributed in the flex container. If the leftover free-space is negative or there is only a single flex line in the flex container, this value is identical to flex-start. Otherwise, the cross-start edge of the first line in the flex container is placed flush with the cross-start content edge of the flex container, the cross-end edge of the last line in the flex container is placed flush with the cross-end content edge of the flex container, and the remaining lines in the flex container are distributed so that the spacing between any two adjacent lines is the same. 
space-around
    Lines are evenly distributed in the flex container, with half-size spaces on either end. If the leftover free-space is negative this value is identical to center. Otherwise, the lines in the flex container are distributed such that the spacing between any two adjacent lines is the same, and the spacing between the first/last lines and the flex container edges is half the size of the spacing between flex lines. 
stretch
    Lines stretch to take up the remaining space. If the leftover free-space is negative, this value is identical to flex-start. Otherwise, the free-space is split equally between all of the lines, increasing their cross size. 

Note: Only multi-line flex containers ever have free space in the cross-axis for lines to be aligned in, because in a single-line flex container the sole line automatically stretches to fill the space.



## Grid layout

## Table layout

## Positioning
- Normal
- Absolute
- Static
- Relative


---

## Text styling

### Handling different text directions

---

## Images, media, and form elements

---

## Styling tables

---

## Appendix

### Style guide

Add semicolon after the last declaration in a ruleset.
Each declaration should go on a separate line.
Each selector should go on a separate line.
The opening curly brace should be placed after the last selector with one space in between.
The closing curly brace should be placed on the next line after the last declaration.
Each ruleset should be separated from the other with one blank line.
There should be a blank line at the end of the document.
There should be no blank line at the start of the document.

### Reset style sheets

After your content has finished altering styles, it may find itself in a situation where it needs to restore them to a known state. This may happen in cases of animations, theme changes, and so forth. The CSS property `all` lets you quickly set (almost) everything in CSS back to a known state.

`all` lets you opt to immediately restore all properties to any of their initial (default) state, the state inherited from the previous level of the cascade, a specific origin (the user agent stylesheet, the author stylesheet, or the user stylesheet), or even to clear the values of the properties entirely.

Although some constraints on user agent stylesheets are set by the HTML specification, browsers have a lot of latitude: that means some differences exist between browsers. To simplify the development process, Web developers may use a CSS reset stylesheet, such as _normalize.css_, which sets common properties values to a known state for all browsers before beginning to make alterations to suit their specific needs.

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
: It selects the button of an `<input>` element with `type="file"`. The `::file-selector-button` is a whole element, and hence, rather than inheriting, it matches rules from the user agent style sheet.

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

### At-rules

`@charset`
: It specifies the character encoding used in a style sheet. It must be the first statement in the style sheet and must not be preceded by any other character.

```css
@charset "charset";
```

`@font-face`
: It specifies a custom font to be used for displaying text. The font can either be locally installed or loaded from a remote server.

```css
@font-face {
  font-family: "font-name";
  font-style: normal;
  font-weight: 100;
  src: local("font-name"), url("font-name.woff") format("woff");
}
```

`@import`
: It specifies an external style sheet to be imported, optionally into a layer, and optionally based on specific conditions. It must come before all other rules, except the `@charset` and `@layer` statements.

```css
@import url("file-name") layer(layer-name) supports(<supports-query>) <media-query>;
```

`@keyframes`
: It specifies the intermediate steps in an animation sequence by defining styles for keyframes. This gives more control over the intermediate steps than transitions.

```css
@keyframes identifier {
  from {
    <style-rules>;
  }

  to {
    <style-rules>;
  }
}
```

`@layer`
: It declares a cascade layer, optionally immediately followed by a declaration block. Style rules that are not declared in a layer are gathered together into a single anonymous layer.

```css
@layer layer-name {
  <style-rules>;
}
```

`@media`
: It specifies style rules that are applied based on specific media queries. These style rules are only applied when the media queries match the device on which the content is being used.

```css
@media <media-query> {
  <style-rules>;
}
```

`@supports`
: It specifies style rules that are applied based on the browser support for a specific CSS feature. It must be placed at the top level of code or nested inside an other conditional group rule.

```css
@supports (<supports-query>) {
  <style-rules>;
}
```





----------------------

its best to reflect
the state of CSS at that time. The assumption is that anything covered in detail either
had wide browser support at the time of writing or was known to be coming soon
after publication. CSS features which were still being developed, or were known to
have support dropping soon, are not covered here

Conventions Used in This Book
The following typographical conventions are used in this book (but make sure to read
through the subsection “Value Syntax Conventions” on page xx to see how some of
these are modified):
Italic
Indicates new terms, URLs, email addresses, filenames, and file extensions.
Constant width
Used for program listings, as well as within paragraphs to refer to program ele‐
ments such as variable or function names, databases, data types, environment
variables, statements, and keywords.
Constant width bold
Shows commands or other text that should be typed literally by the user.
Constant width italic
Shows text that should be replaced with user-supplied values or by values deter‐
mined by context.
xix
This element signifies a tip or suggestion.
This element signifies a general note.
This element indicates a warning or caution.
Value Syntax Conventions
Throughout this book, there are boxes that break down a given CSS property’s details,
including what values are permitted. These have been reproduced practically verba‐
tim from the CSS specifications, but some explanation of the syntax is in order.
Throughout, the allowed values for each property are listed with a syntax like the fol‐
lowing:
Value: <family-name>#
Value: <url> ‖ <color>
Value: <url>? <color> [ / <color> ]?
Value: [ <length> | thick | thin ]{1,4}
Any italicized words between “<” and “>” give a type of value, or a reference to
another property’s values. For example, the property font accepts values that origi‐
nally belong to the property font-family. This is denoted by using the text <font-
family>. Similarly, if a value type like a color is permitted, it will be represented using
<color>.
Any words presented in constant width are keywords that must appear literally,
without quotes. The forward slash (/) and the comma (,) must also be used literally.
There are a number of ways to combine components of a value definition:
• Two or more keywords strung together with only space separating them means
that all of them must occur in the given order. For example, help me would mean
that the property must use those keywords in that order.
xx | Preface
• If a vertical bar separates alternatives (X | Y), then any one of them must occur,
but only one. Given “[ X | Y | Z ]”, then any one of X, Y, or Z is permitted.
• A vertical double bar (X ‖ Y) means that X, Y, or both must occur, but they may
appear in any order. Thus: X, Y, X Y, and Y X are all valid interpretations.
• A double ampersand (X && Y) means both X and Y must occur, though they
may appear in any order. Thus: X Y or Y X are both valid interpretations.
• Brackets ([...]) are for grouping things together. Thus “[please ‖ help ‖ me] do
this” means that the words please, help, and me can appear in any order,
though each appear only once. do this must always appear, with those words in
that order. Some examples: please help me do this, help me please do
this, me please help do this.
Every component or bracketed group may (or may not) be followed by one of these
modifiers:
• An asterisk (*) indicates that the preceding value or bracketed group is repeated
zero or more times. Thus, “bucket*” means that the word bucket can be used
any number of times, including zero. There is no upper limit defined on the
number of times it can be used.
• A plus (+) indicates that the preceding value or bracketed group is repeated one
or more times. Thus, “mop+” means that the word mop must be used at least once,
and potentially many more times.
• An octothorpe (#) indicates that the preceding value or bracketed group is
repeated one or more times, separated by commas as needed. Thus, “floor#” can
be floor, floor, floor, floor, and so on. This is most often used in conjunc‐
tion with bracketed groups or value types.
• A question mark (?) indicates that the preceding value or bracketed group is
optional. For example, “[pine tree]?” means that the words pine tree need not
be used (although they must appear in that order if they are used).
• An exclamation point (!) indicates that the preceding value or bracketed group is
required, and thus must result in at least one value, even if the syntax would seem
to indicate otherwise. For example, “[ what? is? happening? ]!” must be at least
one of the three terms marked optional.
• A pair of numbers in curly braces ({M,N}) indicates that the preceding value or
bracketed group is repeated at least M and at most N times. For example, ha{1,3}
means that there can be one, two, or three instances of the word ha.
Preface | xxi
The following are some examples:
give ‖ me ‖ liberty
At least one of the three words must be used, and they can be used in any order.
For example, give liberty, give me, liberty me give, and give me liberty
are all valid interpretations.
[ I | am ]? the ‖ walrus
Either the word I or am may be used, but not both, and use of either is optional.
In addition, either the or walrus, or both, must follow in any order. Thus you
could construct I the walrus, am walrus the, am the, I walrus, walrus the,
and so forth.
koo+ ka-choo
One or more instances of koo must be followed by ka-choo. Therefore koo koo
ka-choo, koo koo koo ka-choo, and koo ka-choo are all legal. The number of
koos is potentially infinite, although there are bound to be implementation-
specific limits.
I really{1,4}? [ love | hate ] [ Microsoft | Netscape | Opera | Safari | Chrome ]
The all-purpose web designer’s opinion-expresser. This can be interpreted as I
love Netscape, I really love Microsoft, and similar expressions. Anywhere
from zero to four reallys may be used, though they may not be separated by
commas. You also get to pick between love and hate, which really seems like
some sort of metaphor.
It’s a [ mad ]# world
This gives the opportunity to put in as many comma-separated mads as possible,
with a minimum of one mad. If there is only one mad, then no comma is added.
Thus: It’s a mad world and It’s a mad, mad, mad, mad, mad world are
both valid results.
[ [ Alpha ‖ Baker ‖ Cray ], ]{2,3} and Delphi
Two to three of Alpha, Baker, and Delta must be followed by and Delphi. One
possible result would be Cray, Alpha, and Delphi. In this case, the comma is
placed because of its position within the nested bracket groups. (Some older ver‐
sions of CSS enforced comma-separation this way, instead of via the # modifier.)