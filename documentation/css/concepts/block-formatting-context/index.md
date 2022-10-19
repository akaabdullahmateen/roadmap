# Block formatting context

A **block formatting context** (BFC) is part of the visual CSS rendering of a web page. It is the region in which the layout of block boxes occurs and in which floats interact with other elements.

A block formatting context is created by at least one of the following:

- The root element of the document (`<html>`).
- Floats (elements where `float` is not `none`).
- Absolutely positioned elements (elements where `position` is `absolute` or `fixed`).
- Inline-blocks (elements with `display: inline-block`).
- Table cells (elements with `display: table-cell`, which is the default for HTML table cells).
- Table captions (elements with `display: table-caption`, which is the default for HTML table captions).
- Anonymous table cells implicitly created by the elements with `display: table / table-row / table-row-group / table-header-group / table-footer-group` (which is the default for HTML tables, table rows, table bodies, table headers, and table footers, respectively), or `inline-table`.
- Block elements where `overflow` has a value other than `visible` and `clip`.
- `display``: flow-root`.
- Elements with `contain: layout / content / paint`.
- Flex items (direct children of the element with `display: flex / inline-flex`) if they are neither `flex` nor `grid` containers themselves.
- Grid items (direct children of the element with `display: grid / inline-grid`) if they are neither `flex` nor `grid` containers themselves.
- Multi-column containers (elements where `column-count` or `column-width` is not `auto`, including elements with `column-count: 1`).
- Having `column-span``: all` should always create a new formatting context, even when the `column-span: all` element is not contained by a multi-column container.

Formatting contexts affect layout, but typically, we create a new block formatting context for the positioning and clearing floats rather than changing the layout, because an element that establishes a new block formatting context will:

- contain internal floats.
- exclude external floats.
- suppress _margin collapsing_.

> **Note:** A flex / grid container (`display: flex / grid / inline-flex / inline-grid`) establishes a new flex / grid formatting context, which is similar to block formatting context except layout. There is no floating children available inside a flex / grid container, but exclude external floats and suppress margin collapsing still works.
