# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 16:13:07 2021

@author: lolop
"""
# This first part is to collect the first five repositories concerning mongodb and in each one of them to collect all their comments

import requests,re
dataName=requests.get("https://api.github.com/search/repositories?q=mysql&per_page=1").json()
reposName=[]
for name in dataName["items"]:
    reposName.append(name["full_name"])
numberOfComments=0
file = open("data/mysql.txt","w+",encoding="utf-8")
for curRepo in reposName:
    count=1
    while True:
        data=requests.get("https://api.github.com/repos/"+curRepo+
                          "/comments?per_page=150&page="+str(count)).json()
        if len(data) == 0:
            break
        for comment in data:
            file.write(re.sub("(\n|\r|(\s(\s)+))","",comment["body"])+"\n")
        numberOfComments+=1
        count+=1
file.close()


"""
# This second part is to create a dataSubset of the first ten comments of the first mongodb repository taking all the fields into account
import requests,re
dataName=requests.get("https://api.github.com/search/repositories?q=mongodb&per_page=1").json()
reposName=[]
for name in dataName["items"]:
    reposName.append(name["full_name"])

file = open("dataSubset.txt","w+",encoding="utf-8")
for curRepo in reposName:
    data=requests.get("https://api.github.com/repos/"+curRepo+
                      "/comments?per_page=10&page=1").json()
    for comment in data:
        for key in comment:
            if key=="user":
                for userKey in comment[key]:
                    file.write(str(comment[key][userKey])+';')
            elif key=="body":
                file.write(re.sub("(\n|\r|(\s(\s)+))","",comment["body"]))
            else:
                file.write(str(comment[key])+';')
        file.write("\n")
file.close()
"""