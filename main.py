import sys
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
from stats import get_word_count
from stats import get_characters_count
from stats import sort_chars

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():
	path = sys.argv[1]
	text = get_book_text(path)
	word_count = len(get_word_count(text))
	chars_count = get_characters_count(text)
	sorted_chars = sort_chars(chars_count)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for char in sorted_chars:
		if char["char"].isalpha():
			print(f"{char["char"]}: {char["num"]}")
	print("============= END ===============")

main()
