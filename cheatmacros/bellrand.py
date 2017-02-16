"""
Bell random function
Date: 2016 Aug
Author: RollerSimmer
"""

import random

def minmax(v,l,h):
	if h<l: return minmax(v,h,l)
	if v<l: return l
	elif v>h: return h
	else: return v 

def gen(lo:int,hi:int,amtSamples:int):
	if amtSamples==0: return random.randint(lo,hi)
	brsum=0
	loops=0
	for i in range(0,amtSamples):
		loops+=1
		brsum+=random.randint(lo,hi)
	br=int(brsum/amtSamples)
	return br

