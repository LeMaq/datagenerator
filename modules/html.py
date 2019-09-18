# -*- coding: utf-8 -*-
"""To HTML"""


def to_html(dataset):
    """Converte um array de dicionários em uma string no formato HTML.

    Args:
        dataset (list): O dataset a ser convertido.

    Returns:
        str: A string equivalente a um objeto HTML para o dataset fornecido.

    """
    columns = ["nome", "telefone", "pais", "uf", "cidade", "endereco", "cep"]

    html_format = "<!DOCTYPE html>\n"
    html_format += "<html lang=\"pt-br\">\n"
    html_format += "\t < head >\n\t\t < meta charset =\"utf-8\">\n"
    html_format += "\t\t<title>Titulo</title>\n"
    html_format += "\t\t<style>\n\t\ttable {\n" + \
        "\t\t\tfont-family: arial, sans-serif; \n" + \
        "\t\t\tborder-collapse: collapse; \n" + \
        "\t\t\twidth: 100%; \n" + \
        "\t\t}\n" + \
        "\t\ttd, th {\n" + \
        "\t\t\tborder: 1px solid  #dddddd;\n" + \
        "\t\t\ttext-align: left; \n" + \
        "\t\t\tpadding: 8px; \n" + \
        "\t\t}\n" + \
        "\t\tthead tr, tr:nth-child(even) {\n" + \
        "\t\t\tbackground-color:  #dddddd;\n" + \
        "\t\t}\n\t\t</style>\n\t</head>\n"
    html_format += "\t<body>\n"
    html_format += "\t\t<table>\n"
    html_format += "\t\t\t<thead>\n\t\t\t\t<tr>\n"
    for column in columns:
        html_format += "\t\t\t\t\t<th>{}</th>\n".format(column)
    html_format += "\t\t\t\t</tr>\n"
    html_format += "\t\t\t</thead>\n"
    html_format += "\t\t\t<tbody>\n"
    for person in dataset:
        html_format += "\t\t\t\t<tr>\n"
        for key in person:
            html_format += "\t\t\t\t\t<td>{}</td>\n".format(person[key])
        html_format += "\t\t\t\t</tr>\n"
    html_format += "\t\t\t</tbody>\n"
    html_format += "\t\t</table>\n\t</body>\n</html>"
    html_format = html_format.expandtabs(2)
    return html_format
