# Introduction

Cascading Style Sheet (CSS) is a stylesheet language used to describe the presentation (or rendering) of a document written in HTML or XML (including XML dialects such as SVG, MathML, or XHTML).

CSS Level 3: CSS Level 3 builds on CSS Level 2 module by module, using the CSS2.1 specification as its core. Each module adds functionality and/or replaces part of the CSS2.1 specification. The CSS Working Group intends that the new CSS modules will not contradict the CSS2.1 specification: only that they will add functionality and refine definitions. As each module is completed, it will be plugged in to the existing system of CSS2.1 plus previously-completed modules.

From this level on modules are levelled independently: for example Selectors Level 4 may well be completed before CSS Line Module Level 3. Modules with no CSS Level 2 equivalent start at Level 1; modules that update features that existed in CSS Level 2 start at Level 3. CSS the language no longer has levels; "CSS Level 3" as a term is used only to differentiate it from the previous monolithic versions.

CSS style sheets that exist in separate files are sent over the Internet as a sequence of bytes accompanied by encoding information. The structure of the transmission, termed a message entity, is defined by RFC 2045 and RFC 2616 (see [RFC2045] and [RFC2616]). A message entity with a content type of "text/css" represents an independent CSS document. The "text/css" content type has been registered by RFC 2318 ([RFC2318]).

Partial implementations: So that authors can exploit the forward-compatible parsing rules to assign fallback values, CSS renderers must treat as invalid (and ignore as appropriate) any at-rules, properties, property values, keywords, and other syntactic constructs for which they have no usable level of support. In particular, user agents must not selectively ignore unsupported property values and honor supported values in a single multi-value property declaration: if any value is considered invalid (as unsupported values must be), CSS requires that the entire declaration be ignored.

Experimental and unstable features: Implementations of unstable features that are described in W3C specifications but are not interoperable should not be released broadly for general use; but may be released for limited, experimental use in controlled environments.

Proprietary and non-standardized features: To avoid clashes with future CSS features, the CSS2.1 specification reserves a prefixed syntax [CSS2] for proprietary and experimental extensions to CSS. A CSS feature is a proprietary extension if it is meant for use in a closed environment accessible only to a single vendor’s user agent(s). A UA should support such proprietary extensions only through a vendor-prefixed syntax and not expose them to open (multi-UA) environments such as the World Wide Web. Avoid encouraging the use of the vendor-prefixed syntax for any purpose other than working around implementation differences.

## Design principles

- Forward and backward compatibility. CSS 2.1 user agents will be able to understand CSS1 style sheets. CSS1 user agents will be able to read CSS 2.1 style sheets and discard parts they do not understand. Also, user agents with no CSS support will be able to display style-enhanced documents. Of course, the stylistic enhancements made possible by CSS will not be rendered, but all content will be presented.
- Complementary to structured documents. Style sheets complement structured documents (e.g., HTML and XML applications), providing stylistic information for the marked-up text. It should be easy to change the style sheet with little or no impact on the markup.
- Vendor, platform, and device independence. Style sheets enable documents to remain vendor, platform, and device independent. Style sheets themselves are also vendor and platform independent, but CSS 2.1 allows you to target a style sheet for a group of devices (e.g., printers).
- Maintainability. By pointing to style sheets from documents, webmasters can simplify site maintenance and retain consistent look and feel throughout the site. For example, if the organization's background color changes, only one file needs to be changed.
- Simplicity. CSS is a simple style language which is human readable and writable. The CSS properties are kept independent of each other to the largest extent possible and there is generally only one way to achieve a certain effect.
- Network performance. CSS provides for compact encodings of how to present content. Compared to images or audio files, which are often used by authors to achieve certain rendering effects, style sheets most often decrease the content size. Also, fewer network connections have to be opened which further increases network performance.
- Flexibility. CSS can be applied to content in several ways. The key feature is the ability to cascade style information specified in the default (user agent) style sheet, user style sheets, linked style sheets, the document head, and in attributes for the elements forming the document body.
- Richness. Providing authors with a rich set of rendering effects increases the richness of the Web as a medium of expression. Designers have been longing for functionality commonly found in desktop publishing and slide-show applications. Some of the requested rendering effects conflict with device independence, but CSS 2.1 goes a long way toward granting designers their requests.
- Alternative language bindings. The set of CSS properties described in this specification form a consistent formatting model for visual and aural presentations. This formatting model can be accessed through the CSS language, but bindings to other languages are also possible. For example, a JavaScript program may dynamically change the value of a certain element's 'color' property.
- Accessibility. Several CSS features will make the Web more accessible to users with disabilities:

    - Properties to control font appearance allow authors to eliminate inaccessible bit-mapped text images.
    - Positioning properties allow authors to eliminate mark-up tricks (e.g., invisible images) to force layout.
    - The semantics of !important rules mean that users with particular presentation requirements can override the author's style sheets.
    - The 'inherit' value for all properties improves cascading generality and allows for easier and more consistent style tuning.
    - Improved media support, including media groups and the braille, embossed, and tty media types, will allow users and authors to tailor pages to those devices. 


## Processing model

This section presents one possible model of how user agents that support CSS work. This is only a conceptual model; real implementations may vary.

In this model, a user agent processes a source by going through the following steps:

1. Parse the source document and create a document tree.
2. Identify the target media type.
3. Retrieve all style sheets associated with the document that are specified for the target media type.
4. Annotate every element of the document tree by assigning a single value to every property that is applicable to the target media type. Properties are assigned values according to the mechanisms described in the section on cascading and inheritance. Part of the calculation of values depends on the formatting algorithm appropriate for the target media type. For example, if the target medium is the screen, user agents apply the visual formatting model.
5. From the annotated document tree, generate a formatting structure. Often, the formatting structure closely resembles the document tree, but it may also differ significantly, notably when authors make use of pseudo-elements and generated content. First, the formatting structure need not be "tree-shaped" at all -- the nature of the structure depends on the implementation. Second, the formatting structure may contain more or less information than the document tree. For instance, if an element in the document tree has a value of 'none' for the 'display' property, that element will generate nothing in the formatting structure. A list element, on the other hand, may generate more information in the formatting structure: the list element's content and list style information (e.g., a bullet image). Note that the CSS user agent does not alter the document tree during this phase. In particular, content generated due to style sheets is not fed back to the document language processor (e.g., for reparsing).
6. Transfer the formatting structure to the target medium (e.g., print the results, display them on the screen, render them as speech, etc.). 

### The canvas

For all media, the term canvas describes "the space where the formatting structure is rendered." The canvas is infinite for each dimension of the space, but rendering generally occurs within a finite region of the canvas, established by the user agent according to the target medium. For instance, user agents rendering to a screen generally impose a minimum width and choose an initial width based on the dimensions of the viewport. User agents rendering to a page generally impose width and height constraints. Aural user agents may impose limits in audio space, but not in time. 

### CSS addressing model

CSS 2.1 selectors and properties allow style sheets to refer to the following parts of a document or user agent:

- Elements in the document tree and certain relationships between them (see the section on selectors).
- Attributes of elements in the document tree, and values of those attributes (see the section on attribute selectors).
- Some parts of element content (see the :first-line and :first-letter pseudo-elements).
- Elements of the document tree when they are in a certain state (see the section on pseudo-classes).
- Some aspects of the canvas where the document will be rendered.
- Some system information (see the section on user interface). 

## Conformance

Conformance: A style sheet is conformant to this specification if all of its statements that use syntax defined in this module are valid according to the generic CSS grammar and the individual grammars of each feature defined in this module.

This section defines conformance with the CSS 2.1 specification only. There may be other levels of CSS in the future that may require a user agent to implement a different set of features in order to conform.

In general, the following points must be observed by a user agent claiming conformance to this specification:

1. It must recognize one or more of the CSS 2.1 media types.
2. For each source document, it must attempt to retrieve all associated style sheets that are appropriate for the recognized media types. If it cannot retrieve all associated style sheets (for instance, because of network errors), it must display the document using those it can retrieve.
3. It must parse the style sheets according to this specification. In particular, it must recognize all at-rules, blocks, declarations, and selectors (see the grammar of CSS 2.1). If a user agent encounters a property that applies for a supported media type, the user agent must parse the value according to the property definition. This means that the user agent must accept all valid values and must ignore declarations with invalid values. User agents must ignore rules that apply to unsupported media types.
4. For each element in a document tree, it must assign a value for every property according to the property's definition and the rules of cascading and inheritance.
5. If the source document comes with alternate style sheet sets (such as with the "alternate" keyword in HTML 4 [HTML4]), the UA must allow the user to select which style sheet set the UA should apply.
6. The UA must allow the user to turn off the influence of author style sheets. 

Not every user agent must observe every point, however:

- An application that reads style sheets without rendering any content (e.g., a CSS 2.1 validator) must respect points 1-3.
- An authoring tool is only required to output valid style sheets
- A user agent that renders a document with associated style sheets must respect points 1-6 and render the document according to the media-specific requirements set forth in this specification. Values may be approximated when required by the user agent. 

The inability of a user agent to implement part of this specification due to the limitations of a particular device (e.g., a user agent cannot render colors on a monochrome monitor or page) does not imply non-conformance.

UAs must allow users to specify a file that contains the user style sheet. UAs that run on devices without any means of writing or specifying files are exempted from this requirement. Additionally, UAs may offer other means to specify user preferences, for example, through a GUI.

CSS 2.1 does not define which properties apply to form controls and frames, or how CSS can be used to style them. User agents may apply CSS properties to these elements. Authors are recommended to treat such support as experimental. A future level of CSS may specify this further. 

## Definitions

- Style sheet: A set of statements that specify presentation of a document. Style sheets may have three different origins: author, user, and user agent. The interaction of these sources is described in the section on cascading and inheritance. 
- Valid style sheet: The validity of a style sheet depends on the level of CSS used for the style sheet. All valid CSS1 style sheets are valid CSS 2.1 style sheets, but some changes from CSS1 mean that a few CSS1 style sheets will have slightly different semantics in CSS 2.1. Some features in CSS2 are not part of CSS 2.1, so not all CSS2 style sheets are valid CSS 2.1 style sheets. A valid CSS 2.1 style sheet must be written according to the grammar of CSS 2.1. Furthermore, it must contain only at-rules, property names, and property values defined in this specification. An illegal (invalid) at-rule, property name, or property value is one that is not valid. 
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
