# Syntax

The basic goal of Cascading Stylesheet (CSS) language is to allow a browser engine to paint elements of the page with specific features, like color, positioning, or decoration. The _CSS syntax_ reflects this goal and its basic building blocks are:

- The **property** which is an identifier, that is a human-readable _name_, that defines which feature is considered.
- The **value** which describes how the feature must be handled by the engine. Each property has a set of valid values, defined by a formal grammar, as well as semantic meaning, implemented by the browser engine.

## CSS declarations

Setting CSS properties to specific values is the core function of the CSS language. A property and value pair is called a **declaration**, and any CSS engine calculates which declarations apply to every single element of a page in order to appropriately lay it out, and to style it.

Both properties and values are case-insensitive by default in CSS. The pair is separated by a colon, '`:`' (`U+003A COLON`), and white spaces before, between, and after properties and values, but not necessarily inside, are ignored.

There are more than 100 different properties in CSS and a nearly infinite number of different values. Not all pairs of properties and values are allowed, and each property defines what are the valid values. When a value is not valid for a given property, the declaration is deemed _invalid_ and is completely ignored by the CSS engine.

## CSS declaration blocks

Declarations are grouped in **blocks**, that is in a structure delimited by an opening braces, '`{`' (`U+007B LEFT CURLY BRACKET`), and a closing brace, '`}`' (`U+007D RIGHT CURLY BRACKET`). Blocks sometimes can be nested, so opening and closing braces must be matched.

Such blocks are naturally called **declaration blocks** and declarations inside them are separated by a semicolon, '`;`' (`U+003B SEMICOLON`). A declaration block may be empty, that is containing null declaration. White spaces around declarations are ignored. The last declaration of a block does not need to be terminated by a semicolon, though, it is often considered _good style_ to do it as it prevents forgetting to add it when extending the block with another declaration.

> **Note:** The content of a CSS declaration block, that is a list of semicolon-separated declarations, without the initial and closing braces, can be put inside an HTML `style` attribute.

## CSS rulesets

If stylesheets could only apply a declaration to each element of a web page, they would be pretty useless. The real goal is to apply different declarations to different parts of a document.

CSS allows this by associating conditions with declaration blocks. Each (valid) declaration block is preceded by one or more comma-separated **selectors**, which are conditions selecting some elements of the page. A selector group and an associated declaration block, together, are called a **ruleset**, or often a **rule**.

As an element on the page may be matched by several selectors, and therefore by several rules potentially containing a given property several times, with different values, the CSS standard defines which one has precedence over the other and must be applied: this is called the **cascade** algorithm.

> **Note:** It is important to note if a ruleset characterized by a group of selectors is a kind of shorthand replacing rulesets with a single selector each, this does not apply to the validity of the ruleset itself.
>
> This leads to an important consequence: if one single basic selector is invalid, like when using an unknown pseudo-element or pseudo-class, the whole _selector_ is invalid and therefore, the entire rule is invalid (and hence, ignored).