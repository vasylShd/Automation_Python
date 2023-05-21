import xml.etree.ElementTree as ET


class XmlProcessing:

    def xml_to_string(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        xml_string = ET.tostring(root).decode()
        return xml_string

    def string_to_xml(self, xml_string, name_xml_file):
        root = ET.fromstring(xml_string)
        tree = ET.ElementTree(root)
        tree.write(name_xml_file, encoding='utf-8', xml_declaration=True)

    def output_child_and_grandchild(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for child in root:
            print(child.tag, child.attrib)
            for grandchild in child.findall('*'):
                print({grandchild.tag:grandchild.text})
            print()



xml_processing_1 = XmlProcessing()
print(xml_processing_1.xml_to_string('PurchaseOrder.xml'))

string_for_xml = xml_processing_1.xml_to_string('PurchaseOrder.xml')

xml_processing_2 = XmlProcessing()
xml_processing_2.string_to_xml(string_for_xml, 'output_PurchaseOrder.xml')


xml_processing_3 = XmlProcessing()
xml_processing_3.output_child_and_grandchild('PurchaseOrder.xml')

