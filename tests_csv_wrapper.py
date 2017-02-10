import unittest
import csv

from csv_wrapper import CsvWrapper

class CsvWrapperTest(unittest.TestCase):
    """
    Tests for the csv wrapper
    """

    def test_add_csv_row(self):
        arr_to_write = ['test', 'test', False]
        csv_wrapper = CsvWrapper()
        csv_wrapper.add(arr_to_write)
        

        # Reading a file to test if the row is there
        with open('skills.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            first_row = next(reader)
            self.assertEqual(first_row, arr_to_write)

    def test_delete_csv_row(self):
        arr_to_delete = ['test', 'test', False]
        csv_wrapper = CsvWrapper()
        csv_wrapper.delete(arr_to_delete)

        #delete a file to test if .delete works
        with open('skills.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                self.assertNotEqual(row, arr_to_delete)

    def test_update_csv_row(self):
        arr_to_update = ['test', 'test', True]
        csv_wrapper = CsvWrapper()
        csv_wrapper.update(arr_to_update)

        #update a file to test if update works
        with open('skills.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                self.assertEqual(row, arr_to_update)


    
            

       



if __name__ == '__main__':
    unittest.main()
