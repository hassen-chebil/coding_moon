from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import requests
import re
import json 
import datetime
from voiceSetup import talk,take_command



def corona():
    today = datetime.date.today().strftime('%Y-%m-%d')
    
    talk( "choose the country please")

    x=take_command()

    link_DataCountry = json.load(open("countriesCodes.json", "r"))

    talk( "Getting cases, please wait...")
        

    soup = BeautifulSoup(requests.get(f"https://www.worldometers.info/coronavirus/news-block/news_main_updates.php?fd=lm_{today}&country={link_DataCountry[x.lower()]}&days_count=3").content, 'html.parser').findAll('button', {'class': 'btn btn-light date-btn'})
        
    dates = []
    cases = []
    for date in soup:
        c = date.find_next_sibling('div', {'class': 'newsdate_div'}).findChild('li', {'class': 'news_li'})
        cases.append(c.text[:c.text.index('in')].strip())
        dates.append(date.text.strip())    

    new_cases = []
    new_deaths = []

    for e in cases:
        if "new cases" in e and "new deaths" in e:
            new_cases.append(e.split('and')[0].strip())
            new_deaths.append(e.split('and')[1].strip())
        elif "new cases" in e:
            new_cases.append(e)
            new_deaths.append("No new deaths")
        elif "new deaths" in e:
            new_cases.append("No new cases")
            new_deaths.append(e)
        else:
            new_cases.append("No new cases")
            new_deaths.append("No new deaths")
        
    return dates, new_cases, new_deaths
        
    