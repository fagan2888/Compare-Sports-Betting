import time
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
sports = ['basketball/usa/ncaa', \
          'basketball/usa/nba', \
          'basketball/usa/nba-g-league', \
          'american-football/usa/nfl', \
          'tennis/australia/atp-australian-open', \
          'tennis/australia/wta-australian-open', \
          'tennis/france/atp-french-open', \
          'tennis/france/wta-french-open' \
         ]
linesCount = {}
linesPositiveCount = {}
linesPositiveSum = {}

for sport in sports:
    linesCount[sport] = 0
    linesPositiveCount[sport] = 0
    linesPositiveSum[sport] = 0

    i = 1
    lastPage = 1
    while i <= lastPage: 
        driver.get('https://www.oddsportal.com/' + sport + '/results/#/page/' + str(i) + '/')
        soup = BeautifulSoup(driver.page_source, "html.parser")

        time.sleep(2)

        winningLines = soup.find_all('td', class_='result-ok')
        linesCount[sport] += len(winningLines)
        for line in winningLines:
            lineValue = line.text
            if lineValue.startswith('+'):
                linesPositiveCount[sport] += 1
                linesPositiveSum[sport] += int(lineValue)

        if lastPage == 1:
            pagination = soup.find(id='pagination')
            pages = pagination.findChildren('a' , recursive=False)
            lastPage = int(pages[-1]['x-page'])
        
        i+=1

# print(linesCount)
# print(linesPositiveCount)
# print(linesPositiveSum)

for sport in sports:
    print(sport)
    print("  Total Gms: " + str(linesCount[sport]))
    print("  Upset Pct: " + str(linesPositiveCount[sport]/linesCount[sport]))
    print("  Upset Avg: " + str(linesPositiveSum[sport]/linesPositiveCount[sport]))