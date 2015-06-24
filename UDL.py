import argparse
import urllib2 as ul
from bs4 import BeautifulSoup

def is_lecture(link):    #this is given priority as always videos comes first
    if (("unit_" in link) or ("lesson" in link) or ("lecture" in link)) and ("problem_set" not in link) and ("subtitle" not in link):
        return True

def is_subtitle(link):  # this is given second priority because in most cases it comes
    if "subtitle" in link:
        return True
def is_problemSet(link):
    if "problem_set" in link:
        return True
def is_Office_Hours(link):
    if "office_hours" in link:
        return True
def is_Q_and_A(link):
    if "q_&_a" in link:
        return True



parser = argparse.ArgumentParser()
parser.add_argument("classId", help="display the udacity class id entered")
args = parser.parse_args()
course_link="https://www.udacity.com/wiki/"+args.classId+"/downloads"
response=ul.urlopen(course_link)
page_content=response.read()
soup=BeautifulSoup(page_content)
"""for link in soup.find_all('a'):
    temp_link=link.get('href')
    if ".zip" in temp_link:
        print temp_link
"""
anchors=soup.findAll('a')
links=[]
downloadables={}
downloadables["Lectures"]=[]      # track Id = 0
downloadables["Subtitles"]=[]     # track Id = 1
downloadables["Problem_Set"]=[]   # track Id = 2
downloadables["Office_Hours"]=[]  # track Id = 3
downloadables["Q_&_A"]=[]         # track Id = 4
downloadables["Others"]=[]

for a in anchors:
    if a.has_attr('href'):
       if ".zip" in a['href']:
          links.append(a['href'])
          temp_link=a['href'].lower()
          if is_lecture(temp_link):
             downloadables["Lectures"].append(temp_link)
             track_id=0
          elif is_subtitle(temp_link):
               downloadables["Subtitles"].append(temp_link)
               track_id=1
          elif is_problemSet(temp_link):
               downloadables["Problem_Set"].append(temp_link)
               track_id=2
          elif is_Office_Hours(temp_link):
               downloadables["Office_Hours"].append(temp_link)
               track_id=3
          elif is_Q_and_A(temp_link):
               downloadables["Q_&_A"].append(temp_link)
               track_id=4
          else:
               if track_id==0:
                  downloadables["Lectures"].append(temp_link)
               elif track_id==1:
                    downloadables["Subtitles"].append(temp_link)
               elif track_id==2:
                    downloadables["Problem_Set"].append(temp_link)
               elif track_id==3:
                    downloadables["Office_Hours"].append(temp_link)
               elif track_id==4:
                    downloadables["Q_&_A"].append(temp_link)
               else:
                    downloadables["Others"].append(temp_link)
print downloadables
