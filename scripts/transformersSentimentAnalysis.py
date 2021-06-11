from transformers import pipeline
import re
classifier = pipeline('sentiment-analysis')
with open("data/mysql_analysis.csv","w") as output:
    with open("data/mysql.txt", 'r',encoding="utf8") as input:
        while True:
            text=re.sub("\n","",input.readline())
            if len(text) < 512:
                dic=classifier(text)
                output.write(text+"\t"+dic[0]['label']+"\t"+str(dic[0]['score'])+"\n")
            if not text:
                break