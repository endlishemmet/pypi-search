import requests, re
from bs4 import BeautifulSoup as bs
from rich import print
from rich.markdown import Markdown

response = requests.get('https://pypi.org/search')
soup = bs(response.content, 'html.parser')

divs = soup.find_all('div', attrs={'class': 'accordion accordion--closed'})

categories = {}
for elems in divs:
    
    button = elems.find('button', 
        attrs={
            'type': 'button', 
            'class': re.compile(r'accordion__link -js-accordion-trigger'),
            'aria-controls': re.compile(r'accordion-.*')
        }
    )

    checkbox_tree = button.find_next_sibling().find('div', 
        attrs={
            'class': 'checkbox-tree'
        }
    ) 
    ul = checkbox_tree.ul
    
    topics = [i.get('for').replace('_', '') for i in ul.find_all('label', attrs={'class': 'checkbox-tree__label', 'for': re.compile('.*')})]
    topic_names = []
    for topic in topics:
        topic = topic.split('.')
        topic_names.append(topic[0]) if topic[0] not in topic_names else ''
    print(topic_names)
    