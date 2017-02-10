import unittest
from skills import Skill

class SkillClassTest(unittest.TestCase):

    def test_skill_add(self):
        skills= Skill()
        self.assertTrue(skills.add("Driving"),msg='Skill must be a valid text')

if __name__ == '__main__':
    unittest.main()