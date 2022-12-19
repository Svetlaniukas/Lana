# from bs4 import BeautifulSoup, element

from elementtree.ElementTree import XML, SubElement, tostring

text = """
<root>
    <phoneNumbers>
        <number topic="sys/phoneNumber/1" update="none" />
        <number topic="sys/phoneNumber/2" update="none" />
        <number topic="sys/phoneNumber/3" update="none" />
    </phoneNumbers>

    <gfenSMSnumbers>
        <number topic="sys2/SMSnumber/1" update="none" />
        <number topic="sys2/SMSnumber/2" update="none" />
    </gfenSMSnumbers>
</root>
"""

elem = XML(text)
for node in elem.find('phoneNumbers'):
    print(node.attrib['topic'])
    # Create sub elements
    if node.attrib['topic'] == "sys/phoneNumber/1":
        tag = SubElement(node, 'TagName')
        tag.attrib['attr'] = 'AttribValue'

print(tostring(elem))
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
