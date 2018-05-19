import unicodedata

import xml.etree.ElementTree as ET
tree = ET.parse('./GRUPO1.XML')
root = tree.getroot()


# class Plant:
#     def __init__(self, name):
#         self.name = name

file = open('baseWithoutAccents.pl', 'w')  # clear file
with open('baseWithoutAccents.pl', 'a') as file:
    file.truncate()
    for i, record in enumerate(root):
        # print('record #', i)
        # plant = Plant('test')
        # print(record.tag, record.attrib)
        file.write('record(')
        for child in record:
            file.write(child.tag.lower() + "('")
            temp = unicode(child.text)
            # for char in temp:

            temp=''.join((c for c in unicodedata.normalize('NFD', temp) if unicodedata.category(c) != 'Mn'))
            temp=temp.encode('utf-8').strip()
            
            file.write(temp)
            file.write("')")
            if child.tag != 'SAUDE':
                file.write(',')
                file.write('\n')
            # print(child.tag.lower(), "('", child.text, "')")

            # print( child.attrib)
            # print('size:', len(child.attrib))
        file.write(').\n\n')
        # prologFile.write('| ?- use_module(library(objects)).\n')