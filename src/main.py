from bs4 import BeautifulSoup, Comment
from requests import Session

from connectivity.toWebsite import request_url, parse_html_to_soup


from typing import Tuple

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
URL ="https://www.pro-football-reference.com"
BOX_URL = URL+"/boxscores"


def extract_current_week_info(soup: BeautifulSoup) -> Tuple[str]:
    h2_element = soup.select_one('h2').text
    return h2_element.split()

def extract_all_boxscore_links(soup: BeautifulSoup) -> list:
    final_links = soup.select('a:-soup-contains("Final")')
    return [BOX_URL+link["href"] for link in final_links]

def build_gameday_links(season: str, current_week_number: str) -> list:
    links = list()
    for week_number in range(int(current_week_number), 0, -1):
        link = f"{URL}/years/{season}/week_{week_number}.htm"
        links.append(link)
    
    return links


def main():
    # Request from site
    http_session = Session()
    html = request_url(session=http_session, url=BOX_URL)
    soup = parse_html_to_soup(html=html)

    # Extract
    season, _ , current_week_number = extract_current_week_info(soup=soup)
    gameday_links = build_gameday_links(season=season, current_week_number=current_week_number)

    links_to_crawl = dict()
    for gameday_link in gameday_links:
        html = request_url(session=http_session, url=gameday_link)
        soup = parse_html_to_soup(html=html)

        week = gameday_link.split("/")[-1].split(".")[0]
        # season, _ , current_week_number = extract_current_week_info(soup=soup)
        boxscore_links = extract_all_boxscore_links(soup=soup)
        links_to_crawl[week] = boxscore_links

    # Load

    print(links_to_crawl)
    return

if __name__ == "__main__":
    main()