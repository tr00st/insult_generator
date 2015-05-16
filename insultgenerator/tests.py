import unittest
import six
import re
from functools import partial
from insultgenerator import words, phrases
from pip._vendor.html5lib import inputstream

class TestWords(unittest.TestCase):
	def do_test_get_word(self, callee):
		adjective = callee()
		self.assertTrue(isinstance(adjective, six.string_types), "Returned adjective is not a string")
		self.assertTrue(len(adjective) > 0, "Returned adjective is too short!")
	
	def do_test_get_word_is_random(self, callee):
		first_adjective = callee()
		was_different = False
		for i in range(0,1000):
			if callee() != first_adjective:
				was_different = True
				break
		self.assertTrue(was_different, "The same adjective was returned 1000 times in a row...")
		
	def do_test_get_word_no_blanks_1000(self, callee):
		for i in range(0,1000):
			self.assertNotEqual(callee(), "", "A blank item was returned")
		
	def test_get_insulting_adjective(self):
		self.do_test_get_word(words.get_insulting_adjective)
	def test_get_insulting_adjective_is_random(self):
		self.do_test_get_word_is_random(words.get_insulting_adjective)
	def test_get_insulting_adjective_no_blanks_1000(self):
		self.do_test_get_word_no_blanks_1000(words.get_insulting_adjective)
		
	def test_get_past_tense_verb(self):
		self.do_test_get_word(words.get_past_tense_verb)
	def test_get_past_tense_verb_is_random(self):
		self.do_test_get_word_is_random(words.get_past_tense_verb)
	def test_get_past_tense_verb_no_blanks_1000(self):
		self.do_test_get_word_no_blanks_1000(words.get_past_tense_verb)
		
	def test_get_noun(self):
		self.do_test_get_word(words.get_noun)
	def test_get_noun_is_random(self):
		self.do_test_get_word_is_random(words.get_noun)
	def test_get_noun_no_blanks_1000(self):
		self.do_test_get_word_no_blanks_1000(words.get_noun)
		
	def test_int_padding_tool(self):
		from binascii import hexlify, unhexlify
		from insultgenerator.phrases import _unpack_bytes
		test_sets = [
			[b'00', 0],
			[b'01', 1],
			[b'0001', 256],
			[b'00000001', 16777216],
			[b'ffff', 65535],
			[b'ffffffff', 4294967295],
			[b'ff', 255],
			[b'ff00', 255],
			[b'00ff', 65280],
			[b'', 0],
			[b'00', 0],
			[b'0000', 0],
			[b'000000', 0],
			[b'00000000', 0],
		]
		for input, expected in test_sets:
			actual = _unpack_bytes(unhexlify(input))
			self.assertEqual(expected, actual, 'Byte padding did not match expectation - input: %s, output: %s, expected: %s'%(input, actual, expected))			
		

class TestPhrases(unittest.TestCase):
	def do_test_get_phrase_parses_1000(self, callee, format):
		validation_regex = re.compile(format)
		for i in range(1,1000):
			phrase = callee()
			self.assertIsNotNone(validation_regex.match(phrase), "Result did not match, expected %s, got %s"%(format, phrase))
			
	def test_get_basic_insult_parses_1000(self):
		self.do_test_get_phrase_parses_1000(partial(phrases.get_simple_insult, "TestNoun"), '\ATestNoun is .*\Z')
			
	def test_get_so_insult_parses_1000(self):
		self.do_test_get_phrase_parses_1000(partial(phrases.get_so_insult, "TestNoun"), '\ATestNoun\'s so .*\Z')
	def test_get_so_insult_with_action_parses_1000(self):
		self.do_test_get_phrase_parses_1000(partial(phrases.get_so_insult_with_action, "TestNoun", "TestPronoun"), '\ATestNoun\'s so .*, TestPronoun .*\Z')
	def test_get_so_insult_with_action_and_target_parses_1000(self):
		self.do_test_get_phrase_parses_1000(partial(phrases.get_so_insult_with_action_and_target, "TestNoun", "TestPronoun"), '\ATestNoun\'s so [a-zA-Z0-9\'-]+, TestPronoun [a-zA-Z0-9\'-]+ the [a-zA-Z0-9\'-]+\Z')