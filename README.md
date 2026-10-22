# levenshtein-distance

Computes the Levenshtein edit distance between two strings using a space-optimized Wagner-Fischer algorithm.

```python
from levenshtein_distance import levenshtein

levenshtein("kitten", "sitting")  # -> 3
levenshtein("", "hello")           # -> 5
```

## Why this exists

Most Levenshtein implementations store the full (m+1) x (n+1) DP matrix.  We only keep two rows at a time, cutting space from O(m*n) to O(n) with no change to the O(m*n) time complexity.  The trade-off is that we cannot reconstruct the edit path — only the distance is returned.

## Edge cases

Empty strings are handled directly: the distance to an empty string equals the length of the other string, and two empty strings have distance zero.  Python's case sensitivity means `Levenshtein("Abc", "abc")` is 1, not 0; normalize your inputs beforehand if you want case-insensitive comparison.
