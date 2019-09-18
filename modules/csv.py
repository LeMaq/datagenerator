# -*- coding: utf-8 -*-
"""To CSV"""


def to_csv(dataset):
    """Converte um array de dicionários em uma string no formato CSV.

    Args:
        dataset (list): O dataset a ser convertido.

    Returns:
        result: Uma string no formato CSV com base no dataset fornecido.

    """
    csv_format = 'nome,telefone,pais,uf,cidade,endereço,cep\r\n'
    for (index, pessoa) in enumerate(dataset):
        csv_format += ",".join(pessoa.values())
        if index < len(dataset)-1:
            csv_format += "\r\n"

    return csv_format
