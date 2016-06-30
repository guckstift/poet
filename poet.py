#!/usr/bin/python

import random

paraFalloff = 1/8
sentFalloff = 1/8
wordFalloff = 1/8
lettFalloff = 1/4
langFalloff = 1/128
capiChance = 1/4
commaChance = 1/8
punctChoice = "."*4 + "?" + "!"

rand = random.random
pickvow = lambda: random.choice ("aeiouy" + "a"*4 + "e"*5 + "i"*4 + "o"*3)
pickcon = lambda: random.choice ("bcdfghklmnprstvwxz"*3 + "jq")

lang = []

#make language
langLength = random.randint (50, 100)
for i in range (langLength):
	word = ""
	# letters
	sylbCount = random.randint (1, 8)
	for j in range (sylbCount):
		if rand () > 0.5:
			word += pickcon ()
			word += pickvow ()
		else:
			word += pickvow ()
			word += pickcon ()
	if rand () > 0.5:
		if rand () > 0.5:
			word += pickcon ()
		else:
			word += pickvow ()
	if rand () < capiChance:
		word = word.title ()
		lang.append (word)
	else:
		for j in range (9 - sylbCount):
			lang.append (word)

result = ""

# paragraphs
paraCount = random.randint (1, 10)
for i in range (paraCount):
	# sentences
	sentCount = random.randint (1, 15)
	for j in range (sentCount):
		senStart = True
		# words
		wordCount = random.randint (2, 30)
		for k in range (wordCount):
			word = random.choice (lang)
			if senStart:
				word = word.title ()
			result += word
			if k < wordCount - 1:
				if rand () < commaChance:
					result += ","
				result += " "
			senStart = False
		result += random.choice (punctChoice)
		if j < sentCount - 1:
			result += " "
	if i < paraCount - 1:
		result += "\n\n"

print (result)

