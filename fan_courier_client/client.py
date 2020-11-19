import requests

from fan_courier_client.common import BaseObject
from .constants import MAIN_URL
from .addresses import Address
from .rates import Rate
from .awb import Awb
from .services import Service
from .remarks import Remark
from .sheets import Sheet
from .transfers import Transfer
from .orders import Order


class Client(BaseObject):
    clients_url = 'get_account_clients_integrat.php'
    def list(self):
        response = requests.post(f'{MAIN_URL}/{self.clients_url}', data=self.params)
        return response.json()

    @property
    def addresses(self):
        return Address(**self.params)

    @property
    def rates(self):
        return Rate(**self.params)

    @property
    def awb(self):
        return Awb(**self.params)

    @property
    def services(self):
        return Service(**self.params)

    @property
    def remarks(self):
        return Remark(**self.params)

    @property
    def sheets(self):
        return Sheet(**self.params)

    @property
    def transfers(self):
        return Transfer(**self.params)

    @property
    def orders(self):
        return Order(**self.params)