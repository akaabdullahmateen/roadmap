# Cascading Style Sheets

<!-- TODO: -->
<!-- Replace the second-level headings with more appropriate alternatives. -->
<!-- Restructure the hierarchy of headings if needed. -->

## Part 1

### Definition

Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language such as HTML or XML (including XML dialects such as SVG, MathML, or XHTML). CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.

### Canvas

For all media, the term **canvas** describes the space where the formatting structure is rendered. The canvas is infinite for each dimension of the space, but rendering generally occurs within a finite region of the canvas, established by the user agent according to the target medium. For instance, user agents rendering to a screen generally impose a minimum width and choose an initial width based on the dimensions of the viewport. User agents rendering to a page generally impose width and height constraints. Aural user agents impose limits in audio space, but not in time.

### Design principles

- **Forward and backwards compatibility:** User agents will be able to read previous and later versions of CSS, and discard parts that they do not understand. Moreover, user agents with no CSS support will be able to display style-enhanced documents (although the stylistic enhancements will not be rendered, but all the content will be presented).
- **Complementary to structured documents:** Style sheets complement structured documents (such as HTML and SVG), providing  stylistic information for the marked-up text and other content. It should be easy to change the style sheet with little or no impact on the markup.
- **Vendor, platform, and device independence:** Style sheets enable documents to remain vendor, platform, and device independent. Style sheets themselves are also vendor and platform independent, however, CSS allows to target specific parts of a style sheet for a group of devices.
- **Maintainability:** Documents can link style sheets instead of containing them, allowing maintainers to retain a consistent look throughout the website.
- **Simplicity:** CSS is a simple style language which is human readable and writable. The CSS properties are kept independent of each other to the largest extent possible, and there is generally only one way to achieve a certain look.
- **Network performance:** CSS provides compact encodings for presenting the content, decreasing the content size. Moreover, few network connections have to be opened which further increases network performance.
- **Flexibility:** CSS can be applied to content in several ways. The key feature is the ability to cascade style information specified in the default (user agent) style sheet, user style sheets, linked style sheets, the document head, and in attributes for the elements forming the document body. 
- **Richness:** Providing authors with a rich set of rendering effects increases the richness of the web as a medium of expression.
- **Alternate language binding:** The CSS properties form a consistent formatting model for visual presentations. This formatting model can be accessed through the CSS language, but bindings to other languages (such as JavaScript) also exist.
- **Accessibility:** Several CSS features make the web more accessible to users with disabilities.

### Processing model

*The model presented here is only a conceptual model and therefore real implementations may vary*. In the processing model, a user agent processes a source by going through the following steps:

- Parse the source document and create a document tree.
- Identify the target media type.
- Retrieve all style sheets associated with the document that are specified for the target media type.
- Annotate every element of the document tree by assigning a single value to every property through cascading and inheritance.
- Generate a formatting structure from the annotated document tree.
- Transfer the formatting structure to the target medium for rendering.

### Applying CSS to HTML

A style sheet is used to describe the presentation of a document written in a supported markup language. For the styling to take effect, the source document must either contain or link to the style sheet. In HTML, there are three methods to add a style sheet:

- **Inline styles:** Applied by using the `style` attribute of an HTML element.
- **Internal style sheet:** Applied by using the `<style>` element in the `<head>` element.
- **External style sheet:** Applied by using the `<link>` element to link to an external CSS file.

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

## Part 2




## Part 4

### Appendix A: Style guide

- Items in a list are separated by a forward slash (`/`) only when the items are interchangeable. For most other cases, items in a list are separated by a comma (`,`).

  | Correct                                                    | Wrong                                                          |
  | ---------------------------------------------------------- | -------------------------------------------------------------- |
  | A keyboard/joystick/mouse should be used to play the game. | A keyword, joystick, or mouse should be used to play the game. |
  | The first few numbers are one, two, three, and four.       | The first few numbers are one/two/three/four.                  |

- If a comma-separated list contains only two items, the conjunction should not be preceded by a comma.
- If a comma-separated list contains more than two items, the conjunction should be preceded by a comma.

  | Correct                   | Wrong                    |
  | ------------------------- | ------------------------ |
  | This and that             | This, and that           |
  | One, two, three, and four | One, two, three and four |

- If a slash-separated list contains only items that are single words, there should not be any space between individual items.
- If a slash-separated list contains at least one item that is a compound word, there should a space on both sides of the slash.
  
  | Correct                             | Wrong                             |
  | ----------------------------------- | --------------------------------- |
  | Keyboard and/or mouse               | Keyboard and / or mouse           |
  | Processing model / addressing model | Processing model/addressing model |

- List items should be terminated by a period (`.`) only when at least one item in a list is a complete sentence or forms a complete sentence when combined with the introductory phrase.

- The spelling and formatting of the following words should be used as written.

  - style sheet
  - whitespace
  - semicolon

### Appendix B: Glossary

Ancestor
: An element A is called an ancestor of an element B, if and only if B is a descendant of A.

At-rule
: A structure that starts with an _at_ symbol, followed by an identifier, and continues up to the end of the statement.

Atomic inline
: An inline-level box that is replaced or that establishes a new formatting context, and cannot split across lines.

Attribute
: A value associated with an element, consisting of a name, and an associated textual value. 

Author
: An author is a person who writes documents and associated style sheets. An authoring tool is a user agent that generates style sheets.

Block box
: A block-level box that is also a block container. A block container does not necessarily have to be a block-level box, and a block-level box does not have to be a block container.

Block container
: A block container either contains only inline-level boxes participating in an inline formatting context, or contains only block-level boxes participating in a block formatting context, possibly generating anonymous block boxes to ensure this constraint.

Block formatting context root
: A block container that establishes a new block formatting context. 

Block layout
: The layout of block-level boxes, performed within a block formatting context. 

Block-level
: Content that participates in block layout, specifically, block-level boxes. 

Child
: An element A is called the child of element B if and only if B is the parent of A.

Containing block chain
: A sequence of successive containing blocks that form a chain of ancestors and descendants, through the containing block relation. 

Containing block
: A rectangle that forms the basis of sizing and positioning for the boxes associated with it. A containing block is a rectangle rather than a box, however it is often derived from the dimensions of a box. Each box is given a position with respect to its containing block, but it is not confined and can overflow.

Content
: The content associated with an element in the source document. Some elements have no content, in which case they are called empty. The content of an element may include text, and it may include a number of sub-elements, in which case the element is called the parent of those sub-elements. 

Declaration block
: A structure containing a list of declarations separated by semicolons and delimited by an opening brace and a closing brace.

Declaration
: A property and value pair separated by a colon, that together controls a presentational feature.

Descendant
: An element A is called a descendant of an element B, if either A is a child of B, or A is the child of some element C that is a descendant of B.

Document language
: The encoding language of the source document, such as HTML, XHTML, or SVG.

Document order
: The order in which boxes and content occurs in the document, which can be different from the order in which it appears for rendering. 

Document tree
: The tree of elements encoded in the source document. Each element in this tree has exactly one parent, with the exception of the root element, which has none.

Element
: The primary syntactic constructs of the document language.

Following element
: An element A is called a following element of an element B, if and only if B is a preceding element of A.

Formatting context
: A formatting context is the environment into which a set of related boxes are laid out.

In-flow
: A box is in-flow if it is not out-of-flow.

Independent formatting context
: An independent layout environment where the layout of its descendants is generally not affected by the rules and contents of the formatting context outside the box, except through the sizing of the box itself.

Initial containing block
: The containing block of the root element. The initial containing block establishes a block formatting context.

Inline box
: A non-replaced inline-level box whose inner display type is flow. The contents of an inline box participate in the same inline formatting context as the inline box itself. 

Inline-level
: Content that participates in inline layout, specifically, inline-level boxes and text runs. 

Intrinsic dimensions
: The width and height as defined by the element itself, not imposed by the surroundings.

Out-of-flow
: A box is out-of-flow if it is extracted from its expected position and laid out using a different paradigm outside the normal flow of content in its parent formatting context.

Preceding element
: An element A is called a preceding element of an element B, if and only if A is an ancestor of B or A is a preceding sibling of B.

Principal box
: When an element generates one or more boxes, one of them is the principal box, which contains its descendant boxes and generated content, and is also the box involved in any positioning scheme.

Property
: A human-readable identifier that defines a presentational feature to be considered.

Rendered content
: The content of an element after the rendering has been applied.

Replaced element
: An element whose content is outside the scope of the CSS formatting model, such as an image or embedded document. Replaced elements always establish an independent formatting context.

Root element
: The element at the root of the document tree. 

Ruleset
: A structure that associates a selector list with a declaration block.

Sibling
: An element A is called a sibling of an element B, if and only if B and A share the same parent element. Element A is a preceding sibling if it comes before B in the document tree. Element B is a following sibling if it comes after A in the document tree.

Source document
: The document to which one or more style sheets apply. This is encoded in some markup language that represents the document as a tree of elements.

Statement
: A structure that begins with any non-space character and ends at the first closing brace or semicolon.

User agent (UA)
: A user agent is any program that interprets a document written in the document language and applies associated style sheets. A user agent may display a document, read it aloud, cause it to be printed, or convert it to another format.

User
: A user is a person who interacts with a user agent to view, hear, or otherwise use a document and its associated style sheet. The user may provide a personal style sheet that encodes personal preferences.

Value
: An expression that describes how the presentational feature, defined by the associated property, must be handled.

Viewport
: A viewport is the viewing area on which the user agent displays the rendered document.

Visual formatting model
: The visual formatting model describes how user agents process the document tree and display it for visual media.
