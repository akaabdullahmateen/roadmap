# Syntax

<!-- omit in toc -->
## Table of contents

- [Glossary](#glossary)
- [Syntax](#syntax)
  - [Selectors list](#selectors-list)
  - [Properties list](#properties-list)
  - [Style rule](#style-rule)

## Glossary

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
