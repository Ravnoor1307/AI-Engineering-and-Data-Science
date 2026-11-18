from collections import Counter

from .common import STOP_WORDS, sentences, words


def summarize(text):
    parts = sentences(text)
    if len(parts) <= 2:
        return ' '.join(parts)
    frequency = Counter(word for word in words(text) if word not in STOP_WORDS)
    scored = []
    for index, sentence in enumerate(parts):
        score = sum(frequency[word] for word in words(sentence) if word not in STOP_WORDS)
        scored.append((score, index, sentence))
    count = max(1, (len(parts) + 2) // 3)
    chosen = sorted(scored, reverse=True)[:count]
    return ' '.join(sentence for _, _, sentence in sorted(chosen, key=lambda item: item[1]))
