# -*- coding: utf-8 -*-
"Data Generator"
import sys
from random import randint, choice
from modules.csv import to_csv
from modules.json import to_json
from modules.html import to_html
from modules.sql import to_sql


def generate_random_name(names, surnames):
    """Retorna um nome aleatório.

    Args:
        names (list): Lista de nomes
        surnames (list): Lista de sobrenomes.Main

    Returns:
        new_name: String formada por nome e sobrenome.

    """
    new_name = choice(names).strip() + \
        " " + choice(surnames).strip() + \
        " " + choice(surnames).strip()
    return new_name


def main():
    """Início da execução do programa"""
    number_of_rows = int(sys.argv[1])
    output_data_format = sys.argv[2]

    names = open("samples/nomes.txt").readlines()
    surnames = open("samples/sobrenomes.txt").readlines()
    telephones = open("samples/telefones.txt").readlines()
    countries = open("samples/paises.txt").readlines()
    states = open("samples/ufs.txt").readlines()
    cities = open("samples/cidades.txt").readlines()
    addresses = open("samples/enderecos.txt").readlines()
    zip_codes = open("samples/ceps.txt").readlines()

    dataset = []
    new_dataset = False

    i = 0
    while i < number_of_rows:
        new_name = generate_random_name(names, surnames)
        while any(new_name == row["nome"] for row in dataset):
            new_name = generate_random_name(names, surnames)

        new_telephone = choice(telephones).strip()
        new_city = choice(cities).strip()
        new_state = choice(states).strip()
        new_country = choice(countries).strip()

        new_address = choice(addresses).strip() + ' '
        new_address += choice(names).strip() + ' '
        new_address += choice(surnames).strip() + ' '
        new_address += 'Nº ' + str(randint(1, 9999))

        new_zip_code = choice(zip_codes).strip()

        dataset.append({
            "nome": new_name,
            "telefone": new_telephone,
            "pais": new_country,
            "uf": new_state,
            "cidade": new_city,
            "endereco": new_address,
            "cep": new_zip_code
        })

        i += 1

    if output_data_format == "csv":
        new_dataset = to_csv(dataset)
    elif output_data_format == "json":
        new_dataset = to_json(dataset)
    elif output_data_format == "html":
        new_dataset = to_html(dataset)
    elif output_data_format == "sql":
        new_dataset = to_sql(dataset)

    if new_dataset:
        print(new_dataset, end="")


main()
