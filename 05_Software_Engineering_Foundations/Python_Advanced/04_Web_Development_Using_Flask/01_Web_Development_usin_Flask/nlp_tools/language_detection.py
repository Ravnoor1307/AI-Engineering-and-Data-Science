from .common import words


LANGUAGE_MARKERS = {
    'English': {'the', 'and', 'is', 'are', 'with', 'this', 'that', 'you'},
    'Spanish': {'el', 'la', 'los', 'las', 'que', 'con', 'una', 'para'},
    'French': {'le', 'la', 'les', 'des', 'une', 'est', 'avec', 'pour'},
    'German': {'der', 'die', 'das', 'und', 'ist', 'mit', 'ein', 'eine'},
}


def detect(text):
    tokens = words(text)
    scores = {
        language: sum(token in markers for token in tokens)
        for language, markers in LANGUAGE_MARKERS.items()
    }
    language, score = max(scores.items(), key=lambda item: item[1])
    if not score:
        return 'Undetermined (the demo supports basic English, Spanish, French, and German markers)'
    return f'{language} (marker matches: {score})'
