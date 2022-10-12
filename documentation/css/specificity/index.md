# Specificity

**Specificity** is the algorithm used by browsers to determine the CSS declaration that is the most relevant to an element, which in turn, determines the property value to apply to that element. The specificity algorithm calculates the weight of a CSS selector to determine which rule from competing CSS declarations gets applied to an element.

> **Note:** Browsers consider specificity **after** determining cascade origin and importance. In other words, for competing property declarations, specificity is relevant and compared only between selectors from the one cascade origin and layer that has precedence for the property. Order of appearance becomes relevant when the selector specificities of the competing declarations in the cascade layer with precedence are equal.

## How is specificity calculated?

Specificity is an algorithm that calculates the weight that is applied to a given CSS declaration. The weight is determined by the number of selectors of each weight category in the selector matching the element (or pseudo-element).
