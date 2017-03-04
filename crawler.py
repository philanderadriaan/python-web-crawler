'''
Phil Adriaan
'''

import urllib.request
import urllib.parse
import re
import sys
from tkinter import *

def read():
    return open("urls.txt", "r").read().splitlines() 

def getLinks(url):
    return re.findall('<a href="(.*?)".*?>(.*?)</a>', str(urllib.request.urlopen(url).read()))

def getMaxKey(count):
    key = ''
    max = 0
    for i in count:
        if count[i] > max:
            key = i
            max = count[i]
    return key
    
def write(dict, count):
    file = open('output.csv', 'w')
    file.write('Page,Links\n')
    for i in dict:
        file.write(i + ',')
        for j in dict[i]:
            file.write(j[0] + ',')
        file.write('\n')
    file.write('\n')
    file.write('Highest number links pointed to,' + getMaxKey(count))
    file.close()
    
def displayResult(count):
    mGui = Tk()

    mGui.geometry()
    mGui.title('Top 10 Words')
    
    i = 10
    
    while (len(count) > 0 and i > 0):
        key = getMaxKey(count)
        max = count[key]
        
        print(key)
        print(max)
        
        max = max / 5.0
        
        l1 = Label(text=key, font=("Arial", )).pack()
        
        count.pop(key, None)
        i = i - 1
        
    mGui.mainloop()
    
def main():

    list = read()
    dict = {}
    while (len(list) > 0 and len(dict) < 100):
        url = list.pop(0)
        
        print('\n')
        print("Checking " + url)
        
        if url not in dict:
            try:
                dict[url] = getLinks(url)
                if len(dict[url]) <= 0:
                    print("No link found.")
                for link in dict[url]:
                    print(urllib.parse.urljoin(url, link[0]))
                    list.append(urllib.parse.urljoin(url, link[0]))
            except:
                print("Bad link.")
                None
        else:
            print("Cycle detected.")

    count = {}
    for i in dict:
        for j in dict[i]:
            word = j[1]
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1 
    

    write(dict, count)
    
    displayResult(count)
    
if __name__ == '__main__':
    main()