import requests
from bs4 import BeautifulSoup
from app.utils.helpers import get_month_name

UF_URL = 'https://www.sii.cl/valores_y_fechas/uf/uf{}.htm'


def get_uf_value(date_str: str) -> str:
    year, month, day = date_str.split("-")
    month = get_month_name(int(month)).lower()
    day = int(day)

    # Hacer el request a la URL y obtener el contenido HTML
    response = requests.get(UF_URL.format(year))
    html_content = response.text
    # Parsear el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Seleccionar el div por id
    div = soup.find('div', {'id': f'mes_{month}'})

    # Seleccionar la tabla dentro del div
    table = div.find('table')
    th = table.find('th', text=str(day))
    td = th.find_next_sibling('td')
    return td.text
