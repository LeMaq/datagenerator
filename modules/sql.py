# -*- coding: utf-8 -*-
"""To SQL"""


def to_sql(dataset):
    """Converte um array de dicionários em uma string no formato SQL.

    Args:
        dataset (list): O dataset a ser convertido.

    Returns:
        result: Uma string no formato SQL com base no dataset fornecido.
    """
    table = "dbo.BANCO_SQL"
    columns = ["nome", "telefone", "pais", "uf", "cidade", "endereco", "cep"]

    result = ""

    result = ("CREATE TABLE " + table + "(\n")
    result += ("  " + columns[0] + " varchar(128) NOT NULL DEFAULT ' ',")
    result += ("  " + columns[1] + " varchar(14) NOT NULL,")
    result += ("  " + columns[2] + " varchar(16) NOT NULL,")
    result += ("  " + columns[3] + " varchar(64) NOT NULL DEFAULT ' ',")
    result += ("  " + columns[4] + " varchar(64) NOT NULL DEFAULT ' ',")
    result += ("  " + columns[5] + " varchar(64) NOT NULL DEFAULT ' ',")
    result += ("  " + columns[6] + " varchar(9) NOT NULL DEFAULT ' ');")

    insert_begin = "\n\nINSERT \nINTO\n\t{} \n\t({}) \nVALUES \n\t".format(
        table, ", ".join(columns))

    for pessoa in dataset:
        result += insert_begin + "({});".format(
            ", ".join(["'" + field + "'" for field in pessoa.values()]))

    return result
