from nose.tools import *
from ex48 import parser
from ex48 import lexicon

raw_sentence = 'the bear kill the princess in the north'
word_list = lexicon.scan(raw_sentence)

print word_list
print '------'

def test_peek():
	assert_equal(parser.peek(word_list), 'stop')
	assert_equal(parser.peek([]), None)
	
def test_match():
	assert_equal(parser.match(word_list, 'stop'), ('stop', 'the'))
	assert_equal(parser.match(word_list, 'verb'), None)

def test_skip():
	assert_equal(parser.skip([('verb', 'kill')], 'verb'), ('verb', 'kill'))

def test_parse_verb():
	assert_equal(parser.parse_verb([('verb', 'kill')]), ('verb', 'kill'))