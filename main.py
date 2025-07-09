from stats import get_num_words
from stats import get_character
def get_book_text(filepath):
	with open(filepath) as f:
		file_contents=f.read()
	return file_contents


def main():
# Call get_book_text with the filepath argument
# And store the returned value (the book's text) in a variable called 'book_contents'
	book_contents = get_book_text("books/frankenstein.txt")
	
	total_words = get_num_words(book_contents) 
	
	print (f"{total_words} words found in the document")   
	
	count = get_character(book_contents)
	print(count)

	
main()





