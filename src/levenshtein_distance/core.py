"""Core implementation of Levenshtein edit distance."""


def levenshtein(a: str, b: str) -> int:
    """Return the Levenshtein edit distance between strings *a* and *b*.

    The distance is the minimum number of single-character insertions,
    deletions, or substitutions required to transform *a* into *b*.

    The classic Wagner-Fischer algorithm fills an (m+1) x (n+1) matrix
    where m and n are the lengths of the two inputs.  We only ever read
    the previous and current rows during the fill, so we keep two 1-D
    arrays of length n+1 instead of the full matrix.  This brings the
    space cost from O(m*n) down to O(n) while leaving the time cost at
    O(m*n).  For the common case of comparing two short strings the
    difference is negligible; for comparing many long strings it avoids
    allocating a large grid on every call.

    An empty string is treated as having length zero, so the distance
    between any string and the empty string is the length of that
    string.
    """
    if a == b:
        return 0

    if not a:
        return len(b)
    if not b:
        return len(a)

    # Make *a* the shorter string so we allocate the smaller row.
    if len(a) < len(b):
        a, b = b, a

    # previous row holds edit distances for a[0..i-1] vs b[0..j].
    previous = list(range(len(b) + 1))

    for i, ca in enumerate(a, start=1):
        current = [i] + [0] * len(b)
        for j, cb in enumerate(b, start=1):
            cost = 0 if ca == cb else 1
            current[j] = min(
                previous[j] + 1,       # deletion
                current[j - 1] + 1,     # insertion
                previous[j - 1] + cost, # substitution
            )
        previous = current

    return previous[len(b)]
