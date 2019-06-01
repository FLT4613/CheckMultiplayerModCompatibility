import csv
import xml.etree.ElementTree as ET
from collections import defaultdict

if __name__ == "__main__":
    status_strs = [
        "Unknown",
        "Does not work",
        "Works but has many/major features that doesn't work",
        "Works but has some minor features that doesn't work",
        "Everything works",
    ]

    with open('modlist.csv') as f:
        modlist = {
            x[2]: (x[0], x[1])
            for x in csv.reader(f)
        }

    with open('modlist.xml') as f:
        xml_str = f.read()

    xml = ET.fromstring(xml_str)
    mods_status = sorted([
        modlist[id.text] for id in xml.findall('./modIds/li')
        if id.text in modlist
    ], key=lambda x: x[0])

    for index, status_str in enumerate(status_strs):
        print(f'[{index}: {status_str}]')
        print(
            '\n'.join([f'\t{x[1]}' for x in mods_status if x[0] == str(index)])
        )
        print('\n')