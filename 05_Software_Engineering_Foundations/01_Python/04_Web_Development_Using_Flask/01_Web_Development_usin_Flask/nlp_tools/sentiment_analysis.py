from .common import words


POSITIVE = {'amazing', 'excellent', 'good', 'great', 'happy', 'love', 'enjoy', 'wonderful', 'best', 'helpful'}
NEGATIVE = {'awful', 'bad', 'boring', 'hate', 'horrible', 'poor', 'sad', 'terrible', 'worst', 'angry'}


def analyze(text):
    tokens = words(text)
    positive = sum(token in POSITIVE for token in tokens)
    negative = sum(token in NEGATIVE for token in tokens)
    if positive > negative:
        label = 'Positive'
    elif negative > positive:
        label = 'Negative'
    else:
        label = 'Neutral'
    return f'{label} (positive words: {positive}, negative words: {negative})'
