from BeautifulSoup import BeautifulSoup
import requests
import re

BASE="https://www.klsdiversified.com"

# Parse home page for contact url
page = requests.get(BASE)
parsed = BeautifulSoup(page.content)
for tag in parsed.findAll('a'):
    resolved = tag.get('href')
    if resolved is not None and "contact" in resolved:
        contact=BASE+resolved
        break

# Parse phone number from contact page
page = requests.get(contact)
parsed = BeautifulSoup(page.content)
# Parse the html for a regex match of 3 4 and 4 digits separated by a .
for data in parsed.findAll(text=re.compile('\d{3}\.\d{3}\.\d{4}')):
    if data.startswith('T'): # The line starting with T is the telephone number
        print data.split()[1] # Get the number by doing a default split and taking the second value
        break
