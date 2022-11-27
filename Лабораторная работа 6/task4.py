import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(file_csv, delimiter=',', new_line='\n'):
    with open(file_csv) as file:
        data_list = []
        for index, line in enumerate(file):
            fields = line.strip(new_line).split(delimiter)
            if index == 0:
                headers = fields
                continue
            data_list.append({})
            for i, _ in enumerate(headers):
                data_list[-1][headers[i]] = fields[i]
    return data_list

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
