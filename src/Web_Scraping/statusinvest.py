import requests
from bs4 import BeautifulSoup
import pandas as pd


def type_state(state: str) -> str:
    """
    Retorna o tipo do estado
    :param state: código de negociação
    :return: string que qualifica o tipo de negociação, None caso código de negociação seja inválido
    """

    # Quando o state não "existe" o usuário é direcionado para uma página de ocorreu um erro, assim é só pegar
    # Uma classe específica para a situação de erro e colocar seu conteúdo em uma lista
    # Assim, caso a lista seja nula, quer dizer que o state existe, caso a lista não seja nula, isto é, com elemento
    # "OPS . . .", isso quer dizer que o state não existe

    print(f"Picking {state} type...")
    lst_state_urls = [f"https://statusinvest.com.br/acoes/{state}", f"https://statusinvest.com.br/fundo-imobiliarios/{state}",
                    f"https://statusinvest.com.br/bdrs/{state}", f"https://statusinvest.com.br/fundos-de-investimento/{state}",
                    f"https://statusinvest.com.br/tesouro/{state}"]

    # Caso o state tenha uma qualificação, ou seja, existe, "exist" guardara o seu índice na lista
    # Caso não exista, "exist" guardara o valor 0
    exist = -1

    for i, url in enumerate(lst_state_urls):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")


        banner = soup.select(".banner-section")
        ops = [(ind.select(".d-block.mb-1.fw-900")[0].text) # classe existente apenas na página de erro
         for ind in banner]

        if not ops: # Caso ops seja uma lista nula
            exist = i

    if exist == -1:
        return (None, None)
    elif exist == 0:
        return ("acoes/", lst_state_urls[exist]) # Retornando o tipo e a respectiva url existente
    elif exist == 1:
        return ("fundo-imobiliario/", lst_state_urls[exist])
    elif exist == 2:
        return ("bdrs/", lst_state_urls[exist])
    elif exist == 3:
        return ("fundos-de-investimento/", lst_state_urls[exist])
    elif exist == 4:
        return ("tesouro/", lst_state_urls[exist])


def scrap_state_info(state: str) -> dict:
    """
    Retorna informações da ação escolhida
    :param state: código de negociação da ação
    :return: dicionário com os indicadores da ação, None se código de negociação inválido
    """

    print(f"Picking {state} info...")

    typestate = type_state(state)

    if typestate[0] == None:
        return typestate[0]

    page = requests.get(typestate[1])

    soup = BeautifulSoup(page.content, "html.parser")
    indicadores = soup.select(".info.special.w-100.w-md-33.w-lg-20") # Onde está o valor atual

    return ([ind.select(".value")[0].text for ind in indicadores], typestate[0][0:-1])


cod = input("Insira o Código de Negociação: ")
value = scrap_state_info(cod)
print(f"Tipo de Negociação: {value[1]}\nValor Atual: {value[0][0]}")
