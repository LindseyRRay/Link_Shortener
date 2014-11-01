#Link Shortener
import random
import string
import pdb 

#Create dictionary of URLS and shortened links
#If URL does not exist in the dictionary, add it

class LinkDict:
	def __init__(self):
		self.link_dict = dict()

	def check_URL_Exists(self, url):
		if url in list(self.link_dict.values()):
			return True
		return False

	def check_Short_Exists(self, short):
		if short in list(self.link_dict.keys()):
			return True
		return False	

	def return_URL(self, url):
		if not self.check_URL_Exists(url):
			short_url = self.shorted_url(url)
			self.link_dict[short_url] = url
			return short_url
		for short, long_url in list(self.link_dict.items()):
			if long_url==url:
				return short

	def shorted_url(self, url, max_len=9000):
		bad_url = True
		new_url = ""
		while bad_url:
			num = list(str(random.randint(1000, max_len)))
			letter = random.choice(string.ascii_letters)
			location = random.randint(0, len(num)-1)
			num[location] = letter
			new_url = "".join(num)
			bad_url = self.check_Short_Exists(new_url)
		return new_url

if __name__=='__main__':
	ld = LinkDict()
	ex1=ld.check_URL_Exists('www.google.com')
	ex2=ld.check_Short_Exists('www.google.com')
	new_url = ld.return_URL('www.google.com')
	print(new_url)
	
