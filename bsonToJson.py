# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:47:46 2021

@author: lolop
"""
import bson

with open("commentsInJson.txt","w") as output:
    for i in range(5):
        with open("commit_comments.bson", 'rb') as file:
            output.write(bson.BSON.decode(file.read()))
