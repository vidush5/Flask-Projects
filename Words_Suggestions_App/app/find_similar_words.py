import requests
import urllib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from urllib.error import HTTPError

def extract_synonym(word):
    #print(word)
    url = f'https://thesaurus.plus/thesaurus/{word}'
    #print(url)
    
    try:
        request = Request(url)
        response = urlopen(request)
        
        soup = BeautifulSoup(response, "html.parser")
        ul_tag =  soup.find('ul', {'class':'list paper'})
        synonyms = ul_tag.find_all('div', 'list_item')
        #print(soup.prettify())
        
        synonyms_list = []
    
        for syms in synonyms:
            synonyms_list.append(syms.text)
            
        synonyms_list = [x.strip(' ') for x in synonyms_list]
        
        return synonyms_list

    except Exception as e:
        print(e)
        



