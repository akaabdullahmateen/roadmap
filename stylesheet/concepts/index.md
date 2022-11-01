# CSS: Cascading Style Sheets


## Archive

ruleset or rule
comma-separated list of selectors {
  property: value; declaration
  declaration block
}

Property is a human-readable identifier that defines which feature of the element is considered.
Value describes how the feature must be handled by the engine.
Both property and values are case-insensitive by default.
A property and value pair is called a declaration.
The pair is separated by colon.
White spaces between, before, and after (but not necessarily inside) properties and values are ignored.
Each property has a set of valid values (not all property and value pairs are valid) implemented by the user agent.
When a value is invalid for a property, the entire declaration is deemed invalid and ignored by the CSS engine.

A declaration block is a structure containing semi-colon separated list of declarations, enclosed in a pair of matching braces.
A declaration block may be empty, that is containing the null declaration.
White spaces around declarations are ignored.
The last declaration in the block does not need to be terminated by a semi-colon, though it is considered good style to do it, as it is easy to forget to add it when extending the block with another declaration.

A ruleset (or rule) is a the sup followed by a declaration block.