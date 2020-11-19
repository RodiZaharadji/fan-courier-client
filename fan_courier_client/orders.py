import requests

from fan_courier_client.common import BaseObject
from fan_courier_client.constants import MAIN_URL
from fan_courier_client.decorators import validate
from fan_courier_client.utils import csv_to_json


class Order(BaseObject):
    get_orders_url = 'export_comenzi_integrat.php'
    create_order_url = 'comanda_curier_integrat.php'

    @validate({'data': {'regex': '\d\d.\d\d.\d\d\d\d'}})
    def get(self, **kwargs):
        kwargs.update(self.params)
        response = requests.post(f'{MAIN_URL}/{self.get_orders_url}', data=kwargs)
        return csv_to_json(response.text)

    fields_create_validation = {
        'pers_contact': {
            'type': str,
        },
        'tel': {
            'type': str,
        },
        'email': {
            'type': str,
            'regex': '^\S+@\S+$'
        },
        'greutate': {
            'type': int,
        },
        'inaltime': {
            'type': int,
        },
        'lungime': {
            'type': int,
        },
        'latime': {
            'type': int,
        },
        'ora_ridicare': {
            'type': str,
            'regex': '\d\d:\d\d'
        },
        'nr_colete': {
            'type': int,
            'default': 1
        },
        'nr_plicuri': {
            'type': int,
            'default': 1
        }
    }

    @validate(fields_create_validation)
    def create(self, **kwargs):
        data = {
            **self.params
        }
        data.update(kwargs)
        response = requests.post(f'{MAIN_URL}/{self.create_order_url}', data=data)
        return response.text