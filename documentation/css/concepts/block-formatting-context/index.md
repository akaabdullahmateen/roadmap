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

> **Note:** A Flex / Grid container (`display: flex / grid / inline-flex / inline-grid`) establishes a new Flex / Grid formatting context, which is similar to block formatting context except layout. There is no floating children available inside a flex / grid container, but exclude external floats and suppress margin collapsing still works.

## Examples

### Contain internal floats

Make float content and alongside content the same height.

Let's have a look at a couple of these in order to see the effect creating a new BFC.

In the following example, we have a floated element inside a `<div>` with a `border` applied. The content of that `<div>` has floated alongside the floated element. As the content of the float is taller than the content alongside it, the border of the `<div>` now runs through the float. As explained in the [guide to in-flow and out of flow elements](/en-US/docs/Web/CSS/CSS_Flow_Layout/In_Flow_and_Out_of_Flow), the float has been taken out of flow so the `background` and `border` of the `<div>` only contain the content and not the float.

**using `overflow: auto`**

Setting `overflow: auto` or set other values than the initial value of `overflow: visible` created a new BFC containing the float. Our `<div>` now becomes a mini-layout inside our layout. Any child element will be contained inside it.

The problem with using `overflow` to create a new BFC is that the `overflow` property is meant for telling the browser how you want to deal with overflowing content. There are some occasions in which you will find you get unwanted scrollbars or clipped shadows when you use this property purely to create a BFC. In addition, it is potentially not readable for a future developer, as it might not be obvious why you used `overflow` for this purpose. If you use `overflow`, it is a good idea to comment the code to explain.

**using `display: flow-root`**

A newer value of `display` lets us create a new BFC without any other potentially problematic side-effects. Using `display: flow-root` on the containing block creates a new BFC .

With `display: flow-root;` on the `<div>`, everything inside that container participates in the block formatting context of that container, and floats will not poke out of the bottom of the element.

The value name of `flow-root` makes sense when you understand you are creating something that acts like the `root` element (`<html>` element in browser) in terms of how it creates a new context for the flow layout inside it.

### Exclude external floats

In the following example, we are using `display:flow-root` and floats to implement double columns layout. We are able to do this because an element in the normal flow that establishes a new BFC does not overlap the margin box of any floats in the same block formatting context as the element itself.

Rather than inline-blocks with width:\<percentage>, in this case we don't have to specify the width of the right div.

Note that flexbox is a more efficient way to implement multi-column layout in modern CSS.

### Prevent margin collapsing

You can create a new BFC to avoid [margin collapsing](/en-US/docs/Web/CSS/CSS_Box_Model/Mastering_margin_collapsing) between two neighbor elements.

#### Margin collapsing example

In this example we have two adjacent `<div>` elements, which each have a vertical margin of `10px`. Because of margin collapsing, the vertical gap between them is 10 pixels, not the 20 we might expect.
