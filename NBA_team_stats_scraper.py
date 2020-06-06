# -*- coding: utf-8 -*-
'''Scrapes the team season total stats from basketballreference.com'''

from functions import *

def main(years):
    """Scrape team total stats from the years specified.

    Args:
        years (str): years in format XXXX-YYYY i.e. 2017-2020
    """
    year_range = parse_years(years)
    file_name = generate_file_name(year_range)

    for year in year_range:
        web_response = get_website(SITE + year + '.html')
        soup = generate_soup(web_response, PARSER)
        comment_string = extract_from_comment(soup)
        table_html = generate_soup(comment_string, PARSER)
        col_labels = scrape_col(table_html, 'th')
        col_labels_extended = col_labels + scrape_col(soup, 'th', True)
        data_rows = scrape_row(table_html, 'tr', year)
        standings_data = scrape_standings(soup, year)
        aggregated_data = aggregate_data(data_rows, standings_data)
        write_csv(file_name, col_labels_extended, aggregated_data)