import csv

def classFactory(class_name, dictionary):
    return(class_name, (object,), dictionary)

class csvReader:
    data = []

    def __init__(self, filepath):
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimeter=',')
            for row in csv_data:
                self.data.append(row)
        pass
