from bs4 import BeautifulSoup, Comment
import requests
import csv
import os
from constants import *

def parse_years(years):
    """Parse input string into list of years

    Args:
        years (str): years formatted as XXXX-YYYY

    Returns:
        list: list of ints depicting the years
    """    
    # Split user input into the years specified, convert to ints
    years_split = list(map(int, years.split('-')))
    # if only 1 year then that is list
    if len(years_split) == 1:
        year_range = years_split
    else:
        # Make a complete list of years from first year specified to last.
        year_range = [str(x) for x in range(min(years_split), max(years_split) + 1)]

    return year_range

def get_website(site):
    """Get website Response object for parsing

    Args:
        site (str): URL address as a string

    Returns:
        (Response): Website reponse object
    """
    web_response = requests.get(site)
    return web_response.text

def generate_soup(html, parser):
    """Return BeautifulSoup object

    Args:
        html (str): text response from website requested
        parser (str): parser used by BeautifulSoup

    Returns:
        BeautifulSoup: Navigable BeautifulSoup object
    """    
    return BeautifulSoup(html, parser)

def extract_from_comment(soup):
    """Extract table data that is hidden in html comments

    Args:
        soup (BeautifulSoup): Navigable BeautifulSoup object

    Returns:
        NavigableString: Comment isolated as a NavigableString obj
    """    
    table_container_contents = soup.find('div', id='all_team-stats-per_game').contents
    # Information is hidden in html comments. This locates the the comment within the contents list
    for content in table_container_contents:
        if isinstance(content, Comment):
            comment_string = content.string
    return comment_string

def scrape_col(soup, tag, extended = False):
    """Return list of column headers

    Args:
        soup (BeautifulSoup): Navigable BeautifulSoup obj
        tag (str): tag you are wishing to locate

    Returns:
        list: list of column headers
    """    
    col_labels = []
    for col in soup.thead.find_all(tag):
        col_labels.append(col.text)
    if extended == True:
        return col_labels[1:]
    else:
        return ['Year'] + col_labels[1:]

def scrape_row(soup, tag, year = None):
    """Scrape all rows of team data

    Args:
        soup (BeautifulSoup): Navigable BeautifulSoup obj
        tag (str): tag which you are looking to scrape
        year (str): year of data that is extracted

    Returns:
        list: nested list containing each team and their stats
    """    
    stats_rows = []
    for team in soup.tbody.find_all(tag):
        # team name needs to be located seperately to remove asterisks
        team_name = team.td.a.text
        row = [year, team_name]
        # skip first instance since that is the name and it has
        # already been located.
        for stat in team.find_all('td')[1:]:
            row.append(stat.text)
        stats_rows.append(row)
    return stats_rows

def write_csv(file_name, col_labels, data_rows):
    """Generate new csv if none exists. Append to already existing csv

    Args:
        file_name (str): name of file to be writtin or appended to
        row (list): list of items to be written to csv.
    """        
    if os.path.exists(file_name):
        append_write = 'a'          # if csv file exists append to it
    else:
        append_write = 'w'          # if not generate new one

    in_file = open(file_name, append_write, newline='', encoding='utf-8')
    csv_writer = csv.writer(in_file)

    if append_write == 'w':
        # file does not exist write the col_labels first
        csv_writer.writerow(col_labels)
    # always write the data rows no matter what.
    for row in data_rows:
        csv_writer.writerow(row)
    in_file.close()

def generate_file_name(year_lst):
    """Generate a csv title including the years being scraped

    Args:
        year_lst (list): list containing the years being scrapped.

    Returns:
        str: csv file name specific to the years being scrapped.
    """    
    return f"{year_lst[0]}-{year_lst[-1]}_Team_Stats.csv"

def scrape_standings(soup, year):
    """Scrape standing information(W/L, etc.)

    Args:
        soup (BeautifulSoup): Navigable BeautifulSoup obj

    Returns:
        list: list of standings team stats
    """    
    stats_rows = []
    # Structure of website changes slightly between 2015 and present
    if int(year) > 2015:
        both_conferences = soup.find('div', class_='standings_confs')
    else:
        both_conferences = soup.find('div', class_='standings_divs')

    for conference in both_conferences.find_all('tbody')[:2]:
        for team in conference.find_all('tr', class_='full_table'):
            team_name = team.th.a.text
            row = [team_name, ]
            for stat in team.find_all('td'):
                row.append(stat.text)
            stats_rows.append(row)
    return stats_rows

def aggregate_data(game_stats_lst, standings_lst):
    """Combine two lists containing standings data and game stats

    Args:
        game_stats_lst (list): list of team game stats
        standings_lst (list): list of team standing stats

    Returns:
        list: Combined list
    """    
    for r1 in standings_lst:
        for r2 in game_stats_lst:
            # if team name is in other list replace that index with concat list.
            if r1[0] in r2:
                game_stats_lst[game_stats_lst.index(r2)] = r2 + r1[1:]
    return game_stats_lst