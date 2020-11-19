import requests

from fan_courier_client.common import BaseObject
from fan_courier_client.constants import MAIN_URL
from fan_courier_client.decorators import validate
from fan_courier_client.utils import csv_to_json


class Sheet(BaseObject):
    get_sheet_url = 'export_borderou_integrat.php'
    export_sheet_url = 'finalizare_borderou_integrat.php'

    @validate({'data': {'regex': '\d\d.\d\d.\d\d\d\d'}})
    def get(self, **kwargs):
        kwargs.update(self.params)
        response = requests.post(f'{MAIN_URL}/{self.get_sheet_url}', data=kwargs)
        return csv_to_json(response.text)

    def export(self):
        response = requests.post(f'{MAIN_URL}/{self.export_sheet_url}', data=self.params)
        return response.content