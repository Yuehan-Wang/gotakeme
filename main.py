from bs4 import BeautifulSoup
from csv import writer
import requests

url = "http://collegecatalog.uchicago.edu/thecollege/economics/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
courses = soup.find_all('div', class_="courseblock main")

with open('courses.csv','w',encoding='utf8',newline='') as f:
    thewriter = writer(f)
    header = ['Title','Desc','Time_Prereq']
    thewriter.writerow(header)

    for course in courses:
        title = course.find('p', class_="courseblocktitle").text.replace('<p class="courseblocktitle"><strong>', '')
        desc = course.find('p', class_="courseblockdesc").text.replace('<p class="courseblockdesc">', '')
        time_prereq = course.find('p', class_="courseblockdetail")
        if time_prereq is not None:
            time_prereq = time_prereq.text.replace('<p class="courseblockdetail">', '')
        info = [title, desc, time_prereq]
        thewriter.writerow(info)