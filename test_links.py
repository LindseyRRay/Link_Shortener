#Test Shorten Link File
import unittest
import shorten_link as sl
import pdb

class test_link(unittest.TestCase):

	def setUp(self):
		self.linkDict = sl.LinkDict()

	def test_URL_exists(self):
		self.assertEqual(self.linkDict.check_URL_Exists('www.google.com'), False)

	def test_short_URL(self):
		self.assertEqual(self.linkDict.check_URL_Exists('www.google.com'), False)


	def test_add_link(self):
		new_url = self.linkDict.return_URL('www.google.com')
		print(new_url)
		print(self.linkDict.link_dict['www.google.com'])
		self.assertEqual(len(self.linkDict.link_dict['www.google.com'])>0, True)

if __name__ == '__main__':
	unittest.main()
