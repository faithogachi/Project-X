import unittest
import csv

from csv_wrapper import CsvWrapper

class CsvWrapperTest(unittest.TestCase):
    """
    Tests for the csv wrapper
    """

    def test_add_csv_row(self):
        arr_to_write = ['test', 'test', 'test']
        csv_wrapper = CsvWrapper()
        csv_wrapper.add(arr_to_write)
        

        # Reading a file to test if the row is there
        with open('skills.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            first_row = next(reader)
            self.assertEqual(first_row, arr_to_write)

       


    def test_read_csv(self):
        arr_to_write = ['testing', 'testing', 'testing']
        csv_wrapper = CsvWrapper()
        
        for i in range(0, 10):
            csv_wrapper.add(arr_to_write)
  
        results = csv_wrapper.read()
        self.assertEqual(len(results), 10)


    def tearDown(self):
        """
        This parts should empty the skills.csv after each tests runs
        """
        open('skills.csv', 'w').close()

if __name__ == '__main__':
    unittest.main()
