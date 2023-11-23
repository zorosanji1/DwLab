import xml.etree.ElementTree as ET
file_path=r"C:\Users\gokul\Desktop\DW Lab\read_xml_file\data.xml"
tree=ET.parse(file_path)
root=tree.getroot()
for i in root.iter():
    print(f"Tag: {i.tag}, Text: {i.text}")
