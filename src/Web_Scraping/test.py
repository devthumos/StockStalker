import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrap_state_info(state: str) -> dict:
    """
    Retorna informações do estado brasileiro
    :param state: nome do estado
    :return: dicionário com indicadores do estado
    """
    print(f"Picking {state} info...")
    state_url = f"https://www.ibge.gov.br/cidades-e-estados/{state}.html"
    page = requests.get(state_url)

    # page.content é onde tem o html
    soup = BeautifulSoup(page.content, "html.parser")
    indicadores = soup.select(".indicador")


    return [(ind.select(".ind-label")[0].text, ind.select(".ind-value")[0].text)
            for ind in indicadores]

print(scrap_state_info("sp"))