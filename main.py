import sys

from stats import count_characters, count_words, sort_char_dict


def main():
    argv = sys.argv
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = argv[1]
    contents = get_book_text(path)
    num_words = count_words(contents)
    char_dict = count_characters(contents)
    char_list = sort_char_dict(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in char_list:
        print(f"{d['char']}: {d['num']}")


def get_book_text(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()

    return file_contents


if __name__ == "__main__":
    main()
