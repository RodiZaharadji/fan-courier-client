import csv
import io


def normalise_fields(fields: list):
    result_fields = []

    for field in fields:
        mapping = map(lambda c: c if c.isalpha() or c == ' ' else '', field)
        result_fields.append(''.join(mapping).replace(' ', '_').lower())

    return result_fields


def csv_to_json(csv_text, headers=None):
    if not headers:
        headers = normalise_fields(csv_text.split('\n')[0].split(','))
        csv_text = '\n'.join(csv_text.split('\n')[1:])

    reader = csv.DictReader(io.StringIO(csv_text), fieldnames=headers)
    json_data = list(reader)

    return json_data


def json_to_csv_file(json_data, csv_headers):
    if not isinstance(json_data, list):
        json_data = [json_data]

    csv_result = ''
    for element in json_data:
        if not csv_result:
            headers = []
            for key in element:
                headers.append(csv_headers.get(key, key))
            csv_result += ','.join(headers)
        csv_result += '\n' + ','.join(map(str, element.values()))

    return io.BytesIO(bytes(csv_result, 'utf-8'))


def text_to_list(text_data):
    return text_data.replace('"', '').split('\n')[1:-1]
