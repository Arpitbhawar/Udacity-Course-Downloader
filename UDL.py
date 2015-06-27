import argparse                 # pip install argparse
import urllib2 as ul            # comes with python 2.7 onwards
import json                     # pip install simplejson
import os                       # inbuilt
from bs4 import BeautifulSoup   # pip install beautifulsoup4
import sys                      # inbuilt  
import time                     # inbuilt
import subprocess               # 
import threading                #
import requests                 # sudo pip install requests
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
def get_size(start_path = 'AppliedCryptography/Subtitles'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def progress(filesize,total):
    try:
        frac = float(filesize)/float(total)
    except:
        frac = 0
    #sys.stdout.write("\r%s %3i%%" % (filename +" ", frac*100)  )
    return frac*100

def download(key,total):
    #href=downloadables[key]
    #href1=href[0:len(href)//2]
    #href2=href[len(href)//2:]


    thread1 = threading.Thread(target=Thread1,args=(key,total,))
    thread2 = threading.Thread(target=Thread2,args=(key,total,))
    thread3 = threading.Thread(target=Thread3,args=(key,total,))
    thread4 = threading.Thread(target=Thread4,args=(key,total,))
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
def Thread1(key,total):
    #print "Thread1 "+key
    href=downloadables[key]
    links=href[0:len(href)//4]
    for i in range (0,len(links)):
        url=links[i].encode('utf-8')
        filename=url.split("/")[-1].strip()
        path=cur_path+"/"+Main_dir+"/"+key+"/"+filename
        
        

        
        try:
            subprocess.call(["curl" ,"-L","-s","-C","-",url,"-o",path])
            #filesize=os.path.getsize(Main_dir+"/"+key)
            filesize=get_size(Main_dir+"/"+key)
            #print filesize
            sys.stdout.write(key+" Download progress: %d%%   \r" % (progress(filesize,total)) )
            sys.stdout.flush()
            
        except:
            errorLog.append(filename)
            print "Exception in downloading file "+filename +" Check if file is already downloaded"
    

def Thread2(key,total):
    #print "Thread2 "+key
    href=downloadables[key]
    links=href[len(href)//4:2*(len(href)//4)]
    for i in range (0,len(links)):
        url=links[i].encode('utf-8')
        filename=url.split("/")[-1].strip()
        path=cur_path+"/"+Main_dir+"/"+key+"/"+filename

        
        
        try:
            subprocess.call(["curl" ,"-L","-s","-C","-",url,"-o",path])
            #filesize=os.path.getsize(Main_dir+"/"+key)
            filesize=get_size(Main_dir+"/"+key)
            #print filesize
            sys.stdout.write(key +" Download progress: %d%%   \r" % (progress(filesize,total)) )
            sys.stdout.flush()
            
        except:
            errorLog.append(filename)
            print "Exception in downloading file "+filename +" Check if file is already downloaded"
    
    
def Thread3(key,total):
    #print "Thread2 "+key
    href=downloadables[key]
    links=href[2*(len(href)//4):3*(len(href)//4)]
    for i in range (0,len(links)):
        url=links[i].encode('utf-8')
        filename=url.split("/")[-1].strip()
        path=cur_path+"/"+Main_dir+"/"+key+"/"+filename

        
        
        try:
            subprocess.call(["curl" ,"-L","-s","-C","-",url,"-o",path])
            #filesize=os.path.getsize(Main_dir+"/"+key)
            filesize=get_size(Main_dir+"/"+key)
            #print filesize
            sys.stdout.write(key+" Download progress: %d%%   \r" % (progress(filesize,total)) )
            sys.stdout.flush()

        except:
            errorLog.append(filename)
            print "Exception in downloading file "+filename +" Check if file is already downloaded"
    
    
def Thread4(key,total):
    #print "Thread2 "+key
    href=downloadables[key]
    links=href[3*(len(href)//4):]
    for i in range (0,len(links)):
        url=links[i].encode('utf-8')
        filename=url.split("/")[-1].strip()
        path=cur_path+"/"+Main_dir+"/"+key+"/"+filename

        
        try:
            subprocess.call(["curl" ,"-L","-s","-C","-",url,"-o",path])
            #filesize=os.path.getsize(Main_dir+"/"+key)
            filesize=get_size(Main_dir+"/"+key)
            #print filesize
            sys.stdout.write(key+" Download progress: %d%%   \r" % (progress(filesize,total)) )
            sys.stdout.flush()

        except:
            errorLog.append(filename)
            print "Exception in downloading file "+filename +" Check if file is already downloaded"
    



start_time = time.time()
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
try:
    Main_dir=course_name.strip().replace(" ","")
except:
    print "Enter a valid Class Id Ex cs387"
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

downloadablesFileSize={}
downloadablesFileSize["Lectures"]=0
downloadablesFileSize["Subtitles"]=0
downloadablesFileSize["Problem_Set"]=0
downloadablesFileSize["Office_Hours"]=0
downloadablesFileSize["Q_&_A"]=0
downloadablesFileSize["Others"]=0



errorLog=[]

for a in anchors:
    if a.has_attr('href'):
       if ".zip" in a['href']:
          links.append(a['href'])
          temp_link=a['href'].lower()
          if is_lecture(temp_link):
             downloadables["Lectures"].append(a['href'])
             # for filesize
             res = requests.head(a['href'])
             downloadablesFileSize["Lectures"]=downloadablesFileSize["Lectures"]+int(res.headers["content-length"])
             track_id=0

          elif is_subtitle(temp_link):
               downloadables["Subtitles"].append(a['href'])
               # for filesize
               res = requests.head(a['href'])
               downloadablesFileSize["Subtitles"]=downloadablesFileSize["Subtitles"]+int(res.headers["content-length"])
               track_id=1

          elif is_problemSet(temp_link):
               downloadables["Problem_Set"].append(a['href'])
               # for filesize
               res = requests.head(a['href'])
               downloadablesFileSize["Problem_Set"]=downloadablesFileSize["Problem_Set"]+int(res.headers["content-length"])
               track_id=2

          elif is_Office_Hours(temp_link):
               downloadables["Office_Hours"].append(a['href'])
               # for filesize
               res = requests.head(a['href'])
               downloadablesFileSize["Office_Hours"]=downloadablesFileSize["Office_Hours"]+int(res.headers["content-length"])
               track_id=3

          elif is_Q_and_A(temp_link):
               downloadables["Q_&_A"].append(a['href'])
               # for filesize
               res = requests.head(a['href'])
               downloadablesFileSize["Q_&_A"]=downloadablesFileSize["Q_&_A"]+int(res.headers["content-length"])
               track_id=4
          else:
               if track_id==0:
                  downloadables["Lectures"].append(a['href'])
                  # for filesize
                  res = requests.head(a['href'])
                  downloadablesFileSize["Lectures"]=downloadablesFileSize["Lectures"]+int(res.headers["content-length"])
               elif track_id==1:
                    downloadables["Subtitles"].append(a['href'])
                    # for filesize
                    res = requests.head(a['href'])
                    downloadablesFileSize["Subtitles"]=downloadablesFileSize["Subtitles"]+int(res.headers["content-length"])
               elif track_id==2:
                    downloadables["Problem_Set"].append(a['href'])
                    # for filesize
                    res = requests.head(a['href'])
                    downloadablesFileSize["Problem_Set"]=downloadablesFileSize["Problem_Set"]+int(res.headers["content-length"])

               elif track_id==3:
                    downloadables["Office_Hours"].append(a['href'])
                    # for filesize
                    res = requests.head(a['href'])
                    downloadablesFileSize["Office_Hours"]=downloadablesFileSize["Office_Hours"]+int(res.headers["content-length"])
               elif track_id==4:
                    downloadables["Q_&_A"].append(a['href'])
                    # for filesize
                    res = requests.head(a['href'])
                    downloadablesFileSize["Q_&_A"]=downloadablesFileSize["Q_&_A"]+int(res.headers["content-length"])
               else:
                    downloadables["Others"].append(a['href'])
                    # for filesize
                    res = requests.head(a['href'])
                    downloadablesFileSize["Others"]=downloadablesFileSize["Others"]+int(res.headers["content-length"])
#print downloadables
print("--- %s seconds to read and write from udacity ---" % (time.time() - start_time))

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

    filesize=0
    #total=965019
    total=downloadablesFileSize[key]
    if  len(downloadables[key]) > 0:
        if not os.path.exists(Main_dir+"/"+key):
               os.makedirs(Main_dir+"/"+key)
        download(key,total)        
print("--- %s seconds to read and write ---" % (time.time() - start_time))

errString="["
if len(errorLog)>0:
   for i in (0,len(errorLog)):
       errString=errString+errorLog[i]+" "
   print errString + "] Check if these files are already downloaded if not resume the download"
else:
   print "All the files successfully downloaded"