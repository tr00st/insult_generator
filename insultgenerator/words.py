import pkg_resources
import random

_insulting_adjectives = []

def _load_wordlists():
	global _insulting_adjectives
	insulting_adjective_list = pkg_resources.resource_string(__name__, "wordlists/insulting_adjectives.txt")
	_insulting_adjectives = insulting_adjective_list.decode().strip().split('\n')

def get_insulting_adjective():
	return random.choice(_insulting_adjectives)

_load_wordlists()
