import time
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

    time.sleep(2)
    print(f"Picking {state} type...")
    lst_state_urls = [f"https://statusinvest.com.br/acoes/{state}", f"https://statusinvest.com.br/fundos-imobiliarios/{state}",
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
        return ("fundos-imobiliarios/", lst_state_urls[exist])
    elif exist == 2:
        return ("bdrs/", lst_state_urls[exist])
    elif exist == 3:
        return ("fundos-de-investimento/", lst_state_urls[exist])
    elif exist == 4:
        return ("tesouro/", lst_state_urls[exist])


# A função retorna erro para tesouros e fundos de investimento, temos que fazer outra função
# Específica para tesouros e fundos de investimento
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

    div_indicadores = soup.select(".top-info.has-special.d-flex.justify-between.flex-wrap") # Onde está o valor atual
    # [0] = VALOR ATUAL DO ATIVO, [1] = MIN. 52 SEMANAS, [2] = MAX. 52 semanas, [3] DIVIDEND YIELD ULTIMOS 12 MESES
    # [4] = VALORIZAÇÃO NO PREÇO DO ATIVO COM BASE NOS ÚLTIMOS 12 MESES
    indicadores = [ind.text for ind in div_indicadores[0].select(".value")]
    nome_empresa = soup.select(".company-description.w-100.w-md-70.ml-md-5") # div onde está o nome da empresa

    return (indicadores, typestate[0][0:-1],
            [ind.select(".d-block.fs-4.m-0.fw-600.text-main-green-dark")[0].text for ind in nome_empresa])


cod = input("Insira o Código de Negociação: ")
value = scrap_state_info(cod)
print(f"Empresa: {value[2][0]}\nTipo de Negociação: {value[1]}")
print(f"Indicadores:\n\tValor Atual: {value[0][0]}\n\tValor Min. 52 Semanas: {value[0][1]}\n\tValor Min. 52 Semanas: {value[0][2]}")
print(f"\tTaxa de Dividendo nos ùltimos 12 meses: {value[0][3]}\n\tValorização no Preço do Ativo durante 12 Meses: {value[0][4]}")
