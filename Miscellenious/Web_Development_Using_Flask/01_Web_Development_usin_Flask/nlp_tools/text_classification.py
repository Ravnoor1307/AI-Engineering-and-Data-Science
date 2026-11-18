from .common import words


CATEGORIES = {
    'Technology': {'computer', 'software', 'technology', 'python', 'website', 'data', 'app', 'digital'},
    'Sports': {'team', 'game', 'player', 'match', 'score', 'coach', 'tournament', 'sport'},
    'Business': {'company', 'market', 'business', 'customer', 'sales', 'profit', 'finance', 'product'},
    'Health': {'health', 'doctor', 'patient', 'medicine', 'hospital', 'exercise', 'medical', 'wellness'},
    'Travel': {'travel', 'hotel', 'flight', 'trip', 'tourism', 'airport', 'destination', 'vacation'},
}


def classify(text):
    tokens = set(words(text))
    scores = {
        category: sum(term.strip() in tokens for term in terms)
        for category, terms in CATEGORIES.items()
    }
    category, score = max(scores.items(), key=lambda item: item[1])
    return f'{category} (keyword matches: {score})' if score else 'Other / undetermined (no category keywords matched)'
