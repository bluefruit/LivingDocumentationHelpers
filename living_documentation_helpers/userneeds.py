import csv

EXPECTED_NUMBER_OF_USERNEED_COLUMNS = 2

def load_userneeds_from_file(filename):
    userneeds = []
    with open(filename, 'r') as tsv:
        next(tsv) # Skip the title row
        for line in csv.reader(tsv, dialect='excel-tab'):
            if(len(line) != EXPECTED_NUMBER_OF_USERNEED_COLUMNS):
                continue
            userneeds.append({
                'id': line[0],
                'description': line[1]
            })
    return userneeds