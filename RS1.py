from collections import *
from itertools import *
from string import punctuation
import numpy as np
import matplotlib.pyplot as plt
import ast
import re

UID = list()
pair = Counter()
num = raw_input('>> Enter Number of Recommendations: ')
if num.isdigit():
	num = int(num)
else:
	print 'Incorrect Number DEFAULT = 1'
	num = 1
likes = raw_input('>> Enter Likes to be Recommend LIKES: ')
likes = likes.split(',')

index = 0
for i in likes:
	likes[index] = i.strip()
	index+=1
rec_like  = list()
counterr = 0
for line in open('/users/Rahul/Desktop/DESK/Python_smaple/1000.csv','r+'):
	 line = re.split('"\W+"',line.strip())
	 line[len(line)-1] = line[len(line)-1].replace('"','')
	 UID.append(line[0].strip('"'))
	 line = line[1:]
	 for x in likes:
	 	if x in line:
	 		counterr+=1
	 		rec_like.extend(line)
	 		break
	 

for i in likes:
	c = rec_like.count(i)
	for j in range(c):
		rec_like.remove(i)

rec_like_count	= Counter(rec_like)

for i in rec_like_count.most_common(num):
	print i





	 
	 
	


	 
	 
