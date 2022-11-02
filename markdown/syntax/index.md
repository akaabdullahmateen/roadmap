# Markdown: Syntax

---

## Table of contents

- [Table of contents](#table-of-contents)
- [Headings](#headings)
- [Paragraphs](#paragraphs)
- [Images](#images)
- [Tables](#tables)
- [Text styles](#text-styles)
  - [Bold](#bold)
  - [Italic](#italic)
  - [Strikethrough](#strikethrough)
  - [Highlight](#highlight)
  - [Subscript](#subscript)
  - [Superscript](#superscript)
- [Lists](#lists)
  - [Ordered lists](#ordered-lists)
  - [Unordered lists](#unordered-lists)
  - [Nested lists](#nested-lists)
  - [Definition lists](#definition-lists)
  - [Task lists](#task-lists)
- [Code](#code)
  - [Inline code fragments](#inline-code-fragments)
  - [Fenced code blocks](#fenced-code-blocks)
  - [Indented code blocks](#indented-code-blocks)
- [Links](#links)
  - [Inline links](#inline-links)
  - [Image links](#image-links)
  - [Section links](#section-links)
  - [Autolinked references](#autolinked-references)
  - [Reference style links](#reference-style-links)
- [Blockquotes](#blockquotes)
  - [Continuous blockquotes](#continuous-blockquotes)
  - [Nested blockquotes](#nested-blockquotes)
- [Control elements](#control-elements)
  - [Line breaks](#line-breaks)
  - [Horizontal rules](#horizontal-rules)
  - [Comments](#comments)
- [Extended elements](#extended-elements)
  - [Footnotes](#footnotes)
  - [Emoji](#emoji)

---

## Headings

| Markdown         | HTML               | Render           |
| ---------------- | ------------------ | ---------------- |
| `# Heading`      | `<h1>Heading</h1>` | <h1>Heading</h1> |
| `## Heading`     | `<h2>Heading</h2>` | <h2>Heading</h2> |
| `### Heading`    | `<h3>Heading</h3>` | <h3>Heading</h3> |
| `#### Heading`   | `<h4>Heading</h4>` | <h4>Heading</h4> |
| `##### Heading`  | `<h5>Heading</h5>` | <h5>Heading</h5> |
| `###### Heading` | `<h6>Heading</h6>` | <h6>Heading</h6> |

---

## Paragraphs

| Markdown                                                            | HTML               | Render           |
| ------------------------------------------------------------------- | ------------------ | ---------------- |
| **`U+000A END OF LINE`**<br>`Paragraph`<br>**`U+000A END OF LINE`** | `<p>Paragraph</p>` | <p>Paragraph</p> |

---

## Images

| Markdown                   | HTML                                     | Render                   |
| -------------------------- | ---------------------------------------- | ------------------------ |
| `![Text](assets/logo.png)` | `<img src="assets/logo.png" alt="Text">` | ![Text](assets/logo.png) |

---

## Tables

| Markdown                                                                              | HTML                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Render                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <pre>\| Header \| Header \|<br>\| ------ \| ------ \|<br>\| Item   \| Item   \|</pre> | <pre>&lt;table&gt;<br>    &lt;thead&gt;<br>        &lt;tr&gt;<br>            &lt;th&gt;Header&lt;/th&gt;<br>            &lt;th&gt;Header&lt;/th&gt;<br>        &lt;/tr&gt;<br>    &lt;/thead&gt;<br>    &lt;tbody&gt;<br>        &lt;tr&gt;<br>            &lt;td&gt;Item&lt;/td&gt;<br>            &lt;td&gt;Item&lt;/td&gt;<br>        &lt;/tr&gt;<br>    &lt;/tbody&gt;<br>&lt;/table&gt;</pre>                                                                                                               | <table><thead><tr><th>Header</th><th>Header</th></tr></thead><tbody><tr><td>Item</td><td>Item</td></tr></tbody></table>                                                                                                               |
| <pre>\| Header \| Header \|<br>\| :----: \| -----: \|<br>\| Item   \| Item   \|</pre> | <pre>&lt;table&gt;<br>    &lt;thead&gt;<br>        &lt;tr&gt;<br>            &lt;th style="text-align: center;"&gt;Header&lt;/th&gt;<br>            &lt;th style="text-align: right;"&gt;Header&lt;/th&gt;<br>        &lt;/tr&gt;<br>    &lt;/thead&gt;<br>    &lt;tbody&gt;<br>        &lt;tr&gt;<br>            &lt;td style="text-align: center;"&gt;Item&lt;/td&gt;<br>            &lt;td style="text-align: right;"&gt;Item&lt;/td&gt;<br>        &lt;/tr&gt;<br>    &lt;/tbody&gt;<br>&lt;/table&gt;</pre> | <table><thead><tr><th style="text-align: center;">Header</th><th style="text-align: right;">Header</th></tr></thead><tbody><tr><td style="text-align: center;">Item</td><td style="text-align: right;">Item</td></tr></tbody></table> |

---

## Text styles

### Bold

| Markdown   | HTML                    | Render   |
| ---------- | ----------------------- | -------- |
| `**Bold**` | `<strong>Bold</strong>` | **Bold** |
| `__Bold__` | `<strong>Bold</strong>` | **Bold** |

### Italic

| Markdown   | HTML              | Render   |
| ---------- | ----------------- | -------- |
| `*Italic*` | `<em>Italic</em>` | *Italic* |
| `_Italic_` | `<em>Italic</em>` | *Italic* |

### Strikethrough

| Markdown            | HTML                   | Render            |
| ------------------- | ---------------------- | ----------------- |
| `~~Strikethrough~~` | `<s>Strikethrough</s>` | ~~Strikethrough~~ |

### Highlight

| Markdown        | HTML                     | Render        |
| --------------- | ------------------------ | ------------- |
| `==Highlight==` | `<mark>Highlight</mark>` | ==Highlight== |

### Subscript

| Markdown      | HTML                   | Render      |
| ------------- | ---------------------- | ----------- |
| `~Subscript~` | `<sub>Subscript</sub>` | ~Subscript~ |

### Superscript

| Markdown        | HTML                     | Render        |
| --------------- | ------------------------ | ------------- |
| `^Superscript^` | `<sup>Superscript</sup>` | ^Superscript^ |

---

## Lists

### Ordered lists

| Markdown                      | HTML                                                                                                   | Render                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| <pre>1. Item<br>2. Item</pre> | <pre>&lt;ol&gt;<br>    &lt;li&gt;Item&lt;/li&gt;<br>    &lt;li&gt;Item&lt;/li&gt;<br>&lt;/ol&gt;</pre> | <ol><li>Item</li><li>Item</li></ol> |

### Unordered lists

| Markdown                    | HTML                                                                                               | Render                              |
| --------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------- |
| <pre>- Item<br>- Item</pre> | <pre>&lt;ul&gt;<br>  &lt;li&gt;Item&lt;/li&gt;<br>  &lt;li&gt;Item&lt;/li&gt;<br>&lt;/ul&gt;</pre> | <ul><li>Item</li><li>Item</li></ul> |

### Nested lists

| Markdown                                                  | HTML                                                                                                                                                                                                                   | Render                                                                 |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| <pre>- Item<br>    1. Item<br>    2. Item<br>- Item</pre> | <pre>&lt;ul&gt;<br>    &lt;li&gt;Item<br>    &lt;ol&gt;<br>        &lt;li&gt;Item&lt;/li&gt;<br>        &lt;li&gt;Item&lt;/li><br>    &lt;/ol&gt;<br>&lt;/li&gt;<br>    &lt;li&gt;Item&lt;/li&gt;<br>&lt;/ul&gt;</pre> | <ul><li>Item</li><ol><li>Item</li><li>Item</li></ol><li>Item</li></ul> |

### Definition lists

| Markdown                        | HTML                                                                                                         | Render                                    |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------- |
| <pre>Term<br>: Definition</pre> | <pre>&lt;dl&gt;<br>    &lt;dt&gt;Term&lt;/dt&gt;<br>    &lt;dd&gt;Definition&lt;/dd&gt;<br>&lt;/dl&gt;</pre> | <dl><dt>Term</dt><dd>Definition</dd></dl> |

### Task lists

| Markdown                                | HTML                                                                                                                                                                                                                                       | Render                   |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| <pre>`- [x]` Task<br>`- [ ]` Task</pre> | <pre>&lt;input type="checkbox" id="checkbox1" checked="true"&gt;<br>&lt;label for="checkbox1"&gt;Task&lt;/label&gt;<br>&lt;br&gt;<br>&lt;input type="checkbox" id="checkbox2"&gt;<br>&lt;label for="checkbox2"&gt;Task&lt;/label&gt;</pre> | - [x] Task<br>- [ ] Task |

---

## Code

### Inline code fragments

| Markdown     | HTML                | Render |
| ------------ | ------------------- | ------ |
| `` `Code` `` | `<code>Code</code>` | `Code` |

### Fenced code blocks

| Markdown                                | HTML              | Render          |
| --------------------------------------- | ----------------- | --------------- |
| <pre>\```markdown<br>Code<br>\```</pre> | `<pre>Code</pre>` | <pre>Code</pre> |

### Indented code blocks

| Markdown                | HTML              | Render          |
| ----------------------- | ----------------- | --------------- |
| **`U+0009 TAB`** `Code` | `<pre>Code</pre>` | <pre>Code</pre> |

---

## Links

### Inline links

| Markdown                              | HTML                                                   | Render                              |
| ------------------------------------- | ------------------------------------------------------ | ----------------------------------- |
| `[Link](https://example.com "Title")` | `<a href="https://example.com" title="Title">Link</a>` | [Link](https://example.com "Title") |

### Image links

| Markdown                                                  | HTML                                                                                                                            | Render                                                  |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| `[![Text](assets/logo.png)](https://example.com "Title")` | <pre>&lt;a href="https://example.com" title="Title"&gt;<br>    &lt;img src="assets/logo.png" alt="Text"&gt;<br>&lt;/a&gt;</pre> | [![Text](assets/logo.png)](https://example.com "Title") |

### Section links

| Markdown                                                        | HTML                                                                                                            | Render                                          |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| <pre># Heading {#identity}<br>\[Link\](#identity "Title")</pre> | <pre>&lt;h1 id="identity"&gt;Heading&lt;/h1&gt;<br>&lt;a href="#identity" title="Title"&gt;Link&lt;/a&gt;</pre> | <h1 id="identity">Heading</h1>[Link](#identity) |

### Autolinked references

| Markdown                | HTML                                                             | Render                |
| ----------------------- | ---------------------------------------------------------------- | --------------------- |
| `<https://example.com>` | `<a href="https://example.com">https://example.com</a>`          | <https://example.com> |
| `<noreply@example.com>` | `<a href="mailto://noreply@example.com">noreply@example.com</a>` | <noreply@example.com> |

### Reference style links

| Markdown                                                 | HTML                                                   | Render                              |
| -------------------------------------------------------- | ------------------------------------------------------ | ----------------------------------- |
| <pre>[Link][1]<br>[1]: https://example.com "Title"</pre> | `<a href="https://example.com" title="Title">Link</a>` | [Link](https://example.com "Title") |

---

## Blockquotes

### Continuous blockquotes

| Markdown                                    | HTML                                                                                                                 | Render                                            |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| `> Blockquote`                              | `<blockquote>Blockquote</blockquote>`                                                                                | <blockquote>Blockquote</blockquote>               |
| <pre>&gt; Quote<br>&gt;<br>&gt; Quote</pre> | <pre>&lt;blockquote&gt;<br>    &lt;p&gt;Quote&lt;/p&gt;<br>    &lt;p&gt;Quote&lt;/p&gt;<br>&lt;/blockquote&gt;</pre> | <blockquote><p>Quote</p><p>Quote</p></blockquote> |

### Nested blockquotes

| Markdown                                        | HTML                                                                                                                | Render                                                       |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| <pre>&gt; Quote<br>&gt;<br>&gt;&gt; Quote</pre> | <pre>&lt;blockquote&gt;<br>    Quote<br>    &lt;blockquote&gt;Quote&lt;/blockquote&gt;<br>&lt;/blockquote&gt;</pre> | <blockquote>Quote<blockquote>Quote</blockquote></blockquote> |

---

## Control elements

### Line breaks

| Markdown                     | HTML              | Render          |
| ---------------------------- | ----------------- | --------------- |
| `Line` **`U+0020 SPACE X2`** | `<p>Line<br></p>` | <p>Line<br></p> |

### Horizontal rules

| Markdown | HTML   | Render |
| -------- | ------ | ------ |
| `---`    | `<hr>` | <hr>   |

### Comments

| Markdown           | HTML               | Render           |
| ------------------ | ------------------ | ---------------- |
| `<!-- Comment -->` | `<!-- Comment -->` | <!-- Comment --> |

---

## Extended elements

### Footnotes

| Markdown                                   | HTML                                                                                                                                                                                                                                                                                                                       | Render   |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| <pre>Text\[\^1\]<br>\[^1\]: Footnote</pre> | <pre>Text<br>&lt;sup id="#fnref:1" role="doc-noteref"&gt;<br>    &lt;a class="footnote" href="#fn:1" rel="footnote"&gt;1&lt;/a&gt;<br>&lt;/sup&gt;<br>&lt;ol&gt;<br>    &lt;li&gt;Footnote<br>    &lt;a class="reversefootnote" href="#fnref:1" role="doc-backlink"&gt;↩&lt;/a&gt;<br>    &lt;/li&gt;<br>&lt;/ol&gt;</pre> | Text[^1] |

[^1]: Footnote

### Emoji

| Markdown  | HTML        | Render  |
| --------- | ----------- | ------- |
| `:smile:` | `&#128516;` | :smile: |

---
