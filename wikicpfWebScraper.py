#importing the important librarys needed to access website and beautiful soup
import requests
from bs4 import BeautifulSoup
import numpy as np

#Initialized string being used for headers
headers = "what, when, where, deadline\n"

#Getting file name, opening and writing the headers into it
file_name = "wikiCS.csv"
f = open(file_name, "w")
f.write(headers)

#concatinating strings with begining of URL
urlFirst = "http://www.wikicfp.com/"
pages = np.arange(1, 10, 1)

#forloop to iterate through desired number of pages on the website
for page in pages:
    k = 1
    j = 1
    url = "http://www.wikicfp.com/cfp/call?conference=computer%20science&page="+ str(page)
    page = requests.get(url)

    # Initializing BeautifulSoup object and parsing
    soup = BeautifulSoup(page.content, 'html.parser')

    # obtaining links in a tags


    # soup object to find text in table body of website
    table = soup.find('tbody')
    table_rows = soup.find_all('tr')



    for tr in table_rows:
            j = j + 1
            td = tr.find_all('td')
            row = [i.text for i in td]

        #if statement to collect data in specific fields of the table
            if 11 < j < 52:
                if j%2 == 0:
                    deadline = row.pop()
                    where = row.pop()
                    when = row.pop()

                    #checking if the data scraped is blank if so null will fill the void
                    if when ==" ":
                        when = "null"
                    if where == " ":
                        where = "null"
                    if deadline == " ":
                        deadline = "null"


                else:
                    what = row.pop(1)
                    if what == " ":
                        what = "null"
                    f.write(what.replace(",", " ") + ","+ when.replace(",", " ")+ ","+ where.replace(",", " ") +"," + deadline.replace(",", " ") + "\n")


f.close()
