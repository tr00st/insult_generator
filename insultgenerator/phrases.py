from . import words
import struct

def _unpack_bytes(bytes):
    """
    Unpack a set of bytes into an integer. First pads to 4 bytes.
    Little endian.
    """
    if bytes == b'':
        return 0
    int_length = 4
    len_diff = int_length - len(bytes)
    bytes = bytes + len_diff * b'\x00'
    return struct.unpack("<L", bytes)[0]

def get_simple_insult(target_noun):
    return "%s is %s"%(target_noun, words.get_insulting_adjective())
def get_so_insult(target_noun):
    return "%s's so %s"%(target_noun, words.get_insulting_adjective())
def get_so_insult_with_action(target_noun, target_pronoun):
    return "%s's so %s, %s %s"%(target_noun, words.get_insulting_adjective(), target_pronoun, words.get_past_tense_verb())
def get_so_insult_with_action_and_target(target_noun, target_pronoun):
    return "%s's so %s, %s %s the %s"%(target_noun, words.get_insulting_adjective(), target_pronoun, words.get_past_tense_verb(), words.get_noun())