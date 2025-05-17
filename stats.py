def get_word_count(text):
        return text.split()

def get_characters_count(text):
	characters_list = list(text.lower())
	characters_count = {}
	
	for char in characters_list:
		if not char in characters_count:
			characters_count[char] = 1
		else:
			characters_count[char] += 1

	return characters_count

def sort_chars(chars_dict):
	unsorted_list = []

	for char in chars_dict:
		temp_dict = {"char": char, "num": chars_dict[char]}
		unsorted_list.append(temp_dict)
	
	return sorted(unsorted_list, key=lambda num: num["num"], reverse=True)

