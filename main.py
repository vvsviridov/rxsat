import csv

from jinja2 import Environment, FileSystemLoader


DATA = {}


def read_csv():
    '''
        "<BSC>": {
            "<rSite>": {
                "Cells": [
                    1,
                    2,
                    3
                ],
                "Tgs": [
                    1,
                    2,
                    3
                ]
            }
        }
    '''
    with open('ch_at.csv') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for item in csvReader:
            bsc = item[0]
            tg = item[4]
            rSite = item[7]
            cell = item[8]
            if bsc not in DATA.keys():
                DATA[bsc] = {}
            if rSite not in DATA[bsc].keys():
                DATA[bsc][rSite] = {
                    'Cells': [],
                    'Tgs': []
                }
            DATA[bsc][rSite]['Cells'].append(cell)
            DATA[bsc][rSite]['Tgs'].append(tg)


def render_template():
    template_env = Environment(loader=FileSystemLoader(searchpath='./'))
    template = template_env.get_template("ch_at.cmd")
    for item in DATA.keys():
        for rSite, data in DATA[item].items():
            with open(f"{item}.cmd", "a") as output_file:
                output_file.write(
                    template.render(
                        rsite=rSite,
                        cells=data["Cells"],
                        tgs=data["Tgs"],
                    )
                )


def main():
    read_csv()
    render_template()


if __name__ == '__main__':
    main()
