class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

lyc1 = ["Happy birthday to you",
		"I don't want to get sued",
		"So I'll stop right there"]
		
lyc2 = ["They rally around the family",
		"With pockets full of shells"]

happy_bday = Song(lyc1)

bulls_on_parade = Song(lyc2)
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()