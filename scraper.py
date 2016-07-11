#!/usr/bin/env python
'''
Created on Apr 28, 2016

@author: Greta
'''
from bs4 import BeautifulSoup
import requests
import re

myurl='http://www.python.org'

def main():
    r=requests.get(myurl)
    soup=BeautifulSoup(r.content)
    print(soup.prettify())
    print(soup.tag_name_re)
    type(soup.tag_name_re)
#   soup.find_all(name, attrs, recursive, text, limit)
    x=soup.find_all()
    
    for tag in soup.find_all(re.compile("^\w.*")):
        print(tag.name)

## Need to load tag + text into hash]

if __name__ == '__main__': 
    main()
    pass