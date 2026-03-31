"""High-throughput text analytics helpers."""

from __future__ import annotations

from collections import Counter
from typing import Iterable


def _normalized_tokens(text: str) -> Iterable[str]:
    """Yield lowercase alphanumeric tokens from input text."""
    token = []
    for ch in text:
        if ch.isalnum():
            token.append(ch.lower())
            continue

        if token:
            yield "".join(token)
            token.clear()

    if token:
        yield "".join(token)


def word_counts(text: str) -> dict[str, int]:
    """Return normalized token frequencies.

    This implementation is optimized for single-pass scanning and avoids
    regex overhead for large inputs.
    """
    return dict(Counter(_normalized_tokens(text)))


def top_terms(text: str, limit: int = 10) -> list[tuple[str, int]]:
    """Return top N tokens sorted by descending frequency then term."""
    if limit <= 0:
        return []

    counts = word_counts(text)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]
