# from bs4 import BeautifulSoup, element


import xml
import xml.etree.ElementTree as ET

tree = ET.parse('models.xml')
root = tree.getroot()

while True:
    try:
        for name in root.iter():
            print(root.tag, name.text)
    except xml.etree.ElementTree.ParseError:
        pass

        for name in root.iter():
            print(name.text)

# with open('models.xml', 'r') as f:
#     data = f.read()
#
#     bs_data = BeautifulSoup(data, 'xml')
#
#     b_unique = bs_data.find_all('weekday')
#     print(b_unique)
#     b_unique = bs_data.find_all('weekend')
#     print(b_unique)
#     b_name = bs_data.find('child', {'day': 'Monday'})
#     print(b_name)
#
#     value = b_name.get('time')
#     print(value)
