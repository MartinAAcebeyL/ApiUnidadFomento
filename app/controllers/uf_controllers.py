import requests
from bs4 import BeautifulSoup
from app.utils.helpers import get_month_name, valide_date


UF_URL = 'https://www.sii.cl/valores_y_fechas/uf/uf{}.htm'


def get_uf_value(date_str: str) -> str:
    if not valide_date(date_str):
        raise Exception("Invalid date")

    day, month, year = date_str.split("-")
    month = get_month_name(int(month)).lower()
    day = int(day)

    # Hacer el request a la URL y obtener el contenido HTML
    response = requests.get(UF_URL.format(year))
    html_content = response.text
    # Parsear el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    div = soup.find('div', {'id': f'mes_{month}'})

    table = div.find('table')
    th = table.find('th', string=str(day))
    td = th.find_next_sibling('td')
    return td.text
