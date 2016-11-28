def scan(raw_sentence):
	
	verbs = ('go', 'kill', 'eat')
	stop = ('the', 'in', 'of')
	nouns = ('bear', 'princess')
	
	words = raw_sentence.split()
	sentence = []
	
	def type(word):
		
		def convert_number(s):
			try:
				return int(s)
			except ValueError:
				return None
				
		
		if word in verbs:
			return ('verb', word)
		
		elif word in stop:
			return ('stop', word)
		
		elif word in nouns:
			return ('noun', word)
			
		elif convert_number(word):
			return ('number', convert_number(word))
			
		else:
			return ('error', word)
			
	
	for i in range(0, len(words)):
		word = words[i]
		sentence.append(type(word))
		
	return sentence