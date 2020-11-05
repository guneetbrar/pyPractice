import xml.etree.ElementTree as ET

data = '''
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<email hide="yes"/>
<body>Don't forget me this weekend!</body>
</note>'''

tree = ET.fromstring(data)
print('Name:', tree.find('from').text)
print('Attr:', tree.find('email').get('hide'))