# Z-index

In the most basic cases, HTML pages can be considered two-dimensional, because text, images, and other elements are arranged on the page without overlapping. In this case, there is a single rendering flow, and all elements are aware of the space taken by others. The `z-index` attribute lets you adjust the order of the layering of objects when rendering content.

This means that CSS style rules allow you to position boxes on layers in addition to the normal rendering layer (layer 0). The z-axis position of each layer is expressed as an integer representing the stacking order for rendering. Greater numbers mean closer to the observer. z-axis position can be controlled with the CSS `z-index` property.

Using `z-index` appears extremely easy: a single property, assigned a single integer number, with an easy-to-understand behavior. However, when z-index is applied to complex hierarchies of HTML elements, its behavior can be hard to understand or predict. This is due to complex stacking rules. In fact a dedicated section has been reserved in the CSS specification _CSS-2.1 Appendix E_ to explain these rules better.

## Stacking without the `z-index` property

When the `z-index` property is not specified on any element, elements are stacked in the following order (from bottom to top):

1. The background and borders of the root element.
2. Descendent non-positioned blocks, in order of appearance in the HTML.
3. Descendent positioned blocks, in order of appearance in the HTML.

Keep in mind, when the `order` property alters rendering from the "order of appearance in the HTML" within `flex` containers, it similarly affects the order for stacking context.

## Stacking with floated blocks

For floated blocks, the stacking order is a bit different. Floating blocks are placed between non-positioned blocks and positioned blocks:

1. The background and borders of the root element.
2. Descendent non-positioned blocks, in order of appearance in the HTML.
3. _Floating blocks_.
4. Descendent positioned blocks, in order of appearance in the HTML.

The background and border of non-positioned block is completely unaffected by floating blocks, but the content is affected. This happens according to standard float behavior. This behavior can be shown with an additional rule to the above list:

1. The background and borders of the root element.
2. Descendent non-positioned blocks, in order of appearance in the HTML.
3. Floating blocks.
4. _Descendent non-positioned inline blocks_.
5. Descendent positioned blocks, in order of appearance in the HTML.

> **Note:** If a declaration with `opacity` property is applied to a non-positioned block, then something strange happens: the background and border of that block pops up above the positioned blocks. This is due to a peculiar part of the specification: applying an `opacity` value creates a new stacking context.

## Using `z-index`

Besides default stacking, if you want to create a custom stacking order, you can use the `z-index` property on a _positioned_ element.

The `z-index` property can be specified with an integer value (positive, zero, or negative), which represents the position of the element along an imaginary z-axis. If you are not familiar with the z-axis, imagine the page as a stack of layers, each one having a number. Layers are rendered in numerical order, with larger numbers above smaller numbers:

| Layer                   | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| Bottom layer            | Farthest from the observer                            |
| Negative indexed layers | Layers with negative `z-index` values                 |
| Default rendering layer | Layer 0: applied when no `z-index` value is specified |
| Positive indexed layers | Layers with positive `z-index` values                 |
| Top layer               | Closest to the observer                               |

> **Note:**
>
> - When no `z-index` property is specified, elements are rendered on the default rendering layer 0.
> - If several elements share the same `z-index` value (thus are placed on the same layer), stacking rules explained in the previous section apply.

## Stacking context

The **stacking context** is a three-dimensional conceptualization of HTML elements along an imaginary z-axis relative to the user, who is assumed to be facing the viewport or the webpage. HTML elements occupy this space in priority order based on element attributes.

The rendering order of certain elements is influenced by their `z-index` value. This occurs because these elements have special properties which cause them to form a _stacking context_.

### Description

A stacking context is formed, anywhere in the document, by any element in the following scenarios:

- Root element of the document (`<html>`).
- Element with a `position` value `absolute` or `relative` and `z-index` value other than `auto`.
- Element with a `position` value `fixed` or `sticky` (sticky for all mobile browsers, but not older desktop).
- Element that is a child of a `flex` container, with `z-index` value other than `auto`.
- Element that is a child of a `grid` container, with `z-index` value other than `auto`.
- Element with an `opacity` value less than `1`.
- Element with a `mix-blend-mode` value other than `normal`.
- Element with any of the following properties with value other than `none`:

  - `transform`
  - `filter`
  - `backdrop-filter`
  - `perspective`
  - `clip-path`
  - `mask` / `mask-image` / `mask-border`

- Element with an `isolation` value `isolate`.
- Element with a `will-change` value specifying any property that would create a stacking context on non-initial value.
- Element with a `contain` value of `layout`, or `paint`, or a composite value that includes either of them (for example, `contain: strict`, `contain: content`).

Within a stacking context, child elements are stacked according to the same rules explained just above. Importantly, the `z-index` values of its child stacking contexts only have meaning in this parent. Stacking contexts are treated atomically as a single unit in the parent stacking context. In summary:

- Stacking contexts can be contained in other stacking contexts, and together create a hierarchy of stacking contexts.
- Each stacking context is completely independent of its siblings: only descendant elements are considered when stacking is processed.
- Each stacking context is self-contained: after the element's contents are stacked, the whole element is considered in the stacking order of the parent stacking context.

> **Note:** The hierarchy of stacking contexts is a subset of the hierarchy of HTML elements because only certain elements create stacking contexts. We can say that elements that do not create their own stacking contexts are _assimilated_ by the parent stacking context.
