# NBA_team_stats_scraper
  ---
## About
NBA_team_stats_scraper is a webscraping application that accesses Basketball-Reference's NBA & ABA League Index located at https://www.basketball-reference.com/leagues/ and returns team's season averages including: Year, Team, G, MP, FG, FGA, FG%, 3P, 3PA, 3P%, 2P, 2PA, 2P%, FT, FTA, FT%, ORB, DRB, TRB, AST, STL, BLK, TOV, PF, PTS, W, L, W/L%, GB, PS/G, PA/G, SRS. After scraping, the application returns the data in the form of comma-seperated-value (csv) table.

What makes this application special is simplicity of the code that it is written in and the ease in which it is used. You are able to grab a single year of team data or a range of years by simply specifiying the desired range (i.e. '2012-2020').

## Module Layout
This module is composed of three main files: NBA_team_stats_scraper.py, functions.py, & constants.py. NBA_team_stats_scraper.py contains the main function (literally called main()) and controlls the execution flow of all functions located within functions.py. Constants.py contains the website url and parser used. Altering anything in constants.py will automatically break the module.

---
## How-To-Use
#### Installation
Start by cloning or downloading this repository.

NBA_team_stats_scraper utilizes BeautifulSoup, Requests, and lxml parser. To ensure the application works properly, install the exact package versions through the requirements.txt

```bash
  $ pip install -r requirements.txt
```

#### Scrapin'
Begin by opening a terminal within the directory in which the scripts are located and start a python session (typing 'python3' or 'python' depending on your setup):

```bash
  $ python
```
from here import everything from NBA_team_stats_scraper.py
```python
>>> from NBA_stats_scraper import *
```
In order to scrape, the only function you will need to use is main() located in NBA_team_stats_scraper.py as this function controls the execution pattern of the functions located in functions.py. main() takes a single argument and that argument is of type str. You can get a single year of team data like so:
```python
>>> from NBA_stats_scraper import *
>>> main('2020')
```
or you can get a range of years by specifying the year range with hyphen inbetween:
```python
>>> from NBA_stats_scraper import *
>>> main('2017-2020')
```
A new csv file containing the data should show in your current directory!

---
That's it! Happy scraping!