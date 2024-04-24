from bs4 import BeautifulSoup
import requests

scrape_url = "https://quotes.toscrape.com"

### Declares a variable that will store the contents of the website via requests
r = requests.get(scrape_url) ### requests.get will push a get request to the scrape_url


#Creates beautiful soup object, this is a parse tree that shows all of the HTML5 content in a readable format
soup = BeautifulSoup(r.content, 'html5lib')



### Tests prettify by printing the contents of the scrape url
#print(soup.prettify())


### Creates a list to store scraped quotes
quotes = []

table = soup.find('div', attrs = {'class' : 'quote'})


for row in table.find_all_next('div', attrs = {'class' : 'quote'}):
    quote = {}
    quote['text'] = row.find('span', attrs = {'class' : 'text'}).text
    quote['author'] = row.find('small', attrs = {'class' : 'author'}).text
    quote['tags'] = [tag.text for tag in row.find_all('a', attrs = {'class' : 'tag'})]
    quotes.append(quote)
    

##### Script is not writing all quotes into the .txt file. Will need to troubleshoot this later and figure out where I am going wrong.

#filename = 'quotes.txt'
#with open(filename, 'w', newline='') as f:
    #for quote in quotes:
        #f.write(quote['text'] + '\n')
        #f.write(quote['author'] + '\n')
       # f.write(quote ['tags'] + '\n')
        #f.write(quote'author'] = row.find('small', attrs = {'class' : 'author'}).text \n