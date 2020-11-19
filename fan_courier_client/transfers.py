import requests

from fan_courier_client.common import BaseObject
from fan_courier_client.constants import MAIN_URL
from fan_courier_client.decorators import validate
from fan_courier_client.utils import csv_to_json


class Transfer(BaseObject):
    get_transfers_url = 'export_raport_viramente_integrat.php'

    @validate({'data': {'regex': '\d\d.\d\d.\d\d\d\d'}})
    def get(self, **kwargs):
        kwargs.update(self.params)
        response = requests.post(f'{MAIN_URL}/{self.get_transfers_url}', data=kwargs)
        return csv_to_json(response.text)