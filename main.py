import csv

from jinja2 import Environment, FileSystemLoader


DATA = {
    "BSC1": {
        "980": {
            "Cells": ["9801", "9802", "9803"],
            "Tgs": ["5", "6", "7"]
        },
        "983": {
            "Cells": ["9831", "9832", "9833"],
            "Tgs": ["13", "14", "15"]
        }
    },
    "BSC2": {
        "770": {
            "Cells": ["7701", "7702", "7703"],
            "Tgs": ["5", "6", "7"]
        },
        "773": {
            "Cells": ["7731", "7732", "7733"],
            "Tgs": ["13", "14", "15"]
        }
    }
}


def row_to_dict(bsc, tg, rSite, cell):
    if bsc not in DATA.keys():
        DATA[bsc] = {}
    if rSite not in DATA[bsc].keys():
        DATA[bsc][rSite] = {
            'Cells': [],
            'Tgs': []
        }
    DATA[bsc][rSite]['Cells'].append(cell)
    DATA[bsc][rSite]['Tgs'].append(tg)


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
            row_to_dict(bsc, tg, rSite, cell)


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
    DATA.clear()
    read_csv()
    render_template()


if __name__ == '__main__':
    main()
