import requests
from .utils import *
from .constants import *
import csv, io, json, re

# CLIENT_ID = '695720'
# USERNAME = 'Zaharadji@mail.ru'
# PASSWORD = 'qwe123'
CLIENT_ID = '7032158'
USERNAME = 'clienttest'
PASSWORD = 'testing'

URL = MAIN_URL



params = {
    'username': USERNAME,
    'user_pass': PASSWORD,
    'client_id': CLIENT_ID,
}






# test


# test


def validate(fields):
    def decorator(func):
        def wrapper(**kwargs):
            for field in fields:
                if not kwargs.get(field):
                    raise Exception(f"Field '{field}' is required")
            return func(**kwargs)

        return wrapper

    return decorator


fields = ['tip_serviciu', 'iban', 'nr_plicuri', 'nr_colete', 'greutate', 'plata_expeditie', 'ramburs_bani',
          'plata_ramburs_la', 'nume_destinatar', 'telefon', 'judet', 'localitate', 'strada', 'cod_postal']

csv_headers = {
    'tip_serviciu': 'Tip serviciu',
    'banca': 'Banca',
    'iban': 'IBAN',
    'nr_plicuri': 'Nr. Plicuri',
    'nr_colete': 'Nr. Colete',
    'greutate': 'Greutate',
    'plata_expeditie': 'Plata expeditie',
    'ramburs_bani': 'Ramburs(bani)',
    'plata_ramburs_la': 'Plata ramburs la',
    'valoare_declarata': 'Valoare declarata',
    'persoana_contact_expeditor': 'Persoana contact expeditor',
    'observatii': 'Observatii',
    'continut': 'Continut',
    'nume_destinatar': 'Nume destinatar',
    'persoana_contact': 'Persoana contact',
    'telefon': 'Telefon',
    'fax': 'Fax',
    'email': 'Email',
    'judet': 'Judet',
    'localitate': 'Localitatea',
    'strada': 'Strada',
    'nr': 'Nr',
    'cod_postal': 'Cod postal',
    'bl': 'Bloc',
    'scara': 'Scara',
    'etaj': 'Etaj',
    'apartament': 'Apartament',
    'inaltime_pachet': 'Inaltime pachet',
    'latime_pachet': 'Latime pachet',
    'lungime_pachet': 'Latime pachet',
    'restituire': 'Restituire',
    'centru_cost': 'Centru Cost',
    'optiuni': 'Optiuni',
    'packing': 'Packing',
    'date_personale': 'Date personale',
}

request_data = {
    'tip_serviciu': 'Standard',
    'banca': 'Test',
    'iban': 'XXXXXXX',
    'nr_plicuri': 1,
    'nr_colete': 0,
    'greutate': 1,
    'plata_expeditie': 'ramburs',
    'rambursbani': 100,
    'plata_ramburs_la': 'destinatar',
    'valoare_declarata': 400,
    'persoana_contact_expeditor': 'Test User',
    'observatii': 'Lorem ipsum',
    'continut': 'Fragil',
    'nume_destinatar': 'Test',
    'persoana_contact': 'Test',
    'telefon': '123456789',
    'fax': '123456789',
    'email': 'example@example.com',
    'judet': 'Galati',
    'localitatea': 'Tecuci',
    'strada': 'Lorem',
    'nr': '2',
    'cod_postal': '123456',
    'bloc': '',
    'scara': '',
    'etaj': '',
    'apartament': '',
    'inaltime_pachet': '',
    'latime_pachet': '',
    'lungime_pachet': '',
    'restituire': '',
    'centru_cost': '',
    'optiuni': '',
    'packing': '',
    'date_personale': ''
}
@validate(fields)
def create_awb(**kwargs):
    csv_data = json_to_csv(kwargs, csv_headers)
    # request_data = {
    #     'fisier': csv_headers,
    #     **params
    # }
    request_data = {
        'fisier': [request_data],
        **params
    }
    response = requests.post(f'{URL}/{create_awb_url}', data=request_data)
    return response.text


# test

# print(tracking_awb_list(['2322000120065']))


data = {
    'serviciu': 'Cont Colector',
    'localitate_dest': 'Vrancea',
    'judet_dest': 'judet_dest',
    'plicuri': 1,
    'colete': 1,
    'greutate': 1,
    'lungime': 1,
    'latime': 1,
    'inaltime': 1,
    'val_decl': 1,
    'plata_ramburs': 'plata_ramburs',
    'optiuni': 'B'
}
# print(get_tariff(**data))

data = {
    'pers_contact': 'pers_contact',
    'tel': 'tel',
    'email': 'email@mail.com',
    'greutate': 10,
    'inaltime': 1,
    'lungime': 1,
    'latime': 1,
    'ora_ridicare': '16:00'
}
# print(create_order(**data))


# print(get_awb('2322000120065'))

# AWB id-s
# print(get_orders('17.11.2020'))


# data = {
#     'tip_serviciu': '1',
#     'iban': '2',
#     'nr_plicuri': '3',
#     'nr_colete': '4',
#     'greutate': '5',
#     'plata_expeditie': '6',
#     'ramburs_bani': '7',
#     'plata_ramburs_la': '8',
#     'nume_destinatar': '9',
#     'telefon': '10',
#     'judet': '11',
#     'localitate': '12',
#     'strada': '13',
#     'cod_postal': '14'
# }
# print(create_awb(**data))
