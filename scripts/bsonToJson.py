# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:47:46 2021

@author: lolop
"""
import bson

with open("thisIsATestSubData.txt","w") as output:
    with open('commit_comments.bson', 'rb') as input:
        count=0
        while count<25:
            try:
                raw_data = input.read()
                output.write(str(bson.decode_all(raw_data)))
                if not raw_data:
                    break
            except (UnicodeDecodeError):
                pass
            count+=1