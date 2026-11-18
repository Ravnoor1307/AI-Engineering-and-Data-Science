from collections import Counter

from .common import STOP_WORDS, words


def extract(text):
    counts = Counter(word for word in words(text) if word not in STOP_WORDS)
    if not counts:
        return 'No keywords found.'
    return '\n'.join(f'{word} — {count}' for word, count in counts.most_common(10))
