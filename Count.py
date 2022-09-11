import json
from time import sleep
import re
import pandas as pd

skills=['objective-c', 'ghostwriting', 'content management systems', 'statistics', 'html', 'geometry', 'wordpress', 'basic math', 'trigonometry', 'java', 'outlook', 'photoshop', 'xml', 'macros', 'sap', 'automated billing systems', 'yoast', 'access', 'excel', 'technical writing', 'css', 'powerpoint', 'slides', 'forms', 'algebra', 'payment processing', 'journalism', 'arithmetic', 'asp.net', 'link to database', 'illustrator', 'crms', 'javascript', 'seo', 'free hand', 'business continuity planning', 'vertical lookups', 'pivot tables', 'sql', 'php', 'acrobat', 'c\+\+', 'word', 'python', 'docs', 'calculus', 'google sheets', 'onenote', 'indesign', 'oracle', 'ruby', 'c', 'ajax', 'netsuite', 'sheets', 'salesforce', 'openoffice', 'perl', 'corel draw', 'comparative analyses']
f=open("job_description.json", "r", encoding="utf-8")
datas=json.load(f)

count={}
skillcount=dict()


for job,job_des in datas.items():
    for skill in skills:
        for element in job_des:
            if re.search(skill,element):
                try:
                    count[job][skill]=count[job].get(skill,0)+1
                except:
                    count[job]=dict()
                    count[job][skill]=count[job].get(skill,0)+1
##
dat=[]
for job in datas.keys():
    for skill in skills:
        try:
            dat.append({"Job":job,"Skill":skill,"Count":count[job][skill]})
        except: continue

df=pd.DataFrame(dat)
df.to_csv('out.csv',index=False)

print("csv file created")