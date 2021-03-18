import csv
import xml.etree.ElementTree as ET

if __name__ == "__main__":
    status_strs = [
        "Unknown",
        "Does not work",
        "Works but has many/major features that doesn't work",
        "Works but has some minor features that doesn't work",
        "Everything works",
    ]

    with open("modlist.csv", encoding="utf8") as f:
        modlist = {x[1]: (x[0], x[1]) for x in csv.reader(f)}

    with open("modlist.xml", encoding="utf8") as f:
        xml_str = f.read()

    xml = ET.fromstring(xml_str)
    mods_status = sorted(
        [modlist[id.text] for id in xml.findall("./modNames/li") if id.text in modlist], key=lambda x: x[0]
    )

    for index, status_str in enumerate(status_strs):
        print(f"[{index}: {status_str}]")
        print("".join([f"\t{x[1]}\n" for x in mods_status if x[0] == str(index)]))
