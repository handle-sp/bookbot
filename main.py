BOOK_TO_ANALYZE = "books/frankenstein.txt"

def get_word_count(text):
    return len(text.split())

def get_char_counts(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def main():
    with open(BOOK_TO_ANALYZE) as f:
        file_contents = f.read()

    word_count = get_word_count(file_contents)
    char_counts = get_char_counts(file_contents)

    # This will return a list of the characters sorted by the frequency of the characters in descending order.
    # We will iterate over this list of sorted characters to display the character details down below.
    sorted_chars_by_count = sorted(char_counts, key=lambda char : char_counts[char], reverse=True)
    
    print(f"--- Begin report of {BOOK_TO_ANALYZE} ---\n")
    print(f"{word_count} words found in the document.\n")
    for char in sorted_chars_by_count:
        if char.isalpha():
            print(f"The '{char}' character was found {char_counts[char]} times.")

main()