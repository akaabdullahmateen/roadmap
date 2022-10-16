---
title: Layout and the containing block
slug: Web/CSS/Containing_block
page-type: guide
tags:
  - CSS
  - CSS Position
  - Containers
  - Guide
  - Layout
  - Position
  - Style
  - blocks
  - containing block
  - size
---

{{CSSRef}}

The size and position of an element are often impacted by its **containing block**. Most often, the containing block is the [content area](/en-US/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model#content_area) of an element's nearest [block-level](/en-US/docs/Web/HTML/Block-level_elements) ancestor, but this is not always the case. In this article, we examine the factors that determine an element's containing block.

When a user agent (such as your browser) lays out a document, it generates a box for every element. Each box is divided into four areas:

1. Content area
2. Padding area
3. Border area
4. Margin area

![Diagram of the box model](box-model.png)

Many developers believe that the containing block of an element is always the content area of its parent, but that isn't necessarily true. Let's investigate the factors that determine what an element's containing block is.

## Effects of the containing block

Before learning what determines the containing block of an element, it's useful to know why it matters in the first place.

The size and position of an element are often impacted by its containing block. Percentage values that are applied to the {{cssxref("width")}}, {{cssxref("height")}}, {{cssxref("padding")}}, {{cssxref("margin")}}, and offset properties of an absolutely positioned element (i.e., which has its {{cssxref("position")}} set to `absolute` or `fixed`) are computed from the element's containing block.

## Identifying the containing block

The process for identifying the containing block depends entirely on the value of the element's {{cssxref("position")}} property:

1. If the `position` property is **`static`**, **`relative`**, or **`sticky`**, the containing block is formed by the edge of the _content box_ of the nearest ancestor element that is either **a block container** (such as an inline-block, block, or list-item element) or **establishes a formatting context** (such as a table container, flex container, grid container, or the block container itself).
2. If the `position` property is **`absolute`**, the containing block is formed by the edge of the _padding box_ of the nearest ancestor element that has a `position` value other than `static` (`fixed`, `absolute`, `relative`, or `sticky`).
3. If the `position` property is **`fixed`**, the containing block is established by the {{glossary("viewport")}} (in the case of continuous media) or the page area (in the case of paged media).
4. If the `position` property is **`absolute`** or **`fixed`**, the containing block may also be formed by the edge of the _padding box_ of the nearest ancestor element that has the following:

   1. A {{cssxref("transform")}} or {{cssxref("perspective")}} value other than `none`
   2. A {{cssxref("will-change")}} value of `transform` or `perspective`
   3. A {{cssxref("filter")}} value other than `none` or a `will-change` value of `filter` (only works on Firefox).
   4. A {{cssxref("contain")}} value of `paint` (e.g. `contain: paint;`)
   5. A {{cssxref("backdrop-filter")}} other than `none` (e.g. `backdrop-filter: blur(10px);`)

> **Note:** The containing block in which the root element ({{HTMLElement("html")}}) resides is a rectangle called the **initial containing block**. It has the dimensions of the viewport (for continuous media) or the page area (for paged media).

## Calculating percentage values from the containing block

As noted above, when certain properties are given a percentage value, the computed value depends on the element's containing block. The properties that work this way are **box model properties** and **offset properties**:

1. The {{cssxref("height")}}, {{cssxref("top")}}, and {{cssxref("bottom")}} properties compute percentage values from the `height` of the containing block.
2. The {{cssxref("width")}}, {{cssxref("left")}}, {{cssxref("right")}}, {{cssxref("padding")}}, and {{cssxref("margin")}} properties compute percentage values from the `width` of the containing block.
