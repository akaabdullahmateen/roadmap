# Functions

**CSS functional notation** is a type of _CSS value_ that can represent more complex data types or invoke special data processing or calculations.

## Syntax

```css
selector {
  property: functional-notation([argument]? [, argument]!);
}
```

The syntax starts with the **name of the functional notation**, followed by a left parenthesis `(`. Next up are the notation argument(s), and the function is finished off with a closing parenthesis `)`.

Functions can take multiple arguments, which are formatted similarly to CSS property values. Whitespace is allowed, but they are optional inside the parentheses. In some functional notations multiple arguments are separated by commas, while others use spaces.

## Transform functions

These functions are used when the `<transform-function>` CSS data type is used as a value of `transform`.

| Function        | Description                                                |
| --------------- | ---------------------------------------------------------- |
| `matrix()`      | Describes a homogeneous 2D transformation matrix.          |
| `matrix3d()`    | Describes a 3D transformation as a 4×4 homogeneous matrix. |
| `perspective()` | Sets the distance between the user and the z=0 plane.      |
| `rotate()`      | Rotates an element around a fixed point on the 2D plane.   |
| `rotate3d()`    | Rotates an element around a fixed axis in 3D space.        |
| `rotateX()`     | Rotates an element around the horizontal axis.             |
| `rotateY()`     | Rotates an element around the vertical axis.               |
| `rotateZ()`     | Rotates an element around the z-axis.                      |
| `scale()`       | Scales an element up or down on the 2D plane.              |
| `scale3d()`     | Scales an element up or down in 3D space.                  |
| `scaleX()`      | Scales an element up or down horizontally.                 |
| `scaleY()`      | Scales an element up or down vertically.                   |
| `scaleZ()`      | Scales an element up or down along the z-axis.             |
| `skew()`        | Skews an element on the 2D plane.                          |
| `skewX()`       | Skews an element in the horizontal direction.              |
| `skewY()`       | Skews an element in the vertical direction.                |
| `translate()`   | Translates an element on the 2D plane.                     |
| `translate3d()` | Translates an element in 3D space.                         |
| `translateX()`  | Translates an element horizontally.                        |
| `translateY()`  | Translates an element vertically.                          |
| `translateZ()`  | Translates an element along the z-axis.                    |

## Math functions

The math functions allow CSS numeric values to be written as mathematical expressions.

### Basic arithmetic

| Function | Description                                                                           |
| -------- | ------------------------------------------------------------------------------------- |
| `calc()` | A math function that allows basic arithmetic to be performed on numerical CSS values. |

### Comparison functions

| Function  | Description                                                                                                    |
| --------- | -------------------------------------------------------------------------------------------------------------- |
| `min()`   | A comparison function that represents the smallest of a list of values.                                        |
| `max()`   | A comparison function that represents the largest of a list of values.                                         |
| `clamp()` | A comparison function that takes a minimum, central, and maximum value and represents its central calculation. |

### Stepped value functions

| Function  | Description                                                                                                   |
| --------- | --------------------------------------------------------------------------------------------------------------|
| `round()` | A stepped value function that returns a rounded number based on a rounding strategy.                          |
| `mod()`   | A function that divides one number by another and returns the modulus (with the same sign as the divisor).    |
| `rem()`   | A function that divides one number by another and returns the remainder (with the same sign as the dividend). |

### Trigonometric functions

| Function  | Description                                                                          |
| --------- | ------------------------------------------------------------------------------------ |
| `sin()`   | A trigonometric function that returns the sine of a number.                          |
| `cos()`   | A trigonometric function that returns the cosine of a number.                        |
| `tan()`   | A trigonometric function that returns the tangent of a number.                       |
| `asin()`  | A trigonometric function that returns the inverse sine of a number.                  |
| `acos()`  | A trigonometric function that returns the inverse cosine of a number.                |
| `atan()`  | A trigonometric function that returns the inverse tangent of a number.               |
| `atan2()` | A trigonometric function that returns the inverse tangent of two-numbers in a plane. |

### Exponential functions

| Function  | Description                                                                                  |
| --------- | -------------------------------------------------------------------------------------------- |
| `pow()`   | An exponential function that returns a base raised to the power of a number.                 |
| `sqrt()`  | An exponential function that returns the square root of a number.                            |
| `hypot()` | An exponential function that returns the square root of the sum of squares of its arguments. |
| `log()`   | An exponential function that returns the logarithm of a number.                              |
| `exp()`   | An exponential function that returns `e` raised to the power of a number.                    |

### Sign-related functions

| Function | Description                                                                    |
| -------- | ------------------------------------------------------------------------------ |
| `abs()`  | Takes a calculation and returns the absolute value.                            |
| `sign()` | Takes a calculation and returns the sign (positive or negative) of the number. |

## Filter functions

The **`<filter-function>`** CSS data type represents a graphical effect that can change the appearance of an input image. It is used in the `filter` and `backdrop-filter` properties.

| Function        | Description                                     |
| ----------------| ----------------------------------------------- |
| `blur()`        | Blurs the image.                                |
| `brightness()`  | Makes the image brighter or darker.             |
| `contrast()`    | Increases or decreases the image's contrast.    |
| `drop-shadow()` | Applies a drop shadow behind the image.         |
| `grayscale()`   | Converts the image to grayscale.                |
| `hue-rotate()`  | Changes the overall hue of the image.           |
| `invert()`      | Inverts the colors of the image.                |
| `opacity()`     | Makes the image transparent.                    |
| `saturate()`    | Super-saturates or desaturates the input image. |
| `sepia()`       | Converts the image to sepia.                    |

## Color functions

Functions which specify different color representations. These may be used anywhere a `<color>` is valid.

| Function           | Description                                                                                                                                                            |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `color()`          | Allows a color to be specified in a particular, specified colorspace (rather than the implicit sRGB colorspace that most of the other color functions operate in).     |
| `color-mix()`      | Takes two `color` values and returns the result of mixing them in a given colorspace by a given amount.                                                                |
| `color-contrast()` | Takes a `color` value and compares it to a list of other `color` values, selecting the one with the highest contrast from the list.                                    |
| `device-cmyk()`    | Used to express CMYK colors in a device-independent way.                                                                                                               |
| `hsl()`            | The HSL color model defines a given color according to its hue, saturation, and lightness components. An optional alpha component represents the color's transparency. |
| `hsla()`           | The HSL color model defines a given color according to its hue, saturation, and lightness components. The alpha component represents the color's transparency.         |
| `hwb()`            | HWB (short for Hue-Whiteness-Blackness) is another method of specifying colors, similar to HSL.                                                                        |
| `lab()`            | Lab color is device-independent and specifies physical measurements of color.                                                                                          |
| `lch()`            | LCH color is device-independent and specifies color using polar coordinates for chroma and hue.                                                                        |
| `oklab()`          | OKLab color is device-independent and specifies physical measurements of color.                                                                                        |
| `oklch()`          | OKLCH color is device-independent and specifies color using polar coordinates for chroma and hue.                                                                      |
| `rgb()`            | The RGB color model defines a given color according to its red, green, and blue components. An optional alpha component represents the color's transparency.           |
| `rgba()`           | The RGB color model defines a given color according to its red, green, and blue components. The alpha component represents the color's transparency.                   |

## Image functions

These functions may be used wherever an `<image>` is valid as the value for a property.

| Function                      | Description                                                                                                                                                      |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `conic-gradient()`            | Conic gradients transition colors progressively around a circle.                                                                                                 |
| `image()`                     | Defines an `<image>` in a similar fashion to the `<url()>` function, but with added functionality including specifying the image's directionality and fallback images for when the preferred image is not supported. |
| `image-set()`                 | A method of letting the browser pick the most appropriate CSS image from a given set, primarily for high pixel density screens.                                  |
| `linear-gradient()`           | Linear gradients transition colors progressively along an imaginary line.                                                                                        |
| `radial-gradient()`           | Radial gradients transition colors progressively from a center point (origin).                                                                                   |
| `repeating-linear-gradient()` | Is similar to `linear-gradient()` and takes the same arguments, but it repeats the color stops infinitely in all directions so as to cover its entire container. |
| `repeating-radial-gradient()` | Is similar to `radial-gradient()` and takes the same arguments, but it repeats the color stops infinitely in all directions so as to cover its entire container. |
| `repeating-conic-gradient()`  | Is similar to `conic-gradient()` and takes the same arguments, but it repeats the color stops infinitely in all directions so as to cover its entire container.  |
| `cross-fade()`                | Can be used to blend two or more images at a defined transparency.                                                                                               |
| `element()`                   | Defines an `<image>` value generated from an arbitrary HTML element.                                                                                             |
| `paint()`                     | Defines an `<image>` value generated with a PaintWorklet.                                                                                                        |

## Counter functions

The counter functions are generally used with the `content` property, although in theory may be used wherever a `<string>` is supported.

| Function     | Description                                                                                                                       |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `counter()`  | Returns a string representing the current value of the named counter, if there is one.                                            |
| `counters()` | Enables nested counters, returning a concatenated string representing the current values of the named counters, if there are any. |
| `symbols()`  | Lets you define counter styles inline, directly as the value of a property.                                                       |

## Font functions

The `font-variant-alternates` property controls the use of alternate glyphs, the following functions are values for this property.

| Function              | Description                                                                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `stylistic()`         | This function enables stylistic alternates for individual characters. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType value `salt`, like `salt 2`. |
| `styleset()`          | This function enables stylistic alternatives for sets of characters. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType value `ssXY`, like `ss02`.    |
| `character-variant()` | This function enables specific stylistic alternatives for characters. It is similar to `styleset()`, but doesn't create coherent glyphs for a set of characters; individual characters will have independent and not necessarily coherent styles. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType value `cvXY`, like `cv02`. |
| `swash()`             | This function enables _swash_ glyphs. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType values `swsh` and `cswh`, like `swsh 2` and `cswh 2`.        |
| `ornaments()`         | This function enables ornaments, like _fleurons_ and other dingbat glyphs. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType value `ornm`, like `ornm 2`. |
| `annotation()`        | This function enables annotations, like circled digits or inverted characters. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType value `nalt`, like `nalt 2`. |

## Shape functions

The following functions may be used as values for the `<basic-shape>` data type, which is used in the `clip-path`, `offset-path`, and `shape-outside` properties.

| Function    | Description                                               |
| ----------- | --------------------------------------------------------- |
| `circle()`  | Defines a circle.                                         |
| `ellipse()` | Defines an ellipse.                                       |
| `inset()`   | Defines an inset rectangle.                               |
| `polygon()` | Defines a polygon.                                        |
| `path()`    | Accepts an SVG path string to enable a shape to be drawn. |

## Reference functions

The following functions are used as a value of properties to reference a value defined elsewhere.

| Function | Description                                                                                      |
| -------- | ------------------------------------------------------------------------------------------------ |
| `attr()` | Used to retrieve the value of an attribute of the selected element and use it in the stylesheet. |
| `env()`  | Used to insert the value of a user-agent defined environment variable.                           |
| `url()`  | Used to include a file.                                                                          |
| `var()`  | Used to insert a value of a custom property instead of any part of a value of another property.  |

## Grid functions

The following functions are used to define a _CSS Grid_.

| Function        | Description                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `fit-content()` | Clamps a given size to an available size according to the formula `min(maximum size, max(minimum size, argument))`.            |
| `minmax()`      | Defines a size range greater than or equal to _min_ and less than or equal to _max_.                                           |
| `repeat()`      | Represents a repeated fragment of the track list, allowing a large number of columns or rows that exhibit a recurring pattern. |
