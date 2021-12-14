import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Bruno</name>
    <phone type="intl">
        +52 55 2034 0796
    </phone>
    <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print("Name:", tree.find("name").text)
print("Phone:", tree.find("phone").text)
print("Email hide:", tree.find("email").get("hide"))
