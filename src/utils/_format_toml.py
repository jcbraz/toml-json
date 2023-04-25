from tomlkit import parse, document, dumps
import re


def sort_toml(toml_str: str):
    toml_document = parse(toml_str)
    new_document = document()
    parent_pattern = re.compile(r'\[(\w+)\]')
    child_pattern = re.compile(r'\[\w+\.\w+\]')
    parent_buffer = []
    child_buffer = []
    result = []

    lines = toml_str.split('\n')
    for line in lines:
        parent_match = re.match(parent_pattern, line)
        if parent_match:
            parent_buffer.append(parent_match.group(1))
        child_match = re.match(child_pattern, line)
        if child_match:
            child_buffer.append(child_match.group(0))

    for parent in parent_buffer:
        result.append(parent)
        for child in child_buffer:
            parent_reference = child.split('.')[0]
            parent_reference = parent_reference.replace('[', '')
            if parent == parent_reference:
                result.append(child[1:-1])

    for table in result:
        if '.' in table:
            parent, child = table.split('.')
            if parent not in new_document:
                new_document[parent] = {}
            new_document[parent][child] = toml_document[parent][child]
        else:
            new_document[table] = toml_document[table]

    return dumps(new_document)


input_toml = '''
title = "TOML Example"

[database.phi]
enable = false
ports = "undefined"

[owner.dizes]
name = "Dizes"
dob = 1990-05-27T07:32:00-08:00

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00

[servers.dizes]
ip = "321123"
role = "data"

[database]
enabled = true
ports = [ 8000, 8001, 8002 ]
data = [ ["delta", "phi"], [3.14] ]
temp_targets = { cpu = 79.5, case = 72.0 }

[servers]
[servers.alpha]
ip = "10.0.0.1"
role = "frontend"

[servers.beta]
ip = "10.0.0.2"
role = "backend"

[bananas]
number = 1
species = "tropical"
'''

print(sort_toml(input_toml))
