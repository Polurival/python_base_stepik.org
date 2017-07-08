import csv
import re

with open('Crimes.csv') as f:
    reader = csv.reader(f)

    popular_crimes_2015 = {}
    for row in reader:
        if re.search(r'.*2015.*', row[2]) is not None:
            if row[5] not in popular_crimes_2015:
                popular_crimes_2015[row[5]] = 1
            else:
                popular_crimes_2015[row[5]] = popular_crimes_2015[row[5]] + 1

    the_most_popular_crime_type = ''
    the_most_popular_crime_type_count = 0
    for crime_type, count in popular_crimes_2015.items():
        if count > the_most_popular_crime_type_count:
            the_most_popular_crime_type = crime_type
            the_most_popular_crime_type_count = count
    print(the_most_popular_crime_type)


