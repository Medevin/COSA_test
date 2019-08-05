s = "aaAAwe Cc crwwwww  wwBBbber WEr  "
k = 3

def chars_met_counter(s, k):
	refactored_string = s.lower().replace(' ', '')
	chars_cout_dict = { chr(character): refactored_string.count(chr(character)) 
		for character in range(ord('a'), ord('z')+1)}
	final_string = ''.join('{}'.format(key) for key, val in sorted(
		chars_cout_dict.items(), key=lambda x: x[1], reverse=True)
	)

	return(final_string[0:k])

print(chars_met_counter(s, k))
