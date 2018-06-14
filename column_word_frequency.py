import csv
from collections import Counter

def column_word_counter():
    input_stream = open('external.csv')
    reader = csv.reader(input_stream, delimiter='\t')

    reader.next() #skip header
    cities = [row[2] for row in reader]

    for (k,v) in Counter(cities).iteritems():
        print ("{} appears {} times".format(k, v))