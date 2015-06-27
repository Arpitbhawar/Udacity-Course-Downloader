import argparse
import urllib2 as ul
import json
import os
from bs4 import BeautifulSoup
import pycurl
import sys
import time
import subprocess
import threading
# install lxml "sudo pip install lxml" and apt-get install python-lxml

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

def download(key):
    #href=downloadables[key]
    #href1=href[0:len(href)//2]
    #href2=href[len(href)//2:]


    thread1 = threading.Thread(target=Thread1,args=(key,))
    thread2 = threading.Thread(target=Thread2,args=(key,))
    thread3 = threading.Thread(target=Thread3,args=(key,))
    thread4 = threading.Thread(target=Thread4,args=(key,))
    thread1.daemon=True
    thread2.daemon=True
    thread3.daemon=True
    thread4.daemon=True
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    """
    for i in range(0,len(downloadables[key])):
        url=downloadables[key][i].encode('utf-8')
        path=cur_path+"/"+Main_dir+"/"+key
        filename=url.split("/")[-1].strip()
        path=path+"/"+filename
        subprocess.call(["curl" ,"-L","-C","-",url,"-o",path])
    """
def Thread1(key):
    #print "Thread1 "+key
    href=downloadables[key]
    links=href[0:len(href)//4]
    for i in range (0,len(links)):
        url=links[i].encode('utf-8')
        filename=url.split("/")[-1].strip()
        path=cur_path+"/"+Main_dir+"/"+key+"/"+filename
        subprocess.call(["curl" ,"-L","-C","-",url,"-o",path])

def Thread2(key):
    #print "Thread2 "+key
    href=downloadables[key]
    links=href[len(href)//4:2*(len(href)//4)]
    for i in range (0,len(links)):
        url=links[i].encode('utf-8')
        filename=url.split("/")[-1].strip()
        path=cur_path+"/"+Main_dir+"/"+key+"/"+filename
        subprocess.call(["curl" ,"-L","-C","-",url,"-o",path])
    
def Thread3(key):
    #print "Thread2 "+key
    href=downloadables[key]
    links=href[2*(len(href)//4):3*(len(href)//4)]
    for i in range (0,len(links)):
        url=links[i].encode('utf-8')
        filename=url.split("/")[-1].strip()
        path=cur_path+"/"+Main_dir+"/"+key+"/"+filename
        subprocess.call(["curl" ,"-L","-C","-",url,"-o",path])
    
def Thread4(key):
    #print "Thread2 "+key
    href=downloadables[key]
    links=href[3*(len(href)//4):]
    for i in range (0,len(links)):
        url=links[i].encode('utf-8')
        filename=url.split("/")[-1].strip()
        path=cur_path+"/"+Main_dir+"/"+key+"/"+filename
        subprocess.call(["curl" ,"-L","-C","-",url,"-o",path])
    




parser = argparse.ArgumentParser()
parser.add_argument("classId", help="display the udacity class id entered")
args = parser.parse_args()

# course name extracted for making folder with that
# 25-6-2015 starts -- folder name
udacity_api_response=ul.urlopen('https://udacity.com/public-api/v0/courses')
json_response = json.loads(udacity_api_response.read())
for course in json_response['courses']:
    if course['key']==args.classId :
       course_name=course['title']
       break
Main_dir=course_name.strip().replace(" ","")
if not os.path.exists(Main_dir):
       os.makedirs(Main_dir)

#cur_path=os.path.dirname(os.getcwd())
cur_path=os.getcwd()
#print cur_path
# 25-6-2015 ends -- folder name

course_link="https://www.udacity.com/wiki/"+args.classId+"/downloads"
response=ul.urlopen(course_link)
page_content=response.read()
soup=BeautifulSoup(page_content)

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
             downloadables["Lectures"].append(a['href'])
             track_id=0
          elif is_subtitle(temp_link):
               downloadables["Subtitles"].append(a['href'])
               track_id=1
          elif is_problemSet(temp_link):
               downloadables["Problem_Set"].append(a['href'])
               track_id=2
          elif is_Office_Hours(temp_link):
               downloadables["Office_Hours"].append(a['href'])
               track_id=3
          elif is_Q_and_A(temp_link):
               downloadables["Q_&_A"].append(a['href'])
               track_id=4
          else:
               if track_id==0:
                  downloadables["Lectures"].append(a['href'])
               elif track_id==1:
                    downloadables["Subtitles"].append(a['href'])
               elif track_id==2:
                    downloadables["Problem_Set"].append(a['href'])
               elif track_id==3:
                    downloadables["Office_Hours"].append(a['href'])
               elif track_id==4:
                    downloadables["Q_&_A"].append(a['href'])
               else:
                    downloadables["Others"].append(a['href'])
#print downloadables


"""
for key in downloadables:
    if  len(downloadables[key]) > 0:
        if not os.path.exists(Main_dir+"/"+key):
               os.makedirs(Main_dir+"/"+key)
        for i in range(0,len(downloadables[key])):
            url=downloadables[key][i].encode('utf-8')
            path=cur_path+"/"+Main_dir+"/"+key
            filename=url.split("/")[-1].strip()
            path=path+"/"+filename
            subprocess.call(["curl" ,"-L","-C","-",url,"-o",path])
"""
start_time = time.time()
for key in downloadables:
    if key=="Problem_Set":
       if  len(downloadables[key]) > 0:
           if not os.path.exists(Main_dir+"/"+key):
                  os.makedirs(Main_dir+"/"+key)
           download(key)        
print("--- %s seconds to read and write ---" % (time.time() - start_time))
