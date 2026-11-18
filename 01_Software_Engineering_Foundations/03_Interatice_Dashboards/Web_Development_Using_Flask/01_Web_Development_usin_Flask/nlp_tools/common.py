import re


STOP_WORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'been', 'but', 'by', 'for',
    'from', 'had', 'has', 'have', 'he', 'her', 'his', 'i', 'in', 'is', 'it',
    'its', 'of', 'on', 'or', 'our', 'she', 'that', 'the', 'their', 'them',
    'there', 'they', 'this', 'to', 'was', 'we', 'were', 'will', 'with', 'you',
    'your',
}


def words(text):
    return re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text.lower())


def sentences(text):
    return [part.strip() for part in re.split(r'(?<=[.!?])\s+', text.strip()) if part.strip()]
