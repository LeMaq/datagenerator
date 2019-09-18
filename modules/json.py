# -*- coding: utf-8 -*-
"""To JSON"""


def to_json(dataset):
    """Converte um array de dicionários em uma string no formato JSON.

    Args:
        dataset (list): O dataset a ser convertido.

    Returns:
        str: A string equivalente a um objeto JSON para o dataset fornecido.

    """
    json_format = "["
    for (index, person) in enumerate(dataset):
        json_format += "\n  {\n"+"    \"nome\""+": " + \
            "\"" + person["nome"] + "\"" + ",\n"
        json_format += "    \"telefone\""+": " + "\"" + \
            person["telefone"] + "\"" + ",\n"
        json_format += "    \"pais\""+": " + "\"" + \
            person["pais"] + "\"" + ",\n"
        json_format += "    \"uf\""+": " + "\"" + \
            person["uf"] + "\"" + ",\n"
        json_format += "    \"cidade\""+": " + "\"" + \
            person["cidade"] + "\"" + ",\n"
        json_format += "    \"endereco\""+": " + "\"" + \
            person["endereco"] + "\"" + ",\n"
        json_format += "    \"cep\""+": " + "\"" + \
            person["cep"] + "\"" + "\n"+"  }"
        if (index) != len(dataset)-1:
            json_format += ","
    json_format += "\n]"
    return json_format
