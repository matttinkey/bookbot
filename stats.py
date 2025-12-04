def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict[str, int]:
    text = text.lower()
    return {char: text.count(char) for char in frozenset(text) if char.isalnum()}


def sort_char_dict(char_dict: dict[str, int]) -> list[dict]:
    char_list = [{"char": key, "num": value} for key, value in char_dict.items()]
    char_list.sort(key=lambda d: d["num"], reverse=True)
    return char_list
