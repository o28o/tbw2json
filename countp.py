#to run script in bash use line below. you versoon of python, imdtsll BeautifulSoup4, your nale of the script
#find bw/sn/ -type f | xargs -I {} python3.11 new/soup.py {}
import sys
from bs4 import BeautifulSoup
import os
import json
import re


# path to file from args
file_path = sys.argv[1]
filename = os.path.splitext(os.path.basename(file_path))[0]

# set of texts only name sn mn dn 
sn_variable = ''.join(filter(str.isalpha, filename))

# mkdir if not exsist function
def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# making dirs
create_directory_if_not_exists(f"roottbw/{sn_variable}")
create_directory_if_not_exists(f"translation/{sn_variable}")

# reading HTML-file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# parsing HTML-content
soup = BeautifulSoup(html_content, 'html.parser')

# lang list
languages = ['pi', 'en']
#languages = ['en']

# iterate langs
for lang in languages:
    # find all <div> elements with lang attribute equal to current lang
    div = soup.find('div', {'lang': lang})
    
    # find all <p> tags inside the current <div>
    paragraphs = div.find_all('p')
    
    # output the result
    print(f'{filename} {lang} pcount: {len(paragraphs)}')
