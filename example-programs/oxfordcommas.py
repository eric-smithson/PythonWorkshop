def oxford(param):
	ret = ""
	# all the stuff
	for i in range(len(param) - 1):
		ret += param[i] + ', '
	ret += 'and ' + param[len(param) - 1]
	
	return ret


list = ["Who","gives","a","fuck","about","an","Oxford","comma?"]

string = oxford(list)

print(string)