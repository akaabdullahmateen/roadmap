## `print()` function

The `print()` function is used to write string to an output stream. More specifically, it prints `objects` to the text stream `file`, separated by `sep`, and followed by `end`.

```py
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

!!! note

    All arguments except for `objects` must be given as keyword arguments.

`objects`
: The objects to be printed to the text stream. All non-keyword arguments are considered as `objects`, and therefore, they are converted to strings like `str()` does, and written to the stream. If no `objects` are given, `print()` will just write `end` and exit.

`sep`
: A string that is to be used as the separator between objects. If it is not present or `None`, the default value is used, which is a single space character (`' '`).

`end`
: A string that is to be used as the terminator at the end. If it is not present or `None`, the default value is used, which is a newline character (`'\n'`).

`file`
: An object with a `write(string)` method. If it is not present or `None`, the default value is used, which is the standard output stream (`sys.stdout`). Since printed arguments are converted to text strings, `print()` can not be used with binary mode file objects; for those, `file.write()` is used instead.

`flush`
: A boolean that forcibly controls whether the output is buffered or not. If it is not present or `None`, the default behavior is determined by the output stream object `file`.
