import unittest
import six
from insultgenerator import words

class TestWords(unittest.TestCase):
	def test_get_insulting_adjective(self):
		adjective = words.get_insulting_adjective()
		self.assertTrue(isinstance(adjective, six.string_types), "Returned adjective is not a string")
		self.assertTrue(len(adjective) > 0, "Returned adjective is too short!")
	def test_get_insulting_adjective_is_random(self):
		first_adjective = words.get_insulting_adjective()
		was_different = False
		for i in range(0,1000):
			if words.get_insulting_adjective() != first_adjective:
				was_different = True
				break
		self.assertTrue(was_different, "The same adjective was returned 1000 times in a row...")
	def test_get_insulting_adjective_no_blanks_1000(self):
		for i in range(0,1000):
			self.assertNotEqual(words.get_insulting_adjective(), "")
