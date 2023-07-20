def extract_integer(text):
    """Extracts and returns an integer from a given text. Limits the returned integer to 10."""
    number = ''.join(filter(str.isdigit, text))
    number = min(int(number), 10) if number else 0
    return number