# from bs4 import BeautifulSoupas bs, element


import xml
import xml.etree.ElementTree as ET

tree = ET.parse('models.xml')
root = tree.getroot()

while True:
    try:
        for name in root.iter("Monday"):
            print(root.tag, name.text)
    except xml.etree.ElementTree.ParseError:
        pass

        for name in root.iter("Friday"):
            print(name.text)

content = []

with open("models.xml", "r") as file:
    # Read each line in the file, readlines() returns a list of lines
    content = file.readlines()
    # Combine the lines in the list into a string
    content = "".join(content)
    bs_content = bs(content, "lxml")
result = bs_content.find("data")

result = bs_content.find("Monday")
print(result)

result = bs_content.find("Tuesday")

print(result)

result = bs_content.find("Friday")

print(result)

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
