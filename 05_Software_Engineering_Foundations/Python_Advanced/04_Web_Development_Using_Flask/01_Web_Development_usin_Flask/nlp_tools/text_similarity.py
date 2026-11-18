import math
from collections import Counter

from .common import words


def compare(first_text, second_text):
    first = Counter(words(first_text))
    second = Counter(words(second_text))
    if not first or not second:
        return 'Similarity: 0.00% (one or both texts contain no words)'
    shared = first.keys() | second.keys()
    dot_product = sum(first[word] * second[word] for word in shared)
    first_norm = math.sqrt(sum(count * count for count in first.values()))
    second_norm = math.sqrt(sum(count * count for count in second.values()))
    similarity = dot_product / (first_norm * second_norm)
    return f'Cosine similarity: {similarity:.2%}'
