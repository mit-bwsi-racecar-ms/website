import os
import os.path
import shutil
from collections import defaultdict
from bs4 import BeautifulSoup
import re 
import json 
import ast
#                0      
def saveFile(filename, content):
    """ 
        writes content into a file w/ filename
    """
    f = open(filename, "w" )    
    f.write(content)    
    f.close() 


def openfile(filename):
    """ 
        opens a file and returns its contents as a string 
    """
    try:
        f = open(filename, "r",encoding='us-ascii')
        string_data = f.read()
        return string_data
    except FileNotFoundError:
        print("FileNotFoundError")

def file4(key, li):
    content = openfile(TEMPLATE[4])
    content = content.replace('<TITLE>', li[0])
    content = content.replace('<LINK1>', '<' + li[1] + '/>')
    content = content.replace('<LINK2>', li[2]) 
    content = content.replace('<LINK3>', '<' + li[3] + '/>')
    content = content.replace('<LINK4>', li[4])
    content = content.replace('<LAB>', li[0] + 'lab')
    saveFile(path+'/'+key, content)

def file5(key, li):
    content = openfile(TEMPLATE[5])
    content = content.replace('<TITLE>', li[0])
    content = content.replace('<LINK1>', '<' + li[1] + '/>')
    content = content.replace('<LINK2>', li[2])
    content = content.replace('<LINK3>', '<' + li[3] + '/>')
    content = content.replace('<LINK4>', li[4])
    content = content.replace('<LINK5>', '<' + li[5] + '/>')
    content = content.replace('<LAB>', li[0] + ' Lab')
    saveFile(path+'/'+key, content)

def createFiles(d):
   unchanged_list = []
   # print(d.keys())
   for key in d.keys():
    # print(key)
    if type(d[key][-1]) == int and d[key][-1] < len(TEMPLATE) and d[key][-1] < len(TEMPLATE_FUNC):
        if TEMPLATE_FUNC[d[key][-1]] is not None:
            TEMPLATE_FUNC[d[key][-1]](key, d[key])
            print(TEMPLATE_FUNC[d[key][-1]].__name__+':', key) 
    else:
        print("not replaced: " + key)

TEMPLATE = [None, None, None, None, 'tmp4.txt', 'tmp5.txt' ]
TEMPLATE_FUNC = [None, None, None, None, file4, file5] 
path = None

def main():
    global path
    path = input("Enter the where files to be created are relative to current path: ")
    filename= input("Enter the .json link file path: ")
    content = openfile(filename)
    d = ast.literal_eval(content) 
    # print(d)
    createFiles(d)
    saveFile('updated_' + filename, json.dumps(d, indent=2, sort_keys=True))
    # print(type(d['./02-curriculum/05-finalchallenge/overview.rst']))

main()

"""
    link_replacements = len(d[key]) - 1 
    if link_replacements == 4 and 'project' not in key:
       file4(key, d[key])  
       print("created4 " + key) 
       # d[key].append(4)
    elif link_replacements == 5 and 'project' not in key:
       file5(key, d[key])  
       print("created5 " + key)
       # d[key].append(5)
    else:
        print("not replaced: " + key + str(link_replacements))
        unchanged_list.append(key)
   return unchanged_list
    
    file4(key, d[key])
            print("created4 " + key) 
            del d[key][-1] 
        elif d[key][-1] == 5:
            file5(key, d[key])
            print("created5 " + key) 
            del d[key][-1] 
        else:
            print("no template: " + key)
    else:
            print("\nnot replaced: " + key +'\n')
"""

