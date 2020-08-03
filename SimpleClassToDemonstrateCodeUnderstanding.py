#!usr/bin/env python
import argparse


class SimpleClassToDemonstrateCleanCode(object):

	def __init__(self):
		self.name = args.employeeName
		self.profession = args.profession

	def iKnowCleanCode(self, name):
		newEmployee = name + """ took software
		architechture lecture. Thus, she knows
		the importance of readable code.""""
		return newEmployee

	def iAmYourOption(self, profession):
		job = "The " + profession + """ suits me well given 
		that I am good at understanding python code.  Thanks 
		to my lectures I learned softwwware principles such 
		as to follow the 100 lines row per class (not always 
		possible). Write properly variable names and 
		definitions in such way that it makes it easy to 
		understand while reading it. I learned how some 
		companies even went into bankruptcy due to the 
		technical debt or wrong selection of noSQL system"""
		return job

	def run(self, name, profession):
		clean = SimpleClassToDemonstrateCleanCode()
		print(clean.iKnowCleanCode(name))
		print(clean.iAmYourOption(profession))
		

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-e',"--employeeName", 
				type=str, default="Benazir", 
				help="write employee name")
	parser.add_argument('-p',"--profession", 
				default= "desire job", 
				type=str,
				help="write employee profession")
    parser.add_argument('-o', "--option",
                default="option",
                type=str
                help="demo git")
	args = parser.parse_args()	

	cleanClass = SimpleClassToDemonstrateCleanCode()
	cleanClass.run(args.employeeName, args.profession)
	
	


