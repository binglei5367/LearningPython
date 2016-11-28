#!/usr/bin/env python

def leastcoin(dollar):
	'''compute the least amount of coins'''
	
	cent = int(dollar * 100)
	coin25 = cent / 25
	coin10 = (cent - coin25 * 25) / 10
	coin5 = (cent - coin25 * 25 - coin10 * 10) / 5
	coin1 = cent - coin25 * 25 - coin10 * 10 - coin5 * 5
	
	return (coin25, coin10, coin5, coin1)
	
def run():
	dollar = round(float(raw_input('dollar: ')), 2)
	coins = leastcoin(dollar)
	print '25 cent: %d\n10 cent: %d\n 5 cent: %d\n 1 cent: %d' % coins

if __name__ == '__main__':
	run()