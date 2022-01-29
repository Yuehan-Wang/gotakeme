import csv
import re
from csv import writer

# with open('courses_detail.csv','w',encoding='utf8',newline='') as f_new:
#     thewriter = writer(f_new)
#     header = ['Term','Prereq OR','Prereq AND']
#     thewriter.writerow(header)

desc_val = []
def desc_get():
    csv_file = csv.reader(open('courses.csv','r'))
    for row in csv_file:
        desc_val.append([row[2]])

desc_get()

def desc_proc(desc_val):
    for val in desc_val[1::]:
        term = re.findall(r'.*Terms Offered:(.*?)Prerequisite(s).*', val[0], re.I)
        print(term)
        print(val[0])
desc_proc(desc_val)
