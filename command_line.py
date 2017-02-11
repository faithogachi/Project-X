"""
This module defines a command line interface for the skills tracking program.
usage:

program_name.py --a or -a : add a new skill
program_name.py --view_all or -l : add a new skill
program_name.py --view_studied or -s : add a new skill
program_name.py --view_unstudied or -u : add a new skill
program_name.py --progress or -p : add a new skill


"""
import argparse
from skills import Skill
parser = argparse.ArgumentParser(
    description="A command line app for tracking personal progress"
)

parser.add_argument('--add', '-a', action='store_true', help='add a skill')
parser.add_argument('--view_all', '-l', action='store_true', help='view all skills')
parser.add_argument('--view_studied', '-s', action='store_true', help='view all skills studied')
parser.add_argument('--view_unstudied', '-u', action='store_true', help='view all unstudied skills')
parser.add_argument('--progress', '-p', action='store_true', help='view progress')
parser.add_argument('--done', '-d', action='store_true', help='mark skill done')

args = parser.parse_args()

skill = Skill()
if args.add:
    print("You have chosen to add a skill:\n")
    skillname = input("Enter the skill name:")
    if (skill.add(skillname)):
    	print("You have successfully added a new Skill: " + skillname)

if args.view_all:
		#incompleteSkills = skills.skillsNotStudied()
	#output = ""
	#for skl in incompleteSkills:
		#output=output+"\n"+ skl[0]."."+ skl[1]
	    #print("You have marked skill completed")
    print(skill.skillsAdded())

if args.view_studied:
    print("You have chosen to view all studied skills")

if args.view_unstudied:
    print("You have chosen to view all unstudied")

if args.progress:
    print("You have chosen to view progress")

if args.done:
	#fetch all skills that are not yet done
	print("")
	#incompleteSkills = skills.skillsNotStudied()
	#output = ""
	#for skl in incompleteSkills:
		#output=output+"\n"+ skl[0]."."+ skl[1]
	    #print("You have marked skill completed")