import requests

from fan_courier_client.common import BaseObject
from fan_courier_client.constants import MAIN_URL
from fan_courier_client.utils import csv_to_json


class Address(BaseObject):
    city_url = 'export_distante_integrat.php'
    addresses_url = 'export_strazi_integrat.php'

    def cities(self):
        response = requests.post(f'{MAIN_URL}/{self.city_url}', data=self.params)
        return csv_to_json(response.text)

    def get(self, **kwargs):
        kwargs.update(self.params)
        response = requests.post(f'{MAIN_URL}/{self.addresses_url}', data=kwargs)
        return csv_to_json(response.text)
