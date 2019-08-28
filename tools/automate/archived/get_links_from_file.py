import os
import os.path
import shutil
from collections import defaultdict
from bs4 import BeautifulSoup
import re 
import json 

FILETYPE_TMP = ['0:', '1:', '2:', '3:', '4:', '5:' ]

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
        f = open(filename, "r", encoding="utf-8" )
        string_data = f.read()
        return string_data
    except FileNotFoundError:
        print("FileNotFoundError")

def getLinksFromFile(fileLoc):
    links = []  
    contents = open(fileLoc, "r").read()
    contents_l = list(filter(None, contents.split('\n')))
    for line in contents_l:
       
       if 'href' in line:
        soup = BeautifulSoup(line)
        links.append(soup.a['href'])
        # links[soup.a.string.rstrip().lstrip()] = soup.a['href']
       if 'iframe' in line:
        soup = BeautifulSoup(line)
        links.append(soup.iframe['src']) 
        # links[] = soup.iframe['src']
    return links

def getLinksFromFolder(path):
    d = {} # defaultdict(list)
    AllFiles = list(os.walk(path))
    for item in AllFiles:
        foldername, LoDirs, LoFiles = item
        print(LoFiles)
        for filename in LoFiles:
            if filename[-4:] == '.rst':
                tmp = getLinksFromFile(foldername + '/' + filename)
                if tmp is not None and len(tmp) > 0:
                    d[foldername + '/' + filename] = [""] + tmp
                # fullfilename = foldername + "/" + filename
                # phone = getNumber(fullfilename)
    return d 
"""
def dict_to_s (dictionary):
    s = "{" 
    for key in dictionary.keys():
        s += key + ':\n' 
        for i in range(len(dictionary[key])):
            s += str(i) + ': ' + dictionary[key][i] +'\n' 
        s += '\n' 
    return s

def dict_to_pretty_json (dictionary):
    s = "{" 
    for key in dictionary.keys():
        s += key + ':\n' 
        for i in range(len(dictionary[key])):
            s += str(i) + ': ' + dictionary[key][i] +'\n' 
        s += '\n' 
    s +="}"
    return s

def list_to_str(li):
    string = ''
    for i in li: 
        string += i +'\n'
    return string

def dict_to_li_pretty(dictionary):
    li = []
    for key in dictionary.keys():
        li.append(key+'\n')  
        for i in range(len(dictionary[key])):
            li[-1] += str(i) + ': ' + dictionary[key][i] +'\n' 
    return li 
"""
def main():
    path = input("Enter the path: ")
    dictionary = getLinksFromFolder(path)
    if dictionary is not None:
        saveFile('links.json', json.dumps(dictionary, indent=2, sort_keys=True))
main()

