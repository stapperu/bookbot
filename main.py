from stats import get_book_text
from stats import count_characters
from stats import count_words
from stats import order_list
import sys

def main():

	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		book_path= sys.argv[1]
	word_count=count_words(book_path)
	orderlist=order_list(book_path)

main()
