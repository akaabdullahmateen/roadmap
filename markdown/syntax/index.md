# Markdown: Syntax

<!-- omit in toc -->
## Table of contents

- [Headings](#headings)
  - [Syntax](#syntax)
  - [Lint](#lint)
- [Paragraphs](#paragraphs)
  - [Syntax](#syntax-1)
  - [Lint](#lint-1)
- [Line breaks](#line-breaks)
  - [Syntax](#syntax-2)
  - [Lint](#lint-2)
- [Typefaces](#typefaces)
  - [Bold](#bold)
    - [Syntax](#syntax-3)
    - [Lint](#lint-3)
  - [Italic](#italic)
    - [Syntax](#syntax-4)
    - [Lint](#lint-4)
  - [Strikethrough](#strikethrough)
    - [Syntax](#syntax-5)
  - [Highlight](#highlight)
    - [Syntax](#syntax-6)
  - [Subscript](#subscript)
    - [Syntax](#syntax-7)
  - [Superscript](#superscript)
    - [Syntax](#syntax-8)
- [Blockquotes](#blockquotes)
  - [Syntax](#syntax-9)
  - [Lint](#lint-5)
- [Lists](#lists)
  - [Ordered lists](#ordered-lists)
    - [Syntax](#syntax-10)
    - [Lint](#lint-6)
  - [Unordered lists](#unordered-lists)
    - [Syntax](#syntax-11)
    - [Lint](#lint-7)
  - [Nested lists](#nested-lists)
    - [Syntax](#syntax-12)
    - [Lint](#lint-8)
  - [Definition lists](#definition-lists)
    - [Syntax](#syntax-13)
  - [Task lists](#task-lists)
    - [Syntax](#syntax-14)
- [Code](#code)
  - [Inline code spans](#inline-code-spans)
    - [Syntax](#syntax-15)
    - [Lint](#lint-9)
  - [Indented code blocks](#indented-code-blocks)
    - [Syntax](#syntax-16)
  - [Fenced code blocks](#fenced-code-blocks)
    - [Syntax](#syntax-17)
    - [Lint](#lint-10)
- [Horizontal rules](#horizontal-rules)
  - [Syntax](#syntax-18)
  - [Lint](#lint-11)
- [Links](#links)
  - [Inline links](#inline-links)
    - [Syntax](#syntax-19)
  - [Image links](#image-links)
    - [Syntax](#syntax-20)
  - [Section links](#section-links)
    - [Syntax](#syntax-21)
  - [Autolinked references](#autolinked-references)
    - [Syntax](#syntax-22)
  - [Reference style links](#reference-style-links)
- [Images](#images)
  - [Syntax](#syntax-23)
- [Tables](#tables)
  - [Syntax](#syntax-24)
- [Comments](#comments)
  - [Syntax](#syntax-25)
- [Footnotes](#footnotes)
  - [Syntax](#syntax-26)
- [Emoji](#emoji)
  - [Syntax](#syntax-27)

## Headings

A heading in *atx* syntax, is created by adding hash characters (`#`) at the beginning of the line. At least one and at most six hash characters are supported corresponding to the heading levels `<h1>` to `<h6>`. Alternatively, in *setext* syntax, a heading is created by adding any number of `=` or `-` characters on the next line of a word or phrase. Although, *setext* syntax is supported by some Markdown parsers, *atx* syntax is more flexible and supported by almost all Markdown parsers.

### Syntax

| Markdown         | HTML               | Render           |
| ---------------- | ------------------ | ---------------- |
| `# Heading`      | `<h1>Heading</h1>` | <h1>Heading</h1> |
| `## Heading`     | `<h2>Heading</h2>` | <h2>Heading</h2> |
| `### Heading`    | `<h3>Heading</h3>` | <h3>Heading</h3> |
| `#### Heading`   | `<h4>Heading</h4>` | <h4>Heading</h4> |
| `##### Heading`  | `<h5>Heading</h5>` | <h5>Heading</h5> |
| `###### Heading` | `<h6>Heading</h6>` | <h6>Heading</h6> |

### Lint

Markdown parsers do not agree on how to handle a missing space between the hash character and the heading text. For compatibility, a space is added between the hash character and the heading text, and blank lines are added before and after a heading.

## Paragraphs

A paragraph is simply one or more consecutive lines of text. It is isolated from the other block elements, including other paragraphs, by any number of blank lines.

### Syntax

| Markdown                                                            | HTML               | Render           |
| ------------------------------------------------------------------- | ------------------ | ---------------- |
| **`U+000A END OF LINE`**<br>`Paragraph`<br>**`U+000A END OF LINE`** | `<p>Paragraph</p>` | <p>Paragraph</p> |

### Lint

Unless the paragraph is nested inside a list, it should not be indented with spaces or horizontal tabs, as indented lines of text characterize a code block. If a paragraph must be indented, HTML entity for non-breaking space (`&nbsp;`) can be used. Every instance of a non-breaking space entity is replaced by a space in the rendered output.

## Line breaks

A line break is created by adding two or more spaces at the end of a line, immediately followed by a line ending. Alternatively, the HTML tag `<br>` can be used to create a line break.

### Syntax

| Markdown                     | HTML              | Render          |
| ---------------------------- | ----------------- | --------------- |
| `Line` **`U+0020 SPACE X2`** | `<p>Line<br></p>` | <p>Line<br></p> |

### Lint

The trailing whitespaces are hard to see in an editor, and can be accidentally placed. It is therefore advised to use the HTML tag for line break, if the Markdown parser supports embedding HTML.

## Typefaces

### Bold

A portion of text is emphasized in bold typeface by adding two asterisk (`*`) or underscore characters (`_`) before and after it.

#### Syntax

| Markdown   | HTML                    | Render   |
| ---------- | ----------------------- | -------- |
| `**Bold**` | `<strong>Bold</strong>` | **Bold** |
| `__Bold__` | `<strong>Bold</strong>` | **Bold** |

#### Lint

Markdown parsers do not agree on how to handle underscores in the middle of a word. For compatibility, asterisks are used instead of underscores to emphasize a portion of a word.

### Italic

A portion of text is emphasized in italic typeface by adding one asterisk (`*`) or underscore character (`_`) before and after it.

#### Syntax

| Markdown   | HTML              | Render   |
| ---------- | ----------------- | -------- |
| `*Italic*` | `<em>Italic</em>` | *Italic* |
| `_Italic_` | `<em>Italic</em>` | *Italic* |

#### Lint

Markdown parsers do not agree on how to handle underscores in the middle of a word. For compatibility, asterisks are used instead of underscores to emphasize a portion of a word.

### Strikethrough

A portion of text is emphasized in strikethrough typeface by adding two tilde characters (`~`) before and after it.

#### Syntax

| Markdown            | HTML                   | Render            |
| ------------------- | ---------------------- | ----------------- |
| `~~Strikethrough~~` | `<s>Strikethrough</s>` | ~~Strikethrough~~ |

### Highlight

A portion of text is emphasized in highlight typeface by adding two equal characters (`=`) before and after it.

#### Syntax

| Markdown        | HTML                     | Render        |
| --------------- | ------------------------ | ------------- |
| `==Highlight==` | `<mark>Highlight</mark>` | ==Highlight== |

### Subscript

A portion of text is emphasized in subscript typeface by adding one tilde character (`~`) before and after it.

#### Syntax

| Markdown      | HTML                   | Render      |
| ------------- | ---------------------- | ----------- |
| `~Subscript~` | `<sub>Subscript</sub>` | ~Subscript~ |

### Superscript

A portion of text is emphasized in superscript typeface by adding one caret character (`^`) before and after it.

#### Syntax

| Markdown        | HTML                     | Render        |
| --------------- | ------------------------ | ------------- |
| `^Superscript^` | `<sup>Superscript</sup>` | ^Superscript^ |
 
## Blockquotes

A blockquote is created by adding a greater-than character (`>`) at the beginning of a block. This block can contain text as well as other block elements, including another blockquote. Multiple block elements are enclosed inside a blockquote by adding a greater-than character at the beginning of each line in the concerned blocks.

### Syntax

| Markdown                                        | HTML                                                                                                                 | Render                                                       |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| `> Block`                                       | `<blockquote>Block</blockquote>`                                                                                     | <blockquote>Block</blockquote>                               |
| <pre>&gt; Block<br>&gt;<br>&gt; Block</pre>     | <pre>&lt;blockquote&gt;<br>    &lt;p&gt;Block&lt;/p&gt;<br>    &lt;p&gt;Block&lt;/p&gt;<br>&lt;/blockquote&gt;</pre> | <blockquote><p>Block</p><p>Block</p></blockquote>            |
| <pre>&gt; Block<br>&gt;<br>&gt;&gt; Block</pre> | <pre>&lt;blockquote&gt;<br>    Block<br>    &lt;blockquote&gt;Block&lt;/blockquote&gt;<br>&lt;/blockquote&gt;</pre>  | <blockquote>Block<blockquote>Block</blockquote></blockquote> |

### Lint

Not all Markdown elements are supported to be nested inside a blockquote. Moreover, for compatibility, blank lines are added before and after a blockquote.

## Lists

### Ordered lists

An ordered list is created by adding an index number followed by a period character (`.`) at the beginning of each item in the list. These index numbers do not have to be in ascending order, but the list should start with the number `1`.

#### Syntax

| Markdown                      | HTML                                                                                                   | Render                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| <pre>1. Item<br>2. Item</pre> | <pre>&lt;ol&gt;<br>    &lt;li&gt;Item&lt;/li&gt;<br>    &lt;li&gt;Item&lt;/li&gt;<br>&lt;/ol&gt;</pre> | <ol><li>Item</li><li>Item</li></ol> |

#### Lint

Some Markdown parsers allow the closing parenthesis character (`)`) to be used as a delimiter, however, not all Markdown parsers support them. For compatibility, periods are used consistently as a delimiter.

### Unordered lists

An unordered list is created by adding either a hyphen (`-`), asterisk (`*`), or plus character (`+`) at the beginning of each item in the list.

#### Syntax

| Markdown                    | HTML                                                                                               | Render                              |
| --------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------- |
| <pre>- Item<br>- Item</pre> | <pre>&lt;ul&gt;<br>  &lt;li&gt;Item&lt;/li&gt;<br>  &lt;li&gt;Item&lt;/li&gt;<br>&lt;/ul&gt;</pre> | <ul><li>Item</li><li>Item</li></ul> |

#### Lint

Markdown parsers do not agree on how to handle different delimiters in the same list. For compatibility, different delimiters are not used interchangeably inside the same list. Moreover, list items starting with a number followed by a period character are escaped by adding a backslash character (`\`) before the period character.  

### Nested lists

Lists can be nested inside another list by indenting each list item four spaces or one horizontal tab. Other block elements can be added by indentation as well, while preserving the continuity of the list.

#### Syntax

| Markdown                                                  | HTML                                                                                                                                                                                                                   | Render                                                                 |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| <pre>- Item<br>    1. Item<br>    2. Item<br>- Item</pre> | <pre>&lt;ul&gt;<br>    &lt;li&gt;Item<br>    &lt;ol&gt;<br>        &lt;li&gt;Item&lt;/li&gt;<br>        &lt;li&gt;Item&lt;/li><br>    &lt;/ol&gt;<br>&lt;/li&gt;<br>    &lt;li&gt;Item&lt;/li&gt;<br>&lt;/ul&gt;</pre> | <ul><li>Item</li><ol><li>Item</li><li>Item</li></ol><li>Item</li></ul> |

#### Lint

Code blocks are characterized by indenting them four spaces or one horizontal tab. Therefore, to nest a code block inside a list, indent each code line by an additional four spaces or one horizontal tab.

### Definition lists

A definition list is created by adding the definition term on one line, and colon followed by a space and the definition text on the next line.

#### Syntax

| Markdown                        | HTML                                                                                                         | Render                                    |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------- |
| <pre>Term<br>: Definition</pre> | <pre>&lt;dl&gt;<br>    &lt;dt&gt;Term&lt;/dt&gt;<br>    &lt;dd&gt;Definition&lt;/dd&gt;<br>&lt;/dl&gt;</pre> | <dl><dt>Term</dt><dd>Definition</dd></dl> |

### Task lists

A task list is created by adding a hyphen character followed by a pair of square brackets with a space inside, in front of each task list item. To select a checkbox, add the character `x` in between the brackets.

#### Syntax

| Markdown                                | HTML                                                                                                                                                                                                                                       | Render                   |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| <pre>`- [x]` Task<br>`- [ ]` Task</pre> | <pre>&lt;input type="checkbox" id="checkbox1" checked="true"&gt;<br>&lt;label for="checkbox1"&gt;Task&lt;/label&gt;<br>&lt;br&gt;<br>&lt;input type="checkbox" id="checkbox2"&gt;<br>&lt;label for="checkbox2"&gt;Task&lt;/label&gt;</pre> | - [x] Task<br>- [ ] Task |

## Code

### Inline code spans

A text fragment is denoted as a code fragment by enclosing it within a backticks (<code>`</code>).

#### Syntax

| Markdown     | HTML                | Render |
| ------------ | ------------------- | ------ |
| `` `Code` `` | `<code>Code</code>` | `Code` |

#### Lint

If the text fragment includes backticks as content, these backticks must be escaped with a backslash, or the enclosing backticks must be replaced by double backticks.

### Indented code blocks

A code block is created by indenting each line of the block by an additional four spaces or one horizontal tab.

#### Syntax

| Markdown                | HTML              | Render          |
| ----------------------- | ----------------- | --------------- |
| **`U+0009 TAB`** `Code` | `<pre>Code</pre>` | <pre>Code</pre> |


### Fenced code blocks

Code blocks can alternatively by created by adding three backtick characters (<code>`</code>) on the lines before and after the code block.

#### Syntax

| Markdown                                | HTML              | Render          |
| --------------------------------------- | ----------------- | --------------- |
| <pre>\```markdown<br>Code<br>\```</pre> | `<pre>Code</pre>` | <pre>Code</pre> |

#### Lint

Syntax highlighting is supported by adding the code language immediately next to the three backtick characters on the line preceding the code block.

## Horizontal rules

Horizontal rules are created by adding three or more asterisk (`*`), hyphen (`-`), or underscore characters (`_`) on a line, containing nothing else.

### Syntax

| Markdown | HTML   | Render |
| -------- | ------ | ------ |
| `---`    | `<hr>` | <hr>   |

### Lint

For compatibility, blank lines are placed before and after a horizontal rule.

## Links

### Inline links

An inline link is created by enclosing the link text within a pair of square brackets (`[]`) and specifying the link address, enclosed within a pair of parenthesis (`()`), immediately next to it. Link titles are an optional feature that appear as a tooltip text on mouse hover. They can be added by adding the title text, enclosed within a pair of quotation marks (`""`), in the link address parenthesis, following the link address.

#### Syntax

| Markdown                              | HTML                                                   | Render                              |
| ------------------------------------- | ------------------------------------------------------ | ----------------------------------- |
| `[Link](https://example.com "Title")` | `<a href="https://example.com" title="Title">Link</a>` | [Link](https://example.com "Title") |

### Image links

#### Syntax

| Markdown                                                    | HTML                                                                                                                              | Render                                                    |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| `[![Text](assets/sample.png)](https://example.com "Title")` | <pre>&lt;a href="https://example.com" title="Title"&gt;<br>    &lt;img src="assets/sample.png" alt="Text"&gt;<br>&lt;/a&gt;</pre> | [![Text](assets/sample.png)](https://example.com "Title") |

### Section links

#### Syntax

| Markdown                                                        | HTML                                                                                                            | Render                                          |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| <pre># Heading {#identity}<br>\[Link\](#identity "Title")</pre> | <pre>&lt;h1 id="identity"&gt;Heading&lt;/h1&gt;<br>&lt;a href="#identity" title="Title"&gt;Link&lt;/a&gt;</pre> | <h1 id="identity">Heading</h1>[Link](#identity) |

### Autolinked references

#### Syntax

| Markdown                | HTML                                                             | Render                |
| ----------------------- | ---------------------------------------------------------------- | --------------------- |
| `<https://example.com>` | `<a href="https://example.com">https://example.com</a>`          | <https://example.com> |
| `<noreply@example.com>` | `<a href="mailto://noreply@example.com">noreply@example.com</a>` | <noreply@example.com> |

### Reference style links

| Markdown                                                 | HTML                                                   | Render                              |
| -------------------------------------------------------- | ------------------------------------------------------ | ----------------------------------- |
| <pre>[Link][1]<br>[1]: https://example.com "Title"</pre> | `<a href="https://example.com" title="Title">Link</a>` | [Link](https://example.com "Title") |

## Images

### Syntax

| Markdown                     | HTML                                       | Render                     |
| ---------------------------- | ------------------------------------------ | -------------------------- |
| `![Text](assets/sample.png)` | `<img src="assets/sample.png" alt="Text">` | ![Text](assets/sample.png) |

## Tables

### Syntax

| Markdown                                                                              | HTML                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Render                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <pre>\| Header \| Header \|<br>\| ------ \| ------ \|<br>\| Item   \| Item   \|</pre> | <pre>&lt;table&gt;<br>    &lt;thead&gt;<br>        &lt;tr&gt;<br>            &lt;th&gt;Header&lt;/th&gt;<br>            &lt;th&gt;Header&lt;/th&gt;<br>        &lt;/tr&gt;<br>    &lt;/thead&gt;<br>    &lt;tbody&gt;<br>        &lt;tr&gt;<br>            &lt;td&gt;Item&lt;/td&gt;<br>            &lt;td&gt;Item&lt;/td&gt;<br>        &lt;/tr&gt;<br>    &lt;/tbody&gt;<br>&lt;/table&gt;</pre>                                                                                                               | <table><thead><tr><th>Header</th><th>Header</th></tr></thead><tbody><tr><td>Item</td><td>Item</td></tr></tbody></table>                                                                                                               |
| <pre>\| Header \| Header \|<br>\| :----: \| -----: \|<br>\| Item   \| Item   \|</pre> | <pre>&lt;table&gt;<br>    &lt;thead&gt;<br>        &lt;tr&gt;<br>            &lt;th style="text-align: center;"&gt;Header&lt;/th&gt;<br>            &lt;th style="text-align: right;"&gt;Header&lt;/th&gt;<br>        &lt;/tr&gt;<br>    &lt;/thead&gt;<br>    &lt;tbody&gt;<br>        &lt;tr&gt;<br>            &lt;td style="text-align: center;"&gt;Item&lt;/td&gt;<br>            &lt;td style="text-align: right;"&gt;Item&lt;/td&gt;<br>        &lt;/tr&gt;<br>    &lt;/tbody&gt;<br>&lt;/table&gt;</pre> | <table><thead><tr><th style="text-align: center;">Header</th><th style="text-align: right;">Header</th></tr></thead><tbody><tr><td style="text-align: center;">Item</td><td style="text-align: right;">Item</td></tr></tbody></table> |

## Comments

### Syntax

| Markdown           | HTML               | Render           |
| ------------------ | ------------------ | ---------------- |
| `<!-- Comment -->` | `<!-- Comment -->` | <!-- Comment --> |

## Footnotes

### Syntax

| Markdown                                   | HTML                                                                                                                                                                                                                                                                                                                       | Render   |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| <pre>Text\[\^1\]<br>\[^1\]: Footnote</pre> | <pre>Text<br>&lt;sup id="#fnref:1" role="doc-noteref"&gt;<br>    &lt;a class="footnote" href="#fn:1" rel="footnote"&gt;1&lt;/a&gt;<br>&lt;/sup&gt;<br>&lt;ol&gt;<br>    &lt;li&gt;Footnote<br>    &lt;a class="reversefootnote" href="#fnref:1" role="doc-backlink"&gt;↩&lt;/a&gt;<br>    &lt;/li&gt;<br>&lt;/ol&gt;</pre> | Text[^1] |

[^1]: Footnote

## Emoji

### Syntax

| Markdown  | HTML        | Render  |
| --------- | ----------- | ------- |
| `:smile:` | `&#128516;` | :smile: |
