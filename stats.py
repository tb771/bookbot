
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

def sort_on(items):
	return items[1]["num"]

def sort_dict(count):
	items = [{"char": char, "num": num} for (char, num) in count.items()]
	items.sort(reverse=True, key=lambda d: d["num"])
	return items
