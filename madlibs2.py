#!python3
#madLibs.py - reads in text files and lets the user add their own text anywhere 
#the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file
#usage:
	#pass the file you want to turn into a madlib to textFile
	#words that you want replaced in the story should be: VERB, NOUN or ADJECTIVE
import re


#import text file
textFile = open('madlibExample.txt')
madlibFile = textFile.read()

#find key words in the file
adjRegex = re.compile(r'ADJECTIVE')
nounRegex = re.compile(r'NOUN')
verbRegex = re.compile(r'VERB')

#make lists to store and retrieve words from
adjList  = []
nounList = []
verbList = []


#receive user input
for adj in range(len(adjRegex.findall(madlibFile))):
	uInput = input('Enter an adjective, please.')
	adjList.append(uInput)
for noun in range(len(nounRegex.findall(madlibFile))):
	uInput = input('Enter a noun, please.')
	nounList.append(uInput)
for verb in range(len(verbRegex.findall(madlibFile))):
	uInput = input('Enter a verb, please.')
	verbList.append(uInput)

#change the words
for adjective in adjList:
	madlibFile = adjRegex.sub(adjective,madlibFile)
for verb in verbList:
	madlibFile = verbRegex.sub(verb, madlibFile)
for noun in nounList:
	madlibFile = nounRegex.sub(noun, madlibFile, 1)


#print the result
print(madlibFile)

input('That was a pretty funny story, human. Press Enter to save it to madlib.txt and exit the program')
madlib = open('madlib.txt','w')
madlib.write(madlibFile)
