from stats import get_num_words
from stats import get_character
from stats import sort_dict
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents=f.read()
	return file_contents


def report(filepath,  word_count, letter_count):
	print("============BOOKBOT============")
	print(f"Analyzing book found at: {filepath}")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	sorted_dict = sort_dict(letter_count)
	for item in sorted_dict:
		char = item["char"]
		num= item["num"]
	for item in sorted_dict:
		if item["char"].isalpha() and item ["char"] >= "a" and item["char"] <= "z":
			print(f"{item['char']}: {item['num']}")
	
	print("============= END ===============")


def main():
	if len(sys.argv) !=2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
		
	else:
		filepath = sys.argv[1]
		
# Call get_book_text with the filepath argument
# And store the returned value (the book's text) in a variable called 'book_contents'
		book_contents = get_book_text(filepath)
	
		total_words = get_num_words(book_contents) 
	
	   
	
		count = get_character(book_contents)
		report(filepath, total_words, count)

	
main()





