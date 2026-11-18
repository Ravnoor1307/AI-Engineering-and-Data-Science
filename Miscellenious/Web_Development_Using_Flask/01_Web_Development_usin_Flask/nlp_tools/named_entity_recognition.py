import re


def analyze(text):
    patterns = (
        ('EMAIL', r'\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b'),
        ('DATE', r'\b(?:\d{1,2}[/-]){2}\d{2,4}\b|\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}\b'),
        ('PROPER_NAME', r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,2}\b'),
    )
    entities = []
    seen = set()
    for label, pattern in patterns:
        for match in re.finditer(pattern, text):
            item = (match.group(), label)
            if item not in seen:
                entities.append(item)
                seen.add(item)
    if not entities:
        return 'No entities found by the demo patterns.'
    return '\n'.join(f'{entity} — {label}' for entity, label in entities)
