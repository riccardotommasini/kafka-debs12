import csv
import time
from datetime import datetime
from sys import argv

script, filename = argv

txt_file = filename
csv_file = filename.replace("txt", "csv")
        	

with open(txt_file, "r") as in_text:
    in_reader = csv.reader(in_text, delimiter = '\t')
    with open(csv_file, "w") as out_csv:
        out_writer = csv.writer(out_csv)
        for row in in_reader:
        	timestamp = row[0].split('+')[0][:-1]
        	d = datetime.strptime(timestamp,'%Y-%m-%dT%H:%M:%S.%f')
        	row[0] = long(time.mktime(d.timetuple()))
        	out_writer.writerow(row)