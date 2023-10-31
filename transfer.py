import os
import sys
import csv
import json
from datetime import datetime

COLUMNS_TO_KEEP = [
    "Data",
    "Weight",
]

input_file = sys.argv[1]
if not os.path.isfile(input_file):
    print("%s is not a valid faile" % input_file)
    sys.exit(1)
input_file = os.path.abspath(input_file)

resultData = []

with open(input_file) as f:
    templates = json.load(f)

    for data in templates["Data Points"]:
        startTime = datetime.utcfromtimestamp(int(data["startTimeNanos"])/1000000000).strftime('%d/%m/%Y')
        weight = int(data['fitValue'][0]['value']['fpVal'] * 1000)
        print(startTime)
        print(data["startTimeNanos"])
        print(weight)
        tmp = []
        tmp.append(startTime)
        tmp.append(weight)
        resultData.append(tmp)

with open("fit_data.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(COLUMNS_TO_KEEP)
    writer.writerows(resultData)
