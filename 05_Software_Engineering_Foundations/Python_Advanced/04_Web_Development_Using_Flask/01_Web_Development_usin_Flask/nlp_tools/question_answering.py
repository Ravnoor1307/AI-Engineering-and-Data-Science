from .common import STOP_WORDS, sentences, words


def answer(text, question):
    question_words = set(words(question)) - STOP_WORDS
    candidates = sentences(text)
    if not candidates or not question_words:
        return 'No answer could be selected from the provided text.'
    ranked = [
        (len((set(words(sentence)) - STOP_WORDS) & question_words), index, sentence)
        for index, sentence in enumerate(candidates)
    ]
    score, _, best = max(ranked)
    return best if score else 'No matching sentence found in the provided text.'
