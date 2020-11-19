import requests

from fan_courier_client.common import BaseObject
from fan_courier_client.constants import MAIN_URL
from fan_courier_client.utils import text_to_list


class Remark(BaseObject):
    get_remarks_url = 'export_observatii_integrat.php'

    def get(self):
        response = requests.post(f'{MAIN_URL}/{self.get_remarks_url}', data=self.params)
        return text_to_list(response.text)
