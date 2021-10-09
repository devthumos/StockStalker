from bs4 import BeautifulSoup
import requests


class Webscrapper:
    def get_link(self, codigo: str) -> tuple or bool:
        """
        Retorna Falso
        :param codigo:
        :return: link do código, caso existente e False caso não existente
        """
        urls = [
            ("".join(["https://statusinvest.com.br/acoes/", codigo]), "Ação"),
            ("".join(["https://statusinvest.com.br/fundos-imobiliarios/", codigo]), "Fundo Imobiliario"),
            ("".join(["https://statusinvest.com.br/fundos-de-investimento/", codigo]), "Fundo de Investimento"),
            ("".join(["https://statusinvest.com.br/bdrs/", codigo]), "BDRS"),
            ("".join(["https://statusinvest.com.br/tesouro/", codigo]), "Tesouro")
        ]

        for enum in range(0, 5):
            result = requests.get(urls[enum][0]).text
            doc = BeautifulSoup(result, "html.parser")

            tag = doc.find(class_="d-block mb-1 fw-900")
            if hasattr(tag, "OPS. . ."):
                if tag.string == "OPS. . .":
                    pass
            else:
                return urls[enum][0], urls[enum][1]

        return False

    def get_indict(self, urls: tuple) -> list:
        """

        :param urls:
        :return: Retorna uma lista contendo uma lista de tuplas, title e value, e o tipo de negociação do código inserido
        """
        result = requests.get(urls[0]).text
        doc = BeautifulSoup(result, "html.parser")

        tag = doc.find_all(class_="value")
        list_values = tag[:6]

        list_clean_indict = [
            [list_values[i].string for i in range(0, len(list_values))],
            urls[1]
        ]

        return list_clean_indict

    def main(self, codigo):
        return self.get_indict(self.get_link(codigo))
