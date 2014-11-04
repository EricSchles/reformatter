from sys import argv
"""
csv to html
html to csv

xml to html
csv to xml

formatting 
"""

text = open(argv[1],"r")
#this captures the formatting which must be applied to all other files passed in
formatting = {"\n":[],"\t":[],"\r":[]," ":[]}
for ind,line in enumerate(text):
    for key in formatting.keys():
        if key in line:
            formatting[key].append(ind)


    
