import csv

class CsvWrapper(object):

    def add(self, arr): 
        """
        Adds a given row to the csv
        """
        with open('skills.csv', 'a', newline='') as csvfile:
           reader = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
           reader.writerow(arr)

    def read(self):
        """
        Returns all the data in the csv
        """
        
        with open('skills.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=",",quotechar="|")
            results = []
          
            for row in reader:
                results.append(row)

            return results
            
