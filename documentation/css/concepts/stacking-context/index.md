# Stacking context

The **stacking context** is a three-dimensional conceptualization of HTML elements along an imaginary z-axis relative to the user, who is assumed to be facing the viewport or the webpage. HTML elements occupy this space in priority order based on element attributes.

## The stacking context

In the previous part of this article, [Using z-index](/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/Adding_z-index), we showed that the rendering order of certain elements is influenced by their `z-index` value. This occurs because these elements have special properties which cause them to form a _stacking context_.

A stacking context is formed, anywhere in the document, by any element in the following scenarios:

- Root element of the document (`<html>`).
- Element with a {{cssxref("position")}} value `absolute` or `relative` and {{cssxref("z-index")}} value other than `auto`.
- Element with a {{cssxref("position")}} value `fixed` or `sticky` (sticky for all mobile browsers, but not older desktop).
- Element that is a child of a [flex](/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox) container, with {{cssxref("z-index")}} value other than `auto`.
- Element that is a child of a {{cssxref("grid")}} container, with {{cssxref("z-index")}} value other than `auto`.
- Element with an {{cssxref("opacity")}} value less than `1` (See [the specification for opacity](https://www.w3.org/TR/css-color-3/#transparency)).
- Element with a {{cssxref("mix-blend-mode")}} value other than `normal`.
- Element with any of the following properties with value other than `none`:

  - {{cssxref("transform")}}
  - {{cssxref("filter")}}
  - {{cssxref("backdrop-filter")}}
  - {{cssxref("perspective")}}
  - {{cssxref("clip-path")}}
  - {{cssxref("mask")}} / {{cssxref("mask-image")}} / {{cssxref("mask-border")}}

- Element with an {{cssxref("isolation")}} value `isolate`.
- Element with a {{cssxref("will-change")}} value specifying any property that would create a stacking context on non-initial value (see [this post](https://dev.opera.com/articles/css-will-change-property/)).
- Element with a {{cssxref("contain")}} value of `layout`, or `paint`, or a composite value that includes either of them (i.e. `contain: strict`, `contain: content`).

Within a stacking context, child elements are stacked according to the same rules explained just above. Importantly, the `z-index` values of its child stacking contexts only have meaning in this parent. Stacking contexts are treated atomically as a single unit in the parent stacking context.

In summary:

- Stacking contexts can be contained in other stacking contexts, and together create a hierarchy of stacking contexts.
- Each stacking context is completely independent of its siblings: only descendant elements are considered when stacking is processed.
- Each stacking context is self-contained: after the element's contents are stacked, the whole element is considered in the stacking order of the parent stacking context.

> **Note:** The hierarchy of stacking contexts is a subset of the hierarchy of HTML elements because only certain elements create stacking contexts. We can say that elements that do not create their own stacking contexts are _assimilated_ by the parent stacking context.
