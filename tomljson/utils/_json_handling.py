import json

def handleNonString(elem) -> bool:
    if isinstance(elem, str) or isinstance(elem, int) or isinstance(elem, bool):
        return True
    else:
        return False
    

def handleChildTable(table_header: str, element: str) -> bool:
    formatted_title = table_header.strip("[]")
    if formatted_title in element:
        return True
    else:
        return False

def fillTables(table_header: str, parserOutput: list):

    table_content = {}
    header_index = parserOutput.index(table_header)
    start_index = header_index + 1

    for i in range(start_index, len(parserOutput)):
        if '[' in str(parserOutput[i]):
            if not handleChildTable(table_header, parserOutput[i]):
                break
            else:
                table_content[parserOutput[i]] = {}
                j = i+1
                while j < len(parserOutput) and '[' not in str(parserOutput[j]):
                    table_content[parserOutput[i]][parserOutput[j]] = parserOutput[j+1]
                    j += 2
                i = j
        else:
            table_content[parserOutput[i]] = parserOutput[i+1]
            i += 2

    return table_content


def handleOutputToDict(parserOutput: list) -> dict:
    global_dict = {}

    for i, elem in enumerate(parserOutput):
        if isinstance(elem, str):
            if elem.startswith('['):
                # array of tables
                if '[[' in elem:
                    current_key = elem.strip("[[]]")
                    global_dict[current_key] = []
                else:
                    current_key = elem.strip("[]")
                    global_dict[current_key] = {}
            elif '=' in elem:
                verify_elem = parserOutput[i + 1]
                if isinstance(verify_elem, list):
                    if verify_elem[0] == '{':
                        current_key = elem.strip(" =") if elem.find(" =") != -1 else elem.strip("=")
                        global_dict[current_key] = {}
                        for j in range(1, len(verify_elem)-2, 2):
                            new_key = verify_elem[j].strip(" =") if verify_elem[j].find(" =") != -1 else verify_elem[j].strip("=")
                            global_dict[current_key][new_key] = verify_elem[j+1]
                    else:
                        current_key = elem.strip(" =") if elem.find(" =") != -1 else elem.strip("=")
                        global_dict[current_key] = verify_elem


    for key in global_dict.keys():
        if isinstance(global_dict[key], dict):
            # verify if the values of the dict is are empty
            if not global_dict[key]:
                global_dict[key] = fillTables('[' + key + ']', parserOutput)

    return global_dict

                            

                # assignment of non string
                # if handleNonString(parserOutput[i + 1]):
                #     current_key = elem.strip(" =") if elem.find(" =") != -1 else elem.strip("=")
                #     global_dict[current_key] = parserOutput[i + 1]
                # # assigment of string
                # elif isinstance(parserOutput[i + 1], str) and '[' not in parserOutput[i+1]:
                #     current_key = elem.strip(" =") if elem.find(" =") != -1 else elem.strip("=")
                #     global_dict[current_key] = parserOutput[i + 1]
                # else:
                # assignment of array or inline table
                

    return global_dict


def printType(result):
    for elem in result:
        print(f"{elem} => {type(elem)}")

# def handleNonString(elem) -> bool:
#     if isinstance(elem, str) or isinstance(elem, int) or isinstance(elem, bool):
#         return True
#     else:
#         return False


# def handleOutputToDict(parserOutput: list) -> dict:
#     global_dict = {}

#     for i, elem in enumerate(parserOutput):
#         if handleNonString(elem):
#             if isinstance(parserOutput[i - 1], str):
#                 current_key = (
#                     parserOutput[i - 1].strip(" =")
#                     if parserOutput[i - 1].find(" =") != -1
#                     else parserOutput[i - 1].strip("=")
#                 )
#                 global_dict[current_key] = elem
#         elif isinstance(elem, list):
#             check_elem = str(elem)
#             if check_elem.startswith("["):
#                 if '[[' in check_elem:
#                     current_key = check_elem.strip("[[]]")
#                     global_dict[current_key] = []
#                     j = i + 1
#                     while '[' not in parserOutput[j]:
#                         new_dict = {}
#                         formatted_key = parserOutput[j].strip(" =") if parserOutput[j].find(" =") != -1 else parserOutput[j].strip("=")
#                         new_dict[formatted_key] = parserOutput[j + 1]
#                         j += 2
#                     global_dict[current_key].append(new_dict)

#             if isinstance(parserOutput[i - 1], str):
#                 current_key = (
#                     parserOutput[i - 1].strip(" =")
#                     if parserOutput[i - 1].find(" =") != -1
#                     else parserOutput[i - 1].strip("=")
#                 )
#                 global_dict[current_key] = elem


# def parserOutputToDict(parserOutput: List[str]) -> dict:
#     global_dict = {}

#     for i, elem in enumerate(parserOutput):
#         stringElement = str(elem)
#         if stringElement.startswith("["):
#             # array
#             if "=" in parserOutput[i - 1]:
#                 current_key = (
#                     parserOutput[i - 1].strip(" =")
#                     if parserOutput[i - 1].find(" =") != -1
#                     else parserOutput[i - 1].strip("=")
#                 )
#                 global_dict[current_key] = stringElement
#             # array of tables
#             elif stringElement[2] == "[":
#                 current_key = stringElement.strip("[[]]")
#                 global_dict[current_key] = []
#                 j = i + 1
#                 while parserOutput[j].startswith("["):
#                     new_dict = {}
#                     formatted_key = parserOutput[j].strip(" =") if parserOutput[j].find(" =") != -1 else parserOutput[j].strip("=")
#                     new_dict[str(formatted_key)] = parserOutput[j + 1].strip()
#                     j += 2
#                 global_dict[current_key].append(new_dict)
#             # inline table
#             elif stringElement[1] == "{":
#                 current_key = (
#                     parserOutput[i - 1].replace(" =", "")
#                     if parserOutput[i - 1].find(" =") != -1
#                     else parserOutput[i - 1].replace("=", "")
#                 )
#                 global_dict[current_key] = {}
#                 j = i + 1
#                 while "}" not in parserOutput[j]:
#                     formatted_key = parserOutput[j].strip(" =") if parserOutput[j].find(" =") != -1 else parserOutput[j].strip("=")
#                     global_dict[current_key][str(formatted_key)] = parserOutput[j + 1].strip()
#                     j += 2
#             # table
#             else:
#                 current_key = stringElement.strip("[]")
#                 global_dict[current_key] = {}
#                 j = i + 1
#                 while not parserOutput[j].startswith("["):
#                     formatted_key = parserOutput[j]
#                     if formatted_key.find(" =") != -1:
#                         formatted_key = formatted_key.strip(" =")
#                     else:
#                         formatted_key = formatted_key.strip("=")
#                     global_dict[current_key][formatted_key] = str(parserOutput[j + 1])
#                     j += 2

#     return json.dumps(global_dict, indent=None)

# for item in parserOutput:
#     element = str(item)
#     if element.startswith('['):
#         current_key = element.strip('[]')
#         current_dict[current_key] = {}
#         current_dict = current_dict[current_key]
#     elif element.endswith('='):
#         current_key = element[:-2]
#     else:
#         current_dict[current_key] = element
