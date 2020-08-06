#importing the important librarys needed to access website and beautiful soup
import requests
from bs4 import BeautifulSoup
import numpy as np





eventsURL = []
what = []
when = []
where = []
deadline =[]


#concatinating strings with begining of URL
urlFirst = "http://www.wikicfp.com/"

pages = np.arange(1, 10, 1)
#forloop to iterate through all the links
for page in pages:

    j = 1
    url = "http://www.wikicfp.com/cfp/call?conference=computer%20science&page="+ str(page)
    print(url)
    page = requests.get(url)

    # Initializing BeautifulSoup object and parsing
    soup = BeautifulSoup(page.content, 'html.parser')

    # obtaining links in a tags
    links = soup.find_all('a')

    # soup object to find text in table body of website
    table = soup.find('tbody')
    table_rows = soup.find_all('tr')
    for link in links:
        finalURL = urlFirst + link['href']
        eventsURL.append(finalURL)
        for tr in table_rows:
            j = j + 1
            td = tr.find_all('td')
            row = [i.text for i in td]

        #if statement to collect data in specfic fields of the table
            if 11 < j < 52:
                if j%2 == 0:
                    deadline.append(row.pop())
                    where.append(row.pop())
                    when.append(row.pop())

                else:
                    what.append(row.pop(1))



