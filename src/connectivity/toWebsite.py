from bs4 import BeautifulSoup
from requests import Session, RequestException

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

def request_url(session:Session, url:str, retries:int=3, timeout:int=10):
    """
    Lädt den Inhalt einer Webseite und gibt ihn zurück.

    Parameters
    ----------
    url : str
        Die URL der Webseite, die abgerufen werden soll.
    retries : int, optional
        Anzahl der Wiederholungsversuche im Falle eines Fehlers, by default 3.
    timeout : int, optional
        Zeitlimit für die Anfrage in Sekunden, by default 10.

    Returns
    -------
    str or None
        Der Inhalt der Webseite als Zeichenfolge oder None im Falle eines Fehlers.
    """
    for _ in range(retries):
        try:
            response = session.get(url, timeout=timeout, headers=HEADERS)
            response.raise_for_status()  # Wirft eine Ausnahme, wenn die Anfrage nicht erfolgreich war

            return response.text

        except RequestException as raised_exception:
            print(f"Fehler beim Abrufen von {url}: {raised_exception}")
            continue  # Versuche es erneut

    # Wenn alle Wiederholungsversuche fehlschlagen, gib None zurück
    print(f"Die Anfrage an {url} ist fehlgeschlagen.")
    return None

def parse_html_to_soup(html: str) -> BeautifulSoup:
    """
    Umwandlung des Seiteninhaltformats; von Text zu Soup.

    Parameters
    ----------
    html : str
        Seiteninhalt in Textform.

    Returns
    -------
    BeautifulSoup
        Seiteninhalt in Soup-Form.
    """
    soup = BeautifulSoup(html, 'html.parser')
    return soup