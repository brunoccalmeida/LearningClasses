import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Bruno</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>    
'''

stuff = ET.fromstring(data)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute x =', item.get("x"))
