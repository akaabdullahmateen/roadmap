# Margin collapse

The _top_ and _bottom_ margins of blocks are sometimes combined (collapsed) into a single margin whose size is the largest of the individual margins (or just one of them, if they are equal), a behavior known as **margin collapsing**. Note that the margins of _floating_ and _absolutely positioned_ elements never collapse.

Margin collapsing occurs in three basic cases:

**Adjacent siblings**
: The margins of adjacent siblings are collapsed (except when the latter sibling needs to be _cleared_ past floats).

**No content separating parent and descendants**
: If there is no border, padding, inline part, _block formatting context_ created, or _clearance_ to separate the `margin-top` of a block from the `margin-top` of one or more of its descendant blocks; or no border, padding, inline content, `height`, or `min-height` to separate the `margin-bottom` of a block from the `margin-bottom` of one or more of its descendant blocks, then those margins collapse. The collapsed margin ends up outside the parent.

**Empty blocks**
: If there is no border, padding, inline content, `height` or `min-height` to separate a block's `margin-top` from its `margin-bottom`, then its top and bottom margins collapse.

Some things to note:

- More complex margin collapsing (of more than two margins) occurs when the above cases are combined.
- These rules apply even to margins that are zero, so the margin of a descendant ends up outside its parent (according to the rules above) whether or not the parent's margin is zero.
- When negative margins are involved, the size of the collapsed margin is the sum of the largest positive margin and the smallest (most negative) negative margin.
- When all margins are negative, the size of the collapsed margin is the smallest (most negative) margin. This applies to both adjacent elements and nested elements.
- Collapsing margins is only relevant in the vertical direction.

## Examples

### HTML

```html
<p>The bottom margin of this paragraph is collapsed …</p>
<p>
  … with the top margin of this paragraph, yielding a margin of
  <code>1.2rem</code> in between.
</p>

<div>
  This parent element contains two paragraphs!
  <p>
    This paragraph has a <code>.4rem</code> margin between it and the text
    above.
  </p>
  <p>
    My bottom margin collapses with my parent, yielding a bottom margin of
    <code>2rem</code>.
  </p>
</div>

<p>I am <code>2rem</code> below the element above.</p>
```

### CSS

```css
div {
  margin: 2rem 0;
  background: lavender;
}

p {
  margin: 0.4rem 0 1.2rem 0;
  background: yellow;
}
```
