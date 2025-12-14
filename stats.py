def get_book_text(path):
        with open(path) as f:
                return f.read()
        
def count_words(path):
        with open(path) as f:
                text=f.read()
                split_text= text.split()
        count=len(split_text)
        return count

def count_characters(path):
	new_dict={}
	with open(path) as f:
		text=f.read()
		split_text=text.split()
		for word in split_text:
			for ch in word:
				low_char=ch.lower()
				if low_char in new_dict:
					new_dict[low_char]+=1
				else:
					new_dict[low_char]=1
	count=len(new_dict)                          
	return count

def order_list(path):
    new_dict = {}
    count=count_words(path)
    with open(path) as f:
        text = f.read()
        split_text = text.split()
        for word in split_text:
            for ch in word:
                ch_dict = {}
                low_char = ch.lower()
                if low_char in new_dict:
                    new_dict[low_char]["num"] += 1
                else:
                    ch_dict["char"] = low_char
                    ch_dict["num"] = 1
                    new_dict[low_char] = ch_dict
    
    result = list(new_dict.values())
    result.sort(key=lambda x: x["num"], reverse=True)
    
    print(" ============ BOOKBOT ============")
    print(f" Analyzing book found at {path}...")
    print(" ----------- Word Count ----------")
    print(f" Found {count} total words")
    print(" --------- Character Count -------")

    for item in result:
        print(f" {item['char']}: {item['num']}")
    return count
