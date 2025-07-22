import sys
from stats import get_word_count, get_character_count, sort_on

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    try:
        with open(filepath, 'r') as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{filepath}': {e}")
        sys.exit(1)

    word_count = get_word_count(filepath)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    char_counts = get_character_count(contents)
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    char_list.sort(reverse=True, key=sort_on)

    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()


