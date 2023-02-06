## Suppress unused variable warnings when compiling

```cpp
int x = 1;
std::nullptr_t y = NULL;
[](...){}(x, y); // suppresses "unused variable" warnings
```