
def get_num_words(book_contents): 
	words = book_contents.split()                 
	num_words= len(words)                    
	return num_words     

def get_character(book_contents):
	count = {}
	for character in book_contents:
		total = character.lower()
		if total in count:
			count[total]+=1
		else:
			count[total]=1
	return count

