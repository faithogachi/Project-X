from csv_wrapper import CsvWrapper
class Skill:
	ids =0
	def __init__(self):
		self.skill = ""
		self.csv = CsvWrapper()
		self.ids = 0

	def add(self, skl):
		self.skill = skl
		#send to the the CV file
		self.ids = len(self.skillsAdded())
		newSkill = [self.ids, skl,False]
		return self.csv.add(newSkill)

	#def skillDone(self):
		#return skilladded();

	def skillsAdded(self):
		return self.csv.read();

	def skillsStudied(self):
		skills = skilladded()
		studied = []
		for skill in skills:
			if skill[2] == True:
				studied.append(skill)
		return studied

	def skillsNotStudied(self):
		skills = skilladded()
		notstudied = []
		for skill in skills:
			if skill[2] == False:
				notstudied.append(skill)
		return notstudied

	#def progress(self):
		#totalSkills = len(skilladded())
		#skillstudied = len(skillsStudied())

		#if totalSkills == 0 :
			#return "No skill have been added to tell the progress"
		#else :
			#prog = (skillstudied /totalSkills) * 100
			#return "Your progress is: " + str(prog)