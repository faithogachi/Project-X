import csv

class CsvWrapper(object):

    def add(self, arr):
        with open('skills.csv', 'a', newline='') as csvfile:
           reader = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
           reader.writerow(arr)
