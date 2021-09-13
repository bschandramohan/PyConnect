encoding = 'utf-8'

properties = {}
with open("../resources/local.env", "rb") as properties_file:
    lines = properties_file.readlines()
    for line in lines:
        property_keyvalues = str(line, encoding).strip().split("=")
        properties[property_keyvalues[0]] = property_keyvalues[1]

print(properties)
