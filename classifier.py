from collections import Counter, defaultdict

import random

import sys

def readTrainingData(fileName):
	with open(fileName) as file:
		lineCounter =0;
		
		priors = Counter()
		likelihood = defaultdict(Counter)
		for line in file:
			lineCounter += 1
			columns = line.split(' ')
			for i in range(1, len(columns)):			
				priors[columns[0]] += 1
				likelihood[columns[0]][columns[i]] += 1

	return(priors, likelihood)

def readTestingData(fileName):
	lines = open(fileName).readlines()
	return(lines)

def classifyRandomly(line, priors, likelihood):
	keys = priors.keys()
	
	return (random.choice(list(keys)))
	
def classifyBayesan(line, priors, likelihood):
	keys = priors.keys()
	print("priors ",priors)

	max_class = (-1E6, '')
	
	print("smallest value ", -1E2)
	for key in keys:
		p = priors[key]
		columns = line.split(' ')

		"""key is not right here, 1st column went to words not categoried"""
		wordsPerCategory = float(sum(likelihood[key].values()))

		for i in range(1,len(columns)):
			word = columns[i]

			print("before calculation p value ", p, " likelhood ",likelihood[key][word]," words in category", wordsPerCategory)

			p = p * likelihood[key][word] / wordsPerCategory
			print("p value ", p, " and max current value is ", max_class[0])
		
		if p > max_class[0]:
			print("max class it to be updated from ", max_class)
			max_class = (p, key)
			print(" to ", max_class)


		print("max class value ", max_class)
	return (max_class[1])
	
def main():

	trainingFileName = sys.argv[1]
	testingFileName = sys.argv[2]

	(priors,likelihood) =readTrainingData(trainingFileName)
	lines = readTestingData(testingFileName)

	correctClassifications = 0;


	for line in lines:
		classification = classifyBayesan(line, priors, likelihood)
		if classification == line[0]:
			correctClassifications += 1


	print("correct classifications = ",(correctClassifications/len(lines))*100)



if __name__ == '__main__':
	main()