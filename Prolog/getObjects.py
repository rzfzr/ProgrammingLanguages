import xml.etree.ElementTree as ET
tree = ET.parse('GRUPO1.xml')
root = tree.getroot()


class Plant:
    def __init__(self, name):
        self.name = name


for i, record in enumerate(root):
    print('record #', i)
    plant = Plant('test')
    # print(record.tag, record.attrib)
    for child in record:
        # print(child.tag, child.attrib)
        print(child.text)
        # print('size:', len(child.attrib))
